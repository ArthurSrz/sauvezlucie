---
title: Techniques de prétraitement pour données mixtes avant clustering
type: concept
tags:
- Data Science
- Prétraitement
- Clustering
- Données mixtes
- Normalisation
- Encodage
- Machine Learning
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Prétraitement des données]]'
relatedTo:
- '[[Métriques d''évaluation spécifiques pour le clustering de données mixtes]]'
- '[[Méthodes de clustering adaptées aux données hybrides (numériques et catégorielles)]]'
---
## Généralité

Le [prétraitement des données](https://fr.wikipedia.org/wiki/Pr%C3%A9traitement_des_donn%C3%A9es) mixtes (combinant variables numériques et catégorielles) est une étape cruciale avant d'appliquer des algorithmes de [clustering](https://fr.wikipedia.org/wiki/Partitionnement_de_donn%C3%A9es). Il vise à harmoniser les échelles, gérer les valeurs manquantes et transformer les données pour améliorer la qualité des regroupements.

## Points clés

- **Standardisation/Normalisation** : Harmonisation des échelles des variables numériques
- **Encodage des variables catégorielles** : Transformation en valeurs numériques exploitables
- **Gestion des valeurs manquantes** : Imputation ou suppression des données incomplètes
- **Réduction de dimensionnalité** : Simplification des données complexes
- **Validation des résultats** : Évaluation de la qualité des clusters formés

## Détails

Les variables numériques doivent être [standardisées](https://fr.wikipedia.org/wiki/Standardisation_(statistiques)) (moyenne=0, écart-type=1) ou [normalisées](https://fr.wikipedia.org/wiki/Normalisation_(statistiques)) (dans une plage fixe, comme [0,1]) pour éviter que les variables avec de grandes échelles ne dominent les calculs de distance dans le clustering. La standardisation Z-score (centrage-réduction convient particulièrement aux algorithmes comme [K-means](https://fr.wikipedia.org/wiki/K-moyennes).

Pour les variables catégorielles, les techniques d'encodage incluent le [One-Hot Encoding](https://fr.wikipedia.org/wiki/One-hot), le Label Encoding et le Target Encoding. La gestion des valeurs manquantes peut se faire par imputation (moyenne/médiane pour les numériques, mode pour les catégoriels), suppression ou utilisation d'algorithmes robustes comme KNN-imputer.

Les techniques de réduction de dimension comprennent l'[ACP](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales), l'[UMAP](https://fr.wikipedia.org/wiki/UMAP) et le PHATE. Il est important d'évaluer l'impact avec des métriques comme le [score de silhouette](https://fr.wikipedia.org/wiki/Silhouette_(clustering)), d'adapter aux algorithmes (certains comme [K-prototypes](https://fr.wikipedia.org/wiki/K-prototypes) gèrent nativement les données mixtes), de conserver l'interprétabilité et de valider la robustesse avec des techniques comme la [validation croisée](https://fr.wikipedia.org/wiki/Validation_crois%C3%A9e_(statistiques)).

---

## Généralité

Problème de programmation visant à trier N mots selon leur longueur et leur ordre alphabétique.

## Points clés

- Tri des mots par longueur croissante
- En cas d'égalité de longueur, tri alphabétique
- Élimination des doublons
- Contraintes : 1 ≤ N ≤ 20,000, longueur ≤ 50

## Détails

La solution algorithmique implique d'abord une étape de dédoublonnage utilisant un set, suivie d'un double tri : d'abord alphabétique, puis par longueur. Cette approche exploite la stabilité du tri Python. En pratique, le problème peut être résolu efficacement avec le code Python suivant :