---
title: Compromis biais-variance dans la sélection de métriques
type: concept
tags:
- science des données
- apprentissage automatique
- biais-variance
- métriques d'évaluation
- modélisation
- statistiques
- overfitting
- performance de modèle
date_creation: '2025-04-08'
date_modification: '2025-04-08'
uses: '[[Validation croisée en apprentissage automatique]]'
subClassOf: '[[Choix de la mesure d''erreur]]'
---
## Généralité

Le [compromis biais-variance](https://fr.wikipedia.org/wiki/Biais-variance) dans la sélection de métriques représente un équilibre fondamental en [science des données](https://fr.wikipedia.org/wiki/Science_des_donn%C3%A9es) et en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique). Ce concept, formulé initialement dans les années 1970 (selon Wikipedia "Bias–variance tradeoff"), a été popularisé par les travaux du statisticien [Leo Breiman](https://fr.wikipedia.org/wiki/Leo_Breiman). Il s'agit de trouver le juste milieu entre des métriques trop simples qui sous-estiment la complexité du problème (biais élevé) et des métriques trop complexes qui s'adaptent excessivement aux données d'entraînement (variance élevée).

## Points clés

- Une métrique à fort biais simplifie trop la réalité mais offre une faible variance, tandis qu'une métrique à forte variance capture plus de nuances mais risque le surapprentissage
- La sélection optimale de métriques doit équilibrer la capacité à représenter fidèlement le phénomène étudié et la stabilité des résultats
- Le contexte d'application (prédiction vs. inférence) et la quantité de données disponibles influencent fortement le point d'équilibre optimal
- Les techniques de [validation croisée](https://fr.wikipedia.org/wiki/Validation_croisée) permettent d'évaluer empiriquement ce compromis
- Des méthodes avancées comme le [bagging](https://fr.wikipedia.org/wiki/Bootstrap_aggregating) et le boosting ont été spécifiquement développées pour manipuler ce compromis

## Détails

Ce compromis est crucial pour sélectionner des métriques d'évaluation qui permettront de construire des modèles robustes et généralisables. En pratique, un biais élevé se manifeste par des erreurs systématiques (comme dans un modèle linéaire appliqué à des données non-linéaires), tandis qu'une variance élevée conduit au surapprentissage (overfitting), où le modèle mémorise les particularités du jeu d'entraînement au détriment de sa capacité à généraliser.

Selon Wikipédia ("Bias–variance tradeoff"), ce dilemme est souvent illustré par la "courbe en U" montrant comment l'erreur totale d'un modèle dépend de sa complexité : l'erreur de biais diminue avec la complexité, tandis que l'erreur de variance augmente, créant un minimum optimal.

Les métriques à fort biais (comme l'erreur quadratique moyenne dans certains contextes) peuvent être trop simplistes et manquer des aspects importants du problème. Par exemple, dans un problème de classification déséquilibrée, l'exactitude (accuracy) présente effectivement un biais comme le confirme Wikipédia. À l'inverse, les métriques à forte variance peuvent s'adapter excessivement aux particularités des données d'entraînement.

La théorie de la capacité de [Vapnik-Chervonenkis](https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_Vapnik-Chervonenkis), citée correctement sur Wikipédia, fournit un cadre théorique pour quantifier cette relation.

Pour trouver le bon équilibre, les praticiens utilisent souvent:
- La validation croisée (comme la k-fold cross-validation) pour comparer la stabilité des différentes métriques
- L'analyse de sensibilité pour évaluer comment les métriques réagissent aux variations dans les données
- Des ensembles de métriques complémentaires plutôt qu'une seule métrique
- L'expertise du domaine pour s'assurer que les métriques choisies ont une pertinence pratique

Des techniques comme la validation croisée ou la régularisation (L1/L2) ont été développées spécifiquement pour gérer ce compromis. La meilleure approche consiste souvent à commencer par des métriques standard bien comprises, puis à les raffiner progressivement tout en surveillant attentivement les signes de surapprentissage.