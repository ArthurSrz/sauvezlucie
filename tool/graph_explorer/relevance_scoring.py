import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import re
from rank_bm25 import BM25Okapi
from config import EMBEDDING_MODEL
from prompts import TAG_GENERATION_SYSTEM_PROMPT
from config import LLM_MODEL, DEFAULT_TEMPERATURE

def get_embedding_model():
    """Charge le modèle d'embedding."""
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(EMBEDDING_MODEL, device='cpu')

def compute_embeddings(texts, query=None, cached_embeddings=None):
    """Calcule les embeddings pour des textes et une requête."""
    if isinstance(texts, str):
        texts = [texts]
    
    result = {}
    
    # Utiliser les embeddings mis en cache si disponibles
    if cached_embeddings is not None:
        result['text_embeddings'] = cached_embeddings
    else:
        # Calculer les embeddings des textes
        model = get_embedding_model()
        result['text_embeddings'] = model.encode([f"passage: {text}" for text in texts])
    
    # Calculer l'embedding de la requête si fournie
    if query:
        model = get_embedding_model()
        query_embedding = model.encode([f"query: {query}"])[0]
        result['query_embedding'] = query_embedding
    
    return result

def calculate_bm25_scores(texts, query):
    """Calcule les scores BM25 entre les textes et une requête."""
    # Tokenisation simple
    tokenized_corpus = [text.lower().split() for text in texts]
    tokenized_query = query.lower().split()
    
    # Création du modèle BM25
    bm25 = BM25Okapi(tokenized_corpus)
    
    # Calcul des scores
    scores = bm25.get_scores(tokenized_query)
    
    return scores

def calculate_cosine_scores(text_embeddings, query_embedding):
    """Calcule les scores de similarité cosinus."""
    query_embedding = query_embedding.reshape(1, -1)
    similarities = cosine_similarity(text_embeddings, query_embedding).flatten()
    return similarities

def calculate_tfidf_scores(texts, query):
    """Calcule les scores TF-IDF entre les textes et une requête."""
    vectorizer = TfidfVectorizer(stop_words='english')
    all_texts = texts + [query]
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    text_vectors = tfidf_matrix[:-1]
    query_vector = tfidf_matrix[-1]
    similarities = cosine_similarity(text_vectors, query_vector).flatten()
    return similarities

def generate_tags_for_query(query, existing_tags, client=None):
    """Génère des tags pour une requête en utilisant un LLM, en se basant sur les tags existants."""
    if client is None:
        return []
    
    # Limiter le nombre de tags si la liste est très longue
    max_tags_to_show = 200
    tags_to_show = existing_tags[:max_tags_to_show] if len(existing_tags) > max_tags_to_show else existing_tags
    
    system_prompt = TAG_GENERATION_SYSTEM_PROMPT.format(tags=', '.join(tags_to_show))
    
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query},
            ],
            temperature=DEFAULT_TEMPERATURE,
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

def calculate_jaccard_similarity(set1, set2):
    """Calcule la similarité de Jaccard entre deux ensembles."""
    if not set1 or not set2:
        return 0.0
    
    intersection = len(set(set1) & set(set2))
    union = len(set(set1) | set(set2))
    
    return intersection / union if union > 0 else 0.0

def calculate_jaccard_scores(node_tags_list, query_tags):
    """Calcule les scores de similarité Jaccard entre les tags des nœuds et les tags de la requête."""
    scores = []
    
    for node_tags in node_tags_list:
        score = calculate_jaccard_similarity(node_tags, query_tags)
        scores.append(score)
    
    return np.array(scores)

