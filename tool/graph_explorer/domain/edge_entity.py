class Edge:
    """
    Entité représentant une arête dans le graphe de connaissances.
    Implémente une Value Object immutable.
    """
    
    def __init__(self, source_id, target_id, edge_type=None, attributes=None):
        """
        Initialise une arête.
        
        Args:
            source_id (str): Identifiant du nœud source.
            target_id (str): Identifiant du nœud cible.
            edge_type (str, optional): Type de relation.
            attributes (dict, optional): Attributs supplémentaires.
        """
        self._source_id = source_id
        self._target_id = target_id
        self._type = edge_type or 'link'
        self._attributes = dict(attributes) if attributes else {}
    
    @property
    def source_id(self):
        return self._source_id
    
    @property
    def target_id(self):
        return self._target_id
    
    @property
    def edge_type(self):
        return self._type
    
    @property
    def attributes(self):
        return self._attributes.copy()  # Retourne une copie pour préserver l'immutabilité
    
    def to_dict(self):
        """
        Convertit l'arête en dictionnaire.
        
        Returns:
            dict: Représentation dictionnaire de l'arête.
        """
        result = {
            'source': self._source_id,
            'target': self._target_id,
            'type': self._type
        }
        # Ajout des attributs supplémentaires
        result.update(self._attributes)
        return result
    
    @classmethod
    def from_dict(cls, data):
        """
        Crée une arête à partir d'un dictionnaire.
        
        Args:
            data (dict): Dictionnaire contenant les données de l'arête.
            
        Returns:
            Edge: Instance d'arête.
        """
        # Extraire les attributs principaux
        source = data.get('source')
        target = data.get('target')
        edge_type = data.get('type')
        
        # Créer une copie sans les attributs principaux
        attributes = data.copy()
        for key in ['source', 'target', 'type']:
            if key in attributes:
                del attributes[key]
        
        return cls(
            source_id=source,
            target_id=target,
            edge_type=edge_type,
            attributes=attributes
        )
    
    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return (self._source_id == other.source_id and 
                self._target_id == other.target_id and 
                self._type == other.edge_type)
    
    def __hash__(self):
        return hash((self._source_id, self._target_id, self._type))
    
    def __repr__(self):
        return f"Edge(source='{self._source_id}', target='{self._target_id}', type='{self._type}')"
