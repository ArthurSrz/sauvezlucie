import streamlit as st
import re
from ui.state import get_service, set_current_node

def render_exploration_tab():
    """Render the exploration tab content."""
    st.header("Explorer le graphe")
    
    if 'graph' not in st.session_state:
        st.info("Aucun graphe n'est chargé. Veuillez analyser un répertoire.")
        return
    
    # Récupérer les services
    graph_service = get_service('graph_service')
    
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
        successors, predecessors = graph_service.get_node_neighbors(node_to_explore)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Liens sortants:**")
            if successors:
                for target, rel_type in successors:
                    if st.button(f"{target} ({rel_type})", key=f"succ_{target}"):
                        display_node_details(target)
            else:
                st.info("Aucun lien sortant.")
        
        with col2:
            st.write("**Liens entrants:**")
            if predecessors:
                for source, rel_type in predecessors:
                    if st.button(f"{source} ({rel_type})", key=f"pred_{source}"):
                        display_node_details(source)
            else:
                st.info("Aucun lien entrant.")
        
        # Bouton pour visualiser ce nœud dans le graphe
        if st.button("Visualiser dans le graphe"):
            set_current_node(node_to_explore)
            st.rerun()
            
        # Afficher le contenu du nœud
        with st.expander("Contenu du nœud", expanded=False):
            content = node_data.get('content', '')
            # Nettoyer le contenu (retirer les métadonnées YAML)
            content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
            st.markdown(content)
            
def display_node_details(node_id):
    """Affiche les détails d'un nœud et met à jour l'état."""
    st.session_state['detailed_node'] = node_id
    st.rerun()

def render_node_details(node_id):
    """Render detailed information about a specific node."""
    if 'file_lookup' not in st.session_state:
        return
        
    if node_id in st.session_state['file_lookup']:
        st.header(f"Contenu: {node_id}")
        
        file_data = st.session_state['file_lookup'][node_id]
        
        # Afficher des informations de base
        st.write(f"**Type:** {file_data.get('type', 'N/A')}")
        st.write(f"**Tags:** {', '.join(file_data.get('tags', []))}")
        
        # Extraire et afficher le contenu sans les métadonnées YAML
        content = file_data['content']
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
                set_current_node(node_id)
                del st.session_state['detailed_node']
                st.rerun()