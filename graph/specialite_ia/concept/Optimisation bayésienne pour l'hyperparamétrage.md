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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
---
## Généralité

L'[optimisation bayésienne](https://fr.wikipedia.org/wiki/Optimisation_bay%C3%A9sienne) est une méthode d'optimisation séquentielle pour les fonctions coûteuses à évaluer, particulièrement efficace pour le réglage des hyperparamètres en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique). Elle combine un modèle probabiliste (typiquement un processus gaussien) avec une fonction d'acquisition pour guider intelligemment la recherche des meilleurs hyperparamètres.

Cette approche s'appuie sur le [théorème de Bayes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bayes) pour mettre à jour les croyances a priori sur la fonction objectif à mesure que de nouvelles observations sont collectées. Historiquement, les bases théoriques remontent aux travaux de Kushner (1964) et Mockus (1975).

## Points clés

- Méthode efficace pour optimiser des fonctions coûteuses avec peu d'évaluations (typiquement moins de 20-100 itérations selon les applications)
- Combine modélisation probabiliste (souvent avec [processus gaussien](https://fr.wikipedia.org/wiki/Processus_gaussien)) et stratégie d'exploration/exploitation via une fonction d'acquisition
- Particulièrement adaptée au [réglage des hyperparamètres](https://fr.wikipedia.org/wiki/Hyperparam%C3%A8tre) en ML, où chaque évaluation peut prendre des heures ou jours de calcul
- Surpasse souvent les méthodes comme la recherche aléatoire ou grid search, notamment dans les espaces de grande dimension
- Utilise un compromis intelligent entre exploration et exploitation via des fonctions comme Expected Improvement (EI), Upper Confidence Bound (UCB) ou Probabilité d'amélioration (PI)

## Détails

L'optimisation bayésienne repose sur deux composants principaux : un **modèle substitut** (généralement un [processus gaussien](https://fr.wikipedia.org/wiki/Processus_gaussien) qui modélise la distribution a posteriori de la fonction objectif) et une **fonction d'acquisition** qui détermine les points suivants à évaluer en équilibrant exploration et exploitation.

Cette méthode présente plusieurs avantages par rapport aux autres approches :
- **Efficacité** : Nécessite généralement moins d'évaluations que grid search ou random search
- **Capacité à gérer le bruit** : Peut fonctionner avec des fonctions objectif bruitées grâce à sa modélisation probabiliste
- **Mémoire des évaluations passées** : Utilise l'historique pour guider les recherches futures via le [théorème de Bayes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bayes)
- **Adaptabilité** : S'ajuste dynamiquement en fonction des résultats obtenus

Le processus typique comprend :
1. Initialisation avec quelques points aléatoires (entre 5-20 selon la dimension du problème)
2. Construction du modèle probabiliste
3. Sélection du prochain point via la fonction d'acquisition
4. Évaluation de la fonction objectif sur ce point
5. Mise à jour du modèle avec les nouvelles observations
6. Répétition jusqu'à convergence ou épuisement du budget

Les principales applications en machine learning incluent :
- Réglage des hyperparamètres des modèles complexes (réseaux neuronaux, SVM)
- Optimisation des architectures de réseaux neuronaux (NAS)
- Sélection de features pour les datasets à haute dimension
- Optimisation des pipelines de traitement

Parmi les fonctions d'acquisition courantes, on trouve :
- Expected Improvement (EI) : La plus populaire selon la littérature
- Probability of Improvement (PI) : Plus simple mais tend à trop exploiter
- Upper Confidence Bound (UCB) : Utile pour les problèmes à bruit gaussien
- Entropy Search : Minimise l'entropie de la distribution de l'optimum

Cependant, cette approche présente certaines limitations :
- Difficulté à scaler en haute dimension (>10-20 paramètres) - phénomène connu sous le nom de "[fléau de la dimension](https://fr.wikipedia.org/wiki/Fl%C3%A9au_de_la_dimension)"
- Coût de calcul du modèle substitut qui augmente cubiquement avec le nombre d'observations
- Sensibilité aux hyperparamètres du modèle substitut lui-même
- Performance dépendante de la qualité de la fonction d'acquisition choisie