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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Méthodes de clustering]]'
hasPart: '[[Segmentation adaptative par modulation des seuils de densité pour distributions
  irrégulières]]'
---
## Généralité

Le clustering est une technique d'[apprentissage non supervisé](https://fr.wikipedia.org/wiki/Apprentissage_non_supervis%C3%A9) qui consiste à regrouper des données similaires en clusters (groupes) sans connaissance préalable des étiquettes. Cette méthode de partitionnement de données est particulièrement utile pour l'[exploration de données](https://fr.wikipedia.org/wiki/Exploration_de_donn%C3%A9es), la segmentation de marché ou l'analyse d'images. Parmi les nombreux algorithmes de clustering, [K-means](https://fr.wikipedia.org/wiki/K-moyennes) est l'un des plus populaires et des plus simples à comprendre.

## Points clés

- [K-means](https://fr.wikipedia.org/wiki/K-moyennes) minimise la somme des distances au carré entre les points de données et le centroïde de leur cluster assigné (méthode connue sous le nom de "critère d'inertie intra-classe")
- L'algorithme nécessite de spécifier à l'avance le nombre k de clusters souhaités, déterminé par des méthodes comme la [méthode du coude](https://fr.wikipedia.org/wiki/M%C3%A9thode_du_coude) ou l'indice de silhouette
- K-means converge toujours mais peut atteindre un minimum local plutôt que global (d'où la pratique des initialisations multiples)
- L'algorithme est sensible aux outliers et fonctionne mieux avec des données sphériques et bien séparées
- Une variante courante est [K-means++](https://fr.wikipedia.org/wiki/K-moyennes#K-moyennes_++), qui améliore l'initialisation des centroïdes

## Détails

### Fonctionnement de K-means

L'algorithme [K-means](https://fr.wikipedia.org/wiki/K-moyennes) suit un processus itératif :
1. Initialisation : sélection aléatoire de k points comme centroïdes initiaux (les points de données peuvent être utilisés). La méthode [K-means++](https://fr.wikipedia.org/wiki/K-moyennes#Initialisation) améliore ce processus en choisissant des centroïdes initiaux bien espacés.
2. Affectation : chaque point de données est assigné au centroïde le plus proche selon la distance [euclidienne](https://fr.wikipedia.org/wiki/Distance_euclidienne).
3. Mise à jour : recalcul des centroïdes comme moyenne des points assignés à chaque cluster.
4. Répétition des étapes 2 et 3 jusqu'à convergence.

Proposé initialement par [Stuart Lloyd](https://fr.wikipedia.org/wiki/Stuart_Lloyd) en 1957 pour la quantification vectorielle, K-means a une complexité temporelle de O(n×k×d×i) où n est le nombre d'échantillons, k le nombre de clusters, d la dimension et i le nombre d'itérations.

### Limitations de K-means

- Nécessité de spécifier k à l'avance
- Sensibilité aux outliers (pouvant être atténuée par des techniques de prétraitement)
- Préférence pour des clusters de forme sphérique et taille similaire
- Difficulté avec des clusters de densité variable ou de formes complexes

### Autres algorithmes de clustering

- **[DBSCAN](https://fr.wikipedia.org/wiki/DBSCAN)** : Identifie des clusters de forme arbitraire basés sur la densité, avec deux paramètres clés (ε et minPts). Particulièrement efficace pour détecter du bruit et des clusters imbriqués.
  
- **Clustering hiérarchique** : Produit un dendrogramme montrant les relations hiérarchiques entre clusters.

- **[Gaussian Mixture Models](https://fr.wikipedia.org/wiki/M%C3%A9lange_gaussien) (GMM)** : Modèle probabiliste où chaque cluster suit une distribution gaussienne multivariée.

- **[Mean-shift](https://fr.wikipedia.org/wiki/Mean_shift)** : Détecte automatiquement le nombre de clusters en trouvant les modes de la distribution de densité.

### Évaluation des clusters

- **Inertie** : Somme des distances au carré, utilisée dans la "méthode du coude" pour estimer k optimal.
- **[Indice de silhouette](https://fr.wikipedia.org/wiki/Silhouette_(clustering))** : Combine cohésion intra-cluster et séparation inter-clusters.
- **Indice de Davies-Bouldin** : Minimal pour un bon clustering.
- **Indice de Calinski-Harabasz** : Ratio entre la dispersion inter-clusters et intra-clusters.

Pour des données étiquetées, on peut utiliser des métriques supervisées comme l'ARI (Adjusted Rand Index) ou l'AMI (Adjusted Mutual Information).