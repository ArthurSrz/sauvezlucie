from domain.knowledge_graph import KnowledgeGraph
from domain.graph_builder import build_graph
import os
import tempfile
import networkx as nx

class GraphService:
    """Service pour la gestion des graphes de connaissances."""
    
    def __init__(self, storage_path=None):
        """
        Initialise le service de graphe.
        
        Args:
            storage_path (str, optional): Chemin vers le fichier de sauvegarde du graphe.
                Si None, un emplacement par défaut est utilisé.
        """
        if storage_path is None:
            cache_dir = os.path.join(tempfile.gettempdir(), "streamlit_graph_cache")
            os.makedirs(cache_dir, exist_ok=True)
            self.storage_path = os.path.join(cache_dir, "knowledge_graph.pkl")
        else:
            self.storage_path = storage_path
        
        # Instance unique de KnowledgeGraph
        self.knowledge_graph = KnowledgeGraph()
    
    def load_or_create_graph(self, parsed_files=None, embedding_model=None, force_rebuild=False):
        """
        Charge un graphe existant ou en crée un nouveau si nécessaire.
        
        Args:
            parsed_files (list, optional): Liste de fichiers Markdown parsés.
            embedding_model: Modèle d'embedding préexistant à utiliser.
            force_rebuild (bool): Si True, force la reconstruction même si un graphe existe.
            
        Returns:
            KnowledgeGraph: Le graphe de connaissances.
        """
        # Si l'instance a déjà un modèle d'embedding, l'utiliser
        if embedding_model:
            self.knowledge_graph = KnowledgeGraph(embedding_model=embedding_model)
            
        if parsed_files is None:
            # Tenter de charger un graphe existant
            if os.path.exists(self.storage_path) and not force_rebuild:
                try:
                    self.knowledge_graph.load(self.storage_path)
                    return self.knowledge_graph
                except Exception as e:
                    print(f"Erreur lors du chargement du graphe: {e}")
            return self.knowledge_graph
        
        # Création d'un nouveau graphe NetworkX
        nx_graph = build_graph(parsed_files)
        
        # Vérifier si le graphe est identique au graphe sauvegardé (sauf en cas de force_rebuild)
        if os.path.exists(self.storage_path) and not force_rebuild:
            try:
                self.knowledge_graph.load(self.storage_path)
                if self.knowledge_graph.is_same_as_session_graph(nx_graph):
                    return self.knowledge_graph
            except Exception as e:
                print(f"Erreur lors de la vérification du graphe: {e}")
                    
        # Construire un nouveau graphe de connaissances
        self.knowledge_graph.load_from_networkx(nx_graph)
        self.knowledge_graph.save(self.storage_path)
        
        return self.knowledge_graph
    
    def get_graph_stats(self):
        """
        Obtient des statistiques sur le graphe actuel.
        
        Returns:
            dict: Statistiques du graphe (nœuds, arêtes, etc.)
        """
        if self.knowledge_graph.G is None:
            return None
            
        G = self.knowledge_graph.G
        stats = {
            'num_nodes': len(G.nodes),
            'num_edges': len(G.edges),
            'density': nx.density(G),
            'connected_components': nx.number_weakly_connected_components(G) if len(G) > 0 else 0,
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
    
    def find_similar_content(self, content, top_k=5):
        """
        Trouve du contenu similaire dans le graphe.
        
        Args:
            content (str): Contenu textuel à comparer.
            top_k (int): Nombre de résultats à retourner.
            
        Returns:
            list: Liste des nœuds similaires avec leur score.
        """
        return self.knowledge_graph.find_similar_nodes(content, top_k)
    
    def add_new_node(self, node_id, attributes):
        """
        Ajoute un nouveau nœud au graphe.
        
        Args:
            node_id (str): Identifiant du nœud.
            attributes (dict): Attributs du nœud.
            
        Returns:
            int: Indice du nœud ajouté.
        """
        node_idx = self.knowledge_graph.add_node(node_id, attributes)
        self.knowledge_graph.save(self.storage_path)
        return node_idx
    
    def add_edge(self, source_id, target_id, edge_attrs=None):
        """
        Ajoute une arête entre deux nœuds.
        
        Args:
            source_id (str): ID du nœud source.
            target_id (str): ID du nœud cible.
            edge_attrs (dict, optional): Attributs de l'arête.
            
        Returns:
            bool: True si l'arête a été ajoutée, False sinon.
        """
        success = self.knowledge_graph.add_edge(source_id, target_id, edge_attrs)
        if success:
            self.knowledge_graph.save(self.storage_path)
        return success
    
    def get_node_neighbors(self, node_id):
        """
        Récupère les voisins d'un nœud.
        
        Args:
            node_id (str): Identifiant du nœud.
            
        Returns:
            tuple: (successeurs, prédécesseurs)
        """
        if self.knowledge_graph.G is None or node_id not in self.knowledge_graph.G:
            return [], []
            
        # Récupérer les successeurs (liens sortants)
        successors = [(neighbor, self.knowledge_graph.G.edges[node_id, neighbor]['type']) 
                     for neighbor in self.knowledge_graph.G.successors(node_id)]
        
        # Récupérer les prédécesseurs (liens entrants)
        predecessors = [(neighbor, self.knowledge_graph.G.edges[neighbor, node_id]['type']) 
                       for neighbor in self.knowledge_graph.G.predecessors(node_id)]
        
        return successors, predecessors
    
    def get_nodes_within_depth(self, start_nodes, max_depth):
        """
        Récupère les nœuds à une certaine profondeur à partir de nœuds de départ.
        
        Args:
            start_nodes (list): Liste des nœuds de départ.
            max_depth (int): Profondeur maximale d'exploration.
            
        Returns:
            set: Ensemble des nœuds trouvés.
        """
        if self.knowledge_graph.G is None:
            return set()
            
        G = self.knowledge_graph.G
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