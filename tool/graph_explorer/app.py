import streamlit as st
from ui.components.sidebar import render_sidebar
from ui.pages.visualization_tab import render_visualization_tab
from ui.pages.exploration_tab import render_exploration_tab
from ui.pages.analysis_tab import render_analysis_tab
from ui.pages.creation_tab import render_creation_tab
from ui.state import initialize_services

# Configuration de la page
st.set_page_config(
    page_title="Explorateur de Graphe de Connaissances",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialiser les services
initialize_services()

# Titre et description
st.markdown("""
# 🔍 Explorateur de Graphe de Connaissances

Cet outil vous permet d'analyser, visualiser et explorer une base de connaissances structurée en Markdown.
""")

# Sidebar pour la configuration
render_sidebar()

# Corps principal divisé en onglets
if 'graph' in st.session_state:
    tab1, tab2, tab3, tab4 = st.tabs([
        "Visualisation", 
        "Exploration", 
        "Analyse de Pertinence",
        "Création de Nœud"  # Nouvel onglet
    ])
    
    # Onglet Visualisation
    with tab1:
        render_visualization_tab()
    
    # Onglet Exploration
    with tab2:
        render_exploration_tab()
    
    # Onglet Analyse de Pertinence
    with tab3:
        render_analysis_tab()
        
    # Onglet Création de Nœud
    with tab4:
        render_creation_tab()

# Afficher un message si aucun graphe n'est chargé
else:
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