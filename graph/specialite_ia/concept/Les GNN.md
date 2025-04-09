---
title: Les GNN
type: concept
tags:
- GNN
- réseaux de neurones
- graphes
- apprentissage automatique
- données structurées
- deep learning
- modélisation relationnelle
date_creation: '2025-03-28'
date_modification: '2025-04-03'
seeAlso: '[[GNN pour la prédiction de liens dans les réseaux sociaux]]'
---
## Généralité

Les [Graph Neural Networks](https://fr.wikipedia.org/wiki/Graph_Neural_Network) (GNN) sont une classe d'architectures de [réseaux de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) conçues pour traiter des données structurées sous forme de graphes. Contrairement aux réseaux de neurones traditionnels, les GNN peuvent capturer les relations complexes entre entités représentées comme des nœuds dans un graphe, ce qui les rend particulièrement adaptés pour modéliser des systèmes où les interactions entre éléments sont essentielles.

## Points clés

- Traitement des données graphiques via des mécanismes de "passage de messages" (message passing)
- Préservation de l'invariance par permutation (l'ordre des nœuds n'affecte pas le résultat)
- Applications variées: chimie computationnelle, réseaux sociaux, systèmes de recommandation, bioinformatique
- Variantes principales: [GCN](https://fr.wikipedia.org/wiki/Graph_Convolutional_Network), GraphSAGE, GAT, GIN
- Défis actuels: scalabilité, interprétabilité, traitement des graphes dynamiques

## Détails

Les GNN trouvent leurs fondements dans les travaux de Gori et al. (2005) et Scarselli et al. (2009). Ils opèrent selon un principe de propagation d'information entre nœuds connectés, permettant à chaque nœud d'accumuler des informations sur son voisinage.

Le fonctionnement des GNN repose sur trois étapes itératives:
1. Agrégation des informations des voisins
2. Combinaison avec l'état actuel du nœud
3. Mise à jour de la représentation du nœud

Cette opération est répétée pour plusieurs couches, permettant la propagation d'information à travers la structure du graphe.

Parmi les variantes principales, on trouve:
- **[GCN](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_convolutions)**: Utilise une moyenne pondérée des voisins
- **GraphSAGE**: Emploie des agrégateurs paramétrables
- **[GAT](https://fr.wikipedia.org/wiki/Attention_(machine_learning))**: Introduit un mécanisme d'attention
- **GIN**: Maximise le pouvoir discriminant entre structures

Les applications des GNN couvrent divers domaines:
- [Chimie moléculaire](https://fr.wikipedia.org/wiki/Chimie_mol%C3%A9culaire): prédiction des propriétés des molécules
- Réseaux sociaux: analyse des relations entre utilisateurs
- [Découverte de médicaments](https://fr.wikipedia.org/wiki/Conception_de_m%C3%A9dicament): modélisation moléculaire
- Détection de [blanchiment d'argent](https://fr.wikipedia.org/wiki/Blanchiment_d%27argent): analyse des réseaux de transactions
- [Physique des particules](https://fr.wikipedia.org/wiki/Physique_des_particules): analyse des trajectoires de particules

Les défis actuels incluent:
- Problèmes de scalabilité
- Sur-lissage (over-smoothing)
- Capture des structures à longue distance

Les développements récents incluent:
- GNN spatio-temporels
- Architectures combinant GNN et transformers
- Approches hiérarchiques pour les graphes à grande échelle