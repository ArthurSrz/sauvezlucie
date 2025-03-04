import streamlit as st
import pandas as pd
import re
from ui.state import (
    get_service, 
    set_relevance_scores, 
    get_relevance_scores,
    clear_relevance_scores
)

def render_analysis_tab():
    """Render the relevance analysis tab content."""
    st.header("Analyse de Pertinence")
    
    if 'graph' not in st.session_state:
        st.info("Aucun graphe n'est chargé. Veuillez analyser un répertoire.")
        return
    
    # Récupérer les services
    search_service = get_service('search_service')
    graph_service = get_service('graph_service')
    llm_service = get_service('llm_service')
    
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
                    
                    # Calculer les scores de pertinence
                    try:
                        relevance_scores, new_embeddings, individual_scores, embeddings_dict = search_service.calculate_combined_scores(
                            st.session_state['graph'],
                            relevance_query,
                            weights,
                            llm_service if jaccard_normalized > 0 else None,
                            cached_embeddings=st.session_state.get('cached_embeddings')
                        )
                        
                        # Stocker le dictionnaire de cache
                        if embeddings_dict:
                            st.session_state['cached_embeddings_dict'] = embeddings_dict
                            
                    except (ValueError, TypeError):
                        # Pour compatibilité avec l'ancienne version de la fonction
                        relevance_scores, new_embeddings, individual_scores = search_service.calculate_combined_scores(
                            st.session_state['graph'],
                            relevance_query,
                            weights,
                            llm_service if jaccard_normalized > 0 else None,
                            cached_embeddings=st.session_state.get('cached_embeddings')
                        )
                    
                    # Convertir en dictionnaire de nombres flottants standard
                    clean_scores = {}
                    for node, score in relevance_scores.items():
                        try:
                            clean_scores[node] = float(score)
                        except:
                            clean_scores[node] = 0.0
                    
                    # Stocker les scores dans la session
                    set_relevance_scores(clean_scores)
                    
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
        render_context_extraction(graph_service, llm_service)
    
    # Option pour réinitialiser
    if get_relevance_scores() is not None:
        if st.button("Réinitialiser la coloration"):
            clear_relevance_scores()
            st.success("Coloration réinitialisée.")
            st.rerun()

def render_context_extraction(graph_service, llm_service):
    """Render the context extraction section."""
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
                    context_nodes = graph_service.get_nodes_within_depth(
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
                    response = llm_service.generate_answer(
                        llm_query, 
                        st.session_state['context_docs']
                    )
                    
                    # Afficher la réponse
                    st.success("Réponse générée!")
                    st.markdown(response)
                    
                    # Option pour afficher le prompt complet
                    with st.expander("Voir le contexte utilisé"):
                        st.info(f"Nombre de documents utilisés: {len(st.session_state['context_docs'])}")
                        for doc in st.session_state['context_docs']:
                            st.markdown(f"#### {doc['title']}")
                            st.markdown(doc['content'][:500] + "..." if len(doc['content']) > 500 else doc['content'])
                            st.divider()
                    
                except Exception as e:
                    st.error(f"Erreur lors de la génération de la réponse: {e}")
                    import traceback
                    st.error(traceback.format_exc())