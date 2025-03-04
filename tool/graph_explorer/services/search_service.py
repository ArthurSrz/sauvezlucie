import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi
import json
import re

class SearchService:
    """Service pour la recherche et le calcul de pertinence dans le graphe."""
    
    def __init__(self, embedding_service=None):
        """
        Initialise le service de recherche.
        
        Args:
            embedding_service: Service d'embedding pour les opérations vectorielles.
        """
        self.embedding_service = embedding_service
    
    def simple_keyword_search(self, G, query):
        """
        Recherche simple par mots-clés dans le graphe.
        
        Args:
            G (networkx.DiGraph): Graphe dans lequel effectuer la recherche.
            query (str): Requête de recherche.
            
        Returns:
            list: Résultats de recherche triés par score.
        """
        query_terms = query.lower().split()
        results = []
        
        for node, attrs in G.nodes(data=True):
            score = 0
            
            # Recherche dans le titre
            title = attrs.get('title', '').lower()
            for term in query_terms:
                if term in title:
                    score += 3  # Poids plus élevé pour les correspondances dans le titre
            
            # Recherche dans le type
            node_type = attrs.get('type', '').lower()
            for term in query_terms:
                if term in node_type:
                    score += 2
            
            # Recherche dans les tags
            tags = ' '.join(attrs.get('tags', [])).lower()
            for term in query_terms:
                if term in tags:
                    score += 2
            
            # Recherche dans le contenu
            content = attrs.get('content', '').lower()
            for term in query_terms:
                if term in content:
                    score += 1
            
            if score > 0:
                results.append({
                    'node': node,
                    'score': score,
                    'data': attrs
                })
        
        # Trier par score décroissant
        results.sort(key=lambda x: x['score'], reverse=True)
        return results
    
    def calculate_combined_scores(self, G, query, weights, llm_client=None, cached_embeddings=None):
        """
        Calcule les scores combinés pour tous les nœuds d'un graphe par rapport à une requête.
        
        Args:
            G (networkx.DiGraph): Graphe à analyser.
            query (str): Requête utilisateur.
            weights (dict): Poids des différentes métriques.
            llm_client: Client LLM pour générer des tags.
            cached_embeddings: Cache des embeddings précédemment calculés.
            
        Returns:
            tuple: (scores, embeddings, individual_scores, embeddings_dict)
        """
        # 1. Préparation des données
        nodes = list(G.nodes())
        node_contents = []
        node_tags_list = []
        
        # Extraire les contenus et tags des nœuds
        for node in nodes:
            attrs = G.nodes[node]
            content = attrs.get('content', '')
            tags = attrs.get('tags', [])
            node_contents.append(content)
            node_tags_list.append(tags)
        
        # Collecter les tags uniques pour la génération LLM
        all_unique_tags = set()
        for tags in node_tags_list:
            all_unique_tags.update(tags)
        existing_tags = list(all_unique_tags)
        
        # 2. Initialisation des scores et du cache
        cosine_scores = np.zeros(len(nodes))
        tfidf_scores = np.zeros(len(nodes))
        bm25_scores = np.zeros(len(nodes))
        jaccard_scores = np.zeros(len(nodes))
        embeddings_dict = {}  # Pour retourner les embeddings calculés
        computed_embeddings_dict = {}  # Pour usage interne
        
        # 3. Calcul des scores par similarité cosinus (embeddings)
        embeddings_result = None
        
        if weights.get('cosine', 0) > 0 and self.embedding_service:
            try:
                # Récupérer le graphe de connaissances
                kg = self._get_knowledge_graph(G)
                
                # Obtenir les embeddings textuels
                text_embeddings = self._get_text_embeddings(
                    kg, nodes, node_contents, cached_embeddings, computed_embeddings_dict
                )
                
                # Calculer l'embedding de la requête
                query_embedding = self.embedding_service.encode(query, prefix="query: ")
                
                # Calculer les scores cosinus et les normaliser
                cosine_scores = self.calculate_cosine_scores(text_embeddings, query_embedding)
                cosine_scores = self._normalize_scores(cosine_scores)
                
                # Stocker les embeddings pour le cache
                embeddings_result = {
                    'text_embeddings': text_embeddings,
                    'query_embedding': query_embedding
                }
            except Exception as e:
                print(f"Erreur dans le calcul des embeddings: {e}")
                import traceback
                traceback.print_exc()
        
        # 4. Calcul des scores TF-IDF
        if weights.get('tfidf', 0) > 0:
            try:
                tfidf_scores = self.calculate_tfidf_scores(node_contents, query)
                tfidf_scores = self._normalize_scores(tfidf_scores)
            except Exception as e:
                print(f"Erreur dans le calcul TF-IDF: {e}")
        
        # 5. Calcul des scores BM25
        if weights.get('bm25', 0) > 0:
            try:
                bm25_scores = self.calculate_bm25_scores(node_contents, query)
                bm25_scores = self._normalize_scores(bm25_scores)
            except Exception as e:
                print(f"Erreur dans le calcul BM25: {e}")
        
        # 6. Calcul des scores Jaccard sur les tags
        if weights.get('jaccard', 0) > 0 and llm_client:
            try:
                # Générer les tags pour la requête
                query_tags = self._get_query_tags(query, existing_tags, llm_client)
                
                # Calculer et normaliser les scores Jaccard
                jaccard_scores = self.calculate_jaccard_scores(node_tags_list, query_tags)
                jaccard_scores = self._normalize_scores(jaccard_scores)
            except Exception as e:
                print(f"Erreur dans le calcul Jaccard: {e}")
                import traceback
                traceback.print_exc()
        
        # 7. Combiner les scores selon les poids
        combined_scores = (
            weights.get('cosine', 0) * cosine_scores +
            weights.get('tfidf', 0) * tfidf_scores +
            weights.get('bm25', 0) * bm25_scores +
            weights.get('jaccard', 0) * jaccard_scores
        )
        
        # 8. Préparer les résultats
        # Créer les dictionnaires de scores par métrique
        individual_scores = {
            'cosine': {node: float(score) for node, score in zip(nodes, cosine_scores)},
            'tfidf': {node: float(score) for node, score in zip(nodes, tfidf_scores)},
            'bm25': {node: float(score) for node, score in zip(nodes, bm25_scores)},
            'jaccard': {node: float(score) for node, score in zip(nodes, jaccard_scores)}
        }
        
        # Créer le dictionnaire de scores combinés
        result = {}
        for i, node in enumerate(nodes):
            try:
                result[node] = float(combined_scores[i])
            except:
                result[node] = 0.0
        
        # Préparer les embeddings à retourner pour le cache
        embeddings_to_return = None
        if embeddings_result and 'text_embeddings' in embeddings_result:
            try:
                embeddings_to_return = embeddings_result['text_embeddings'].tolist()
            except:
                pass
        
        return result, embeddings_to_return, individual_scores, computed_embeddings_dict

    def _get_knowledge_graph(self, G):
        """Récupère l'instance KnowledgeGraph du graphe ou du service"""
        # Essayer d'accéder au knowledge_graph depuis différentes sources
        if hasattr(G, 'knowledge_graph'):
            return G.knowledge_graph
        elif 'knowledge_graph' in G.graph:
            return G.graph['knowledge_graph']
        
        # Essayer via le service graphe
        graph_service = self.get_graph_service()
        if graph_service and hasattr(graph_service, 'knowledge_graph'):
            return graph_service.knowledge_graph
        
        return None

    def _get_text_embeddings(self, kg, nodes, node_contents, cached_embeddings=None, computed_embeddings_dict=None):
        """Récupère ou calcule les embeddings textuels pour tous les nœuds"""
        import hashlib
        
        # Si le cache externe est fourni, l'utiliser directement
        if cached_embeddings is not None:
            return cached_embeddings
        
        # Si on a accès au KnowledgeGraph
        if kg is not None:
            # Essayer d'accéder aux embeddings stockés dans node_features
            if hasattr(kg, 'node_features') and kg.node_features:
                # Vérifier si tous les nœuds sont disponibles
                if all(node in kg.node_features for node in nodes):
                    embeddings_from_kg = []
                    embedding_size = 1024  # Taille pour E5-large, à ajuster selon votre modèle
                    
                    for i, node in enumerate(nodes):
                        # Extraire la partie textuelle
                        feature = kg.node_features[node]
                        embedding = feature[:embedding_size]
                        embeddings_from_kg.append(embedding)
                        
                        # Stocker pour référence future
                        if computed_embeddings_dict is not None:
                            content = node_contents[i]
                            if content:
                                computed_embeddings_dict[content] = embedding
                    
                    return np.array(embeddings_from_kg)
            
            # Sinon, essayer d'utiliser le cache d'embeddings textuels
            if hasattr(kg, 'text_embeddings_cache') and kg.text_embeddings_cache:
                embeddings_from_cache = []
                all_in_cache = True
                
                for content in node_contents:
                    if not content:
                        # Pour les contenus vides, utiliser un vecteur nul
                        dummy_embedding = np.zeros(1024)  # Ajuster selon votre modèle
                        embeddings_from_cache.append(dummy_embedding)
                        continue
                    
                    # Calculer le hash comme dans KnowledgeGraph
                    content_hash = hashlib.md5(content.encode()).hexdigest()
                    
                    if content_hash in kg.text_embeddings_cache:
                        embedding = kg.text_embeddings_cache[content_hash]
                        embeddings_from_cache.append(embedding)
                        if computed_embeddings_dict is not None:
                            computed_embeddings_dict[content] = embedding
                    else:
                        all_in_cache = False
                        break
                
                if all_in_cache:
                    return np.array(embeddings_from_cache)
        
        # Si aucune des méthodes ci-dessus n'a fonctionné, calculer les embeddings
        text_embeddings = self.embedding_service.batch_encode(node_contents)
        
        # Mettre à jour les caches
        if kg is not None and hasattr(kg, 'text_embeddings_cache'):
            for i, content in enumerate(node_contents):
                if content:
                    content_hash = hashlib.md5(content.encode()).hexdigest()
                    kg.text_embeddings_cache[content_hash] = text_embeddings[i]
        
        # Mettre à jour le dictionnaire externe
        if computed_embeddings_dict is not None:
            for i, content in enumerate(node_contents):
                if content:
                    computed_embeddings_dict[content] = text_embeddings[i]
        
        return text_embeddings

    def _get_query_tags(self, query, existing_tags, llm_client):
        """Récupère les tags associés à la requête via le LLM"""
        # Essayer différentes méthodes d'accès à la fonction de génération de tags
        if hasattr(llm_client, 'generate_tags_for_query'):
            return llm_client.generate_tags_for_query(query, existing_tags)
        elif hasattr(llm_client, 'llm_service') and hasattr(llm_client.llm_service, 'generate_tags_for_query'):
            return llm_client.llm_service.generate_tags_for_query(query, existing_tags)
        else:
            return self._generate_tags_for_query(query, existing_tags, llm_client)
    
    def _generate_tags_for_query(self, query, existing_tags, client):
        """
        Génère des tags pour une requête (ancienne interface).
        
        Args:
            query (str): Requête utilisateur.
            existing_tags (list): Liste des tags existants.
            client: Client LLM.
            
        Returns:
            list: Tags générés.
        """
        # Système de repli pour l'interface ancienne
        max_tags_to_show = 200
        tags_to_show = existing_tags[:max_tags_to_show] if len(existing_tags) > max_tags_to_show else existing_tags
        
        system_prompt = f"""Tu es un expert en catégorisation. 
Parmi la liste de tags existants suivante, sélectionne 3 à 10 tags qui sont les plus pertinents pour la requête de l'utilisateur.
Ces tags doivent représenter les concepts clés, entités et sujets de la requête.
Sélectionne uniquement des tags de la liste fournie, ne crée pas de nouveaux tags.

Tags disponibles: {', '.join(tags_to_show)}

Réponds UNIQUEMENT avec un tableau JSON de chaînes: ["tag1", "tag2", "tag3"]"""
        
        try:
            response = client.chat.completions.create(
                model=getattr(client, 'model', "gpt-3.5-turbo"),
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query},
                ],
                temperature=0.3,
                max_tokens=150
            )
            
            content = response.choices[0].message.content.strip()
            content = re.sub(r'^```json\s*', '', content)
            content = re.sub(r'\s*```$', '', content)
            
            # Vérifier que le contenu a bien la structure d'un tableau JSON
            if not (content.startswith('[') and content.endswith(']')):
                content = f"[{content}]"
            
            try:
                tags = json.loads(content)
                # Vérifier que tous les tags sélectionnés font partie des tags existants
                valid_tags = [tag for tag in tags if tag in existing_tags]
                return valid_tags
            except:
                # En cas d'erreur de parsing, faire un parsing simple
                tags = content.replace('[', '').replace(']', '').replace('"', '').split(',')
                tags = [tag.strip() for tag in tags if tag.strip() in existing_tags]
                return tags
                
        except Exception as e:
            print(f"Erreur lors de la génération des tags: {e}")
            return []
    
    def _normalize_scores(self, scores):
        """
        Normalise un tableau de scores entre 0 et 1 avec une approche robuste.
        
        Args:
            scores (ndarray): Scores à normaliser.
            
        Returns:
            ndarray: Scores normalisés.
        """
        if len(scores) == 0:
            return scores
            
        max_score = np.max(scores)
        min_score = np.min(scores)
        
        if max_score == min_score:
            return np.zeros_like(scores)
            
        return (scores - min_score) / (max_score - min_score)
    
    def calculate_bm25_scores(self, texts, query):
        """
        Calcule les scores BM25 entre les textes et une requête.
        
        Args:
            texts (list): Liste de textes.
            query (str): Requête de recherche.
            
        Returns:
            ndarray: Scores BM25.
        """
        # Protéger contre les textes vides
        safe_texts = [text if text else " " for text in texts]
        
        # Tokenisation simple
        tokenized_corpus = [text.lower().split() for text in safe_texts]
        tokenized_query = query.lower().split()
        
        # Création du modèle BM25
        bm25 = BM25Okapi(tokenized_corpus)
        
        # Calcul des scores
        scores = bm25.get_scores(tokenized_query)
        
        return scores
    
    def calculate_cosine_scores(self, text_embeddings, query_embedding):
        """
        Calcule les scores de similarité cosinus.
        
        Args:
            text_embeddings (ndarray): Embeddings des textes.
            query_embedding (ndarray): Embedding de la requête.
            
        Returns:
            ndarray: Scores de similarité.
        """
        query_embedding = query_embedding.reshape(1, -1)
        similarities = cosine_similarity(text_embeddings, query_embedding).flatten()
        return similarities
    
    def calculate_tfidf_scores(self, texts, query):
        """
        Calcule les scores TF-IDF entre les textes et une requête.
        
        Args:
            texts (list): Liste de textes.
            query (str): Requête de recherche.
            
        Returns:
            ndarray: Scores TF-IDF.
        """
        # Protéger contre les textes vides
        safe_texts = [text if text else " " for text in texts]
        
        # Créer un vectoriseur TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english')
        all_texts = safe_texts + [query]
        
        try:
            tfidf_matrix = vectorizer.fit_transform(all_texts)
            text_vectors = tfidf_matrix[:-1]
            query_vector = tfidf_matrix[-1]
            similarities = cosine_similarity(text_vectors, query_vector).flatten()
            return similarities
        except Exception as e:
            print(f"Erreur TF-IDF: {e}")
            return np.zeros(len(texts))
    
    def calculate_jaccard_similarity(self, set1, set2):
        """
        Calcule la similarité de Jaccard entre deux ensembles.
        
        Args:
            set1, set2 (set): Ensembles à comparer.
            
        Returns:
            float: Score de similarité entre 0 et 1.
        """
        if not set1 or not set2:
            return 0.0
        
        intersection = len(set(set1) & set(set2))
        union = len(set(set1) | set(set2))
        
        return intersection / union if union > 0 else 0.0
    
    def calculate_jaccard_scores(self, node_tags_list, query_tags):
        """
        Calcule les scores de similarité Jaccard entre les tags des nœuds et les tags de la requête.
        
        Args:
            node_tags_list (list): Liste des tags pour chaque nœud.
            query_tags (list): Tags de la requête.
            
        Returns:
            ndarray: Scores de similarité Jaccard.
        """
        scores = []
        
        for node_tags in node_tags_list:
            score = self.calculate_jaccard_similarity(node_tags, query_tags)
            scores.append(score)
        
        return np.array(scores)
    
    def get_graph_service(self):
        """
        Tente de récupérer le service de graphe pour accéder au KnowledgeGraph.
        
        Returns:
            GraphService ou None: Le service de graphe s'il est disponible.
        """
        try:
            # Essayer d'accéder à la session
            import streamlit as st
            if 'graph_service' in st.session_state:
                return st.session_state.graph_service
        except:
            pass
    
        return None