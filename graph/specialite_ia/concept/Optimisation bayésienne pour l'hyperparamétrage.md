---
title: Optimisation bayésienne pour l'hyperparamétrage
type: concept
tags:
- machine learning
- optimisation bayésienne
- hyperparamètres
- apprentissage automatique
- optimisation
- probabilité
- modélisation
- data science
- algorithmes
date_creation: '2025-03-18'
date_modification: '2025-03-18'
---
## Généralité

L'optimisation bayésienne est une approche probabiliste pour trouver les valeurs optimales des hyperparamètres dans les algorithmes d'apprentissage automatique. Contrairement aux méthodes traditionnelles comme la recherche par grille ou aléatoire, l'optimisation bayésienne construit un modèle probabiliste de la fonction objectif (généralement la performance du modèle) et l'utilise pour sélectionner intelligemment les prochains hyperparamètres à évaluer, réduisant ainsi considérablement le temps et les ressources nécessaires pour trouver une configuration optimale.

## Points clés

- L'optimisation bayésienne utilise un processus gaussien (ou d'autres modèles probabilistes) pour modéliser la relation entre les hyperparamètres et la performance du modèle
- Elle emploie une fonction d'acquisition pour équilibrer l'exploration (tester de nouvelles zones) et l'exploitation (affiner les zones prometteuses)
- Cette méthode est particulièrement efficace pour l'optimisation de fonctions coûteuses à évaluer, comme l'entraînement de réseaux de neurones profonds
- Elle converge généralement vers l'optimum global avec moins d'évaluations que les méthodes de recherche par grille ou aléatoire

## Détails

L'optimisation bayésienne fonctionne en deux étapes principales qui s'alternent de manière itérative:

1. **Construction du modèle probabiliste** : Un processus gaussien (GP) est généralement utilisé pour modéliser la distribution de probabilité sur toutes les fonctions possibles qui pourraient correspondre aux observations actuelles. Ce modèle capture l'incertitude sur la fonction objectif.

2. **Optimisation de la fonction d'acquisition** : Cette fonction détermine quels hyperparamètres tester ensuite en équilibrant:
   - L'exploitation des régions où le modèle prédit une bonne performance
   - L'exploration des régions où l'incertitude est élevée

Les fonctions d'acquisition couramment utilisées incluent:
- **Expected Improvement (EI)** : Maximise l'amélioration attendue par rapport à la meilleure observation actuelle
- **Upper Confidence Bound (UCB)** : Équilibre directement l'exploration et l'exploitation via un paramètre ajustable
- **Probability of Improvement (PI)** : Maximise la probabilité d'améliorer la meilleure observation actuelle

L'optimisation bayésienne est particulièrement avantageuse dans les scénarios suivants:
- Lorsque l'évaluation de la fonction objectif est coûteuse (en temps ou en ressources)
- Quand l'espace des hyperparamètres est complexe et difficile à explorer exhaustivement
- Pour les modèles avec de nombreux hyperparamètres interdépendants

Des bibliothèques comme Hyperopt, Optuna, et scikit-optimize implémentent l'optimisation bayésienne et facilitent son intégration dans les workflows d'apprentissage automatique. Ces outils offrent également des visualisations qui aident à comprendre l'espace des hyperparamètres et l'évolution de l'optimisation.

## Limitations

- La complexité computationnelle augmente avec le nombre d'évaluations (O(n³) pour les processus gaussiens standards)
- L'efficacité diminue généralement dans les espaces de très haute dimension (>20 hyperparamètres)
- Le choix du prior et de la fonction d'acquisition peut influencer significativement les résultats
- Les contraintes entre hyperparamètres peuvent être difficiles à modéliser