---
title: Critères d'erreur pour séries temporelles
type: concept
tags:
- séries temporelles
- métriques d'évaluation
- prévision
- modèles prédictifs
- analyse quantitative
- validation de modèle
- statistiques
- erreur de prédiction
date_creation: '2025-03-20'
date_modification: '2025-03-20'
isPartOf: '[[Choix de la mesure d''erreur]]'
relatedTo: '[[Métriques d''évaluation pour les modèles de régression]]'
---
## Généralité

Les critères d'erreur pour [séries temporelles](https://fr.wikipedia.org/wiki/S%C3%A9rie_temporelle) sont des métriques quantitatives utilisées pour évaluer la précision des modèles de prévision. Ces critères permettent de mesurer l'écart entre les valeurs prédites par un modèle et les valeurs réellement observées dans une série temporelle. Ils constituent un élément fondamental dans le processus de sélection, de validation et d'optimisation des modèles prédictifs.

## Points clés

- Les critères d'erreur permettent de quantifier objectivement la performance des modèles de prévision
- Différents critères mettent l'accent sur différents aspects de l'erreur:
  - [MAE](https://fr.wikipedia.org/wiki/Erreur_absolue_moyenne) pour la magnitude absolue
  - [MAPE](https://fr.wikipedia.org/wiki/Erreur_en_pourcentage_moyenne_absolue) pour l'erreur relative
  - [MSE](https://fr.wikipedia.org/wiki/Erreur_quadratique_moyenne)/[RMSE](https://fr.wikipedia.org/wiki/Racine_de_l%27erreur_quadratique_moyenne) qui pénalisent les grandes erreurs
- Le choix du critère doit être adapté au contexte d'application et aux caractéristiques des données

## Détails

Les critères d'erreur pour séries temporelles se divisent en plusieurs catégories principales :

**Critères basés sur les valeurs absolues**  
Le [MAE (Mean Absolute Error)](https://fr.wikipedia.org/wiki/Mean_absolute_error) calcule la moyenne des valeurs absolues des erreurs. Simple à interpréter, il représente l'amplitude moyenne des erreurs sans tenir compte de leur direction (`MAE = (1/n) × Σ|y_i - ŷ_i|`). Le [MAPE (Mean Absolute Percentage Error)](https://fr.wikipedia.org/wiki/Mean_absolute_percentage_error) exprime l'erreur en pourcentage de la valeur réelle, utile pour comparer entre séries d'échelles différentes (`MAPE = (100%/n) × Σ|(y_i - ŷ_i)/y_i|`). Le [MdAE (Median Absolute Error)](https://fr.wikipedia.org/wiki/Median_absolute_deviation) utilise la médiane des erreurs absolues, ce qui le rend moins sensible aux valeurs aberrantes que la MAE.

**Critères basés sur les erreurs quadratiques**  
Le [MSE (Mean Squared Error)](https://fr.wikipedia.org/wiki/Mean_squared_error) calcule la moyenne des carrés des erreurs, pénalisant davantage les grandes erreurs (`MSE = (1/n) × Σ(y_i - ŷ_i)²`). Le [RMSE (Root Mean Squared Error)](https://fr.wikipedia.org/wiki/Root_mean_square_error) est la racine carrée de la MSE, exprimée dans la même unité que la variable d'origine (`RMSE = √MSE`). Le [RMSLE (Root Mean Squared Logarithmic Error)](https://fr.wikipedia.org/wiki/Root_mean_square_deviation) est particulièrement utile lorsque les erreurs relatives sont plus importantes que les erreurs absolues.

**Critères spécifiques aux séries temporelles**  
Le [MASE (Mean Absolute Scaled Error)](https://fr.wikipedia.org/wiki/Mean_absolute_scaled_error) compare l'erreur du modèle à celle d'une méthode naïve, particulièrement utile pour les séries temporelles saisonnières. [Theil's U](https://fr.wikipedia.org/wiki/Theil%27s_U) mesure la précision relative d'un modèle par rapport à une prévision naïve, avec valeurs entre 0 et 1.

**Considérations pratiques**  
Le choix du critère d'erreur doit tenir compte de plusieurs facteurs : la présence de valeurs extrêmes ou aberrantes, l'importance relative des grandes erreurs, la nécessité de comparabilité entre différentes séries, et la présence de valeurs nulles ou proches de zéro. Dans la pratique, il est souvent recommandé d'utiliser plusieurs critères d'erreur complémentaires pour obtenir une évaluation plus complète de la performance des modèles.