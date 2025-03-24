---
title: TF-IDF et pondération de termes
type: concept
tags:
- TF-IDF
- recherche d'information
- fouille de textes
- pondération
- statistique
- analyse textuelle
- fréquence de termes
- traitement du langage naturel
- indexation
date_creation: '2025-03-20'
date_modification: '2025-03-20'
seeAlso: '[[Algorithme BM25 pour la recherche d''information]]'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
relatedTo: '[[Word Embeddings et représentations vectorielles]]'
---
## Généralité

[TF-IDF](https://fr.wikipedia.org/wiki/TF-IDF) ([Term Frequency-Inverse Document Frequency](https://fr.wikipedia.org/wiki/Term_Frequency-Inverse_Document_Frequency)) est une méthode statistique de pondération utilisée en recherche d'information et en fouille de textes pour évaluer l'importance d'un terme dans un document par rapport à une collection de documents. Cette technique combine deux mesures : la fréquence d'un terme dans un document (TF) et l'inverse de la fréquence de ce terme dans l'ensemble des documents (IDF). TF-IDF permet de mettre en évidence les termes qui sont caractéristiques d'un document tout en minimisant l'importance des termes communs à tous les documents.

## Points clés

- TF-IDF combine la fréquence d'un terme dans un document (TF) avec sa rareté dans l'ensemble du corpus (IDF)
- Les termes avec un score TF-IDF élevé sont considérés comme plus pertinents et distinctifs pour un document
- Cette méthode est fondamentale pour de nombreuses applications comme la recherche documentaire, la classification de textes et le résumé automatique
- TF-IDF permet de filtrer les mots vides (stopwords) qui apparaissent fréquemment dans tous les documents
- La pondération TF-IDF transforme les documents textuels en vecteurs numériques exploitables par des algorithmes d'apprentissage

## Détails

La formule TF-IDF se décompose en deux parties principales :

1. **Term Frequency (TF)** : Mesure la fréquence d'apparition d'un terme dans un document. Plusieurs variantes existent :
   - TF brute : nombre d'occurrences du terme
   - TF normalisée : fréquence divisée par le nombre total de termes
   - TF logarithmique : 1 + log(fréquence) pour atténuer l'impact des termes très fréquents

2. **[Inverse Document Frequency](https://fr.wikipedia.org/wiki/Inverse_Document_Frequency) (IDF)** : Mesure la rareté d'un terme dans l'ensemble du corpus :
   - IDF = log(N/df) où N est le nombre total de documents et df le nombre de documents contenant le terme
   - Plus un terme est rare dans le corpus, plus sa valeur IDF est élevée

Le score final TF-IDF est le produit de ces deux mesures : TF-IDF = TF × IDF.

Cette pondération présente plusieurs avantages :
- Elle attribue un poids faible aux termes apparaissant dans de nombreux documents (comme les articles et prépositions)
- Elle valorise les termes qui apparaissent fréquemment dans un document mais rarement dans les autres
- Elle permet de représenter chaque document comme un vecteur dans un espace vectoriel où chaque dimension correspond à un terme

Dans les applications pratiques, TF-IDF est utilisé pour :
- Améliorer la pertinence des résultats des moteurs de recherche
- Extraire les mots-clés représentatifs d'un document
- Construire des matrices document-terme pour l'analyse de similarité entre textes
- Servir de prétraitement pour des algorithmes de clustering ou de classification

Malgré sa simplicité, TF-IDF reste une méthode efficace et largement utilisée, même avec l'avènement de techniques plus sophistiquées comme les embeddings de mots et les modèles de langage. Elle constitue souvent une baseline solide pour comparer les performances d'autres algorithmes de traitement du langage naturel.