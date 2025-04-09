---
title: Impureté de Gini, entropie et erreur de classification
type: concept
tags:
- machine learning
- arbres de décision
- impureté de Gini
- entropie
- erreur de classification
- métriques
- classification
- apprentissage supervisé
- data science
- algorithmes
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Arbre de décision]]'
---
## Généralité

Les mesures d'[impureté](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision#Mesures_d'impuret%C3%A9) sont des métriques fondamentales utilisées dans les algorithmes d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique), particulièrement dans les [arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision), pour évaluer la qualité des divisions des données. Elles quantifient l'homogénéité des échantillons au sein des nœuds d'un arbre de décision et guident le processus de construction de l'arbre en identifiant les divisions optimales.

## Points clés

- **Impureté de Gini**: Mesure la probabilité d'erreur de classification (indice de [Corrado Gini](https://fr.wikipedia.org/wiki/Corrado_Gini))
- **[Entropie](https://fr.wikipedia.org/wiki/Entropie_(th%C3%A9orie_de_l%27information))**: Mesure le désordre selon la théorie de l'information de [Shannon](https://fr.wikipedia.org/wiki/Claude_Shannon)
- **Erreur de classification**: Mesure simple de la proportion d'éléments mal classés
- Utilisées dans les algorithmes comme [CART](https://fr.wikipedia.org/wiki/Classification_and_regression_tree) et ID3
- Différence de performance généralement inférieure à 2% entre Gini et entropie

## Détails

L'impureté de [Gini](https://fr.wikipedia.org/wiki/Corrado_Gini), également appelée indice de Gini, est calculée comme: