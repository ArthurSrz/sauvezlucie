---
title: La régression linéaire
type: concept
tags:
- statistiques
- régression linéaire
- modélisation
- analyse de données
- mathématiques
- prédiction
- apprentissage automatique
date_creation: '2025-03-17'
date_modification: '2025-03-17'
---

## Généralité

La régression linéaire est un modèle statistique qui établit une relation linéaire entre une variable expliquée et une ou plusieurs variables explicatives. C'est l'un des outils fondamentaux de l'analyse statistique, utilisé tant pour la prédiction que pour l'explication de phénomènes.

## Points clés

- La régression linéaire cherche à modéliser la relation entre variables par une fonction affine (y = β₀ + β₁x₁ + ... + βₖxₖ + ε)
- L'estimation des paramètres se fait généralement par la méthode des moindres carrés ordinaires (MCO)
- Le modèle repose sur plusieurs hypothèses importantes: non-colinéarité des variables explicatives, indépendance des erreurs, homoscédasticité et exogénéité
- La qualité du modèle peut être évaluée par le coefficient de détermination (R²) et divers tests statistiques

## Détails

### Formes du modèle
- **Régression linéaire simple**: utilise une seule variable explicative (y = β₀ + β₁x + ε)
- **Régression linéaire multiple**: utilise plusieurs variables explicatives

### Estimation
L'estimateur des moindres carrés ordinaires minimise la somme des carrés des résidus:
- Sous forme matricielle: β̂ = (X'X)⁻¹X'y
- Selon le théorème de Gauss-Markov, c'est le meilleur estimateur linéaire sans biais

### Évaluation du modèle
- **Coefficient de détermination (R²)**: mesure la proportion de variance expliquée par le modèle
- **Test de Fisher**: évalue la significativité globale du modèle
- **Test de Student**: teste la significativité de chaque coefficient

### Extensions et variantes
- Régression avec variables instrumentales (pour traiter l'endogénéité)
- Modèles linéaires hiérarchiques (pour données multiniveaux)
- Régression quantile (pour modéliser différents quantiles de la distribution)
- Méthodes robustes (pour traiter les points aberrants)

### Applications
La régression linéaire est largement utilisée dans de nombreux domaines:
- Économie et économétrie (ex: rendements de l'éducation)
- Sciences politiques (ex: analyse électorale)
- Sociologie et psychologie (ex: études comportementales)
- Métrologie et sciences de l'ingénieur
- Géographie et sciences environnementales