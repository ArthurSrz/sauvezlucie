import streamlit as st
from services import (
    GraphService, 
    StorageService, 
    SearchService, 
    LLMService, 
    EmbeddingService, 
    VisualizationService
)

def initialize_services():
    """Initialise tous les services nécessaires à l'application."""
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        
        # Initialiser l'ordre est important car certains services dépendent d'autres
        embedding_service = EmbeddingService()
        st.session_state.embedding_service = embedding_service
        
        st.session_state.llm_service = LLMService()
        st.session_state.storage_service = StorageService()
        st.session_state.search_service = SearchService(embedding_service=embedding_service)
        st.session_state.graph_service = GraphService()
        st.session_state.visualization_service = VisualizationService()

def get_service(service_name):
    """Récupère un service par son nom."""
    initialize_services()
    
    if service_name not in st.session_state:
        raise ValueError(f"Service '{service_name}' non trouvé")
        
    return st.session_state[service_name]

def set_current_node(node_id):
    """Définit le nœud actuellement sélectionné."""
    st.session_state.selected_node = node_id
    
def get_current_node():
    """Récupère le nœud actuellement sélectionné."""
    return st.session_state.get('selected_node', None)

def set_relevance_scores(scores):
    """Définit les scores de pertinence."""
    st.session_state.relevance_scores = scores
    
def get_relevance_scores():
    """Récupère les scores de pertinence."""
    return st.session_state.get('relevance_scores', None)

def clear_relevance_scores():
    """Efface les scores de pertinence."""
    if 'relevance_scores' in st.session_state:
        del st.session_state['relevance_scores']
    if 'sorted_nodes' in st.session_state:
        del st.session_state['sorted_nodes']
    if 'context_docs' in st.session_state:
        del st.session_state['context_docs']