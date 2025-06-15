---
title: GNN pour la prédiction de liens dans les réseaux sociaux
type: concept
tags:
- GNN
- réseaux sociaux
- prédiction de liens
- apprentissage automatique
- graphes
- recommandation
- analyse de réseaux
- deep learning
- IA
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Les GNN]]'
uses:
- '[[Agrégation de voisinage dans les réseaux neuronaux de graphes]]'
- '[[Architectures d''attention dans les GNN (Graph Neural Networks)]]'
---
## Généralité

Les [Graph Neural Networks](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_graphes) (GNN) appliqués à la prédiction de liens dans les [réseaux sociaux](https://fr.wikipedia.org/wiki/R%C3%A9seau_social) représentent une approche avancée d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui exploite la structure des graphes pour prédire l'émergence de nouvelles connexions entre utilisateurs. Inspirés par les réseaux de neurones traditionnels, les GNN se spécialisent dans le traitement de données structurées en graphes, où les nœuds représentent des entités (comme des utilisateurs) et les arêtes symbolisent leurs relations.

## Points clés

- Les GNN capturent simultanément les caractéristiques topologiques du réseau et les attributs des nœuds en utilisant des mécanismes de propagation de message entre nœuds voisins
- La prédiction de liens est formulée comme un problème de classification binaire où le modèle évalue la probabilité qu'un lien existe entre deux nœuds
- Les architectures courantes incluent [GraphSAGE](https://fr.wikipedia.org/wiki/GraphSAGE), [Graph Convolutional Networks](https://fr.wikipedia.org/wiki/Graph_Convolutional_Network) (GCN) et Graph Attention Networks (GAT)
- Les performances dépassent généralement les méthodes traditionnelles basées sur des heuristiques
- Applications pratiques dans les grandes plateformes sociales comme [Facebook](https://fr.wikipedia.org/wiki/Facebook) et [LinkedIn](https://fr.wikipedia.org/wiki/LinkedIn)

## Détails

Les GNN abordent la prédiction de liens en transformant les utilisateurs en nœuds et leurs interactions en arêtes au sein d'un graphe. Le processus d'apprentissage comprend plusieurs étapes clés : agrégation de l'information du voisinage, propagation de messages permettant d'intégrer des informations sur la structure locale et globale, et combinaison des représentations vectorielles des nœuds par paires.

Les fonctions d'agrégation peuvent varier, allant de moyennes simples à des mécanismes d'attention plus sophistiqués comme dans les GAT. Pour la combinaison des embeddings, plusieurs opérateurs sont utilisables : concaténation, produit hadamard (élément par élément), somme ou différence absolue.

Les défis particuliers dans les réseaux sociaux incluent la gestion de graphes dynamiques, le déséquilibre des classes (avec des ratios atteignant 1000:1) et le passage à l'échelle pour des réseaux comportant des millions d'utilisateurs. Les solutions employées comprennent des techniques d'échantillonnage comme le [negative sampling](https://fr.wikipedia.org/wiki/Word2vec#Architecture_et_formation), ainsi que des approches comme GraphSAINT ou ClusterGCN pour gérer les graphes de grande taille, permettant de réduire la complexité de O(n²) à O(n log n).

Les plateformes majeures utilisent diverses variantes de ces architectures : [LinkedIn](https://fr.wikipedia.org/wiki/LinkedIn) emploie une architecture basée sur GraphSAGE pour son système "People You May Know", [Facebook](https://fr.wikipedia.org/wiki/Facebook) utilise des GNN combinés avec des techniques d'échantillonnage négatif, et [Twitter](https://fr.wikipedia.org/wiki/Twitter) a implémenté des Graph Attention Networks (GAT) pour identifier les influenceurs potentiels.

Pour l'évaluation des modèles, les métriques principales incluent AUC-ROC, précision moyenne (AP) et Hit@K. Selon les benchmarks, les architectures modernes permettent de réduire considérablement la complexité computationnelle tout en conservant la majorité des performances.