---
title: Agrégation de voisinage dans les réseaux neuronaux de graphes
type: concept
tags:
- GNN
- réseaux neuronaux
- graphes
- agrégation de voisinage
- apprentissage automatique
- topologie
- représentation de nœuds
- deep learning
- traitement de graphes
- machine learning
date_creation: '2025-03-28'
date_modification: '2025-03-28'
hasPart: '[[Apprentissage par représentation de graphes (Graph Representation Learning)]]'
isPartOf: '[[Les GNN]]'
---
## Généralité

L'agrégation de voisinage est un mécanisme fondamental dans les réseaux neuronaux de graphes (GNN) qui permet de capturer et d'intégrer les informations des nœuds voisins pour mettre à jour la représentation d'un nœud central. Ce processus est essentiel pour permettre aux GNN d'apprendre des représentations qui tiennent compte de la structure topologique du graphe et des caractéristiques des nœuds environnants. L'agrégation de voisinage constitue le cœur du fonctionnement des GNN et leur permet de traiter efficacement des données structurées en graphe.

## Points clés

- L'agrégation de voisinage permet aux GNN de capturer l'information contextuelle en combinant les caractéristiques des nœuds voisins
- Différentes fonctions d'agrégation (moyenne, somme, max, LSTM, attention) offrent diverses capacités de modélisation
- Le processus d'agrégation est généralement invariant à la permutation des voisins pour respecter la nature non ordonnée des graphes
- L'agrégation multi-couches permet de capturer des informations de voisinage à différentes distances (k-hop neighborhood)

## Détails

Dans un réseau neuronal de graphes, chaque nœud est initialement représenté par un vecteur de caractéristiques. L'agrégation de voisinage consiste à mettre à jour cette représentation en tenant compte des caractéristiques des nœuds voisins. Ce processus se déroule généralement en deux étapes principales : l'agrégation des informations des voisins, puis la combinaison de cette information agrégée avec les caractéristiques du nœud central.

Formellement, si l'on considère un nœud v avec un ensemble de voisins N(v), l'opération d'agrégation peut s'écrire :

1. Agrégation : a_v = AGRÉGATION({h_u pour tout u ∈ N(v)})
2. Mise à jour : h_v' = MISE À JOUR(h_v, a_v)

Où h_v représente les caractéristiques du nœud v, et h_v' sa représentation mise à jour.

Plusieurs fonctions d'agrégation peuvent être utilisées :

- **[Moyenne](https://fr.wikipedia.org/wiki/Moyenne)/Somme** : Simple mais efficace, utilisée dans les GCN ([Graph Convolutional Networks](https://fr.wikipedia.org/wiki/Graph_Convolutional_Networks))
- **Max-pooling** : Capture les caractéristiques les plus saillantes, utilisée dans GraphSAGE
- **LSTM** : Pour capturer des séquences ordonnées de voisins
- **Mécanismes d'attention** : Pondèrent l'importance de chaque voisin, comme dans les GAT (Graph Attention Networks)

L'empilement de plusieurs couches d'agrégation permet aux GNN de capturer des informations de voisinage à des distances croissantes. Avec k couches, un nœud peut intégrer des informations provenant de son k-hop neighborhood (voisins jusqu'à k sauts de distance).

Un défi majeur dans la conception des fonctions d'agrégation est de maintenir l'invariance à la permutation, car l'ordre des voisins n'a généralement pas d'importance dans un graphe. Les fonctions comme la somme, la moyenne ou le max sont naturellement invariantes à la permutation.

L'agrégation de voisinage doit également être capable de gérer des graphes de tailles variables et des nœuds ayant un nombre différent de voisins, ce qui est généralement résolu par la normalisation ou l'échantillonnage de voisinage.

## Applications

L'agrégation de voisinage est au cœur de nombreuses architectures de GNN comme GraphSAGE, GCN, GAT et GIN (Graph Isomorphism Network), chacune proposant différentes approches pour agréger et mettre à jour les représentations des nœuds en fonction des caractéristiques de la tâche à accomplir et de la structure du graphe.