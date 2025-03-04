import streamlit as st
import streamlit.components.v1 as components
from ui.state import get_service, get_current_node, get_relevance_scores

def render_visualization_tab():
    """Render the visualization tab content."""
    st.header("Visualisation du Graphe")
    
    if 'graph' not in st.session_state:
        st.info("Aucun graphe n'est chargé. Veuillez analyser un répertoire.")
        return
    
    # Récupérer les services et paramètres
    visualization_service = get_service('visualization_service')
    G = st.session_state['graph']
    height = st.session_state.graph_height
    max_nodes = st.session_state.max_nodes
    
    # Obtenir le nœud sélectionné et les scores de pertinence
    selected_node = get_current_node()
    relevance_scores = get_relevance_scores()
    
    # Générer la visualisation
    try:
        html_file = visualization_service.visualize_graph(
            G, 
            height=height, 
            selected_node=selected_node,
            max_nodes=max_nodes,
            relevance_scores=relevance_scores,
        )
        
        # Afficher le graphe interactif
        with open(html_file, 'r', encoding='utf-8') as f:
            html_string = f.read()
        components.html(html_string, height=height)
        
        st.info("Note: Pour les grands graphes, seuls les nœuds les plus connectés sont affichés. Utilisez la recherche pour explorer plus en détail.")
        
        # Si des scores de pertinence sont calculés, ajouter une légende
        if relevance_scores:
            st.success("🔍 Les nœuds sont colorés selon leur pertinence: 🟢 Pertinent → 🔴 Non pertinent")
            
    except Exception as e:
        st.error(f"Erreur lors de l'affichage du graphe: {e}")