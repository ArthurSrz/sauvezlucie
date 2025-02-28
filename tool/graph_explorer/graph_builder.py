import networkx as nx


def get_nodes_within_depth(G, start_nodes, max_depth):
    """
    Récupère les nœuds à une certaine profondeur à partir d'un ensemble de nœuds de départ.
    
    Args:
        G (NetworkX.Graph): Le graphe à explorer
        start_nodes (list): Liste des nœuds de départ
        max_depth (int): Profondeur maximale d'exploration
        
    Returns:
        set: Ensemble des nœuds trouvés (incluant les nœuds de départ)
    """
    result_nodes = set(start_nodes)
    frontier = set(start_nodes)
    
    for depth in range(max_depth):
        new_frontier = set()
        for node in frontier:
            # Récupérer tous les voisins (entrants et sortants)
            neighbors = set(G.predecessors(node)) | set(G.successors(node))
            # Ajouter les nouveaux nœuds à la frontière
            new_nodes = neighbors - result_nodes
            new_frontier.update(new_nodes)
            # Ajouter tous les voisins au résultat
            result_nodes.update(neighbors)
        
        # Si plus de nouveaux nœuds à explorer, on arrête
        if not new_frontier:
            break
        
        frontier = new_frontier
    
    return result_nodes

def build_graph(parsed_files):
    """Construit un graphe NetworkX à partir des fichiers Markdown analysés."""
    G = nx.DiGraph()
    
    # Créer un dictionnaire pour accélérer les lookups par titre
    title_to_file = {file['title']: file for file in parsed_files}
    
    # Ajouter les nœuds
    for file in parsed_files:
        node_id = file['title']
        G.add_node(node_id, **file)
    
    # Ajouter les arêtes
    for file in parsed_files:
        source = file['title']
        
        # Ajouter les liens internes
        for target in file['internal_links']:
            if target in title_to_file:
                G.add_edge(source, target, type='internal_link')
        
        # Ajouter les relations définies dans les métadonnées
        for rel_type, target in file['relations']:
            if target in title_to_file:
                G.add_edge(source, target, type=rel_type)
    
    return G

def get_node_neighbors(G, node_id):
    """Récupère les voisins d'un nœud dans le graphe."""
    if node_id not in G:
        return [], []
    
    # Récupérer les successeurs (liens sortants)
    successors = [(neighbor, G.edges[node_id, neighbor]['type']) 
                 for neighbor in G.successors(node_id)]
    
    # Récupérer les prédécesseurs (liens entrants)
    predecessors = [(neighbor, G.edges[neighbor, node_id]['type']) 
                   for neighbor in G.predecessors(node_id)]
    
    return successors, predecessors

def get_graph_stats(G):
    """Calcule des statistiques sur le graphe."""
    stats = {
        'num_nodes': len(G.nodes),
        'num_edges': len(G.edges),
        'density': nx.density(G),
        'connected_components': nx.number_weakly_connected_components(G),
        'avg_degree': sum(dict(G.degree()).values()) / len(G.nodes) if len(G.nodes) > 0 else 0
    }
    
    # Distribution des types de nœuds
    node_types = {}
    for _, attrs in G.nodes(data=True):
        node_type = attrs.get('type', 'N/A')
        node_types[node_type] = node_types.get(node_type, 0) + 1
    
    # Tags les plus fréquents
    all_tags = []
    for _, attrs in G.nodes(data=True):
        all_tags.extend(attrs.get('tags', []))
    
    tag_counts = {}
    for tag in all_tags:
        tag_counts[tag] = tag_counts.get(tag, 0) + 1
    
    stats['node_types'] = node_types
    stats['tag_counts'] = tag_counts
    
    return stats
