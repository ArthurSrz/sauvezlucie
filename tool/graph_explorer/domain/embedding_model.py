import numpy as np
from sentence_transformers import SentenceTransformer
import os
from .exceptions import EmbeddingModelNotAvailableError

class EmbeddingModel:
    """
    Classe pour gérer les modèles d'embedding vectoriel.
    Implémente le pattern Singleton.
    """
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EmbeddingModel, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, model_name=None):
        """
        Initialise le modèle d'embedding.
        
        Args:
            model_name (str, optional): Nom du modèle à utiliser.
        """
        # Éviter la réinitialisation si déjà initialisé
        if hasattr(self, '_initialized') and self._initialized:
            return
            
        self.model_name = model_name or os.getenv(
            "EMBEDDING_MODEL", "intfloat/multilingual-e5-large-instruct"
        )
        self.model = None
        self._initialized = True
    
    def load_model(self):
        """
        Charge le modèle s'il n'est pas déjà chargé.
        
        Returns:
            SentenceTransformer: Modèle chargé.
            
        Raises:
            EmbeddingModelNotAvailableError: Si le modèle ne peut pas être chargé.
        """
        if self.model is None:
            try:
                self.model = SentenceTransformer(self.model_name, device='cpu')
            except Exception as e:
                raise EmbeddingModelNotAvailableError(f"Impossible de charger le modèle: {e}")
        
        return self.model
    
    def encode(self, text, prefix="passage: "):
        """
        Encode un texte en vecteur.
        
        Args:
            text (str): Texte à encoder.
            prefix (str, optional): Préfixe à ajouter au texte.
            
        Returns:
            ndarray: Vecteur d'embedding.
            
        Raises:
            EmbeddingModelNotAvailableError: Si le modèle n'est pas disponible.
        """
        model = self.load_model()
        
        # Préfixer le texte si nécessaire
        prepared_text = f"{prefix}{text}" if prefix and not text.startswith(prefix) else text
        
        try:
            return model.encode(prepared_text, device='cpu')
        except Exception as e:
            raise EmbeddingModelNotAvailableError(f"Erreur lors de l'encodage: {e}")
    
    def batch_encode(self, texts, prefix="passage: "):
        """
        Encode une liste de textes en vecteurs.
        
        Args:
            texts (list): Liste de textes à encoder.
            prefix (str, optional): Préfixe à ajouter aux textes.
            
        Returns:
            ndarray: Matrice d'embeddings (n_texts × dimensions).
            
        Raises:
            EmbeddingModelNotAvailableError: Si le modèle n'est pas disponible.
        """
        model = self.load_model()
        
        # Préfixer les textes si nécessaire
        prepared_texts = [
            f"{prefix}{text}" if prefix and not text.startswith(prefix) else text
            for text in texts
        ]
        
        try:
            return model.encode(prepared_texts, device='cpu')
        except Exception as e:
            raise EmbeddingModelNotAvailableError(f"Erreur lors de l'encodage par lot: {e}")
    
    def cosine_similarity(self, embedding1, embedding2):
        """
        Calcule la similarité cosinus entre deux embeddings.
        
        Args:
            embedding1 (ndarray): Premier embedding.
            embedding2 (ndarray): Second embedding.
            
        Returns:
            float: Similarité cosinus entre -1 et 1.
        """
        norm1 = np.linalg.norm(embedding1)
        norm2 = np.linalg.norm(embedding2)
        
        if norm1 == 0 or norm2 == 0:
            return 0
        
        return np.dot(embedding1, embedding2) / (norm1 * norm2)
    
    def batch_cosine_similarity(self, embeddings, query_embedding):
        """
        Calcule la similarité cosinus entre plusieurs embeddings et un embedding de requête.
        
        Args:
            embeddings (ndarray): Matrice d'embeddings (n_embeddings × dimensions).
            query_embedding (ndarray): Embedding de la requête.
            
        Returns:
            ndarray: Vecteur de similarités.
        """
        # Normaliser la requête
        query_norm = np.linalg.norm(query_embedding)
        if query_norm == 0:
            return np.zeros(len(embeddings))
        
        normalized_query = query_embedding / query_norm
        
        # Normaliser les embeddings
        norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
        norms[norms == 0] = 1  # Éviter la division par zéro
        normalized_embeddings = embeddings / norms
        
        # Calculer la similarité cosinus
        return np.dot(normalized_embeddings, normalized_query)