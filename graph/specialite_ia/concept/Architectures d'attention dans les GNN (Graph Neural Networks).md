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
date_creation: '2025-03-28'
date_modification: '2025-03-28'
relatedTo: '[[Agrégation de voisinage dans les réseaux neuronaux de graphes]]'
isPartOf:
- '[[Apprentissage par représentation de graphes (Graph Representation Learning)]]'
- '[[Les GNN]]'
uses: '[[GNN pour la prédiction de liens dans les réseaux sociaux]]'
---
## Généralité

Les architectures d'attention dans les Graph Neural Networks (GNN) sont des mécanismes qui permettent au réseau de pondérer différemment l'importance des nœuds voisins lors de l'agrégation des caractéristiques. Contrairement aux GNN classiques qui traitent tous les voisins de manière égale, les mécanismes d'attention permettent au modèle d'apprendre quelles connexions sont les plus pertinentes pour la tâche à accomplir, améliorant ainsi la capacité du réseau à capturer des relations complexes dans les données graphiques.

## Points clés

- Les mécanismes d'attention permettent aux GNN de pondérer dynamiquement l'importance des nœuds voisins lors de l'agrégation des caractéristiques
- Le Graph Attention Network (GAT) est l'une des architectures d'attention les plus populaires pour les GNN
- L'attention multi-têtes permet de capturer différents aspects des relations entre nœuds
- Les mécanismes d'attention améliorent l'interprétabilité des modèles GNN en révélant l'importance relative des connexions

## Détails

### Principe de fonctionnement

Dans une architecture d'attention pour GNN, chaque nœud calcule des coefficients d'attention pour ses voisins. Ces coefficients déterminent l'importance de chaque voisin dans la mise à jour des caractéristiques du nœud central. Le processus se déroule généralement en trois étapes :

1. **Calcul des scores d'attention bruts** : Pour chaque paire de nœuds connectés (i, j), un score d'attention est calculé en fonction de leurs caractéristiques.
2. **Normalisation** : Les scores sont normalisés (souvent via softmax) pour obtenir des coefficients d'attention.
3. **Agrégation pondérée** : Les caractéristiques des voisins sont agrégées en utilisant les coefficients d'attention comme poids.

### Graph Attention Networks (GAT)

Le GAT, introduit par Veličković et al. (2018), est l'une des implémentations les plus influentes des mécanismes d'attention dans les GNN. Dans un GAT, le coefficient d'attention entre deux nœuds i et j est calculé comme suit :

1. Application d'une transformation linéaire aux caractéristiques des nœuds
2. [Concaténation des caractéristiques transformées](https://fr.wikipedia.org/wiki/Concaténation_des_caractéristiques_transformées)
3. Application d'un vecteur de paramètres suivi d'une activation LeakyReLU
4. Normalisation via softmax sur tous les voisins

### Attention multi-têtes

Pour stabiliser le processus d'apprentissage et capturer différents aspects des relations, les GAT utilisent généralement plusieurs têtes d'attention indépendantes. Chaque tête apprend un ensemble différent de coefficients d'attention. Les résultats de toutes les têtes sont ensuite combinés, soit par concaténation, soit par moyenne.

### Variantes et extensions

Plusieurs variantes des mécanismes d'attention pour GNN ont été proposées :

- **Attention basée sur les arêtes** : Intègre les caractéristiques des arêtes dans le calcul de l'attention
- **Attention hiérarchique** : Applique l'attention à différents niveaux de granularité du graphe
- **Attention spatiale-temporelle** : Étend l'attention aux graphes dynamiques en considérant à la fois les relations spatiales et temporelles

### Avantages et applications

Les architectures d'attention dans les GNN offrent plusieurs avantages :
- Meilleure performance sur des tâches complexes de prédiction sur graphes
- Capacité à gérer des graphes hétérogènes où tous les voisins n'ont pas la même importance
- Interprétabilité accrue grâce à la visualisation des coefficients d'attention
- Adaptabilité à différentes structures de graphes sans nécessiter de connaissances préalables sur la structure

Ces architectures sont particulièrement efficaces dans des domaines comme la chimie moléculaire, les réseaux sociaux, les systèmes de recommandation et la bioinformatique.