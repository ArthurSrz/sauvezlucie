---
title: La bibliothèque NumPy
type: concept
tags:
- Python Libraries
- Scientific Computing
- Data Analysis
- Machine Learning
- ndarray
- Multidimensional Arrays
- Array Manipulation
- Performance Optimization
- Data Science
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Frameworks Python pour le Deep Learning]]'
---
## Généralité

NumPy est une bibliothèque [Python](https://fr.wikipedia.org/wiki/Python_(langage)) fondamentale pour le calcul scientifique et la manipulation d'arrays multidimensionnels. Créée en 2006 par Travis Oliphant comme un projet [open source](https://fr.wikipedia.org/wiki/Open_source), elle est devenue un pilier de l'écosystème scientifique Python. NumPy repose sur des bibliothèques C et Fortran (notamment [BLAS](https://fr.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) et [LAPACK](https://fr.wikipedia.org/wiki/LAPACK)) pour optimiser les performances des opérations numériques.

## Points clés

- **Objet `ndarray`** : Tableau multidimensionnel homogène optimisé pour les calculs, permettant des opérations vectorisées significativement plus rapides que les listes Python standard
- **Fonctions mathématiques intégrées** : Opérations linéaires, [algèbre linéaire](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_lin%C3%A9aire), transformations de Fourier, génération de nombres aléatoires, et statistiques descriptives
- **Performance et interopérabilité** : Intègre des bibliothèques C/Fortran pour la vitesse et s'interface avec d'autres outils scientifiques comme [SciPy](https://fr.wikipedia.org/wiki/SciPy) et [pandas](https://fr.wikipedia.org/wiki/Pandas_(biblioth%C3%A8que_Python))

## Détails

NumPy est construit autour de l'objet `ndarray` ([N-dimensional array](https://fr.wikipedia.org/wiki/NumPy#Les_tableaux_NumPy)), un tableau à N dimensions contenant des éléments de même type. Ces tableaux supportent jusqu'à 32 dimensions (théoriquement illimitées) et divers types de données, offrant plusieurs avantages majeurs :

- **Homogénéité** : Tous les éléments partagent un type de données
- **Vectorisation** : Les opérations s'appliquent à l'ensemble des éléments sans boucles explicites
- **Efficacité mémoire** : Stockage compact et accès rapide grâce à une structure C sous-jacente

La bibliothèque inclut des centaines de fonctions mathématiques optimisées, notamment pour :

- **Algèbre linéaire** : Produit matriciel, décomposition [SVD](https://fr.wikipedia.org/wiki/D%C3%A9composition_en_valeurs_singuli%C3%A8res), inversion de matrices
- **Transformations** : Transformée de Fourier rapide, convolution
- **Statistiques** : Moyenne, médiane, variance, corrélations
- **Génération de données** : Nombres aléatoires, espaces linéaires, grilles

Les performances sont optimisées grâce à :

- **Vectorisation** : Exploite les opérations en C optimisées ([BLAS](https://fr.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms), OpenMP)
- **Mémoire partagée** : Utilise des vues pour éviter les copies inutiles
- **Interopérabilité** : Convertit facilement des données de pandas, MATLAB ou CSV

NumPy sert de base à de nombreuses autres bibliothèques scientifiques :

- **SciPy** : Extension pour l'analyse numérique
- **Pandas** : Structures de données comme les DataFrames
- **Librairies d'apprentissage automatique** : TensorFlow/PyTorch
- **Visualisation** : Matplotlib
- **Accélération matérielle** : Compatible avec Dask et Intel MKL

Exemple d'utilisation :