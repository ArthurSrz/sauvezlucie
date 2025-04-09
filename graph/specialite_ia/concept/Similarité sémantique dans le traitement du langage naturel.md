---
title: Similarité sémantique dans le traitement du langage naturel
type: concept
tags:
- NLP
- traitement du langage naturel
- similarité sémantique
- linguistique computationnelle
- IA
- analyse textuelle
- sémantique
- machine learning
date_creation: '2025-03-20'
date_modification: '2025-03-20'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
uses: '[[Word Embeddings et représentations vectorielles]]'
---
## Généralité

La [similarité sémantique](https://fr.wikipedia.org/wiki/Similarit%C3%A9_s%C3%A9mantique) est un concept fondamental dans le [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) (NLP) qui mesure le degré de ressemblance entre des mots, des phrases ou des documents en fonction de leur sens plutôt que de leur forme. Ce concept trouve ses racines dans la linguistique computationnelle et s'appuie sur des théories comme la distributionnalité et les [réseaux sémantiques](https://fr.wikipedia.org/wiki/R%C3%A9seau_s%C3%A9mantique).

## Points clés

- La similarité sémantique repose sur des représentations vectorielles ([embeddings](https://fr.wikipedia.org/wiki/Word_embedding)) qui capturent le sens des mots et des phrases
- Les techniques courantes incluent [Word2Vec](https://fr.wikipedia.org/wiki/Word2vec), GloVe, et [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage))
- Les mesures de similarité comme la [similarité cosinus](https://fr.wikipedia.org/wiki/Similarit%C3%A9_cosinus) sont utilisées pour quantifier la proximité sémantique
- Applications majeures : recherche d'information, systèmes de recommandation, détection de paraphrase, systèmes de questions-réponses
- Évaluée via des benchmarks comme STS (Semantic Textual Similarity) et SICK

## Détails

### Fondements théoriques

La similarité sémantique s'appuie sur le principe que les mots ou expressions qui apparaissent dans des contextes similaires ont tendance à avoir des significations similaires. Cette intuition, formalisée par la [linguistique distributionnelle](https://fr.wikipedia.org/wiki/S%C3%A9mantique_distributionnelle) (théorie formulée par [John Rupert Firth](https://fr.wikipedia.org/wiki/John_Rupert_Firth)), est à la base de nombreuses techniques modernes de NLP.

### Techniques et modèles

Les représentations vectorielles ([word embeddings](https://fr.wikipedia.org/wiki/Word_embedding)) constituent la pierre angulaire de la similarité sémantique :

- **Word2Vec** (incluant CBOW et Skip-gram, développé par l'équipe de Tomas Mikolov chez Google en 2013)
- **GloVe** (créé par l'équipe de Christopher Manning à Stanford en 2014)
- **BERT** (2018, Google) utilisant des mécanismes d'attention multi-têtes

Pour les textes plus longs, plusieurs approches existent :
1. **Agrégation simple** : moyenne des vecteurs de mots
2. **Doc2Vec** : extension de Word2Vec pour les documents entiers
3. **Modèles transformers** : BERT, RoBERTa, ou GPT génèrent des embeddings contextuels

### Mesures de similarité

La mesure de similarité la plus couramment utilisée est la [similarité cosinus](https://fr.wikipedia.org/wiki/Similarit%C3%A9_cosinus), qui calcule le cosinus de l'angle entre deux vecteurs. D'autres mesures incluent :
- Distance euclidienne
- Divergence de Kullback-Leibler

### Applications

Les principales applications incluent :
- **Moteurs de recherche** : expansion de requêtes
- **Systèmes de recommandation** : technologie utilisée par Amazon et Netflix
- **Détection de paraphrase et de plagiat**
- **Systèmes de questions-réponses** : comme [IBM Watson](https://fr.wikipedia.org/wiki/Watson_(intelligence_artificielle))
- **Analyse de sentiment**
- Catégorisation de textes et génération de résumés automatiques

### Évaluation et défis

Les benchmarks STS et SICK permettent d'évaluer ces systèmes. Les meilleurs modèles atteignent des scores de corrélation >0.85 avec des évaluations humaines sur certains jeux de données.

Les défis actuels incluent :
- Ambiguïté lexicale
- Expressions idiomatiques
- Sarcasme
- Domaines spécifiques