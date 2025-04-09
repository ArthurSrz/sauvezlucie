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

L'agrégation de voisinage est un mécanisme fondamental dans les [réseaux neuronaux de graphes](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_graphes) (GNN) qui permet de capturer et d'intégrer les informations des nœuds voisins pour mettre à jour la représentation d'un nœud central. Inspiré par le concept de "passage de messages" entre nœuds, ce processus repose sur des fonctions d'agrégation comme la somme, la moyenne ou le maximum des caractéristiques des voisins. Ce mécanisme constitue la base du fonctionnement des GNN et leur permet de traiter efficacement des données structurées en graphe.

## Points clés

- Permet aux GNN de capturer l'information contextuelle en combinant les caractéristiques des nœuds voisins via le principe de "passage de messages" (inspiré des travaux de [Judea Pearl](https://fr.wikipedia.org/wiki/Judea_Pearl) sur les réseaux bayésiens)
- Utilise différentes fonctions d'agrégation (moyenne, somme, max, LSTM, attention) offrant diverses capacités de modélisation
- Est invariant à la permutation des voisins pour respecter la nature non ordonnée des graphes
- Peut capturer des informations à différentes distances via l'agrégation multi-couches (k-hop neighborhood)
- S'adapte dynamiquement grâce à des techniques avancées comme l'agrégation différentiée ou les mécanismes d'attention

## Détails

Dans un [réseau neuronal de graphes](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_graphe), chaque nœud est initialement représenté par un vecteur de caractéristiques. L'agrégation de voisinage consiste à mettre à jour cette représentation en tenant compte des caractéristiques des nœuds voisins, via deux étapes principales : l'agrégation (`a_v = AGRÉGATION({h_u pour tout u ∈ N(v)})`) et la mise à jour (`h_v' = MISE À JOUR(h_v, a_v)`).

Plusieurs fonctions d'agrégation existent, chacune avec ses spécificités :
- **Moyenne/Somme** : Simple mais efficace, utilisée dans les GCN (Graph Convolutional Networks)
- **Max-pooling** : Capture les caractéristiques les plus saillantes, utilisée dans GraphSAGE
- **LSTM** : Pour capturer des séquences ordonnées de voisins
- **Mécanismes d'attention** : Pondèrent l'importance de chaque voisin de manière dynamique (comme dans les GAT)

Différentes architectures implémentent ces mécanismes d'agrégation :
- **GraphSAGE** (Hamilton et al., 2017) : Méthode d'échantillonnage des voisins supportant plusieurs fonctions d'agrégation
- **GCN** (Kipf & Welling, 2017) : Utilise une agrégation par moyenne pondérée normalisée par le degré des nœuds
- **GAT** (Veličković et al., 2018) : Intègre des mécanismes d'attention apprenables
- **GIN** (Xu et al., 2018) : Fonction d'agrégation maximale expressive basée sur le test d'isomorphisme de Weisfeiler-Lehman

L'empilement de plusieurs couches permet d'intégrer des informations à distances croissantes (k-hop neighborhood), avec des similarités conceptuelles aux champs réceptifs dans les [CNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif). Des techniques avancées comme l'agrégation différentiée (Corso et al., 2020) permettent d'adapter dynamiquement la stratégie d'agrégation.

Ces méthodes ont démontré leur efficacité dans divers domaines comme la [bioinformatique](https://fr.wikipedia.org/wiki/Bio-informatique), les systèmes de recommandation ou l'analyse de réseaux routiers, et sur des benchmarks comme les graphes moléculaires (ZINC, OGB) ou les graphes de citation (Cora, Pubmed).

[1] Source Wikipedia: "Graph neural network"  
[2] Source Wikipedia: "Graph attention network"  
[3] Source Wikipedia: "Applications of graph neural networks"