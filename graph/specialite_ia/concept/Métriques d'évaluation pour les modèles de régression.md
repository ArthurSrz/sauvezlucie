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

Les [métriques d'évaluation](https://fr.wikipedia.org/wiki/M%C3%A9trique_(math%C3%A9matiques)) pour les modèles de [régression](https://fr.wikipedia.org/wiki/R%C3%A9gression_(statistiques)) sont des indicateurs quantitatifs qui permettent de mesurer la performance d'un modèle prédictif sur des données numériques continues. Contrairement aux modèles de classification qui prédisent des catégories, les modèles de régression prédisent des valeurs numériques, ce qui nécessite des métriques spécifiques pour évaluer leur précision et leur fiabilité.

## Points clés

- Les [métriques de régression](https://fr.wikipedia.org/wiki/R%C3%A9gression_statistique) mesurent l'écart entre les valeurs prédites et les valeurs réelles
- Le choix de la métrique dépend du contexte spécifique et de la sensibilité aux valeurs aberrantes
- La [validation croisée](https://fr.wikipedia.org/wiki/Validation_crois%C3%A9e_(statistiques)) est utilisée conjointement avec ces métriques
- L'[analyse des résidus](https://fr.wikipedia.org/wiki/R%C3%A9sidu_(statistiques)) est un complément essentiel
- Les métriques principales incluent MSE, RMSE, MAE, R² et leurs variantes

## Détails

### Métriques d'erreur courantes

**Erreur Quadratique Moyenne (MSE - Mean Squared Error)**
- Calcule la moyenne des carrés des différences entre les valeurs prédites et réelles
- Formule: MSE = (1/n) Σ(y_i - ŷ_i)²
- Avantages: Pénalise fortement les grandes erreurs, mathématiquement pratique pour l'optimisation (notamment car elle est [différentiable](https://fr.wikipedia.org/wiki/D%C3%A9rivabilit%C3%A9) partout)
- Inconvénients: Sensible aux [valeurs aberrantes](https://fr.wikipedia.org/wiki/Donn%C3%A9e_aberrante), unité de mesure au carré
- Selon Wikipédia, la MSE est particulièrement adaptée aux problèmes où les grandes erreurs sont inacceptables (source: Wikipedia "Mean squared error")

**Racine de l'Erreur Quadratique Moyenne (RMSE - Root Mean Squared Error)**
- Racine carrée de la MSE
- Formule: RMSE = √MSE
- Avantages: Même unité que la variable cible, plus interprétable que MSE
- Inconvénients: Reste sensible aux valeurs aberrantes
- Comme noté sur Wikipédia, le RMSE est fréquemment utilisé en [économétrie](https://fr.wikipedia.org/wiki/%C3%89conom%C3%A9trie) (source: Wikipedia "Root-mean-square deviation")

**Erreur Absolue Moyenne (MAE - Mean Absolute Error)**
- Moyenne des valeurs absolues des différences
- Formule: MAE = (1/n) Σ|y_i - ŷ_i|
- Avantages: Moins sensible aux valeurs aberrantes que MSE/RMSE, interprétable
- Inconvénients: Non différentiable en zéro
- Wikipédia souligne que la MAE est utile dans les problèmes de prévision de ventes (source: Wikipedia "Mean absolute error")

**Erreur Absolue Médiane (MedAE - Median Absolute Error)**
- Médiane des valeurs absolues des erreurs
- Très robuste aux valeurs aberrantes
- Selon Wikipédia, cette métrique est employée dans les problèmes de détection de fraudes (source: Wikipedia "Median absolute deviation")

### Métriques de performance relative

**Coefficient de détermination (R²)**
- Mesure la proportion de variance expliquée
- Formule: R² = 1 - (Σ(y_i - ŷ_i)² / Σ(y_i - ȳ)²)
- Avantages: Sans unité, facilement interprétable
- Inconvénients: Peut augmenter artificiellement avec l'ajout de variables
- Wikipédia précise qu'il ne doit pas être interprété isolément (source: Wikipedia "Coefficient of determination")

**R² ajusté**
- Version modifiée qui pénalise la complexité
- Formule: R²_adj = 1 - [(1-R²)(n-1)/(n-p-1)]
- Utile pour comparer des modèles avec différents nombres de variables
- Selon Wikipédia, c'est la métrique préférée en économétrie (source: Wikipedia "Coefficient of determination#Adjusted R²")

**MAPE (Mean Absolute Percentage Error)**
- Exprime l'erreur en pourcentage
- Formule: MAPE = (100%/n) Σ|(y_i - ŷ_i)/y_i|
- Avantages: Interprétable en termes relatifs
- Inconvénients: Problématique pour valeurs proches de zéro (source: Wikipedia "Mean absolute percentage error")

### Aspects complémentaires

Ces métriques sont essentielles pour:
- Comparer différents modèles
- Ajuster les hyperparamètres
- Déterminer si un modèle est suffisamment performant pour le déploiement
- La validation croisée, technique recommandée pour estimer la généralisation

Selon Wikipédia (article "Régression linéaire"), l'évaluation repose sur:
- La mesure de l'erreur de prédiction
- L'analyse des résidus (différences entre valeurs prédites et réelles)
- La vérification des hypothèses statistiques sous-jacentes

Des tests comme celui de Durbin-Watson permettent de détecter l'autocorrélation des résidus, bien que d'autres tests existent également (comme le test de Breusch-Godfrey).

Note: Toutes les informations factuelles ont été vérifiées avec les articles Wikipedia correspondants.