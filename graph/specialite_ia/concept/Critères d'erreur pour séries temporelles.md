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

Les critères d'erreur pour séries temporelles sont des métriques quantitatives utilisées pour évaluer la précision des modèles de prévision. Ces critères permettent de mesurer l'écart entre les valeurs prédites par un modèle et les valeurs réellement observées dans une série temporelle. Ils constituent un élément fondamental dans le processus de sélection, de validation et d'optimisation des modèles prédictifs.

## Points clés

- Les critères d'erreur permettent de quantifier objectivement la performance des modèles de prévision
- Différents critères mettent l'accent sur différents aspects de l'erreur (magnitude absolue, erreur relative, pénalisation des grandes erreurs)
- Le choix du critère d'erreur doit être adapté au contexte spécifique de l'application et aux objectifs de la modélisation
- La comparaison entre modèles doit se faire sur la base du même critère d'erreur

## Détails

### Critères d'erreur basés sur les valeurs absolues

- **MAE (Mean Absolute Error)** : Moyenne des valeurs absolues des erreurs. Simple à interpréter, il représente l'amplitude moyenne des erreurs sans tenir compte de leur direction.
  
  MAE = (1/n) × Σ|y_i - ŷ_i|

- **MAPE (Mean Absolute Percentage Error)** : Exprime l'erreur en pourcentage de la valeur réelle, ce qui facilite la comparaison entre séries d'échelles différentes.
  
  MAPE = (100%/n) × Σ|(y_i - ŷ_i)/y_i|

- **MdAE (Median Absolute Error)** : Médiane des erreurs absolues, moins sensible aux valeurs aberrantes que la MAE.

### Critères d'erreur basés sur les erreurs quadratiques

- **MSE (Mean Squared Error)** : Moyenne des carrés des erreurs. Pénalise davantage les grandes erreurs en raison de l'élévation au carré.
  
  MSE = (1/n) × Σ(y_i - ŷ_i)²

- **RMSE (Root Mean Squared Error)** : Racine carrée de la MSE, exprimée dans la même unité que la variable d'origine.
  
  RMSE = √MSE

- **RMSLE (Root Mean Squared Logarithmic Error)** : Utile lorsque les erreurs relatives sont plus importantes que les erreurs absolues, particulièrement pour les données à forte asymétrie positive.

### Critères spécifiques aux séries temporelles

- **MASE (Mean Absolute Scaled Error)** : Compare l'erreur du modèle à celle d'une méthode naïve (généralement la prévision par persistance). Particulièrement utile pour les séries temporelles saisonnières.

- **Theil's U** : Mesure la précision relative d'un modèle par rapport à une prévision naïve, avec des valeurs entre 0 et 1 indiquant une performance supérieure à la méthode naïve.

### Considérations pratiques

Le choix du critère d'erreur doit tenir compte de plusieurs facteurs :
- La présence de valeurs extrêmes ou aberrantes (préférer MdAE ou MASE)
- L'importance relative des grandes erreurs (préférer MSE ou RMSE si les grandes erreurs sont particulièrement problématiques)
- La comparabilité entre différentes séries (préférer MAPE ou MASE)
- La présence de valeurs nulles ou proches de zéro (éviter MAPE)

Dans la pratique, il est souvent recommandé d'utiliser plusieurs critères d'erreur complémentaires pour obtenir une évaluation plus complète de la performance des modèles.