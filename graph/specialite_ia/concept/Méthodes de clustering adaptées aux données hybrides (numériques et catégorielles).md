---
title: Méthodes de clustering adaptées aux données hybrides (numériques et catégorielles)
type: concept
tags:
- clustering
- données hybrides
- analyse de données
- apprentissage automatique
- variables numériques
- variables catégorielles
- data mining
date_creation: '2025-04-03'
date_modification: '2025-04-03'
subClassOf: '[[Méthodes de clustering]]'
uses: '[[Métriques d''évaluation spécifiques pour le clustering de données mixtes]]'
---
## Généralité

Les méthodes de [clustering](https://fr.wikipedia.org/wiki/Partitionnement_de_donn%C3%A9es) adaptées aux données hybrides sont des algorithmes conçus pour gérer simultanément des variables numériques (quantitatives) et catégorielles (qualitatives) dans un même jeu de données. Ces méthodes sont essentielles dans de nombreux domaines où les données sont naturellement mixtes.

## Points clés

- Les [données hybrides](https://fr.wikipedia.org/wiki/Donn%C3%A9es_hybrides) combinent des attributs numériques et catégoriels
- Les algorithmes comme [k-prototypes](https://fr.wikipedia.org/wiki/K-moyennes) et les approches probabilistes sont spécialement conçus pour ce type de données
- L'efficacité dépend du prétraitement des données, du choix des métriques et de la nature des données

## Détails

Le clustering hybride doit résoudre le défi complexe de la mise à l'échelle des différentes métriques :
- Distances [euclidiennes](https://fr.wikipedia.org/wiki/Distance_euclidienne) pour les données numériques
- Mesures de similarité (comme l'indice de Jaccard) pour les catégories

Les principales méthodes incluent :

**Méthodes basées sur la dissimilarité**:
- Utilisation de mesures composites comme la [distance de Gower](https://fr.wikipedia.org/wiki/Distance_de_Gower)
- Algorithme k-prototypes (extension validée du k-means)

**Approches probabilistes**:
- Modélisation des variables numériques par des distributions normales
- Variables catégorielles par des distributions multinomiales
- Modèle de mélange gaussien-multinomial (GMM)

Le choix d'une méthode dépend de plusieurs facteurs :
- Proportion relative de variables [numériques](https://fr.wikipedia.org/wiki/Variable_num%C3%A9rique) et [catégorielles](https://fr.wikipedia.org/wiki/Variable_cat%C3%A9gorielle)
- Taille du jeu de données
- Présence de bruit ou de valeurs manquantes
- Interprétabilité requise des résultats

Parmi les applications typiques :
- **[Segmentation de clientèle](https://fr.wikipedia.org/wiki/Segmentation_(marketing))** combinant données démographiques (catégorielles) et comportementales (numériques)
- **Analyse de [données médicales](https://fr.wikipedia.org/wiki/Informatique_m%C3%A9dicale)** mêlant diagnostics (catégoriels) et mesures biologiques (numériques)
- **Classification de documents** avec métadonnées mixtes (catégorielles et numériques)

Pour évaluer ces méthodes, on utilise :
- Indice de silhouette modifié
- Indice de Davies-Bouldin adapté
- [Indice de Rand](https://fr.wikipedia.org/wiki/Indice_de_Rand) ajusté