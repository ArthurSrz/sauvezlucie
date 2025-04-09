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
date_creation: '2025-03-30'
date_modification: '2025-03-30'
subClassOf: '[[Validation croisée en apprentissage automatique]]'
relatedTo: '[[Optimisation bayésienne pour l''hyperparamétrage]]'
isPartOf: '[[Métriques robustes aux valeurs aberrantes]]'
seeAlso: '[[Méthodes d''évaluation des modèles]]'
---
## Généralité

La [validation croisée](https://fr.wikipedia.org/wiki/Validation_crois%C3%A9e_(statistiques)) et l'[évaluation de modèles](https://fr.wikipedia.org/wiki/%C3%89valuation_d%27un_algorithme_d%27apprentissage_automatique) sont des techniques essentielles en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) permettant d'estimer la performance d'un modèle sur des données non vues. Ces méthodes, formalisées dans les années 1970 par des statisticiens comme [Seymour Geisser](https://fr.wikipedia.org/wiki/Seymour_Geisser), consistent à diviser les données disponibles en sous-ensembles pour entraîner et tester le modèle de manière rigoureuse.

## Points clés

- La [validation croisée](https://fr.wikipedia.org/wiki/Validation_croisée) permet d'évaluer la performance d'un modèle en utilisant différentes partitions des données (entraînement/test)
- Les métriques d'évaluation ([précision](https://fr.wikipedia.org/wiki/Précision_et_rappel), [rappel](https://fr.wikipedia.org/wiki/Précision_et_rappel), [AUC-ROC](https://fr.wikipedia.org/wiki/Courbe_ROC)) doivent être adaptées au problème
- La validation croisée k-fold (k=5 ou 10) est la technique la plus courante selon Wikipédia
- Ces méthodes détectent les problèmes de [sur-apprentissage](https://fr.wikipedia.org/wiki/Surapprentissage) et sous-apprentissage
- La validation croisée stratifiée préserve les proportions des classes dans les partitions

## Détails

### Techniques principales

1. **K-fold cross-validation**  
   Les données sont divisées en k sous-ensembles. Le modèle est entraîné sur k-1 sous-ensembles et testé sur le reste, avec rotation. Performance finale = moyenne des k évaluations. k=10 est un bon compromis (source Wikipédia).

2. **Leave-one-out (LOOCV)**  
   Cas particulier où k = nombre d'observations. Chaque observation sert une fois de test. Méthode précise mais computationnellement intensive (O(N²)).

3. **Stratified k-fold**  
   Préserve la distribution des classes dans chaque fold, essentielle pour les données déséquilibrées.

4. **Time series cross-validation**  
   Méthode spécialisée pour données temporelles, préservant l'ordre chronologique ("walk-forward validation").

5. **Repeated k-fold**  
   Répétition de la procédure k-fold avec différentes initialisations aléatoires pour une estimation plus robuste.

### Métriques d'évaluation

**Classification**:
- Précision: TP/(TP+FP)  
- Rappel: TP/(TP+FN)  
- F1-score: moyenne harmonique précision/rappel  
- AUC-ROC: surface sous la courbe ROC (entre 0.5 et 1)  
- Matrice de confusion  

**Régression**:
- MSE (Mean Squared Error)  
- RMSE (Racine carrée du MSE)  
- MAE (Mean Absolute Error)  
- R² (Coefficient de détermination)  

**Clustering**:
- Silhouette score (-1 à +1)  
- Indice de Davies-Bouldin  
- Indice de Calinski-Harabasz  

### Bonnes pratiques

1. **Séparation des données**: Utiliser la méthode holdout (train/val/test split) avec proportions adaptées.

2. **Hyperparamètres**: Optimiser uniquement sur l'ensemble de test via validation croisée ou ensemble dédié.

3. **Reproductibilité**: Fixer une graine aléatoire (random seed) pour garantir la reproductibilité.

4. **Équilibrage des classes**: Utiliser [SMOTE](https://fr.wikipedia.org/wiki/SMOTE) (Synthetic Minority Oversampling Technique) pour les classes déséquilibrées.

5. **Interprétation**: Analyser les erreurs caractéristiques et examiner l'importance des features.