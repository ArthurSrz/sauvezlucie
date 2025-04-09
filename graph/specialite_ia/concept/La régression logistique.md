---
title: La régression logistique
type: concept
tags:
- régression logistique
- statistiques
- modélisation
- analyse prédictive
- machine learning
- classification
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Apprentissage supervisé]]'
subClassOf: '[[Algorithme de classification]]'
---
## Généralité

La [régression logistique](https://fr.wikipedia.org/wiki/R%C3%A9gression_logistique) est une méthode statistique d'apprentissage supervisé utilisée principalement pour la classification binaire, bien qu'elle puisse être étendue à des problèmes multi-classes. Contrairement à son nom, il s'agit d'un algorithme de classification et non de régression. Développée initialement par [David Cox](https://fr.wikipedia.org/wiki/David_Cox_(statisticien)) et d'autres statisticiens, cette technique modélise la probabilité qu'une observation appartienne à une catégorie particulière en utilisant une [fonction logistique](https://fr.wikipedia.org/wiki/Fonction_logistique) (sigmoïde) pour transformer une combinaison linéaire de variables prédictives en une probabilité comprise entre 0 et 1.

## Points clés

- Prédit la probabilité d'appartenance à une classe via la [fonction sigmoïde](https://fr.wikipedia.org/wiki/Sigmo%C3%AFde) σ(z) = 1/(1+e^-z)
- Offre une interprétabilité des coefficients en termes de rapport de cotes (odds ratio)
- Peut être étendue à la classification multi-classes via des approches one-vs-rest ou [softmax](https://fr.wikipedia.org/wiki/Fonction_softmax)
- Fait partie des [modèles linéaires généralisés](https://fr.wikipedia.org/wiki/Mod%C3%A8le_lin%C3%A9aire_g%C3%A9n%C3%A9ralis%C3%A9)
- Utilise la méthode du [maximum de vraisemblance](https://fr.wikipedia.org/wiki/Maximum_de_vraisemblance) pour l'estimation des paramètres

## Détails

La régression logistique modélise la probabilité qu'une observation appartienne à la classe positive (y=1) comme suit:

P(y=1|x) = 1 / (1 + e^(-z))

où z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ est une combinaison linéaire des variables prédictives x₁, x₂, ..., xₙ et des coefficients β.

La fonction sigmoïde présente plusieurs propriétés mathématiques intéressantes :
- Sa dérivée est simple : σ'(z) = σ(z)(1-σ(z))
- Elle est symétrique autour de z=0 : σ(-z) = 1-σ(z)

Les coefficients β sont estimés par la méthode du maximum de vraisemblance, utilisant des méthodes d'optimisation itératives comme :
- Descente de gradient
- Algorithme Newton-Raphson

Le coefficient βᵢ représente :
- Changement dans le logarithme du rapport de cotes lorsque xᵢ augmente d'une unité
- L'exponentielle de βᵢ donne le rapport de cotes (ex: 2 signifie que la cote double)

Métriques d'évaluation principales :
- Précision (accuracy)
- Matrice de confusion
- Courbe ROC et aire sous la courbe (AUC)
- Log-vraisemblance
- Test du rapport de vraisemblance
- Statistiques d'information (AIC, BIC)

Techniques de régularisation pour éviter le surapprentissage :
- L1 (Lasso) : sélection automatique des variables
- L2 (Ridge) : réduction d'amplitude des coefficients
- Elastic Net : combinaison de L1 et L2

Extensions possibles :
- Classification multi-classes (fonction softmax)
- Problèmes ordinaux (modèles proportionnels de cotes)
- Données séquentielles (modèles logistiques conditionnels)
- Modèles mixtes pour données groupées
- Régression logistique pénalisée pour haute dimension

Malgré sa simplicité relative, la régression logistique reste un outil fondamental en statistique et en apprentissage automatique, offrant un bon équilibre entre performance, interprétabilité et efficacité computationnelle.