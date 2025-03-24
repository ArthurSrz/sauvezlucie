---
title: Préparation des données
type: concept
tags:
- données
- préparation
- traitement de données
- data preparation
- analyse de données
date_creation: '2025-03-17'
date_modification: '2025-03-17'
subClassOf: '[[Les étapes clés pour concevoir un système d''Intelligence Artificielle]]'
precedes: '[[Choix du modèle]]'
---
## Généralité

La préparation des données est l'étape fondamentale dans le développement d'un système d'intelligence artificielle, consistant à transformer des données brutes en un format adapté à l'analyse et à l'apprentissage automatique.

## Points clés

- Représente 60 à 80% du temps consacré aux projets d'intelligence artificielle
- Inclut la collecte, le nettoyage, la normalisation et la transformation des données
- Détermine en grande partie la qualité et la performance du modèle final
- Nécessite une compréhension approfondie du domaine concerné

## Détails

La préparation des données est souvent considérée comme la pierre angulaire de tout projet d'intelligence artificielle. Cette étape cruciale transforme des données brutes, souvent imparfaites, en un ensemble structuré et exploitable pour l'entraînement de modèles.

### Collecte des données

Ce processus initial implique:
- L'identification des sources pertinentes (bases de données internes, API, web scraping, données publiques)
- L'évaluation de la qualité et de la quantité des données disponibles
- L'établissement de procédures d'échantillonnage pour garantir la représentativité
- Le respect des considérations éthiques et légales (RGPD, droits d'auteur)

### Nettoyage des données

Cette phase vise à améliorer la qualité intrinsèque des données:
- Gestion des valeurs manquantes (suppression, imputation par moyenne/médiane, modèles prédictifs)
- Identification et traitement des valeurs aberrantes (outliers)
- Correction des incohérences et des erreurs de saisie
- Élimination des doublons et des redondances

### Transformation et normalisation

Pour rendre les données exploitables par les algorithmes:
- Normalisation (mise à l'échelle entre 0 et 1) ou standardisation (moyenne 0, écart-type 1)
- Encodage des variables catégorielles (one-hot encoding, label encoding)
- Discrétisation des variables continues si nécessaire
- Réduction de dimensionnalité (PCA, t-SNE) pour les jeux de données à haute dimension

### Feature engineering

Création de nouvelles caractéristiques pour améliorer les performances du modèle:
- Extraction de caractéristiques pertinentes à partir des données brutes
- Création de variables d'interaction
- Décomposition de variables complexes (dates, adresses)
- Agrégations et transformations basées sur l'expertise du domaine

### Partitionnement des données

[Division](https://fr.wikipedia.org/wiki/Division) stratégique du jeu de données:
- Ensemble d'entraînement (60-80%): pour l'apprentissage du modèle
- Ensemble de validation (10-20%): pour l'ajustement des hyperparamètres
- Ensemble de test (10-20%): pour l'évaluation finale des performances

Une préparation des données rigoureuse est déterminante pour la réussite d'un projet d'IA, car elle permet d'éviter le célèbre principe "garbage in, garbage out" (des données de mauvaise qualité produiront nécessairement des résultats médiocres).