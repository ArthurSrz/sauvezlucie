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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Métriques d''évaluation pour les modèles de régression]]'
---
## Généralité

Le [coefficient de détermination](https://fr.wikipedia.org/wiki/Coefficient_de_d%C3%A9termination), communément noté R², est une mesure statistique qui indique la proportion de la variance d'une variable dépendante qui est prévisible à partir des variables indépendantes dans un modèle de [régression](https://fr.wikipedia.org/wiki/R%C3%A9gression_statistique). Sa valeur est généralement comprise entre 0 et 1, où 0 indique que le modèle n'explique aucune variabilité des données, et 1 indique que le modèle explique parfaitement toute la variabilité des données. Le R² est largement utilisé dans les analyses de régression linéaire et constitue un indicateur clé de la qualité des prédictions du modèle.

## Points clés

- Le R² mesure la qualité d'ajustement d'un modèle de régression, indiquant quelle proportion de la variance des données est expliquée par le modèle (introduit par [Karl Pearson](https://fr.wikipedia.org/wiki/Karl_Pearson))
- Sa valeur varie généralement de 0 (aucune corrélation) à 1 (corrélation parfaite), avec possibilité de valeurs négatives dans certains cas particuliers
- Le R² augmente mécaniquement avec l'ajout de variables explicatives, pouvant conduire à un [surajustement](https://fr.wikipedia.org/wiki/Surajustement)
- Le R² ajusté corrige ce biais en pénalisant l'ajout de variables peu pertinentes
- Un R² élevé ne garantit pas la validité du modèle et doit être complété par d'autres métriques comme l'[erreur quadratique moyenne](https://fr.wikipedia.org/wiki/Erreur_quadratique_moyenne)

## Détails

### Formule et calcul

Le coefficient de détermination se calcule comme suit :

R² = 1 - (SSR / SST)

Où :
- SSR (Sum of Squared Residuals) est la somme des carrés des résidus
- SST (Total Sum of Squares) est la somme totale des carrés

Dans le cas d'une régression linéaire simple, R² est égal au carré du coefficient de corrélation de Pearson entre les variables observées et prédites.

### Interprétation

Un R² de 0,75 signifie que 75% de la variabilité de la variable dépendante est expliquée par le modèle. L'interprétation varie selon le domaine :

- Sciences physiques : R² > 0,9 souvent attendu
- Sciences sociales : R² de 0,3 peut être substantiel
- [Économétrie](https://fr.wikipedia.org/wiki/%C3%89conom%C3%A9trie) : valeurs typiques entre 0,2 et 0,6

### Limites et précautions

1. **Ajout de variables** : Le R² augmente mécaniquement avec l'ajout de variables
2. **R² ajusté** : Compense ce biais en pénalisant les variables peu pertinentes
3. **Causalité** : Un R² élevé n'implique pas de relation causale
4. **Comparaison entre modèles** : Ne pas utiliser pour comparer des modèles avec différentes variables dépendantes
5. **Données non linéaires** : Peut sous-estimer la qualité d'ajustement pour des relations non linéaires

### Alternatives et compléments

Pour une évaluation plus complète :
- **RMSE** : Mesure l'erreur de prédiction moyenne
- **MAE** : Alternative moins sensible aux valeurs extrêmes
- **[AIC](https://fr.wikipedia.org/wiki/Crit%C3%A8re_d%27information_d%27Akaike)** et **BIC** : Prendent en compte qualité d'ajustement et complexité
- **Tests de validation croisée** : Évaluent la capacité de généralisation