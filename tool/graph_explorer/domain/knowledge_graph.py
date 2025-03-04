import networkx as nx
import numpy as np
import os
import pickle
import hashlib
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

from .node_entity import Node
from .edge_entity import Edge
from .exceptions import GraphNotInitializedError

class KnowledgeGraph:
    """
    Classe centrale représentant un graphe de connaissances.
    Implémente le pattern Singleton pour garantir une instance unique.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(KnowledgeGraph, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, embedding_model=None):
        """
        Initialise le graphe de connaissances.
        
        Args:
            embedding_model: Modèle d'embedding externe à utiliser.
        """
        # Éviter la réinitialisation si l'instance est déjà initialisée
        if hasattr(self, '_initialized') and self._initialized:
            return

        self.G = None
        self.graph_hash = None

        # Stockage du modèle d'embedding
        self.text_encoder = embedding_model
        self.type_encoder = None
        self.tag_vectorizer = None

        # Données d'encodage
        self.node_features = {}          # Features finales par nœud
        self.edges = []                  # Liste des arêtes sous forme de paires d'indices
        self.node_indices = {}           # Mapping des noms de nœuds vers indices
        self.text_embeddings_cache = {}  # Cache pour les embeddings déjà calculés
        self.node_content_hashes = {}    # Stocke le hash du contenu (et métadonnées) de chaque nœud

        self._initialized = True

    @classmethod
    def reset_instance(cls):
        """Réinitialise l'instance singleton pour forcer une nouvelle création."""
        cls._instance = None

    def update_embeddings_cache(self, external_cache):
        """
        Met à jour le cache d'embeddings avec des embeddings externes.
        
        Args:
            external_cache (dict): Dictionnaire associant un hash de contenu à un embedding.
        """
        if external_cache:
            self.text_embeddings_cache.update(external_cache)

    def load_from_networkx(self, G):
        """
        Transforme un graphe NetworkX en une structure adaptée à GraphSAGE.
        
        Args:
            G (networkx.DiGraph): Graphe à convertir.
            
        Returns:
            self: Instance de KnowledgeGraph pour le chaînage de méthodes.
        """
        self.G = G.copy()
        self.graph_hash = self._compute_graph_hash(G)

        # Préparation des encodeurs et calcul des features du graphe
        self._prepare_encoders()
        self._encode_graph_features()

        return self

    def is_same_as_session_graph(self, session_graph):
        """
        Vérifie si le graphe actuellement chargé est identique à celui de la session.
        
        Args:
            session_graph (networkx.DiGraph): Graphe de la session.
            
        Returns:
            bool: True si les graphes sont identiques, False sinon.
        """
        if not self.graph_hash:
            return False
        session_hash = self._compute_graph_hash(session_graph)
        return self.graph_hash == session_hash

    def get_text_embedding(self, text):
        """
        Récupère l'embedding d'un texte via le modèle d'encodage.
        
        Args:
            text (str): Texte à encoder.
            
        Returns:
            ndarray: Vecteur d'embedding du texte.
        """
        # Utiliser un hash pour identifier le texte de manière cohérente
        text_hash = hashlib.md5(text.encode()).hexdigest()
        if text_hash in self.text_embeddings_cache:
            return self.text_embeddings_cache[text_hash]
        
        # Préparer le texte et calculer l'embedding
        prepared_text = f"passage: {text}"
        embedding = self.text_encoder.encode(prepared_text)
        self.text_embeddings_cache[text_hash] = embedding
        return embedding

    def save(self, filepath):
        """
        Sauvegarde l'état du graphe dans un fichier.
        
        Args:
            filepath (str): Chemin du fichier de sauvegarde.
        """
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)

        save_data = {
            'graph': self.G,
            'graph_hash': self.graph_hash,
            'node_features': self.node_features,
            'edges': self.edges,
            'node_indices': self.node_indices,
            'text_embeddings_cache': self.text_embeddings_cache,
            'node_content_hashes': self.node_content_hashes,
            'type_encoder': self.type_encoder,
            'tag_vectorizer': self.tag_vectorizer
        }

        with open(filepath, 'wb') as f:
            pickle.dump(save_data, f)

    def load(self, filepath):
        """
        Charge l'état du graphe depuis un fichier.
        
        Args:
            filepath (str): Chemin du fichier de sauvegarde.
            
        Returns:
            self: Instance de KnowledgeGraph pour le chaînage de méthodes.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Le fichier {filepath} n'existe pas")

        with open(filepath, 'rb') as f:
            save_data = pickle.load(f)

        self.G = save_data['graph']
        self.graph_hash = save_data['graph_hash']
        self.node_features = save_data['node_features']
        self.edges = save_data['edges']
        self.node_indices = save_data['node_indices']
        self.text_embeddings_cache = save_data['text_embeddings_cache']
        self.node_content_hashes = save_data.get('node_content_hashes', {})
        self.type_encoder = save_data['type_encoder']
        self.tag_vectorizer = save_data['tag_vectorizer']

        return self

    def get_graphsage_data(self):
        """
        Prépare les données du graphe pour être utilisées avec GraphSAGE.
        
        Returns:
            dict: Dictionnaire contenant :
                - 'features': Tableau numpy des features de chaque nœud.
                - 'edges': Liste des arêtes sous forme de paires d'indices.
                - 'node_map': Mapping des noms de nœuds vers indices.
                - 'reverse_map': Mapping des indices vers noms de nœuds.
        """
        if not self.G:
            raise GraphNotInitializedError("Le graphe n'est pas initialisé")
            
        features = np.array([self.node_features[node] for node in self.G.nodes()])
        reverse_map = {idx: node for node, idx in self.node_indices.items()}
        return {
            'features': features,
            'edges': self.edges,
            'node_map': self.node_indices,
            'reverse_map': reverse_map
        }

    def get_embeddings_cache(self):
        """
        Récupère le cache des embeddings calculés.
        
        Returns:
            dict: Dictionnaire associant le hash d'un contenu à son embedding.
        """
        return self.text_embeddings_cache

    def _compute_graph_hash(self, G):
        """
        Calcule un hash unique pour le graphe afin de vérifier son intégrité.
        
        Args:
            G (networkx.DiGraph): Graphe à hasher.
            
        Returns:
            str: Hash hexadécimal représentant le graphe.
        """
        nodes_str = str(sorted([(n, str(d)) for n, d in G.nodes(data=True)]))
        edges_str = str(sorted([(u, v, str(d)) for u, v, d in G.edges(data=True)]))
        graph_repr = nodes_str + edges_str
        return hashlib.md5(graph_repr.encode()).hexdigest()

    def _prepare_encoders(self):
        """
        Prépare les encodeurs pour les types de nœuds et les tags.
        """
        if not self.G:
            return

        # Récupérer les types de nœuds uniques (par défaut "unknown" si non défini)
        node_types = list(set(attrs.get('type', '') for _, attrs in self.G.nodes(data=True)))
        node_types = [t if t else "unknown" for t in node_types]

        # Initialiser l'encodeur OneHot pour le type des nœuds
        try:
            self.type_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        except TypeError:
            self.type_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')

        self.type_encoder.fit(np.array(node_types).reshape(-1, 1))

        # Préparer le vectoriseur TF-IDF pour les tags
        all_tags_text = [' '.join(attrs.get('tags', [])) for _, attrs in self.G.nodes(data=True)]
        self.tag_vectorizer = TfidfVectorizer(max_features=100)
        self.tag_vectorizer.fit(all_tags_text)

    def _encode_graph_features(self):
        """
        Encode les caractéristiques de chaque nœud du graphe pour GraphSAGE,
        incluant l'embedding du contenu textuel, l'encodage du type et des tags.
        """
        if not self.G:
            return

        # Mapping des nœuds vers des indices
        self.node_indices = {node: idx for idx, node in enumerate(self.G.nodes())}
        self.node_features = {}

        for node, attrs in self.G.nodes(data=True):
            self._encode_node_features(node, attrs)

        # Conversion des arêtes du graphe : les noms de nœuds sont remplacés par leurs indices
        self.edges = []
        for u, v in self.G.edges():
            if u in self.node_indices and v in self.node_indices:
                self.edges.append((self.node_indices[u], self.node_indices[v]))

    def _encode_node_features(self, node, attrs):
        """
        Encode les caractéristiques d'un nœud spécifique.
        
        Args:
            node (str): Identifiant du nœud.
            attrs (dict): Attributs du nœud.
            
        Returns:
            ndarray: Vecteur de caractéristiques du nœud.
        """
        content = attrs.get('content', '')
        node_type = attrs.get('type', 'unknown')
        tags = attrs.get('tags', [])

        # Calcul du hash unique pour le nœud (basé sur contenu, type et tags)
        node_hash = hashlib.md5(f"{content}|{node_type}|{' '.join(tags)}".encode()).hexdigest()
        self.node_content_hashes[node] = node_hash

        # Réutilisation de l'embedding si le hash existe déjà dans le cache, sinon calcul
        if node_hash in self.text_embeddings_cache:
            text_embedding = self.text_embeddings_cache[node_hash]
        else:
            text_embedding = self.text_encoder.encode(f"passage: {content}")
            self.text_embeddings_cache[node_hash] = text_embedding

        # Encodage du type du nœud
        type_embedding = self.type_encoder.transform(np.array([node_type]).reshape(-1, 1))[0]

        # Encodage des tags
        tags_text = ' '.join(tags)
        if tags_text:
            tags_embedding = self.tag_vectorizer.transform([tags_text]).toarray()[0]
        else:
            tags_embedding = np.zeros(self.tag_vectorizer.max_features)

        # Concaténation des embeddings pour constituer la feature finale du nœud
        feature_vector = np.concatenate([
            text_embedding,
            type_embedding,
            tags_embedding
        ])
        
        self.node_features[node] = feature_vector
        return feature_vector

    def reuse_existing_embeddings(self, old_graph):
        """
        Réutilise les embeddings des nœuds inchangés entre deux graphes.
        Pour chaque nœud du graphe actuel, si le hash de son contenu correspond à celui d'un nœud
        de l'ancien graphe, son embedding et ses features sont récupérés pour éviter un recalcul.
        
        Args:
            old_graph: Objet contenant les propriétés 'node_content_hashes',
            'node_features' et 'text_embeddings_cache' de l'ancien graphe.
        """
        if not old_graph or not hasattr(old_graph, 'node_content_hashes'):
            return

        for node, new_hash in self.node_content_hashes.items():
            if node in old_graph.node_content_hashes and old_graph.node_content_hashes[node] == new_hash:
                self.node_features[node] = old_graph.node_features[node]
                self.text_embeddings_cache[new_hash] = old_graph.text_embeddings_cache.get(new_hash)

    def updateAndSaveGraph(self, new_graph, filepath):
        """
        Met à jour le graphe courant avec un nouveau graphe NetworkX,
        réutilise les embeddings existants pour les nœuds inchangés,
        et sauvegarde l'état mis à jour dans le fichier spécifié.
        
        Args:
            new_graph (networkx.DiGraph): Nouveau graphe à intégrer.
            filepath (str): Chemin de sauvegarde du graphe mis à jour.
        """
        # Sauvegarder l'état actuel pour réutilisation des embeddings
        old_state = {
            'node_content_hashes': self.node_content_hashes.copy(),
            'node_features': self.node_features.copy(),
            'text_embeddings_cache': self.text_embeddings_cache.copy()
        }
        
        # Créer un objet avec les propriétés nécessaires pour réutiliser les embeddings
        old_graph = type('', (), {
            'node_content_hashes': old_state['node_content_hashes'],
            'node_features': old_state['node_features'],
            'text_embeddings_cache': old_state['text_embeddings_cache']
        })()

        # Charger le nouveau graphe et mettre à jour les caractéristiques
        self.load_from_networkx(new_graph)
        # Réutiliser les embeddings existants pour les nœuds inchangés
        self.reuse_existing_embeddings(old_graph)
        # Sauvegarder l'état mis à jour du graphe
        self.save(filepath)
        
    def add_node(self, node_id, attributes):
        """
        Ajoute un nouveau nœud au graphe et calcule ses caractéristiques sans avoir à recalculer
        l'ensemble du graphe. Retourne les indices mis à jour.
        
        Args:
            node_id (str): Identifiant du nouveau nœud.
            attributes (dict): Attributs du nœud (contenu, type, tags, etc.).
            
        Returns:
            int: Indice du nœud ajouté.
        """
        if not self.G:
            raise GraphNotInitializedError("Le graphe n'est pas initialisé")
            
        # Vérifier si le nœud existe déjà
        if node_id in self.G:
            # Mise à jour des attributs du nœud existant
            for key, value in attributes.items():
                self.G.nodes[node_id][key] = value
        else:
            # Ajout du nouveau nœud au graphe
            self.G.add_node(node_id, **attributes)
            
        # Encodage des caractéristiques du nœud
        feature_vector = self._encode_node_features(node_id, attributes)
        
        # Mise à jour des indices de nœuds
        if node_id not in self.node_indices:
            new_index = len(self.node_indices)
            self.node_indices[node_id] = new_index
        
        # Recalcul du hash du graphe
        self.graph_hash = self._compute_graph_hash(self.G)
        
        return self.node_indices[node_id]
    
    def add_edge(self, source_id, target_id, edge_attrs=None):
        """
        Ajoute une arête entre deux nœuds existants du graphe.
        
        Args:
            source_id (str): Identifiant du nœud source.
            target_id (str): Identifiant du nœud cible.
            edge_attrs (dict, optional): Attributs de l'arête.
            
        Returns:
            bool: True si l'arête a été ajoutée avec succès, False sinon.
        """
        if not self.G:
            raise GraphNotInitializedError("Le graphe n'est pas initialisé")
            
        if source_id not in self.G or target_id not in self.G:
            return False
            
        if edge_attrs is None:
            edge_attrs = {'type': 'link'}
            
        # Ajout de l'arête au graphe
        self.G.add_edge(source_id, target_id, **edge_attrs)
        
        # Mise à jour de la liste des arêtes pour GraphSAGE
        if (source_id in self.node_indices and target_id in self.node_indices):
            source_idx = self.node_indices[source_id]
            target_idx = self.node_indices[target_id]
            self.edges.append((source_idx, target_idx))
        
        # Recalcul du hash du graphe
        self.graph_hash = self._compute_graph_hash(self.G)
        
        return True
    
    def find_similar_nodes(self, content, top_k=5):
        """
        Trouve les nœuds similaires à un contenu donné en utilisant la similarité cosinus
        entre les embeddings.
        
        Args:
            content (str): Contenu textuel pour lequel chercher des similitudes.
            top_k (int): Nombre de nœuds similaires à retourner.
            
        Returns:
            list: Liste de tuples (node_id, score) des nœuds les plus similaires.
        """
        if not self.G or not self.node_features:
            return []
            
        # Vérifier si text_encoder est disponible
        if self.text_encoder is None:
            # Essayer de récupérer le service d'embedding
            try:
                import streamlit as st
                if 'embedding_service' in st.session_state:
                    self.text_encoder = st.session_state.embedding_service.get_model()
                else:
                    print("Erreur: Service d'embedding non disponible dans la session")
                    return []
            except Exception as e:
                print(f"Erreur lors de la récupération du service d'embedding: {e}")
                return []
        
        try:
            # Obtenir l'embedding du contenu
            content_embedding = self.get_text_embedding(content)
            
            # Calculer la similarité avec tous les nœuds
            similarities = []
            for node, features in self.node_features.items():
                # La taille de l'embedding textuel est la taille des features - taille des encodages de type et de tags
                text_embedding_size = len(content_embedding)
                node_embedding = features[:text_embedding_size]  # Prendre uniquement la partie textuelle
                
                # Calculer la similarité cosinus
                norm_content = np.linalg.norm(content_embedding)
                norm_node = np.linalg.norm(node_embedding)
                
                if norm_content > 0 and norm_node > 0:
                    similarity = np.dot(content_embedding, node_embedding) / (norm_content * norm_node)
                    similarities.append((node, float(similarity)))
                    
            # Trier les nœuds par similarité décroissante
            similarities.sort(key=lambda x: x[1], reverse=True)
            
            return similarities[:top_k]
        except Exception as e:
            print(f"Erreur lors de la recherche de nœuds similaires: {e}")
            import traceback
            traceback.print_exc()
            return []

    def get_node(self, node_id):
        """
        Récupère les informations d'un nœud sous forme d'objet Node.
        
        Args:
            node_id (str): Identifiant du nœud.
            
        Returns:
            Node: Objet représentant le nœud.
        """
        if not self.G or node_id not in self.G:
            return None
            
        attrs = self.G.nodes[node_id]
        from .node_entity import Node
        
        return Node(
            id=node_id,
            title=attrs.get('title', node_id),
            node_type=attrs.get('type', ''),
            tags=attrs.get('tags', []),
            content=attrs.get('content', ''),
            path=attrs.get('path', '')
        )