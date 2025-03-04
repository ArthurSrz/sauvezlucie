class Node:
    """
    Entité représentant un nœud dans le graphe de connaissances.
    Implémente une Value Object immutable.
    """
    
    def __init__(self, id, title=None, node_type=None, tags=None, content=None, path=None):
        """
        Initialise un nœud.
        
        Args:
            id (str): Identifiant unique du nœud.
            title (str, optional): Titre du nœud.
            node_type (str, optional): Type du nœud.
            tags (list, optional): Liste des tags associés au nœud.
            content (str, optional): Contenu textuel du nœud.
            path (str, optional): Chemin du fichier source.
        """
        self._id = id
        self._title = title or id
        self._node_type = node_type or ''
        self._tags = list(tags) if tags else []
        self._content = content or ''
        self._path = path or ''
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @property
    def node_type(self):
        return self._node_type
    
    @property
    def tags(self):
        return self._tags.copy()  # Retourne une copie pour préserver l'immutabilité
    
    @property
    def content(self):
        return self._content
    
    @property
    def path(self):
        return self._path
    
    def to_dict(self):
        """
        Convertit le nœud en dictionnaire.
        
        Returns:
            dict: Représentation dictionnaire du nœud.
        """
        return {
            'id': self._id,
            'title': self._title,
            'type': self._node_type,
            'tags': self._tags,
            'content': self._content,
            'path': self._path
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Crée un nœud à partir d'un dictionnaire.
        
        Args:
            data (dict): Dictionnaire contenant les données du nœud.
            
        Returns:
            Node: Instance de nœud.
        """
        return cls(
            id=data.get('id') or data.get('title'),
            title=data.get('title'),
            node_type=data.get('type'),
            tags=data.get('tags'),
            content=data.get('content'),
            path=data.get('path')
        )
    
    def has_tag(self, tag):
        """
        Vérifie si le nœud possède un tag spécifique.
        
        Args:
            tag (str): Tag à rechercher.
            
        Returns:
            bool: True si le tag est présent, False sinon.
        """
        return tag in self._tags
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self._id == other.id
    
    def __hash__(self):
        return hash(self._id)
    
    def __repr__(self):
        return f"Node(id='{self._id}', type='{self._node_type}', tags={self._tags})"