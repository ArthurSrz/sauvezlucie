---
title: Algorithme BM25 pour la recherche d'information
type: concept
tags:
- BM25
- recherche d'information
- algorithme
- moteur de recherche
- TF-IDF
- classement
- pertinence
- Robertson
- Spärck Jones
date_creation: '2025-03-20'
date_modification: '2025-03-20'
subClassOf: '[[TF-IDF et pondération de termes]]'
---
## Généralité

[BM25](https://fr.wikipedia.org/wiki/Okapi_BM25) (Best Matching 25) est un algorithme de classement utilisé dans les systèmes de [recherche d'information](https://fr.wikipedia.org/wiki/Recherche_d%27information) pour évaluer la pertinence d'un document par rapport à une requête. Développé dans les années 1970-1980 par Stephen E. Robertson et Karen Spärck Jones comme une évolution du modèle probabiliste [TF-IDF](https://fr.wikipedia.org/wiki/TF-IDF), BM25 est devenu l'un des algorithmes de référence dans les moteurs de recherche modernes.

## Points clés

- Améliore [TF-IDF](https://fr.wikipedia.org/wiki/TF-IDF) en introduisant une saturation non linéaire de la fréquence des termes et une normalisation sophistiquée de la longueur des documents
- Utilise deux paramètres ajustables (k1 entre 1.2-2.0 et b=0.75) pour optimiser les performances selon les caractéristiques du corpus
- Large utilisation comme référence dans l'évaluation des systèmes de recherche (benchmarks [TREC](https://fr.wikipedia.org/wiki/Text_Retrieval_Conference)) et implémenté dans des bibliothèques majeures comme [Lucene](https://fr.wikipedia.org/wiki/Apache_Lucene) et [Elasticsearch](https://fr.wikipedia.org/wiki/Elasticsearch)
- Basé sur le [modèle de pertinence probabiliste](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_pertinence_probabiliste) de Robertson et Spärck Jones
- Possède plusieurs variantes (BM25F, BM25+, BM25L) pour étendre son applicabilité à des scénarios complexes

## Détails

La formule de base de BM25 pour calculer le score d'un document D par rapport à une requête Q est :