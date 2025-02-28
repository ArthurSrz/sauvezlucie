from pyvis.network import Network
import streamlit.components.v1 as components
import tempfile
import os
import networkx as nx
import colorsys

def get_distinct_colors(n):
    """Génère n couleurs distinctes pour la visualisation."""
    colors = []
    for i in range(n):
        hue = i / n
        saturation = 0.7
        value = 0.9
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        hex_color = "#{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
        )
        colors.append(hex_color)
    return colors

def visualize_graph(G, height=600, selected_node=None, max_nodes=150, relevance_scores=None):
    """
    Crée une visualisation interactive du graphe avec pyvis.
    """
    # Si le graphe est trop grand, sélectionner un sous-graphe
    if len(G.nodes) > max_nodes and selected_node is None:
        # Prendre les nœuds avec le plus de connections
        degree_dict = dict(G.degree())
        top_nodes = sorted(degree_dict, key=degree_dict.get, reverse=True)[:max_nodes]
        G = G.subgraph(top_nodes)
    elif selected_node is not None:
        # Si un nœud est sélectionné, montrer ce nœud et ses voisins
        neighbors = list(nx.all_neighbors(G, selected_node))
        nodes_to_show = [selected_node] + neighbors
        if len(nodes_to_show) > max_nodes:
            nodes_to_show = nodes_to_show[:max_nodes]
        G = G.subgraph(nodes_to_show)
    
    # Créer un réseau pyvis
    net = Network(height=f"{height}px", width="100%", notebook=True, directed=True)
    
    # Définir des couleurs pour les différents types de nœuds
    node_types = set()
    for _, attrs in G.nodes(data=True):
        node_types.add(attrs.get('type', 'unknown'))
    
    # Générer des couleurs distinctes
    colors = get_distinct_colors(len(node_types))
    color_map = {ntype: colors[i] for i, ntype in enumerate(node_types)}
    
    # Ajouter les nœuds avec leurs attributs
    for node, attrs in G.nodes(data=True):
        node_type = attrs.get('type', 'unknown')
        title = f"<b>{attrs.get('title', node)}</b><br>Type: {node_type}<br>Tags: {', '.join(attrs.get('tags', []))}"
        
        # Définir la taille et les options de mise en évidence
        size = 25
        border_width = 1
        font_size = 14
        
        if node == selected_node:
            size = 35
            border_width = 3
            font_size = 18
        
        # Déterminer la couleur du nœud de façon sécurisée
        if relevance_scores is not None and node in relevance_scores:
            try:
                score = float(relevance_scores[node])
                score = max(0, min(1, score))  # Assurer que le score est entre 0 et 1
                r = int(255 * (1 - score))
                g = int(255 * score)
                b = 0
                color = f"#{r:02x}{g:02x}{b:02x}"
                title += f"<br>Score de pertinence: {score:.3f}"
            except:
                color = color_map.get(node_type, '#cccccc')
        else:
            color = color_map.get(node_type, '#cccccc')
        
        net.add_node(
            node, 
            label=node, 
            title=title, 
            color=color,
            size=size,
            borderWidth=border_width,
            font={'size': font_size}
        )
    
    # Ajouter les arêtes
    for source, target, attrs in G.edges(data=True):
        edge_type = attrs.get('type', 'link')
        edge_title = f"Type: {edge_type}"
        net.add_edge(source, target, title=edge_title, arrows='to')
    
    # Centrage sur le nœud sélectionné
    if selected_node is not None:
        script = f"""
        setTimeout(function() {{
            try {{
                network.focus('{selected_node}');
            }} catch(e) {{
                console.error("Focus error:", e);
            }}
        }}, 1000);
        """
        net.set_options(net.options + script)
    
    # Créer un répertoire temporaire persistant si nécessaire
    temp_dir = os.path.join(tempfile.gettempdir(), "streamlit_graph_viz")
    os.makedirs(temp_dir, exist_ok=True)
    
    # Sauvegarder dans un fichier avec un nom unique basé sur les nœuds
    filename = f"graph_{len(G.nodes)}_{len(G.edges)}.html"
    filepath = os.path.join(temp_dir, filename)
    net.save_graph(filepath)
    
    return filepath