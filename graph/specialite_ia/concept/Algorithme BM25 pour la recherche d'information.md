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

BM25 (Best Matching 25) est un algorithme de classement utilisé dans les systèmes de recherche d'information pour évaluer la pertinence d'un document par rapport à une requête. Développé par Stephen E. Robertson et Karen Spärck Jones comme une évolution du modèle probabiliste [TF-IDF](https://fr.wikipedia.org/wiki/TF-IDF), BM25 est devenu l'un des algorithmes de référence dans les moteurs de recherche modernes. Il équilibre la fréquence des termes dans les documents avec leur rareté dans la collection, tout en tenant compte de la longueur des documents.

## Points clés

- BM25 améliore le modèle TF-IDF en introduisant une saturation de la fréquence des termes, évitant ainsi la surpondération des termes très fréquents
- L'algorithme prend en compte la longueur des documents pour normaliser les scores, réduisant le biais envers les documents longs
- BM25 utilise deux paramètres ajustables (k1 et b) qui permettent d'optimiser les performances selon les caractéristiques spécifiques du corpus
- Il est largement utilisé comme référence (baseline) pour évaluer de nouveaux algorithmes de recherche d'information

## Détails

La formule de base de BM25 pour calculer le score d'un document D par rapport à une requête Q est la suivante :

```
score(D,Q) = ∑(IDF(qi) × (f(qi,D) × (k1 + 1)) / (f(qi,D) + k1 × (1 - b + b × |D|/avgdl)))
```

Où :
- qi représente chaque terme de la requête Q
- f(qi,D) est la fréquence du terme qi dans le document D
- |D| est la longueur du document (nombre de mots)
- avgdl est la longueur moyenne des documents dans la collection
- k1 et b sont des paramètres ajustables (typiquement, k1 ∈ [1.2, 2.0] et b = 0.75)
- IDF(qi) est la fréquence inverse du document, calculée comme : log((N - n(qi) + 0.5) / (n(qi) + 0.5) + 1)
  - N est le nombre total de documents
  - n(qi) est le nombre de documents contenant le terme qi

L'un des avantages majeurs de BM25 par rapport à TF-IDF est sa gestion de la saturation de la fréquence des termes. Alors que TF-IDF augmente linéairement avec la fréquence des termes, BM25 utilise une fonction qui sature, reconnaissant qu'un terme apparaissant 10 fois n'est pas nécessairement 10 fois plus important qu'un terme apparaissant une seule fois.

Le paramètre k1 contrôle la saturation de la fréquence des termes. Une valeur plus élevée de k1 signifie que la saturation est plus lente, tandis qu'une valeur plus faible entraîne une saturation plus rapide.

Le paramètre b (entre 0 et 1) contrôle la normalisation de la longueur du document. Une valeur de b = 1 signifie une normalisation complète, tandis que b = 0 signifie aucune normalisation.

BM25 a connu plusieurs variantes, notamment BM25F qui prend en compte la structure des documents (titres, corps, etc.) et BM25+ qui ajoute un terme delta pour améliorer les performances sur les documents courts.

Malgré l'émergence de techniques d'apprentissage profond pour la recherche d'information, BM25 reste pertinent en raison de sa simplicité, de son efficacité et de sa robustesse, servant souvent de composant dans des systèmes de recherche hybrides plus complexes.