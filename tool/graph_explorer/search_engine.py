def simple_keyword_search(G, query):
    """
    Recherche simple par mots-clés dans le graphe.
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

def semantic_search(G, query, model=None):
    """
    Point d'entrée pour une future recherche sémantique utilisant des embeddings.
    À implémenter ultérieurement.
    """
    # Pour l'instant, on utilise la recherche par mots-clés
    return simple_keyword_search(G, query)
