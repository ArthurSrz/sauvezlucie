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
date_creation: '2025-03-20'
date_modification: '2025-03-20'
uses: '[[Validation croisée en apprentissage automatique]]'
relatedTo: '[[Fonctions de perte en apprentissage profond]]'
rdfs:subClassOf: '[[Choix de la mesure d''erreur]]'
---

## Généralité

Le compromis biais-variance dans la sélection de métriques représente un équilibre fondamental en science des données et en apprentissage automatique. Il s'agit de trouver le juste milieu entre des métriques trop simples qui sous-estiment la complexité du problème (biais élevé) et des métriques trop complexes qui s'adaptent excessivement aux données d'entraînement (variance élevée). Ce compromis est crucial pour sélectionner des métriques d'évaluation qui permettront de construire des modèles robustes et généralisables.

## Points clés

- Une métrique à fort biais simplifie trop la réalité mais offre une faible variance, tandis qu'une métrique à forte variance capture plus de nuances mais risque le surapprentissage
- La sélection optimale de métriques doit équilibrer la capacité à représenter fidèlement le phénomène étudié et la stabilité des résultats
- Le contexte d'application et la quantité de données disponibles influencent fortement le point d'équilibre optimal du compromis biais-variance
- Les techniques de validation croisée permettent d'évaluer empiriquement ce compromis pour différentes métriques candidates

## Détails

Le compromis biais-variance est un concept fondamental qui s'applique non seulement aux modèles mais aussi aux métriques utilisées pour les évaluer. Une métrique idéale devrait capturer l'essence du problème sans être trop sensible aux fluctuations aléatoires dans les données.

Les métriques à fort biais (comme l'erreur quadratique moyenne dans certains contextes) peuvent être trop simplistes et manquer des aspects importants du problème. Par exemple, dans un problème de classification déséquilibrée, l'exactitude (accuracy) présente un biais car elle ne tient pas compte de la distribution des classes. Cependant, ces métriques offrent généralement une faible variance, ce qui signifie qu'elles produisent des résultats cohérents sur différents échantillons.

À l'inverse, les métriques à forte variance (comme certaines métriques personnalisées complexes) peuvent s'adapter excessivement aux particularités des données d'entraînement. Elles peuvent sembler performantes sur l'ensemble d'entraînement mais échouer à généraliser sur de nouvelles données. Par exemple, une métrique qui donne un poids très spécifique à certaines erreurs basées sur les caractéristiques observées uniquement dans l'ensemble d'entraînement.

La quantité de données disponibles influence considérablement ce compromis. Avec peu de données, des métriques simples à faible variance sont souvent préférables pour éviter le surapprentissage. Avec beaucoup de données, des métriques plus complexes peuvent être utilisées sans risque excessif de surapprentissage.

Pour trouver le bon équilibre, les praticiens utilisent souvent:
1. La validation croisée pour comparer la stabilité des différentes métriques
2. L'analyse de sensibilité pour évaluer comment les métriques réagissent aux variations dans les données
3. Des ensembles de métriques complémentaires plutôt qu'une seule métrique
4. L'expertise du domaine pour s'assurer que les métriques choisies ont une pertinence pratique

En pratique, ce compromis se manifeste dans des décisions comme choisir entre la précision et le rappel, ou déterminer la complexité d'une fonction de coût personnalisée. La meilleure approche consiste souvent à commencer par des métriques standard bien comprises, puis à les raffiner progressivement tout en surveillant attentivement les signes de surapprentissage.