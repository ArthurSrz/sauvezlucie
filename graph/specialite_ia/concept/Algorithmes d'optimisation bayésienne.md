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

L'[optimisation bayésienne](https://fr.wikipedia.org/wiki/Optimisation_bay%C3%A9sienne) est une approche séquentielle d'optimisation globale pour des fonctions coûteuses à évaluer, inconnues ou de type "boîte noire". Elle utilise un [modèle probabiliste](https://fr.wikipedia.org/wiki/Mod%C3%A8le_probabiliste) (généralement un [processus gaussien](https://fr.wikipedia.org/wiki/Processus_gaussien)) pour modéliser la fonction objectif et une fonction d'acquisition pour guider la recherche. Ses fondements remontent aux travaux de Kushner (1964) et Mockus (1975).

## Points clés

- Particulièrement efficace pour les fonctions coûteuses à évaluer (comme l'hyperparamétrage en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique))
- Utilise deux composants principaux : modèle probabiliste (souvent processus gaussien) et fonction d'acquisition
- Équilibre exploration (zones inconnues) et exploitation (zones prometteuses)
- Applications variées : optimisation de conception, processus industriels, simulations numériques
- Plus efficace que les méthodes classiques pour les problèmes non convexes ou bruyants

## Détails

L'optimisation bayésienne fonctionne itérativement selon ce processus :
1. Construction d'un modèle probabiliste à partir des observations disponibles
2. Utilisation d'une fonction d'acquisition pour déterminer le prochain point à évaluer
3. Évaluation coûteuse de la fonction objectif en ce point
4. Mise à jour du modèle probabiliste avec cette nouvelle observation
5. Répétition jusqu'à atteindre un critère d'arrêt

Les modèles probabilistes couramment utilisés incluent :
- **Processus gaussien (GP)** : Modèle le plus courant, définit une distribution de probabilité sur les fonctions
- **Forêts aléatoires** : Préférées pour les espaces de haute dimension
- **Réseaux de neurones bayésiens** : Pour capturer des relations non linéaires complexes
- **Processus de Dirichlet** : Modèles non paramétriques plus flexibles

Les principales fonctions d'acquisition sont :
- **Expected Improvement (EI)** : Amélioration attendue par rapport au meilleur point connu
- **Upper Confidence Bound (UCB)** : Borne supérieure de confiance
- **Probability of Improvement (PI)** : Probabilité d'amélioration
- **Entropy Search** : Réduction de l'entropie sur la localisation du maximum global

Parmi les applications majeures, on trouve :
- Hyperparamétrage automatique des modèles d'apprentissage automatique
- [Optimisation de conception](https://fr.wikipedia.org/wiki/Optimisation_de_la_conception) en ingénierie
- Optimisation des paramètres de production industrielle
- Conception expérimentale en chimie et biologie
- Simulations numériques complexes

Les variantes importantes incluent :
- **Multi-objective Bayesian Optimization (MOBO)** : Optimisation multi-objective
- **Batch Bayesian Optimization** : Évaluation de plusieurs points en parallèle
- **High-dimensional Bayesian Optimization** : Pour espaces de grande dimension
- **Constrained Bayesian Optimization** : Gestion des contraintes
- **Bayesian Optimization with Context** : Intégration de variables contextuelles