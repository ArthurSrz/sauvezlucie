---
title: La régression linéaire multiple
type: concept
tags:
- statistiques
- régression
- analyse de données
- modélisation
- mathématiques
- prédiction
- variables multiples
date_creation: '2025-03-17'
date_modification: '2025-03-17'

- type: isPartOf
  target: '[[La régression linéaire]]'
---

##Généralité

La régression linéaire multiple est une extension de la régression linéaire simple qui permet de modéliser la relation entre une variable dépendante (ou variable à expliquer) et plusieurs variables indépendantes (ou variables explicatives). Cette technique statistique est largement utilisée dans divers domaines comme l'économie, la finance, les sciences sociales et l'apprentissage automatique pour prédire des valeurs ou comprendre l'influence de différents facteurs sur un phénomène.

## Points clés

- La régression linéaire multiple modélise une relation linéaire entre une variable dépendante et plusieurs variables explicatives
- L'équation générale s'écrit sous la forme Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε, où les β représentent les coefficients et ε l'erreur résiduelle
- Les coefficients sont estimés par la méthode des moindres carrés ordinaires (MCO) qui minimise la somme des carrés des résidus
- L'interprétation des coefficients permet de quantifier l'effet marginal de chaque variable explicative sur la variable dépendante

## Détails

### Formulation mathématique

La régression linéaire multiple s'exprime par l'équation :

Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε

Où :
- Y est la variable dépendante à prédire
- X₁, X₂, ..., Xₙ sont les variables indépendantes (explicatives)
- β₀ est l'ordonnée à l'origine (constante)
- β₁, β₂, ..., βₙ sont les coefficients de régression
- ε représente le terme d'erreur aléatoire

### Hypothèses du modèle

Pour que le modèle de régression linéaire multiple soit valide, plusieurs hypothèses doivent être respectées :
1. Linéarité : la relation entre les variables explicatives et la variable dépendante est linéaire
2. Indépendance : les observations sont indépendantes les unes des autres
3. Homoscédasticité : la variance des erreurs est constante
4. Normalité : les erreurs suivent une distribution normale
5. Absence de multicolinéarité : les variables explicatives ne sont pas fortement corrélées entre elles

### Estimation des coefficients

Les coefficients β sont généralement estimés par la méthode des moindres carrés ordinaires (MCO), qui minimise la somme des carrés des écarts entre les valeurs observées et les valeurs prédites. En notation matricielle, la solution s'écrit :

β̂ = (X'X)⁻¹X'Y

Où X est la matrice des variables explicatives et Y le vecteur de la variable dépendante.

### Évaluation du modèle

Plusieurs indicateurs permettent d'évaluer la qualité d'un modèle de régression linéaire multiple :

- Le coefficient de détermination (R²) : mesure la proportion de la variance de Y expliquée par le modèle
- Le R² ajusté : version du R² qui prend en compte le nombre de variables explicatives
- L'erreur quadratique moyenne (MSE) : moyenne des carrés des résidus
- Les tests de significativité (test F pour le modèle global, test t pour chaque coefficient)

### Applications et limites

La régression linéaire multiple est utilisée pour :
- Prédire des valeurs futures de la variable dépendante
- Identifier les variables qui influencent significativement la variable dépendante
- Quantifier l'effet de chaque variable explicative

Cependant, elle présente certaines limites :
- Elle ne capture que les relations linéaires
- Elle est sensible aux valeurs aberrantes
- Elle peut être inadaptée en présence de multicolinéarité forte
- Elle suppose que les variables explicatives sont indépendantes de l'erreur

Pour surmonter ces limitations, d'autres techniques comme la régression ridge, la régression lasso ou les modèles non linéaires peuvent être envisagées selon le contexte.