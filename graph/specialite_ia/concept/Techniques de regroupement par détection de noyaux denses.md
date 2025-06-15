---
title: Techniques de regroupement par détection de noyaux denses
type: concept
tags:
- clustering
- apprentissage non supervisé
- data mining
- analyse de données
- algorithmes
- intelligence artificielle
- machine learning
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Méthodes de clustering]]'
---
## Généralité

Les techniques de regroupement par détection de noyaux denses ([Density-Based Clustering](https://fr.wikipedia.org/wiki/Regroupement_de_donn%C3%A9es#M%C3%A9thodes_de_partitionnement)) sont des méthodes d'[apprentissage non supervisé](https://fr.wikipedia.org/wiki/Apprentissage_non_supervis%C3%A9) qui identifient des groupes de données en se basant sur la densité locale des points. L'algorithme le plus connu est [DBSCAN](https://fr.wikipedia.org/wiki/DBSCAN) (Density-Based Spatial Clustering of Applications with Noise), capable de détecter des clusters de formes arbitraires et de gérer efficacement le bruit.

## Points clés

- **[Détection de clusters non convexes](https://fr.wikipedia.org/wiki/Classification_automatique)** : Trouve des groupes de formes variées (cercles, spirales, lignes sinueuses)
- **[Résistance au bruit](https://fr.wikipedia.org/wiki/Bruit_(physique))** : Identifie et exclut les points isolés (valeurs aberrantes)
- **Pas besoin de spécifier le nombre de clusters** : Déterminé automatiquement via les paramètres ε et MinPts
- **Hiérarchie de densité** : Variantes comme [OPTICS](https://fr.wikipedia.org/wiki/OPTICS_(algorithm)) détectent des clusters emboîtés
- **Applications variées** : Analyse spatiale, biologie, sécurité, marketing, astronomie

## Détails

Les techniques reposent sur l'idée qu'un cluster est une région dense de points séparée par des régions moins denses ([détection de noyaux denses](https://fr.wikipedia.org/wiki/Cluster_%28statistiques%29)).

DBSCAN fonctionne avec deux paramètres principaux :
- **eps (ε)** : Rayon de voisinage autour d'un point
- **minPts** : Nombre minimum de points requis pour former un noyau

Les points sont classés en trois catégories :
- **Core point** : Au moins `minPts` voisins dans le rayon `eps`
- **Border point** : Dans le voisinage d'un core point mais avec moins de `minPts` voisins
- **Noise point** : Ni core point ni border point

### Avantages
- **Flexibilité** : Adapté à des clusters de densités variables et de formes arbitraires
- **Robustesse** : Gère efficacement les outliers et le bruit
- **Automatisation** : Ne nécessite pas de connaître à l'avance le nombre de clusters
- **Hiérarchie de densité** : Variantes comme [OPTICS](https://fr.wikipedia.org/wiki/OPTICS_(algorithm)) et [HDBSCAN](https://fr.wikipedia.org/wiki/HDBSCAN) permettent des analyses multi-échelles

### Limites
- **Sensibilité aux paramètres** : Choix critique de `eps` et `minPts` qui peut affecter significativement les résultats
- **Difficulté avec densités variables** : Performance réduite pour des clusters de densités très différentes
- **Complexité algorithmique** : O(n²) dans l'implémentation de base, pouvant être réduit à O(n log n) avec des index spatiaux
- **Problèmes en haute dimension** : Efficacité réduite due au "fléau de la dimensionnalité"

### Applications pratiques
- **Analyse spatiale** : Détection de zones urbaines denses, analyse de [données géospatiales](https://fr.wikipedia.org/wiki/Donn%C3%A9e_g%C3%A9ospatiale)
- **Biologie** : Regroupement de cellules ou gènes, analyse d'[ADN](https://fr.wikipedia.org/wiki/Acide_d%C3%A9soxyribonucl%C3%A9ique)
- **Sécurité informatique** : Détection d'intrusions et prévention des attaques
- **Astronomie** : Identification de groupements stellaires et classification de corps célestes
- **Marketing** : Segmentation de clientèle basée sur le comportement d'achat