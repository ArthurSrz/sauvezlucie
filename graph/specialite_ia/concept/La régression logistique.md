---
title: La régression logistique
type: '[[Algorithme de classification]]'
tags:
- régression logistique
- statistiques
- modélisation
- analyse prédictive
- machine learning
- classification
date_creation: '2025-03-17'
date_modification: '2025-03-17'
isPartOf: '[[Apprentissage supervisé]]'
---
##Généralité

La régression logistique est une méthode statistique d'apprentissage supervisé utilisée pour la classification binaire. Contrairement à son nom, il s'agit d'un algorithme de classification et non de régression. Elle modélise la probabilité qu'une observation appartienne à une catégorie particulière en utilisant une fonction logistique (sigmoïde) pour transformer une combinaison linéaire de variables prédictives en une probabilité comprise entre 0 et 1.

## Points clés

- La régression logistique prédit la probabilité d'appartenance à une classe plutôt qu'une valeur numérique continue
- Elle utilise la fonction sigmoïde pour transformer une entrée linéaire en une probabilité entre 0 et 1
- Bien qu'elle soit simple, elle reste très efficace pour de nombreux problèmes de classification binaire
- Elle offre une bonne interprétabilité des coefficients en termes de rapport de cotes (odds ratio)
- Elle peut être étendue à la classification multi-classes via des approches one-vs-rest ou softmax

## Détails

### Fondement mathématique

La régression logistique modélise la probabilité qu'une observation appartienne à la classe positive (y=1) comme suit:

P(y=1|x) = 1 / (1 + e^(-z))

où z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ est une combinaison linéaire des variables prédictives x₁, x₂, ..., xₙ et des coefficients β.

La fonction 1/(1+e^(-z)) est appelée fonction sigmoïde ou logistique, qui transforme n'importe quelle valeur réelle en une valeur entre 0 et 1, interprétable comme une probabilité.

### Estimation des paramètres

Les coefficients β sont généralement estimés par la méthode du maximum de vraisemblance. Contrairement à la régression linéaire, il n'existe pas de solution analytique, et des méthodes d'optimisation itératives comme la descente de gradient sont utilisées.

### Interprétation des coefficients

Un avantage majeur de la régression logistique est l'interprétabilité de ses coefficients. Le coefficient βᵢ représente le changement dans le logarithme du rapport de cotes (log-odds) lorsque la variable xᵢ augmente d'une unité, toutes les autres variables restant constantes. L'exponentielle de βᵢ donne directement le rapport de cotes.

### [Évaluation](https://fr.wikipedia.org/wiki/Évaluation) du modèle

La performance d'un modèle de régression logistique peut être évaluée par diverses métriques:
- Précision (accuracy): proportion de prédictions correctes
- Matrice de confusion: tableau des vrais/faux positifs/négatifs
- Courbe ROC et aire sous la courbe (AUC): évaluation de la capacité discriminative
- Log-vraisemblance: mesure de l'ajustement du modèle

### Régularisation

Pour éviter le surapprentissage, particulièrement avec de nombreuses variables ou des données limitées, on peut appliquer une régularisation:
- L1 (Lasso): favorise la parcimonie en réduisant certains coefficients à zéro
- L2 (Ridge): réduit l'amplitude de tous les coefficients

### Extensions

La régression logistique peut être étendue à:
- [Classification](https://fr.wikipedia.org/wiki/Classification) multi-classes via la régression logistique multinomiale
- Problèmes ordinaux via la régression logistique ordinale
- Données séquentielles via des modèles logistiques conditionnels

Malgré sa simplicité relative par rapport aux méthodes d'apprentissage profond, la régression logistique reste un outil fondamental en statistique et en apprentissage automatique, offrant un bon équilibre entre performance, interprétabilité et efficacité computationnelle.