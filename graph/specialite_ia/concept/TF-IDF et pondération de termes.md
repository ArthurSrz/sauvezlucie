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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
seeAlso: '[[Algorithme BM25 pour la recherche d''information]]'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
relatedTo: '[[Word Embeddings et représentations vectorielles]]'
---
## Généralité

[TF-IDF](https://fr.wikipedia.org/wiki/TF-IDF) (Term Frequency-Inverse Document Frequency) est une méthode statistique de pondération utilisée en [recherche d'information](https://fr.wikipedia.org/wiki/Recherche_d%27information) et en fouille de textes. Développée dans les années 1960-1970 par [Karen Spärck Jones](https://fr.wikipedia.org/wiki/Karen_Sp%C3%A4rck_Jones) et popularisée par Gerard Salton, elle permet d'évaluer l'importance d'un terme dans un document par rapport à une collection de documents.

## Points clés

- Combine deux mesures : **Term Frequency (TF)** (fréquence relative dans un document) et **Inverse Document Frequency (IDF)** (importance globale dans le corpus)
- Met en évidence les termes caractéristiques d'un document tout en minimisant l'importance des termes communs
- Transforme les documents textuels en vecteurs numériques exploitables par des algorithmes
- Fondamentale pour les moteurs de recherche, classification de textes et systèmes de recommandation
- Reste largement utilisée comme baseline en [TALN](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) malgré des techniques plus récentes

## Détails

La formule complète est :  
\[ \text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t) \]  
avec  
\[ \text{IDF}(t) = \log\left(\frac{N}{n_t}\right) \]  
où :
- \(N\) = nombre total de documents
- \(n_t\) = nombre de documents contenant le terme \(t\)

Les composantes principales sont :
1. **Term Frequency (TF)** :
   - TF brute : nombre d'occurrences du terme
   - TF normalisée : fréquence divisée par le nombre total de termes
   - TF logarithmique : 1 + log(fréquence) pour atténuer l'impact des termes très fréquents

2. **Inverse Document Frequency (IDF)** :
   - IDF = log(N/df) où df = nombre de documents contenant le terme
   - Formulation originale de Karen Spärck Jones (1972) : log(N/df + 1)

Parmi les applications pratiques de TF-IDF, on trouve :
- Amélioration de la pertinence des résultats des [moteurs de recherche](https://fr.wikipedia.org/wiki/Moteur_de_recherche) (système [SMART](https://fr.wikipedia.org/wiki/Syst%C3%A8me_SMART))
- Extraction des mots-clés représentatifs d'un document
- Construction de matrices document-terme pour l'analyse de similarité
- Prétraitement pour des algorithmes (K-means, Naive Bayes)
- Filtrage automatique des stopwords (termes très fréquents comme "le", "un")

Cette méthode présente plusieurs avantages :
- Attribution d'un poids faible aux termes apparaissant dans de nombreux documents
- Valorisation des termes fréquents dans un document mais rares dans les autres
- Permet une représentation vectorielle dans un [espace vectoriel](https://fr.wikipedia.org/wiki/Espace_vectoriel)
- Méthode robuste et interprétable

Cependant, elle a quelques limitations :
- Ne capture pas les relations sémantiques entre termes
- Sensible à la taille et à la composition du corpus
- Nécessite souvent des ajustements (listes de stopwords, normalisation)

Selon les travaux de [Gerard Salton](https://fr.wikipedia.org/wiki/Gerard_Salton), cette représentation vectorielle est particulièrement efficace pour calculer la similarité entre documents via la similarité cosinus.