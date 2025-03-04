import streamlit as st
from pathlib import Path
import os
from ui.state import get_service

def render_sidebar():
    """Render the application sidebar."""
    with st.sidebar:
        st.header("Configuration")
        
        # Sélection du répertoire
        directory = st.text_input(
            "Chemin du répertoire:",
            value=str(Path.home())
        )
        
        # Options de visualisation
        st.subheader("Options de visualisation")
        graph_height = st.slider("Hauteur du graphe", 400, 1000, 800)
        max_nodes = st.slider("Nombre maximum de nœuds", 10, 300, 100)
        
        # Stockage dans la session state
        st.session_state.graph_height = graph_height
        st.session_state.max_nodes = max_nodes
        
        # Bouton pour analyser le répertoire
        if st.button("Analyser le répertoire"):
            analyze_directory(directory)
            
        # Option pour forcer la reconstruction du graphe
        if 'graph' in st.session_state and 'parsed_files' in st.session_state:
            if st.button("⟳ Reconstruire le graphe d'embeddings"):
                with st.spinner("Reconstruction du graphe d'embeddings..."):
                    try:
                        # Récupérer les services nécessaires
                        graph_service = get_service('graph_service')
                        embedding_service = get_service('embedding_service')
                        
                        # Forcer la reconstruction complète
                        # 1. Supprimer le graphe actuel de la mémoire
                        if hasattr(graph_service, 'knowledge_graph'):
                            # Réinitialiser manuellement le singleton
                            from domain.knowledge_graph import KnowledgeGraph
                            KnowledgeGraph._instance = None
                            
                        # 2. Reconstruire avec les données existantes
                        parsed_files = st.session_state['parsed_files']
                        G = graph_service.load_or_create_graph(
                            parsed_files=parsed_files,
                            embedding_model=embedding_service.get_model(),
                            force_rebuild=True  # Option à ajouter à GraphService
                        )
                        
                        # 3. Mettre à jour la session Streamlit
                        st.session_state['graph'] = G.G
                        
                        st.success("✓ Graphe d'embeddings reconstruit avec succès!")
                    except Exception as e:
                        st.error(f"Erreur lors de la reconstruction: {e}")
                        import traceback
                        st.error(traceback.format_exc())
            
            # Afficher des statistiques dans la sidebar si disponibles
            if 'stats' in st.session_state:
                st.subheader("Statistiques du graphe")
                stats = st.session_state['stats']
                st.write(f"Nœuds: {stats['num_nodes']}")
                st.write(f"Liens: {stats['num_edges']}")
                st.write(f"Composantes: {stats['connected_components']}")
                st.write(f"Degré moyen: {stats['avg_degree']:.2f}")

def analyze_directory(directory):
    """Analyze the markdown files in the specified directory."""
    if os.path.isdir(directory):
        with st.spinner("Analyse des fichiers Markdown..."):
            # Obtenir les services nécessaires
            storage_service = get_service('storage_service')
            graph_service = get_service('graph_service')
            embedding_service = get_service('embedding_service')
            
            # Parser les fichiers Markdown
            parsed_files = storage_service.parse_directory(directory)
            
            if not parsed_files:
                st.error("Aucun fichier Markdown trouvé dans le répertoire spécifié.")
            else:
                # Construire le graphe
                G = graph_service.load_or_create_graph(parsed_files, embedding_service)
                
                # Sauvegarder dans la session
                st.session_state['parsed_files'] = parsed_files
                
                # Créer un dictionnaire pour accéder rapidement aux données
                file_lookup = {file['title']: file for file in parsed_files}
                st.session_state['file_lookup'] = file_lookup
                
                # Calculer les statistiques
                stats = graph_service.get_graph_stats()
                st.session_state['stats'] = stats
                
                # Garder une référence au graphe NetworkX pour la visualisation
                st.session_state['graph'] = G.G
                
                st.success(f"Analyse terminée: {len(parsed_files)} fichiers trouvés, {len(G.G.nodes)} nœuds et {len(G.G.edges)} liens dans le graphe.")
    else:
        st.error("Le chemin spécifié n'est pas un répertoire valide.")