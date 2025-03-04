import os
import streamlit as st
import re
import yaml
from datetime import datetime
from ui.state import get_service

def render_creation_tab():
    """Render the node creation tab content."""
    st.header("Création de Nœud")
    
    if 'graph' not in st.session_state:
        st.info("Aucun graphe n'est chargé. Veuillez analyser un répertoire pour pouvoir créer des nœuds.")
        return
    
    # Récupérer les services
    graph_service = get_service('graph_service')
    llm_service = get_service('llm_service')
    storage_service = get_service('storage_service')
    
    # Récupérer les types et tags existants
    existing_types = set()
    existing_tags = set()
    
    for _, attrs in st.session_state['graph'].nodes(data=True):
        if 'type' in attrs and attrs['type']:
            existing_types.add(attrs['type'])
        if 'tags' in attrs:
            existing_tags.update(attrs['tags'])
    
    # Convertir en listes triées
    existing_types = sorted(list(existing_types))
    existing_tags = sorted(list(existing_tags))
    
    # Interface de création
    st.subheader("Nouveau Document")
    
    # Titre du document
    title = st.text_input("Titre", value="", help="Titre du document")
    
    # Type du document (avec suggestions des types existants)
    if existing_types:
        node_type = st.selectbox("Type", [""] + existing_types, help="Type de document")
    else:
        node_type = st.text_input("Type", value="", help="Type de document (ex: concept, technique, personne...)")
    
    # Tags multiples avec autocomplete
    if 'creation_tags' not in st.session_state:
        st.session_state.creation_tags = []
    
    # Interface pour ajouter des tags
    tag_input = st.text_input("Ajouter un tag", value="", key="tag_input")
    tag_suggestions = [tag for tag in existing_tags if tag_input.lower() in tag.lower()]
    
    if tag_suggestions and tag_input:
        suggested_tag = st.selectbox("Suggestions de tags", tag_suggestions)
        if st.button("Ajouter ce tag"):
            if suggested_tag not in st.session_state.creation_tags:
                st.session_state.creation_tags.append(suggested_tag)
    elif tag_input:
        if st.button("Créer nouveau tag"):
            if tag_input not in st.session_state.creation_tags:
                st.session_state.creation_tags.append(tag_input)
    
    # Afficher et gérer les tags sélectionnés
    if st.session_state.creation_tags:
        st.write("Tags sélectionnés:")
        cols = st.columns(4)
        for i, tag in enumerate(st.session_state.creation_tags):
            col_idx = i % 4
            with cols[col_idx]:
                if st.button(f"❌ {tag}", key=f"remove_tag_{i}"):
                    st.session_state.creation_tags.remove(tag)
                    st.rerun()
    
    # Contenu Markdown
    st.subheader("Contenu")
    content = st.text_area("Contenu Markdown", height=300, help="Contenu au format Markdown")
    
    # Bouton pour analyser le contenu et suggérer des métadonnées
    if st.button("Suggérer métadonnées") and content:
        with st.spinner("Analyse du contenu..."):
            suggested_metadata = llm_service.suggest_metadata(
                content, 
                existing_types=existing_types,
                existing_tags=list(existing_tags)
            )
            
            # Mettre à jour l'interface avec les suggestions
            if suggested_metadata["title"] and not title:
                st.session_state.suggested_title = suggested_metadata["title"]
                
            if suggested_metadata["type"] and not node_type:
                st.session_state.suggested_type = suggested_metadata["type"]
                
            if suggested_metadata["tags"]:
                st.session_state.suggested_tags = suggested_metadata["tags"]
            
            st.success("Suggestions générées!")
            st.rerun()
    
    # Afficher les suggestions
    if 'suggested_title' in st.session_state and not title:
        title = st.session_state.suggested_title
        st.info(f"Titre suggéré: {title}")
        
    if 'suggested_type' in st.session_state and not node_type:
        node_type = st.session_state.suggested_type
        st.info(f"Type suggéré: {node_type}")
        
    if 'suggested_tags' in st.session_state and not st.session_state.creation_tags:
        st.info(f"Tags suggérés: {', '.join(st.session_state.suggested_tags)}")
        if st.button("Utiliser ces tags"):
            st.session_state.creation_tags = st.session_state.suggested_tags
            st.rerun()
    
    # Section pour trouver des connexions potentielles
    if content and st.button("Trouver connexions potentielles"):
        with st.spinner("Recherche de nœuds similaires..."):
            # S'assurer que le modèle d'embedding est disponible dans le KnowledgeGraph
            if not hasattr(graph_service.knowledge_graph, 'text_encoder') or graph_service.knowledge_graph.text_encoder is None:
                embedding_service = get_service('embedding_service')
                graph_service.knowledge_graph.text_encoder = embedding_service.get_model()
                
            similar_nodes = graph_service.knowledge_graph.find_similar_nodes(content, top_k=10)
            
            if similar_nodes:
                st.subheader("Connexions potentielles")
                st.write("Ces nœuds existants semblent liés à votre contenu:")
                
                # Afficher les nœuds similaires avec leurs scores
                for node_id, score in similar_nodes:
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.write(f"**{node_id}**")
                    with col2:
                        st.write(f"Score: {score:.2f}")
                    with col3:
                        if st.button("Lier", key=f"link_{node_id}"):
                            if 'relations_to_add' not in st.session_state:
                                st.session_state.relations_to_add = []
                            st.session_state.relations_to_add.append(node_id)
                            st.success(f"Lien avec '{node_id}' ajouté!")
            else:
                st.info("Aucun nœud similaire trouvé.")
    
    # Afficher les relations à ajouter
    if 'relations_to_add' in st.session_state and st.session_state.relations_to_add:
        st.subheader("Relations à créer")
        for i, target in enumerate(st.session_state.relations_to_add):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"Lien vers: **{target}**")
            with col2:
                if st.button("Supprimer", key=f"remove_rel_{i}"):
                    st.session_state.relations_to_add.remove(target)
                    st.rerun()
    
    # Bouton de création finale
    if st.button("Créer le nœud") and title and content:
        # Préparer les métadonnées
        metadata = {
            "title": title,
            "type": node_type,
            "tags": st.session_state.creation_tags,
            "date_creation": datetime.now().strftime("%Y-%m-%d"),
            "date_modification": datetime.now().strftime("%Y-%m-%d")
        }
        
        # Ajouter les relations si définies
        if 'relations_to_add' in st.session_state and st.session_state.relations_to_add:
            metadata["relations"] = []
            for target in st.session_state.relations_to_add:
                metadata["relations"].append({
                    "type": "rdfs:seeAlso",
                    "target": f"[[{target}]]"
                })
        
        try:
            # Sauvegarder le fichier
            directory = os.path.dirname(st.session_state['parsed_files'][0]['path'])
            file_path = storage_service.save_markdown_file(directory, title, content, metadata)
            
            # Ajouter au graphe
            st.session_state['parsed_files'].append({
                'path': file_path,
                'filename': os.path.basename(file_path),
                'title': title,
                'type': node_type,
                'tags': st.session_state.creation_tags.copy(),
                'relations': [(rel['type'], rel['target'][2:-2]) for rel in metadata.get('relations', [])],
                'internal_links': [],
                'content': content
            })
            
            # Mettre à jour le graphe
            graph_service.load_or_create_graph(st.session_state['parsed_files'])
            
            # Mettre à jour l'interface
            st.success(f"Nœud '{title}' créé avec succès!")
            
            # Réinitialiser les champs
            st.session_state.creation_tags = []
            if 'relations_to_add' in st.session_state:
                del st.session_state.relations_to_add
            if 'suggested_title' in st.session_state:
                del st.session_state.suggested_title
            if 'suggested_type' in st.session_state:
                del st.session_state.suggested_type
            if 'suggested_tags' in st.session_state:
                del st.session_state.suggested_tags
                
            # Recalculer les statistiques
            stats = graph_service.get_graph_stats()
            st.session_state['stats'] = stats
            
            st.rerun()
            
        except Exception as e:
            st.error(f"Erreur lors de la création du nœud: {e}")
    
    # Aide pour le format Markdown
    with st.expander("Aide format Markdown"):
        st.markdown("""
        ## Syntaxe Markdown de base
        
        - **Gras**: `**texte**`
        - *Italique*: `*texte*`
        - Titre: `# Titre`, `## Sous-titre`, etc.
        - Liste: `- élément` ou `1. élément`
        - [Lien](https://exemple.com): `[texte](url)`
        - Lien interne vers un autre nœud: `[[nom du nœud]]`
        - Code: `` `code` ``
        - Bloc de code:
        ```
        ```python
        def hello():
            print("Hello world")
        ```
        ```
        """)