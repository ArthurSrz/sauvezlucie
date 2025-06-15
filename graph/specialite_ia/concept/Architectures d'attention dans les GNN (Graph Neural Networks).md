---
title: Architectures d'attention dans les GNN (Graph Neural Networks)
type: concept
tags:
- GNN
- réseaux de neurones
- graphes
- mécanismes d'attention
- apprentissage profond
- agrégation de caractéristiques
- traitement de graphes
- IA
- deep learning
- neural networks
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

Les architectures d'[attention](https://fr.wikipedia.org/wiki/Attention_(machine_learning)) dans les [Graph Neural Networks](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_graphes) (GNN) sont des mécanismes qui permettent au réseau de pondérer différemment l'importance des nœuds voisins lors de l'agrégation des caractéristiques. Introduits initialement dans le domaine du [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) avec les Transformers, ces mécanismes ont été adaptés avec succès aux réseaux de neurones graphiques pour capturer des relations complexes dans les données graphiques.

## Points clés

- Les mécanismes d'attention permettent aux GNN de pondérer dynamiquement l'importance des nœuds voisins, offrant une meilleure flexibilité que les approches classiques
- Le Graph Attention Network (GAT) est l'architecture la plus populaire, utilisant des têtes d'attention multiples pour capturer différents types de relations
- Les principaux avantages incluent : meilleure interprétabilité, capacité à traiter des graphes hétérogènes, et possibilité d'ignorer les connexions non pertinentes
- Les applications couvrent divers domaines comme la bioinformatique, les réseaux sociaux et les systèmes de recommandation
- L'attention multi-têtes (typiquement 4-8) permet de stabiliser l'apprentissage et capturer différents aspects des relations

## Détails

Le mécanisme d'attention dans les GNN fonctionne en trois étapes principales : calcul des scores d'attention bruts (pour chaque paire de nœuds connectés via une fonction de similarité), normalisation via softmax pour obtenir des coefficients interprétables, et agrégation pondérée des caractéristiques des voisins.

Le Graph Attention Network (GAT), introduit par Veličković et al. (2018), repose sur une transformation linéaire des caractéristiques, leur concaténation, l'application d'un vecteur paramétrique avec activation LeakyReLU, et une normalisation via softmax. Sa complexité computationnelle est de O(|V|FF' + |E|F').

Parmi les variantes notables, on trouve l'attention basée sur les arêtes qui intègre les caractéristiques des arêtes, l'attention hiérarchique combinant attention locale et globale, et l'attention spatiale-temporelle pour les graphes dynamiques.

Les applications concrètes couvrent plusieurs domaines : chimie computationnelle (propriétés moléculaires), réseaux sociaux (détection de communautés), systèmes de recommandation (Pinterest, Alibaba), bioinformatique (réseaux protéiques), et vision par ordinateur (scènes relationnelles). Ces architectures montrent des améliorations de performance significatives (+20% sur Cora vs GCN), une capacité à gérer des graphes hétérogènes complexes, et une interprétabilité particulièrement utile en analyse moléculaire.