import numpy as np
from sentence_transformers import SentenceTransformer
import os

class EmbeddingService:
    """Service pour la gestion des embeddings vectoriels."""
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EmbeddingService, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, model_name=None):
        """
        Initialise le service d'embeddings.
        
        Args:
            model_name (str, optional): Nom du modèle d'embedding à utiliser.
        """
        # Éviter la réinitialisation si déjà initialisé
        if hasattr(self, '_initialized') and self._initialized:
            return
            
        self.model_name = model_name or os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-large-instruct")
        self.model = None
        self._initialized = True
    
    def get_model(self):
        """
        Charge et retourne le modèle d'embedding.
        
        Returns:
            SentenceTransformer: Modèle d'embedding.
        """
        if self.model is None:
            try:
                self.model = SentenceTransformer(self.model_name, device='cpu')
            except Exception as e:
                print(f"Erreur lors du chargement du modèle d'embedding: {e}")
                raise
        
        return self.model
    
    def compute_embeddings(self, texts, query=None, cached_embeddings=None, return_dict=False):
        """
        Calcule les embeddings pour des textes et éventuellement une requête.
        
        Args:
            texts (list): Liste de textes à encoder.
            query (str, optional): Requête à encoder.
            cached_embeddings (ndarray, optional): Embeddings déjà calculés.
            return_dict (bool): Si True, retourne aussi un dictionnaire texte -> embedding.
            
        Returns:
            dict: Résultats des embeddings.
            dict (optional): Dictionnaire text -> embedding si return_dict=True.
        """
        if isinstance(texts, str):
            texts = [texts]
        
        result = {}
        text_to_embedding = {}
        
        # Utiliser les embeddings mis en cache si disponibles
        if cached_embeddings is not None:
            result['text_embeddings'] = cached_embeddings
        else:
            # Calculer les embeddings des textes
            model = self.get_model()
            
            # Calculer les embeddings et construire le cache
            embeddings = []
            for text in texts:
                prepared_text = f"passage: {text}"
                embedding = model.encode(prepared_text, device='cpu')
                embeddings.append(embedding)
                text_to_embedding[text] = embedding
            
            result['text_embeddings'] = np.array(embeddings)
        
        # Calculer l'embedding de la requête si fournie
        if query:
            model = self.get_model()
            query_embedding = model.encode(f"query: {query}", device='cpu')
            result['query_embedding'] = query_embedding
        
        if return_dict:
            return result, text_to_embedding
        
        return result
    
    def cosine_similarity(self, embedding1, embedding2):
        """
        Calcule la similarité cosinus entre deux embeddings.
        
        Args:
            embedding1, embedding2 (ndarray): Les embeddings à comparer.
            
        Returns:
            float: Score de similarité entre -1 et 1.
        """
        norm1 = np.linalg.norm(embedding1)
        norm2 = np.linalg.norm(embedding2)
        
        if norm1 > 0 and norm2 > 0:
            return np.dot(embedding1, embedding2) / (norm1 * norm2)
        
        return 0.0
    
    def batch_cosine_similarity(self, embeddings, query_embedding):
        """
        Calcule la similarité cosinus entre un ensemble d'embeddings et un embedding de requête.
        
        Args:
            embeddings (ndarray): Tableau d'embeddings.
            query_embedding (ndarray): Embedding de la requête.
            
        Returns:
            ndarray: Scores de similarité.
        """
        query_norm = np.linalg.norm(query_embedding)
        if query_norm == 0:
            return np.zeros(len(embeddings))
        
        dot_products = np.dot(embeddings, query_embedding)
        embedding_norms = np.linalg.norm(embeddings, axis=1)
        
        # Éviter la division par zéro
        embedding_norms[embedding_norms == 0] = 1
        
        return dot_products / (embedding_norms * query_norm)
    
    def batch_encode(self, texts, prefix="passage: "):
        """
        Encode une liste de textes en vecteurs d'embedding.
        
        Args:
            texts (list): Liste de textes à encoder.
            prefix (str, optional): Préfixe à ajouter aux textes.
            
        Returns:
            ndarray: Matrice d'embeddings (chaque ligne est un embedding).
        """
        model = self.get_model()
        
        # Préparer les textes avec le préfixe
        prepared_texts = [f"{prefix}{text}" if text else f"{prefix} " for text in texts]
        
        # Encoder en batch
        return model.encode(prepared_texts, device='cpu')

    def encode(self, text, prefix="passage: "):
        """
        Encode un texte en vecteur d'embedding.
        
        Args:
            text (str): Texte à encoder.
            prefix (str, optional): Préfixe à ajouter au texte.
            
        Returns:
            ndarray: Vecteur d'embedding.
        """
        model = self.get_model()
        
        # Préparer le texte avec le préfixe
        prepared_text = f"{prefix}{text}" if text else f"{prefix} "
        
        # Encoder
        return model.encode(prepared_text, device='cpu')