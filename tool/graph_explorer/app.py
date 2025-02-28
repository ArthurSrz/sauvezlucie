import streamlit as st
import os
from pathlib import Path
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import base64
from openai import OpenAI

# Importer nos modules
from markdown_parser import parse_markdown_directory
from graph_builder import build_graph, get_node_neighbors, get_graph_stats, get_nodes_within_depth
from search_engine import simple_keyword_search
from visualization import visualize_graph
from relevance_scoring import calculate_combined_scores
from config import LLM_BASE_URL, LLM_API_KEY, LLM_MODEL, DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS
from prompts import QA_SYSTEM_PROMPT, QA_USER_PROMPT_TEMPLATE
# Configuration de la page
st.set_page_config(
    page_title="Explorateur de Graphe de Connaissances",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fonctions utilitaires
@st.cache_resource
def get_llm_client():
    """Initialise et met en cache le client LLM"""
    try:
        # Pour les modèles locaux compatibles avec l'API OpenAI
        client = OpenAI(
            api_key=LLM_API_KEY,
            base_url=LLM_BASE_URL,
        )
        return client
    except Exception as e:
        print(f"Impossible d'initialiser le client LLM: {e}")
        return None

def get_table_download_link(df, filename, text):
    """Génère un lien pour télécharger un DataFrame en CSV"""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">{text}</a>'
    return href

# Titre et description
st.markdown("""
# 🔍 Explorateur de Graphe de Connaissances

Cet outil vous permet d'analyser, visualiser et explorer une base de connaissances structurée en Markdown.
""")

# Sidebar pour la sélection du répertoire et les options
with st.sidebar:
    st.header("Configuration")
    
    # Sélection du répertoire
    directory = st.text_input(
        "Chemin du répertoire:",
        value=str(Path.home())
    )
    
    # Options de visualisation
    st.subheader("Options de visualisation")
    graph_height = st.slider("Hauteur du graphe", 400, 1000, 800)  # Hauteur augmentée à 800px
    max_nodes = st.slider("Nombre maximum de nœuds à afficher", 10, 300, 100)
    
    # Bouton pour analyser le répertoire
    if st.button("Analyser le répertoire"):
        if os.path.isdir(directory):
            with st.spinner("Analyse des fichiers Markdown..."):
                parsed_files = parse_markdown_directory(directory)
                
                if not parsed_files:
                    st.error("Aucun fichier Markdown trouvé dans le répertoire spécifié.")
                else:
                    # Construire le graphe
                    G = build_graph(parsed_files)
                    
                    # Sauvegarder dans la session
                    st.session_state['graph'] = G
                    st.session_state['parsed_files'] = parsed_files
                    
                    # Créer un dictionnaire pour accéder rapidement aux données
                    file_lookup = {file['title']: file for file in parsed_files}
                    st.session_state['file_lookup'] = file_lookup
                    
                    # Calculer les statistiques
                    stats = get_graph_stats(G)
                    st.session_state['stats'] = stats
                    
                    st.success(f"Analyse terminée: {len(parsed_files)} fichiers trouvés, {len(G.nodes)} nœuds et {len(G.edges)} liens dans le graphe.")
        else:
            st.error("Le chemin spécifié n'est pas un répertoire valide.")
    
    # Afficher des statistiques dans la sidebar si disponibles
    if 'stats' in st.session_state:
        st.subheader("Statistiques du graphe")
        stats = st.session_state['stats']
        st.write(f"Nœuds: {stats['num_nodes']}")
        st.write(f"Liens: {stats['num_edges']}")
        st.write(f"Composantes: {stats['connected_components']}")
        st.write(f"Degré moyen: {stats['avg_degree']:.2f}")

# Corps principal divisé en onglets
if 'graph' in st.session_state:
    tab1,  tab2, tab3 = st.tabs(["Visualisation", "Exploration", "Analyse de Pertinence"])
    
    # Onglet Visualisation
    with tab1:
        # Visualiser le graphe
        selected_node = st.session_state.get('selected_node', None)
        relevance_scores = st.session_state.get('relevance_scores', None)
        
        # Générer la visualisation
        try:
            html_file = visualize_graph(
                st.session_state['graph'], 
                height=graph_height, 
                selected_node=selected_node,
                max_nodes=max_nodes,
                relevance_scores=relevance_scores,
            )
            
            # Afficher le graphe interactif
            with open(html_file, 'r', encoding='utf-8') as f:
                html_string = f.read()
            components.html(html_string, height=graph_height)
            
            st.info("Note: Pour les grands graphes, seuls les nœuds les plus connectés sont affichés. Utilisez la recherche pour explorer plus en détail.")
            
            # Si des scores de pertinence sont calculés, ajouter une légende
            if relevance_scores:
                st.success("🔍 Les nœuds sont colorés selon leur pertinence: 🟢 Pertinent → 🔴 Non pertinent")
                
        except Exception as e:
            st.error(f"Erreur lors de l'affichage du graphe: {e}")
    
    
    # Onglet Exploration
    with tab2:
        st.header("Explorer le graphe")
        
        # Ajouter une fonction de filtrage pour les grands graphes
        node_filter = st.text_input("Filtrer les nœuds par nom:", "")
        
        # Liste déroulante pour sélectionner un nœud
        all_nodes = sorted(list(st.session_state['graph'].nodes()))
        
        # Filtrer les nœuds si nécessaire
        if node_filter:
            filtered_nodes = [node for node in all_nodes if node_filter.lower() in node.lower()]
            if not filtered_nodes:
                st.warning(f"Aucun nœud ne correspond à '{node_filter}'")
                node_to_explore = None
            else:
                node_to_explore = st.selectbox(
                    "Sélectionnez un nœud à explorer:",
                    filtered_nodes
                )
        else:
            node_to_explore = st.selectbox(
                "Sélectionnez un nœud à explorer:",
                all_nodes
            )
        
        if node_to_explore:
            # Récupérer les informations du nœud
            node_data = st.session_state['graph'].nodes[node_to_explore]
            
            # Afficher les détails du nœud
            st.subheader(node_data.get('title', node_to_explore))
            st.write(f"**Type:** {node_data.get('type', 'N/A')}")
            st.write(f"**Tags:** {', '.join(node_data.get('tags', []))}")
            
            # Récupérer et afficher les voisins
            successors, predecessors = get_node_neighbors(st.session_state['graph'], node_to_explore)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Liens sortants:**")
                if successors:
                    for target, rel_type in successors:
                        if st.button(f"{target} ({rel_type})", key=f"succ_{target}"):
                            st.session_state['detailed_node'] = target
                            st.rerun()
                else:
                    st.info("Aucun lien sortant.")
            
            with col2:
                st.write("**Liens entrants:**")
                if predecessors:
                    for source, rel_type in predecessors:
                        if st.button(f"{source} ({rel_type})", key=f"pred_{source}"):
                            st.session_state['detailed_node'] = source
                            st.rerun()
                else:
                    st.info("Aucun lien entrant.")
            
            # Bouton pour visualiser ce nœud dans le graphe
            if st.button("Visualiser dans le graphe"):
                st.session_state['selected_node'] = node_to_explore
                st.rerun()
    
    # Onglet Analyse de Pertinence
    with tab3:
        st.header("Analyse de Pertinence")
        
        # Interface de requête avec exemple
        relevance_query = st.text_area(
            "Entrez votre requête pour colorer les nœuds selon leur pertinence:",
            placeholder="Exemple: techniques d'apprentissage automatique pour le traitement du langage naturel",
            height=100
        )
        
        # Configuration des poids des différentes métriques
        st.subheader("Configuration des métriques")
        
        col1, col2 = st.columns(2)
        
        with col1:
            cosine_weight = st.slider("Similarité cosinus (embeddings)", 0, 100, 50, 1, 
                                     help="Utilise des embeddings vectoriels pour mesurer la similarité sémantique")
            
            tfidf_weight = st.slider("TF-IDF", 0, 100, 20, 1,
                                    help="Compare les fréquences des mots pour mesurer la similarité lexicale")
            
        with col2:
            bm25_weight = st.slider("BM25", 0, 100, 20, 1,
                                   help="Algorithme de ranking optimisé pour la recherche documentaire")
            
            jaccard_weight = st.slider("Jaccard (tags)", 0, 100, 10, 1,
                                      help="Compare les tags pour mesurer la similarité thématique")
        
        # Calculer et afficher les poids normalisés
        total_weight = cosine_weight + tfidf_weight + bm25_weight + jaccard_weight
        
        if total_weight > 0:
            cosine_normalized = cosine_weight / total_weight
            tfidf_normalized = tfidf_weight / total_weight
            bm25_normalized = bm25_weight / total_weight
            jaccard_normalized = jaccard_weight / total_weight
            
            st.write(f"**Coefficients normalisés:**")
            st.write(f"- Similarité cosinus: {cosine_normalized:.3f}")
            st.write(f"- TF-IDF: {tfidf_normalized:.3f}")
            st.write(f"- BM25: {bm25_normalized:.3f}")
            st.write(f"- Jaccard (tags): {jaccard_normalized:.3f}")
        else:
            st.warning("Au moins un des poids doit être supérieur à zéro.")
            cosine_normalized = tfidf_normalized = bm25_normalized = jaccard_normalized = 0

        # Initialiser le cache pour les embeddings
        if 'cached_embeddings' not in st.session_state:
            st.session_state['cached_embeddings'] = None
        
        # Bouton pour calculer la pertinence
        if st.button("Calculer et appliquer la coloration"):
            if not relevance_query:
                st.warning("Veuillez saisir une requête pour continuer.")
            elif total_weight == 0:
                st.warning("Au moins un coefficient doit être supérieur à zéro.")
            else:
                with st.spinner("Calcul des scores de pertinence..."):
                    try:
                        # Créer le dictionnaire de poids
                        weights = {
                            'cosine': cosine_normalized,
                            'tfidf': tfidf_normalized,
                            'bm25': bm25_normalized,
                            'jaccard': jaccard_normalized
                        }
                        
                        # Obtenir le client LLM pour générer des tags si nécessaire
                        llm_client = None
                        if jaccard_normalized > 0:
                            try:
                                llm_client = get_llm_client()
                            except:
                                st.warning("Impossible de connecter au service LLM. L'algorithme Jaccard fonctionnera sans générer de tags.")
                        
                        # Calculer les scores de pertinence en utilisant le cache
                        relevance_scores, new_embeddings, individual_scores = calculate_combined_scores(
                            st.session_state['graph'],
                            relevance_query,
                            weights,
                            llm_client,
                            cached_embeddings=st.session_state['cached_embeddings']
                        )
                        
                        # Convertir explicitement en dictionnaire de nombres flottants Python standard
                        clean_scores = {}
                        for node, score in relevance_scores.items():
                            try:
                                clean_scores[node] = float(score)
                            except:
                                clean_scores[node] = 0.0
                        
                        # Stocker les scores dans la session
                        st.session_state['relevance_scores'] = clean_scores
                        
                        # Mettre à jour le cache d'embeddings si possible
                        if new_embeddings is not None:
                            st.session_state['cached_embeddings'] = new_embeddings
                        
                        # Afficher les nœuds les plus pertinents
                        sorted_nodes = sorted(clean_scores.items(), key=lambda x: x[1], reverse=True)
                        
                        # Créer un DataFrame avec les scores détaillés
                        top_nodes = sorted_nodes[:10]
                        
                        detailed_scores_df = pd.DataFrame([
                            {
                                "Nœud": node,
                                "Score combiné": f"{score:.3f}",
                                "Cosinus": f"{individual_scores['cosine'].get(node, 0):.3f}",
                                "TF-IDF": f"{individual_scores['tfidf'].get(node, 0):.3f}",
                                "BM25": f"{individual_scores['bm25'].get(node, 0):.3f}",
                                "Jaccard": f"{individual_scores['jaccard'].get(node, 0):.3f}"
                            } for node, score in top_nodes
                        ])
                        
                        st.subheader("Top 10 des nœuds les plus pertinents")
                        st.table(detailed_scores_df)
                        
                        st.success("Scores de pertinence calculés! Les nœuds sont maintenant colorés du rouge (faible pertinence) au vert (haute pertinence) dans la visualisation.")
                        st.info("Rendez-vous dans l'onglet 'Visualisation' pour voir le résultat.")
                        
                        # Stocker les noeuds triés dans la session state pour les réutiliser plus tard
                        st.session_state['sorted_nodes'] = sorted_nodes
                        
                    except Exception as e:
                        st.error(f"Erreur lors du calcul des scores de pertinence: {e}")
                        import traceback
                        st.error(traceback.format_exc())
        
        # Extraction de contexte pour requête LLM (si des scores ont été calculés)
        if 'sorted_nodes' in st.session_state:
            st.divider()
            st.subheader("Extraction de contexte pour requête LLM")
            
            # Option pour définir un seuil de pertinence
            threshold = st.slider(
                "Seuil de pertinence (score minimum)",
                min_value=0.0,
                max_value=1.0,
                value=0.5,
                step=0.05,
                help="Sélectionne les documents avec un score supérieur ou égal à ce seuil"
            )
            
            # Option pour définir une profondeur de contexte
            depth = st.slider(
                "Profondeur de contexte",
                min_value=0,
                max_value=3,
                value=1,
                step=1,
                help="0 = seulement les documents pertinents, 1 = documents pertinents + voisins directs, etc."
            )
            
            # Bouton pour extraire le contexte
            if st.button("Extraire le contexte"):
                # Sélectionner les documents pertinents selon le seuil
                sorted_nodes = st.session_state['sorted_nodes']
                relevant_nodes = [node for node, score in sorted_nodes if score >= threshold]
                
                if not relevant_nodes:
                    st.warning(f"Aucun document ne dépasse le seuil de pertinence de {threshold}.")
                else:
                    # Si profondeur > 0, inclure les voisins
                    if depth > 0:
                        with st.spinner(f"Extraction des nœuds jusqu'à la profondeur {depth}..."):
                            context_nodes = get_nodes_within_depth(
                                st.session_state['graph'],
                                relevant_nodes,
                                depth
                            )
                    else:
                        context_nodes = set(relevant_nodes)
                    
                    # Extraire le contenu des documents sélectionnés
                    context_docs = []
                    for node in context_nodes:
                        if node in st.session_state['file_lookup']:
                            doc_data = st.session_state['file_lookup'][node]
                            content = doc_data.get('content', '')
                            # Supprimer les métadonnées YAML
                            import re
                            content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
                            
                            context_docs.append({
                                'title': node,
                                'content': content,
                                'is_relevant': node in relevant_nodes  # Indique si le nœud était dans la sélection initiale
                            })
                    
                    # Stocker le contexte dans la session
                    st.session_state['context_docs'] = context_docs
                    
                    # Afficher un résumé
                    st.success(f"Contexte extrait: {len(context_docs)} documents ({len(relevant_nodes)} pertinents + {len(context_docs) - len(relevant_nodes)} voisins)")
                    
                    # Afficher la liste des documents
                    context_df = pd.DataFrame([
                        {
                            "Document": doc['title'],
                            "Pertinent": "✓" if doc['is_relevant'] else "○",
                            "Longueur": len(doc['content'])
                        } for doc in context_docs
                    ])
                    
                    st.table(context_df)
            
            # Interface pour la requête LLM
            if 'context_docs' in st.session_state and st.session_state['context_docs']:
                st.divider()
                st.subheader("Requête au LLM avec contexte")
                
                # Zone de texte pour la question
                llm_query = st.text_area(
                    "Votre question:",
                    placeholder="Posez une question basée sur les documents extraits..."
                )
                
                # Bouton pour envoyer la requête au LLM
                if st.button("Obtenir une réponse") and llm_query:
                    with st.spinner("Génération de la réponse..."):
                        try:
                            # Obtenir le client LLM
                            llm_client = get_llm_client()
                            
                            if not llm_client:
                                st.error("Impossible de se connecter au service LLM.")
                            else:
                                # Préparer le contexte
                                context_text = "\n\n".join([
                                    f"# {doc['title']}\n{doc['content']}" 
                                    for doc in st.session_state['context_docs']
                                ])
                                
                                # Créer le prompt
                                system_prompt = QA_SYSTEM_PROMPT
                                                                
                                user_prompt = QA_USER_PROMPT_TEMPLATE.format(
                                    query=llm_query,
                                    context=context_text
                                )
                                
                                response = llm_client.chat.completions.create(
                                    model=LLM_MODEL,
                                    messages=[
                                        {"role": "system", "content": system_prompt},
                                        {"role": "user", "content": user_prompt}
                                    ],
                                    temperature=DEFAULT_TEMPERATURE,
                                    max_tokens=DEFAULT_MAX_TOKENS
                                )
                                
                                # Afficher la réponse
                                st.success("Réponse générée!")
                                st.markdown(response.choices[0].message.content)
                                
                                # Option pour afficher le prompt complet
                                with st.expander("Voir le prompt complet"):
                                    st.code(user_prompt)
                        
                        except Exception as e:
                            st.error(f"Erreur lors de la génération de la réponse: {e}")
                            import traceback
                            st.error(traceback.format_exc())
        
        # Option pour réinitialiser
        if 'relevance_scores' in st.session_state:
            if st.button("Réinitialiser la coloration"):
                del st.session_state['relevance_scores']
                if 'sorted_nodes' in st.session_state:
                    del st.session_state['sorted_nodes']
                if 'context_docs' in st.session_state:
                    del st.session_state['context_docs']
                st.success("Coloration réinitialisée.")
                st.rerun()

# Afficher le contenu détaillé d'un nœud si sélectionné
if 'detailed_node' in st.session_state and 'file_lookup' in st.session_state:
    node_id = st.session_state['detailed_node']
    
    if node_id in st.session_state['file_lookup']:
        st.header(f"Contenu: {node_id}")
        
        file_data = st.session_state['file_lookup'][node_id]
        
        # Afficher des informations de base
        st.write(f"**Type:** {file_data.get('type', 'N/A')}")
        st.write(f"**Tags:** {', '.join(file_data.get('tags', []))}")
        
        # Extraire et afficher le contenu sans les métadonnées YAML
        content = file_data['content']
        import re
        content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
        
        st.markdown(content)
        
        # Ajouter des boutons d'action
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Fermer"):
                del st.session_state['detailed_node']
                st.rerun()
        with col2:
            if st.button("Visualiser ce nœud"):
                st.session_state['selected_node'] = node_id
                del st.session_state['detailed_node']
                st.rerun()

# Afficher un message si aucun graphe n'est chargé
if 'graph' not in st.session_state:
    st.info("Veuillez sélectionner un répertoire contenant des fichiers Markdown et cliquer sur 'Analyser le répertoire' pour commencer.")
    
    # Exemple de structure attendue
    with st.expander("Voir un exemple de structure de fichier Markdown attendue"):
        st.code("""---
title: "Titre du document"
type: "concept/technique/application/acteur/etc."
tags: ["tag1", "tag2"]
relations:
  - type: "rdfs:subClassOf"
    target: "[[Document parent]]"
  - type: "rdfs:seeAlso"
    target: ["[[Document connexe 1]]", "[[Document connexe 2]]"]
date_creation: "YYYY-MM-DD"
date_modification: "YYYY-MM-DD"
---

Contenu du document...
""", language="markdown")