import networkx as nx
from .node_entity import Node
from .edge_entity import Edge

def build_graph(parsed_files):
    """
    Construit un graphe NetworkX à partir des fichiers Markdown analysés.
    
    Args:
        parsed_files (list): Liste de dictionnaires représentant les fichiers Markdown parsés.
        
    Returns:
        nx.DiGraph: Graphe dirigé contenant les nœuds et les arêtes.
    """
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

def extract_nodes_and_edges(G):
    """
    Extrait les nœuds et les arêtes d'un graphe NetworkX sous forme d'entités du domaine.
    
    Args:
        G (nx.DiGraph): Graphe dirigé.
        
    Returns:
        tuple: (liste de Node, liste de Edge)
    """
    nodes = []
    edges = []
    
    # Extraire les nœuds
    for node_id, attrs in G.nodes(data=True):
        nodes.append(Node(
            id=node_id,
            title=attrs.get('title', node_id),
            node_type=attrs.get('type', ''),
            tags=attrs.get('tags', []),
            content=attrs.get('content', ''),
            path=attrs.get('path', '')
        ))
    
    # Extraire les arêtes
    for source, target, attrs in G.edges(data=True):
        edges.append(Edge(
            source_id=source,
            target_id=target,
            edge_type=attrs.get('type', 'link'),
            attributes=attrs
        ))
    
    return nodes, edges

def get_node_neighbors(G, node_id):
    """
    Récupère les voisins d'un nœud dans le graphe sous forme de tuples.
    
    Args:
        G (nx.DiGraph): Graphe dirigé.
        node_id (str): Identifiant du nœud.
        
    Returns:
        tuple: (successeurs, prédécesseurs)
    """
    if node_id not in G:
        return [], []
    
    # Récupérer les successeurs (liens sortants)
    successors = [(neighbor, G.edges[node_id, neighbor]['type']) 
                 for neighbor in G.successors(node_id)]
    
    # Récupérer les prédécesseurs (liens entrants)
    predecessors = [(neighbor, G.edges[neighbor, node_id]['type']) 
                   for neighbor in G.predecessors(node_id)]
    
    return successors, predecessors

def get_nodes_within_depth(G, start_nodes, max_depth):
    """
    Récupère les nœuds à une certaine profondeur à partir d'un ensemble de nœuds de départ.
    
    Args:
        G (nx.DiGraph): Graphe à explorer.
        start_nodes (list): Liste des nœuds de départ.
        max_depth (int): Profondeur maximale d'exploration.
        
    Returns:
        set: Ensemble des nœuds trouvés (incluant les nœuds de départ).
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