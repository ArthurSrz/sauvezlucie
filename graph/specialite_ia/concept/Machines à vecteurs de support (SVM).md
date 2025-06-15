---
title: Machines à vecteurs de support (SVM)
type: concept
tags:
- Machine Learning
- SVM
- Classification
- Apprentissage supervisé
- Algorithmes
- Vecteurs de support
- Modèles prédictifs
- Intelligence artificielle
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Algorithme de classification]]'
isPartOf: '[[Apprentissage supervisé]]'
hasPart: '[[Apprentissage profond (Deep Learning)]]'
---
## Généralité

Les [Machines à Vecteurs de Support](https://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support) (SVM) constituent une famille d'[algorithmes d'apprentissage supervisé](https://fr.wikipedia.org/wiki/Apprentissage_supervisé) particulièrement efficaces pour la classification et la régression. Développées initialement par [Vladimir Vapnik](https://fr.wikipedia.org/wiki/Vladimir_Vapnik) et Alexey Chervonenkis dans les années 1960-1970, les SVM trouvent leurs fondements théoriques dans la théorie de l'apprentissage statistique et le principe de minimisation du risque structurel.

## Points clés

- Les SVM maximisent la marge entre les classes pour une meilleure généralisation, s'appuyant sur des fondements mathématiques solides
- Elles utilisent l'astuce du noyau (kernel trick) pour résoudre des problèmes non-linéaires en projetant les données dans un espace de plus haute dimension
- Particulièrement performantes pour la classification binaire, elles peuvent être étendues au cas multiclasse via des approches comme "un-contre-un" ou "un-contre-tous"
- Robustes face au "fléau de la dimension" et efficaces même avec des ensembles d'entraînement relativement petits
- L'optimisation repose sur la résolution d'un problème de programmation quadratique convexe, garantissant théoriquement un optimum global

## Détails

Le principe fondamental des [SVM](https://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support) repose sur la recherche d'un hyperplan séparateur qui maximise la distance (marge) avec les points les plus proches de chaque classe, appelés vecteurs de support. Mathématiquement, cela revient à résoudre un problème d'[optimisation quadratique](https://fr.wikipedia.org/wiki/Programmation_quadratique) sous contraintes. Pour un problème de classification binaire avec des données linéairement séparables, l'équation de l'hyperplan est donnée par: w·x + b = 0, où w est le vecteur normal à l'hyperplan, b est le biais, et x représente les données.

L'une des forces majeures des SVM réside dans leur capacité à traiter des problèmes non-linéaires grâce à l'astuce du noyau. Cette technique permet de projeter implicitement les données dans un espace de dimension supérieure où elles deviennent linéairement séparables. Les noyaux les plus couramment utilisés sont:
- Noyau linéaire: K(x, y) = x·y
- Noyau polynomial: K(x, y) = (γx·y + r)^d
- Noyau RBF (Radial Basis Function): K(x, y) = exp(-γ||x-y||²)
- Noyau sigmoïde: K(x, y) = tanh(γx·y + r)

Les performances des SVM dépendent de plusieurs paramètres clés:
- Le paramètre de régularisation C: contrôle le compromis entre la maximisation de la marge et la minimisation de l'erreur
- Les paramètres spécifiques au noyau choisi (γ, d, r)
- La stratégie pour gérer les problèmes multi-classes (approche "un-contre-tous" ou "un-contre-un")

Les SVM excellent dans de nombreux domaines:
- Reconnaissance d'images et classification de textes
- Détection de fraudes et d'anomalies
- [Bio-informatique](https://fr.wikipedia.org/wiki/Bio-informatique)
- Analyse de sentiments et traitement du langage naturel
- Diagnostic médical

**Avantages:**
- Efficacité dans les espaces de grande dimension
- Robustesse face au surapprentissage
- Flexibilité théorique grâce aux différents noyaux
- Fondement mathématique solide avec garantie de convergence

**Limites:**
- Complexité computationnelle élevée pour les grands jeux de données
- Difficulté d'interprétation du modèle final
- Nécessité d'un réglage précis des hyperparamètres
- Performances médiocres sur les très grands datasets