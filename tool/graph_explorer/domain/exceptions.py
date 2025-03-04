class DomainException(Exception):
    """Exception de base pour les erreurs du domaine."""
    pass

class GraphNotInitializedError(DomainException):
    """Erreur levée lorsqu'une opération est tentée sur un graphe non initialisé."""
    pass

class NodeNotFoundError(DomainException):
    """Erreur levée lorsqu'un nœud demandé n'existe pas."""
    pass

class EmbeddingModelNotAvailableError(DomainException):
    """Erreur levée lorsque le modèle d'embedding n'est pas disponible."""
    pass

class InvalidNodeAttributesError(DomainException):
    """Erreur levée lorsque les attributs d'un nœud sont invalides."""
    pass