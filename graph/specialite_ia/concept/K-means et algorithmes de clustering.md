---
title: K-means et algorithmes de clustering
type: concept
tags:
- clustering
- k-means
- apprentissage non supervisé
- data mining
- analyse de données
- partitionnement
- centroïdes
- machine learning
- algorithmes
- classification
date_creation: '2025-03-18'
date_modification: '2025-03-18'

- type: rdfs:subClassOf
  target: '[[Apprentissage non supervisé]]'
---

## Généralité

Le clustering est une technique d'apprentissage non supervisé qui consiste à regrouper des données similaires en clusters (groupes) sans connaissance préalable des étiquettes. Parmi les nombreux algorithmes de clustering, K-means est l'un des plus populaires et des plus simples à comprendre. Il vise à partitionner n observations en k clusters, où chaque observation appartient au cluster dont la moyenne (centroïde) est la plus proche.

## Points clés

- K-means minimise la somme des distances au carré entre les points de données et le centroïde de leur cluster assigné
- L'algorithme nécessite de spécifier à l'avance le nombre k de clusters souhaités
- K-means converge toujours, mais peut atteindre un minimum local plutôt que global
- La complexité temporelle est généralement O(n×k×d×i) où n est le nombre d'échantillons, k le nombre de clusters, d la dimension et i le nombre d'itérations

## Détails

### Fonctionnement de K-means

L'algorithme K-means suit un processus itératif simple :
1. Initialisation : sélection aléatoire de k points comme centroïdes initiaux
2. Affectation : chaque point de données est assigné au centroïde le plus proche
3. Mise à jour : recalcul des centroïdes comme moyenne des points assignés à chaque cluster
4. Répétition des étapes 2 et 3 jusqu'à convergence (les centroïdes ne changent plus significativement)

L'initialisation des centroïdes peut influencer considérablement le résultat final. Pour améliorer cela, la variante K-means++ propose une méthode d'initialisation plus robuste qui sélectionne les centroïdes initiaux de manière à ce qu'ils soient bien espacés.

### Autres algorithmes de clustering

Bien que K-means soit populaire, il présente certaines limitations, notamment sa sensibilité aux valeurs aberrantes et sa tendance à créer des clusters de taille similaire et de forme sphérique. D'autres algorithmes de clustering offrent des alternatives :

- **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) : identifie les clusters comme des zones de haute densité séparées par des zones de faible densité, sans nécessiter de spécifier le nombre de clusters
- **Clustering hiérarchique** : construit une hiérarchie de clusters, soit par agglomération (bottom-up) soit par division (top-down)
- **Gaussian Mixture Models (GMM)** : modélise les clusters comme un mélange de distributions gaussiennes
- **Mean-shift** : algorithme non paramétrique qui ne nécessite pas de spécifier le nombre de clusters
- **OPTICS** : extension de DBSCAN qui gère mieux les clusters de densités variables

### Évaluation des clusters

Pour évaluer la qualité d'un clustering, plusieurs métriques existent :
- Inertie (somme des distances au carré à l'intérieur des clusters)
- Indice de silhouette (mesure la cohésion et la séparation des clusters)
- Indice de Davies-Bouldin (ratio entre la dispersion intra-cluster et la séparation inter-clusters)
- Indice de Calinski-Harabasz (ratio entre la variance inter-clusters et intra-clusters)

Le choix de l'algorithme de clustering dépend de la nature des données, de la forme attendue des clusters et des contraintes spécifiques au problème.