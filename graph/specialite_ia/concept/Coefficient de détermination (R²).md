---
title: Coefficient de détermination (R²)
type: concept
tags:
- statistique
- régression
- modélisation
- R²
- analyse de données
- qualité d'ajustement
- variance expliquée
- prédiction
date_creation: '2025-03-22'
date_modification: '2025-03-22'
relatedTo: '[[La régression linéaire multiple]]'
isPartOf: '[[Métriques d''évaluation pour les modèles de régression]]'
relatedTo: '[[La régression linéaire]]'
---

##Généralité

Le coefficient de détermination, communément noté R², est une mesure statistique qui indique la proportion de la variance d'une variable dépendante qui est prévisible à partir des variables indépendantes dans un modèle de régression. Sa valeur est comprise entre 0 et 1, où 0 indique que le modèle n'explique aucune variabilité des données, et 1 indique que le modèle explique parfaitement toute la variabilité des données.

## Points clés

- Le R² mesure la qualité d'ajustement d'un modèle de régression, indiquant quelle proportion de la variance des données est expliquée par le modèle.
- Sa valeur varie de 0 (aucune corrélation) à 1 (corrélation parfaite), et peut être interprétée comme un pourcentage d'explication.
- Le R² augmente mécaniquement avec l'ajout de variables explicatives, ce qui peut conduire à un surajustement (overfitting) si utilisé seul comme critère de sélection de modèle.
- Le R² ajusté corrige ce biais en pénalisant l'ajout de variables peu pertinentes.

## Détails

### Formule et calcul

Le coefficient de détermination se calcule comme suit :

R² = 1 - (SSR / SST)

Où :
- SSR (Sum of Squared Residuals) est la somme des carrés des résidus
- SST (Total Sum of Squares) est la somme totale des carrés

Alternativement, dans le cas d'une régression linéaire simple, R² est égal au carré du coefficient de corrélation de Pearson entre les variables observées et prédites.

### Interprétation

Un R² de 0,75 signifie que 75% de la variabilité de la variable dépendante est expliquée par les variables indépendantes du modèle. Cependant, l'interprétation du R² dépend fortement du domaine d'application :
- En sciences physiques, un R² > 0,9 peut être attendu
- En sciences sociales ou comportementales, un R² de 0,3 peut déjà être considéré comme substantiel
- En économétrie, les valeurs typiques varient généralement entre 0,2 et 0,6

### Limites et précautions

Le R² présente plusieurs limitations importantes :

1. **Ajout de variables** : Le R² augmente mécaniquement (ou reste stable) lorsqu'on ajoute des variables au modèle, même si ces variables n'ont pas de pouvoir explicatif réel.

2. **R² ajusté** : Pour compenser ce biais, on utilise souvent le R² ajusté qui pénalise l'ajout de variables peu pertinentes :
   R² ajusté = 1 - [(1 - R²) × (n - 1) / (n - p - 1)]
   où n est le nombre d'observations et p le nombre de variables explicatives.

3. **Causalité** : Un R² élevé n'implique pas une relation causale entre les variables.

4. **Comparaison entre modèles** : Le R² ne devrait pas être utilisé pour comparer des modèles avec différentes variables dépendantes.

5. **Données non linéaires** : Le R² peut sous-estimer la qualité d'ajustement pour des relations non linéaires.

### Alternatives et compléments

Pour une évaluation plus complète d'un modèle, le R² devrait être utilisé conjointement avec d'autres métriques :
- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)
- AIC (Akaike Information Criterion)
- BIC (Bayesian Information Criterion)
- Tests de validation croisée

Ces métriques offrent des perspectives complémentaires sur la qualité prédictive du modèle et sa généralisation à de nouvelles données.