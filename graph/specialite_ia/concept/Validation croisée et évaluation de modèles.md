---
title: Validation croisée et évaluation de modèles
type: concept
tags:
- machine learning
- validation croisée
- évaluation de modèles
- sur-apprentissage
- généralisation
- data science
- statistiques
- modélisation
- apprentissage automatique
date_creation: '2025-03-22'
date_modification: '2025-03-22'
subClassOf: '[[Validation croisée en apprentissage automatique]]'
relatedTo: '[[Optimisation bayésienne pour l''hyperparamétrage]]'
isPartOf: '[[Métriques robustes aux valeurs aberrantes]]'
---
## Généralité

La validation croisée et l'évaluation de modèles sont des techniques essentielles en apprentissage automatique permettant d'estimer la performance d'un modèle sur des données non vues et de détecter les problèmes de sur-apprentissage ou sous-apprentissage. Ces méthodes consistent à diviser les données disponibles en sous-ensembles pour entraîner et tester le modèle de manière rigoureuse, garantissant ainsi une évaluation plus fiable de sa capacité de généralisation.

## Points clés

- La validation croisée permet d'évaluer la performance d'un modèle en utilisant différentes partitions des données d'entraînement et de test
- Les métriques d'évaluation (précision, rappel, F1-score, AUC-ROC, etc.) doivent être choisies en fonction du problème spécifique à résoudre
- La validation croisée k-fold est la technique la plus courante, divisant les données en k sous-ensembles de taille égale
- L'évaluation de modèles aide à détecter et corriger les problèmes de sur-apprentissage (overfitting) et sous-apprentissage (underfitting)

## Détails

### Types de validation croisée

1. **K-fold cross-validation** : Les données sont divisées en k sous-ensembles (folds) de taille égale. Le modèle est entraîné sur k-1 sous-ensembles et testé sur le sous-ensemble restant. Ce processus est répété k fois, chaque sous-ensemble servant une fois de test. La performance finale est la moyenne des k évaluations.

2. **[Leave-one-out cross-validation](https://fr.wikipedia.org/wiki/Leave-one-out_cross-validation) (LOOCV)** : Cas particulier où k est égal au nombre d'observations. Chaque observation sert une fois de test, tandis que toutes les autres sont utilisées pour l'entraînement. Cette méthode est coûteuse en calcul mais utile pour les petits jeux de données.

3. **Stratified k-fold** : Variante du k-fold qui préserve la proportion des classes dans chaque fold, particulièrement importante pour les problèmes de classification avec des classes déséquilibrées.

4. **Time series cross-validation** : Pour les données temporelles, où les observations futures ne peuvent pas être utilisées pour prédire les observations passées.

### Métriques d'évaluation courantes

- **Classification** : Précision, rappel, F1-score, AUC-ROC, matrice de confusion
- **Régression** : MSE (Mean Squared Error), RMSE (Root Mean Squared Error), MAE (Mean Absolute Error), R²
- **Clustering** : Silhouette score, indice de Davies-Bouldin, indice de Calinski-Harabasz

### Bonnes pratiques

1. **Séparation des données** : Diviser les données en ensembles d'entraînement, de validation et de test avant toute analyse pour éviter les fuites de données.

2. **Hyperparamètres** : Utiliser la validation croisée pour optimiser les hyperparamètres du modèle, mais jamais sur l'ensemble de test final.

3. **[Reproductibilité](https://fr.wikipedia.org/wiki/Reproductibilité)** : Fixer une graine aléatoire (random seed) pour assurer la reproductibilité des résultats.

4. **Équilibrage des classes** : Pour les problèmes de classification déséquilibrée, utiliser des techniques comme la stratification ou le rééchantillonnage.

5. **Interprétation des résultats** : Ne pas se fier uniquement aux métriques numériques, mais aussi analyser les erreurs du modèle pour comprendre ses limites.

La validation croisée et l'évaluation rigoureuse des modèles sont des étapes cruciales pour développer des modèles d'apprentissage automatique robustes et fiables, capables de généraliser correctement sur de nouvelles données.