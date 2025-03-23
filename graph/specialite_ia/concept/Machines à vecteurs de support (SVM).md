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
date_creation: '2025-03-17'
date_modification: '2025-03-17'
rdfs:subClassOf: '[[Algorithme de classification]]'
isPartOf: '[[Apprentissage supervisé]]'
hasPart: '[[Apprentissage profond (Deep Learning)]]'
---

##Généralité

Les Machines à Vecteurs de Support (SVM) constituent une famille d'algorithmes d'apprentissage supervisé particulièrement efficaces pour la classification et la régression. Développées initialement par Vladimir Vapnik dans les années 1990, les SVM cherchent à trouver l'hyperplan optimal qui sépare les données en différentes classes tout en maximisant la marge entre ces classes. Cette approche leur confère une excellente capacité de généralisation, même avec des ensembles de données relativement petits.

## Points clés

- Les SVM trouvent l'hyperplan optimal qui maximise la marge entre les classes, offrant ainsi une meilleure généralisation
- Grâce à l'astuce du noyau (kernel trick), les SVM peuvent résoudre efficacement des problèmes non-linéaires
- Les SVM sont moins sensibles au surapprentissage que d'autres algorithmes, particulièrement dans les espaces de grande dimension
- Ils sont particulièrement performants pour les problèmes de classification binaire, mais peuvent être étendus à la classification multi-classes

## Détails

### Principe fondamental

Le principe fondamental des SVM repose sur la recherche d'un hyperplan séparateur qui maximise la distance (marge) avec les points les plus proches de chaque classe, appelés vecteurs de support. Mathématiquement, cela revient à résoudre un problème d'optimisation quadratique sous contraintes.

Pour un problème de classification binaire avec des données linéairement séparables, l'équation de l'hyperplan est donnée par:
w·x + b = 0, où w est le vecteur normal à l'hyperplan, b est le biais, et x représente les données.

### L'astuce du noyau (Kernel Trick)

L'une des forces majeures des SVM réside dans leur capacité à traiter des problèmes non-linéaires grâce à l'astuce du noyau. Cette technique permet de projeter implicitement les données dans un espace de dimension supérieure où elles deviennent linéairement séparables, sans calculer explicitement cette transformation coûteuse.

Les noyaux les plus couramment utilisés sont:
- Noyau linéaire: K(x, y) = x·y
- Noyau polynomial: K(x, y) = (γx·y + r)^d
- Noyau RBF (Radial Basis Function): K(x, y) = exp(-γ||x-y||²)
- Noyau sigmoïde: K(x, y) = tanh(γx·y + r)

### Paramètres importants

Les performances des SVM dépendent de plusieurs paramètres clés:
- Le paramètre de régularisation C: contrôle le compromis entre la maximisation de la marge et la minimisation de l'erreur de classification
- Les paramètres spécifiques au noyau choisi (γ, d, r)
- La stratégie pour gérer les problèmes multi-classes (one-vs-one, one-vs-rest)

### Applications

Les SVM excellent dans de nombreux domaines:
- Reconnaissance d'images et classification de textes
- Détection de fraudes et d'anomalies
- Bio-informatique (classification de protéines, prédiction de structure)
- Analyse de sentiments et traitement du langage naturel

### Avantages et limites

**Avantages:**
- Efficacité dans les espaces de grande dimension
- Robustesse face au surapprentissage
- Flexibilité grâce aux différents noyaux disponibles

**Limites:**
- Complexité computationnelle élevée pour les grands jeux de données (O(n²) à O(n³))
- Difficulté d'interprétation du modèle final, particulièrement avec des noyaux non-linéaires
- Nécessité d'un réglage précis des hyperparamètres

Les SVM restent un outil puissant dans l'arsenal des data scientists, offrant souvent d'excellentes performances lorsqu'une séparation claire entre classes est recherchée.