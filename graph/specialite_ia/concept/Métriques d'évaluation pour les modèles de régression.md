---
title: Métriques d'évaluation pour les modèles de régression
type: concept
tags:
- data science
- régression
- évaluation de modèle
- métriques
- machine learning
- statistiques
- performance
- modélisation prédictive
- analyse quantitative
date_creation: '2025-03-22'
date_modification: '2025-03-22'
subClassOf: '[[Choix de la mesure d''erreur]]'
relatedTo: '[[La régression linéaire]]'
hasPart: '[[Coefficient de détermination (R²)]]'
---
## Généralité

Les métriques d'évaluation pour les modèles de régression sont des indicateurs quantitatifs qui permettent de mesurer la performance d'un modèle prédictif sur des données numériques continues. Contrairement aux modèles de classification qui prédisent des catégories, les modèles de régression prédisent des valeurs numériques, ce qui nécessite des métriques spécifiques pour évaluer leur précision et leur fiabilité. Ces métriques sont essentielles pour comparer différents modèles, ajuster les hyperparamètres et déterminer si un modèle est suffisamment performant pour être déployé en production.

## Points clés

- Les métriques de régression mesurent l'écart entre les valeurs prédites et les valeurs réelles
- Le choix de la métrique dépend du contexte spécifique du problème et de la sensibilité aux valeurs aberrantes
- La validation croisée est souvent utilisée conjointement avec ces métriques pour évaluer la généralisation du modèle
- Certaines métriques sont plus interprétables que d'autres dans le contexte métier

## Détails

### Métriques d'erreur courantes

1. **Erreur Quadratique Moyenne (MSE - Mean Squared Error)**
   - Calcule la moyenne des carrés des différences entre les valeurs prédites et réelles
   - Formule: MSE = (1/n) Σ(y_i - ŷ_i)²
   - Avantages: Pénalise fortement les grandes erreurs, mathématiquement pratique pour l'optimisation
   - Inconvénients: Sensible aux valeurs aberrantes, unité de mesure au carré (moins interprétable)

2. **Racine de l'Erreur Quadratique Moyenne (RMSE - Root Mean Squared Error)**
   - Racine carrée de la MSE
   - Formule: RMSE = √MSE
   - Avantages: Même unité que la variable cible, plus interprétable que MSE
   - Inconvénients: Reste sensible aux valeurs aberrantes

3. **Erreur Absolue Moyenne (MAE - Mean Absolute Error)**
   - Moyenne des valeurs absolues des différences entre prédictions et valeurs réelles
   - Formule: MAE = (1/n) Σ|y_i - ŷ_i|
   - Avantages: Moins sensible aux valeurs aberrantes que MSE/RMSE, interprétable
   - Inconvénients: Gradient non constant, moins adapté à certains algorithmes d'optimisation

4. **Erreur Absolue Médiane (MedAE - Median Absolute Error)**
   - Médiane des valeurs absolues des erreurs
   - Très robuste aux valeurs aberrantes
   - Utile quand les données contiennent des valeurs extrêmes

### Métriques de performance relative

1. **Coefficient de détermination (R²)**
   - Mesure la proportion de variance expliquée par le modèle
   - Formule: R² = 1 - (Σ(y_i - ŷ_i)² / Σ(y_i - ȳ)²)
   - Varie généralement entre 0 et 1 (1 étant parfait)
   - Peut être négatif si le modèle est pire que la prédiction par la moyenne
   - Avantages: Sans unité, facilement interprétable
   - Inconvénients: Peut augmenter artificiellement avec l'ajout de variables

2. **R² ajusté**
   - Version modifiée du R² qui pénalise la complexité du modèle
   - Utile pour comparer des modèles avec différents nombres de variables

3. **MAPE (Mean Absolute Percentage Error)**
   - Exprime l'erreur en pourcentage de la valeur réelle
   - Formule: MAPE = (100%/n) Σ|(y_i - ŷ_i)/y_i|
   - Avantages: Interprétable en termes relatifs
   - Inconvénients: Problématique quand les valeurs réelles sont proches de zéro

Le choix de la métrique appropriée doit être guidé par la nature du problème. Par exemple, si les grandes erreurs sont particulièrement coûteuses, MSE ou RMSE peuvent être préférables. Si l'interprétabilité est cruciale ou si les données contiennent des valeurs aberrantes, MAE ou MedAE peuvent être plus adaptées. Dans un contexte de communication avec des parties prenantes non techniques, R² est souvent privilégié pour sa facilité d'interprétation.