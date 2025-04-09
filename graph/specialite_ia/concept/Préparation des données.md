---
title: Préparation des données
type: concept
tags:
- données
- préparation
- traitement de données
- data preparation
- analyse de données
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Les étapes clés pour concevoir un système d''Intelligence Artificielle]]'
precedes: '[[Choix du modèle]]'
seeAlso: '[[Prétraitement des données]]'
---
## Généralité

La préparation des données est l'étape fondamentale dans le développement d'un système d'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle), consistant à transformer des données brutes en un format adapté à l'analyse et à l'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique). Ce processus, souvent appelé "data wrangling" ou "data munging", représente selon diverses études 60 à 80% du temps consacré aux projets d'IA (comme mentionné dans l'article "Data preparation" de Wikipédia). La qualité de cette préparation influence directement les performances des modèles d'IA.

## Points clés

- Transformation des données brutes en format exploitable via des étapes comme le nettoyage, la normalisation et la réduction de dimensionnalité
- Représente 60 à 80% du temps dans les projets de [data science](https://fr.wikipedia.org/wiki/Science_des_donn%C3%A9es)
- Comprend des techniques avancées comme l'augmentation de données, cruciale en [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur)
- Nécessite des outils spécialisés comme [Pandas](https://fr.wikipedia.org/wiki/Pandas_(biblioth%C3%A8que_Python)) et [OpenRefine](https://fr.wikipedia.org/wiki/OpenRefine)
- Influence directe sur le principe "garbage in, garbage out" des modèles d'IA

## Détails

### Collecte des données
Ce processus initial implique:
- L'identification des sources pertinentes (bases de données internes, API, web scraping, données publiques)
- L'évaluation de la qualité et de la quantité des données disponibles, incluant la détection des biais potentiels
- L'établissement de procédures d'échantillonnage pour garantir la représentativité
- Le respect des considérations éthiques et légales ([RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es), droits d'auteur)

### Nettoyage des données
Cette phase vise à améliorer la qualité intrinsèque des données:
- Gestion des valeurs manquantes (suppression, imputation par moyenne/médiane, modèles prédictifs)
- Identification et traitement des valeurs aberrantes (outliers)
- Correction des incohérences et des erreurs de saisie
- Élimination des doublons et des redondances

### Transformation et normalisation
Pour rendre les données exploitables par les algorithmes:
- [Normalisation](https://fr.wikipedia.org/wiki/Normalisation_(statistiques)) (mise à l'échelle entre 0 et 1) ou standardisation (moyenne 0, écart-type 1)
- Encodage des variables catégorielles (one-hot encoding, label encoding)
- Discrétisation des variables continues si nécessaire
- Réduction de dimensionnalité ([PCA](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales), t-SNE) pour les jeux de données à haute dimension
- Techniques avancées comme l'augmentation de données (data augmentation) pour les projets de vision par ordinateur

### Feature engineering
Création de nouvelles caractéristiques pour améliorer les performances du modèle:
- Extraction de caractéristiques pertinentes à partir des données brutes
- Création de variables d'interaction
- Décomposition de variables complexes (dates, adresses)
- Agrégations et transformations basées sur l'expertise du domaine

### Partitionnement des données
Division stratégique du jeu de données:
- Ensemble d'entraînement (60-80%): pour l'apprentissage du modèle
- Ensemble de validation (10-20%): pour l'ajustement des hyperparamètres
- Ensemble de test (10-20%): pour l'évaluation finale des performances

Une préparation des données rigoureuse est déterminante pour la réussite d'un projet d'IA, car elle permet d'éviter le principe "garbage in, garbage out". comme le souligne l'article Wikipédia sur le sujet, cette étape influence directement la qualité et la performance du modèle final.