def calculate_combined_scores(G, query, weights, llm_client=None, cached_embeddings=None):
    """Calcule les scores combinés pour tous les nœuds d'un graphe par rapport à une requête."""
    # Extraire les données des nœuds
    nodes = list(G.nodes())
    node_contents = []
    node_tags_list = []
    
    # Récupérer tous les tags uniques
    all_unique_tags = set()
    for node in nodes:
        attrs = G.nodes[node]
        content = attrs.get('content', '')
        tags = attrs.get('tags', [])
        
        node_contents.append(content)
        node_tags_list.append(tags)
        
        # Ajouter à l'ensemble des tags uniques
        all_unique_tags.update(tags)
    
    # Convertir en liste pour la génération de tags
    existing_tags = list(all_unique_tags)
    
    # Calculer les scores selon les métriques sélectionnées
    cosine_scores = np.zeros(len(nodes))
    tfidf_scores = np.zeros(len(nodes))
    bm25_scores = np.zeros(len(nodes))
    jaccard_scores = np.zeros(len(nodes))
    
    # Similarité cosinus avec embeddings
    embeddings_result = None
    if weights.get('cosine', 0) > 0:
        try:
            embeddings_result = compute_embeddings(
                node_contents, 
                query, 
                cached_embeddings=cached_embeddings
            )
            cosine_scores = calculate_cosine_scores(
                embeddings_result['text_embeddings'], 
                embeddings_result['query_embedding']
            )
        except Exception as e:
            print(f"Erreur dans le calcul des embeddings: {e}")
    
    # TF-IDF
    if weights.get('tfidf', 0) > 0:
        try:
            tfidf_scores = calculate_tfidf_scores(node_contents, query)
        except Exception as e:
            print(f"Erreur dans le calcul TF-IDF: {e}")
    
    # BM25
    if weights.get('bm25', 0) > 0:
        try:
            bm25_scores = calculate_bm25_scores(node_contents, query)
        except Exception as e:
            print(f"Erreur dans le calcul BM25: {e}")
    
    # Jaccard sur les tags
    if weights.get('jaccard', 0) > 0 and llm_client is not None:
        try:
            query_tags = generate_tags_for_query(query, existing_tags, llm_client)
            jaccard_scores = calculate_jaccard_scores(node_tags_list, query_tags)
            
            # Assurer que les scores Jaccard sont normalisés de 0 à 1
            # où 1 est le score maximum trouvé
            max_jaccard = np.max(jaccard_scores) if len(jaccard_scores) > 0 and np.max(jaccard_scores) > 0 else 1
            jaccard_scores = jaccard_scores / max_jaccard
            
        except Exception as e:
            print(f"Erreur dans le calcul Jaccard: {e}")
    
    # Normaliser les autres scores
    def normalize(scores):
        max_score = np.max(scores) if len(scores) > 0 and np.max(scores) > 0 else 1
        return scores / max_score
    
    cosine_scores = normalize(cosine_scores)
    tfidf_scores = normalize(tfidf_scores)
    bm25_scores = normalize(bm25_scores)
    
    # Combiner les scores selon les poids
    combined_scores = (
        weights.get('cosine', 0) * cosine_scores +
        weights.get('tfidf', 0) * tfidf_scores +
        weights.get('bm25', 0) * bm25_scores +
        weights.get('jaccard', 0) * jaccard_scores
    )
    
    # Créer des dictionnaires pour les scores individuels
    individual_scores = {
        'cosine': {node: float(score) for node, score in zip(nodes, cosine_scores)},
        'tfidf': {node: float(score) for node, score in zip(nodes, tfidf_scores)},
        'bm25': {node: float(score) for node, score in zip(nodes, bm25_scores)},
        'jaccard': {node: float(score) for node, score in zip(nodes, jaccard_scores)}
    }
    
    # Créer le dictionnaire de résultats avec des valeurs flottantes standard
    result = {}
    for i, node in enumerate(nodes):
        try:
            result[node] = float(combined_scores[i])
        except:
            result[node] = 0.0
    
    # Pour la sécurité, convertir les embeddings en liste Python standard
    embeddings_to_return = None
    if embeddings_result and 'text_embeddings' in embeddings_result:
        try:
            embeddings_to_return = embeddings_result['text_embeddings'].tolist() 
        except:
            pass
    
    return result, embeddings_to_return, individual_scores

def score_to_color(score):
    """Convertit un score entre 0 et 1 en une couleur du rouge au vert."""
    score = max(0, min(1, score))
    r = int(255 * (1 - score))
    g = int(255 * score)
    b = 0
    return f"#{r:02x}{g:02x}{b:02x}"
