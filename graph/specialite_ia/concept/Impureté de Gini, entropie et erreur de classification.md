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
date_creation: '2025-03-21'
date_modification: '2025-03-21'
isPartOf: '[[Arbre de décision]]'
---
## Généralité

Les mesures d'impureté sont des métriques fondamentales utilisées dans les algorithmes d'apprentissage automatique, particulièrement dans les arbres de décision, pour évaluer la qualité des divisions des données. Les trois mesures les plus courantes sont l'impureté de Gini, l'entropie et l'erreur de classification. Ces métriques quantifient l'homogénéité des échantillons au sein des nœuds d'un arbre de décision et guident le processus de construction de l'arbre en identifiant les divisions optimales.

## Points clés

- L'impureté de Gini mesure la probabilité qu'un élément soit mal classé s'il est étiqueté aléatoirement selon la distribution des classes dans un ensemble.
- L'entropie, issue de la théorie de l'information, quantifie le désordre ou l'incertitude dans un ensemble de données.
- L'erreur de classification représente simplement la proportion d'éléments qui n'appartiennent pas à la classe majoritaire.
- Le choix entre ces mesures influence la structure finale de l'arbre de décision et ses performances prédictives.

## Détails

### Impureté de Gini

L'impureté de Gini est calculée comme:
```
Gini = 1 - Σ(pi²)
```
où pi est la proportion d'éléments appartenant à la classe i.

Cette mesure atteint son minimum (0) lorsque tous les éléments appartiennent à une seule classe (pureté parfaite) et son maximum lorsque les éléments sont uniformément répartis entre toutes les classes. L'impureté de Gini est privilégiée dans l'algorithme CART ([Classification and Regression Trees](https://fr.wikipedia.org/wiki/Classification_and_Regression_Trees)) et est généralement plus rapide à calculer que l'entropie.

### Entropie

L'entropie est définie par:
```
Entropie = -Σ(pi * log2(pi))
```

Elle mesure la quantité d'information nécessaire pour décrire un ensemble. Une entropie de 0 indique une pureté parfaite (tous les éléments appartiennent à la même classe), tandis qu'une valeur élevée indique un mélange de classes. L'entropie est utilisée dans les algorithmes ID3 et C4.5 et tend à créer des arbres plus équilibrés que l'impureté de Gini.

### Erreur de classification

L'erreur de classification est simplement:
```
Erreur = 1 - max(pi)
```
où max(pi) est la proportion de la classe majoritaire.

Cette mesure est la plus intuitive mais aussi la moins sensible aux changements de distribution des probabilités, ce qui la rend moins efficace pour la construction d'arbres de décision.

## [Comparaison](https://fr.wikipedia.org/wiki/Comparaison) et choix

En pratique, l'impureté de Gini et l'entropie donnent souvent des résultats similaires, bien que l'entropie puisse être légèrement plus coûteuse en calcul. L'erreur de classification est rarement utilisée comme critère de division car elle ne pénalise pas suffisamment les nœuds impurs lors de la construction de l'arbre.

Le choix de la mesure d'impureté dépend du problème spécifique, des caractéristiques des données et des objectifs de l'analyse. Il est souvent recommandé d'expérimenter avec différentes mesures pour déterminer celle qui produit les meilleurs résultats pour un ensemble de données particulier.