---
title: Algorithmes d'optimisation bayésienne
type: concept
tags:
- optimisation bayésienne
- processus gaussien
- optimisation globale
- fonction d'acquisition
- modèle probabiliste
- optimisation séquentielle
- boîte noire
- machine learning
- optimisation
date_creation: '2025-03-20'
date_modification: '2025-03-20'
hasPart:
- '[[L''algorithme du gradient]]'
- '[[Choix de la fonction de minimisation]]'
relatedTo: '[[Réseaux bayésiens]]'
---
## Généralité

L'optimisation bayésienne est une approche séquentielle d'optimisation globale pour des fonctions coûteuses à évaluer, inconnues ou de type "boîte noire". Contrairement aux méthodes d'optimisation classiques, elle utilise un modèle probabiliste (généralement un processus gaussien) pour modéliser la fonction objectif inconnue et une fonction d'acquisition pour déterminer les points à évaluer ensuite. Cette méthode est particulièrement efficace lorsque les évaluations de la fonction objectif sont coûteuses en temps ou en ressources.

## Points clés

- L'optimisation bayésienne repose sur deux composants principaux: un modèle probabiliste (souvent un processus gaussien) et une fonction d'acquisition qui guide l'exploration-exploitation.
- Elle est particulièrement adaptée aux problèmes d'optimisation où chaque évaluation est coûteuse, comme l'hyperparamétrage des modèles d'apprentissage automatique.
- Les algorithmes d'optimisation bayésienne équilibrent l'exploration (recherche dans des zones inconnues) et l'exploitation (recherche près des optima connus).
- Ils construisent progressivement un modèle de substitution (surrogate model) de la fonction objectif qui s'améliore à chaque itération.

## Détails

### Fonctionnement général

L'optimisation bayésienne fonctionne de manière itérative:
1. Construction d'un modèle probabiliste de la fonction objectif à partir des observations disponibles
2. Utilisation d'une fonction d'acquisition pour déterminer le prochain point à évaluer
3. Évaluation de la fonction objectif en ce point
4. Mise à jour du modèle probabiliste avec cette nouvelle observation
5. Répétition jusqu'à atteindre un critère d'arrêt

### Modèles probabilistes

Le processus gaussien (GP) est le modèle le plus couramment utilisé en optimisation bayésienne. Il définit une distribution de probabilité sur les fonctions, permettant de quantifier l'incertitude sur la fonction objectif. D'autres modèles comme les forêts aléatoires ou les réseaux de neurones bayésiens peuvent également être utilisés.

### Fonctions d'acquisition

Les fonctions d'acquisition déterminent le compromis entre exploration et exploitation:

- **Expected Improvement (EI)**: Sélectionne les points qui offrent la plus grande amélioration attendue par rapport au meilleur point connu.
- **Upper Confidence Bound (UCB)**: Sélectionne les points avec la plus grande borne supérieure de confiance.
- **Probability of Improvement (PI)**: Sélectionne les points avec la plus grande probabilité d'amélioration.
- **Entropy Search**: Sélectionne les points qui réduisent le plus l'entropie sur la localisation du maximum global.

### Applications principales

- Hyperparamétrage automatique des modèles d'apprentissage automatique
- Optimisation de conception en ingénierie
- Optimisation de processus industriels
- Conception expérimentale en sciences
- Optimisation de simulations numériques coûteuses

### Variantes et extensions

- **Multi-objective Bayesian Optimization**: Pour optimiser plusieurs objectifs contradictoires simultanément
- **Batch Bayesian Optimization**: Pour proposer plusieurs points d'évaluation en parallèle
- **High-dimensional Bayesian Optimization**: Techniques spécifiques pour traiter les espaces de grande dimension
- **Constrained Bayesian Optimization**: Pour gérer les contraintes dans l'espace de recherche

L'optimisation bayésienne continue d'être un domaine de recherche actif, avec des développements constants pour améliorer son efficacité et son applicabilité à des problèmes plus complexes.