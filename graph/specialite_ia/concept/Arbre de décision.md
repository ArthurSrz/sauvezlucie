---
title: Arbre de décision
type: concept
tags:
- arbre de décision
- algorithme
- machine learning
- data science
- aide à la décision
- classification
- modèle prédictif
date_creation: '2025-03-22'
date_modification: '2025-03-22'
isPartOf:
- '[[Apprentissage automatique (Machine Learning)]]'
- '[[Apprentissage supervisé]]'
seeAlso: '[[Forêt d''arbres décisionnels IA]]'
hasPart:
- '[[Impureté de Gini, entropie et erreur de classification]]'
- '[[Algorithme ID3]]'
- '[[Algorithme C4.5]]'
- '[[CHAID (CHi-squared Automatic Interaction Detector) ]]'
---
##Généralité

Un arbre de décision est un modèle prédictif utilisé en apprentissage automatique et en statistiques qui représente les décisions et leurs conséquences possibles sous forme d'arbre. Cette structure hiérarchique permet de décomposer un problème complexe en une série de décisions plus simples, facilitant ainsi l'analyse et la prise de décision. Les arbres de décision sont particulièrement appréciés pour leur interprétabilité et leur capacité à modéliser des relations non linéaires entre variables.

## Points clés

- Structure intuitive composée de nœuds (tests sur les attributs), de branches (résultats des tests) et de feuilles (décisions finales ou prédictions)
- Algorithmes populaires incluent ID3, C4.5, CART et Random Forest (ensemble d'arbres de décision)
- Utilisable pour des tâches de classification (prédire une catégorie) et de régression (prédire une valeur numérique)
- Avantage majeur : facilité d'interprétation et de visualisation des règles de décision

## Détails

### Structure et terminologie

Un arbre de décision se compose de plusieurs éléments clés :
- **Nœud racine** : Point de départ de l'arbre, représentant l'attribut le plus discriminant
- **Nœuds internes** : Tests effectués sur des attributs spécifiques
- **Branches** : Résultats possibles des tests aux nœuds
- **Feuilles** : Nœuds terminaux représentant les décisions finales ou prédictions

### Principes de construction

La construction d'un arbre de décision repose sur la division récursive des données selon des critères d'homogénéité. Les algorithmes utilisent différentes mesures pour déterminer la meilleure division à chaque étape :
- **Entropie et gain d'information** : Utilisés par l'algorithme ID3
- **Indice de Gini** : Mesure d'impureté privilégiée par l'algorithme CART
- **Ratio de gain** : Amélioration du gain d'information utilisée par C4.5

Le processus s'arrête lorsque certaines conditions sont remplies, comme l'atteinte d'une profondeur maximale, un nombre minimal d'échantillons par feuille, ou une homogénéité suffisante.

### Avantages et limites

**Avantages :**
- Interprétabilité élevée : les règles de décision sont explicites et compréhensibles
- Peu de prétraitement des données nécessaire (pas de normalisation requise)
- Gestion naturelle des valeurs manquantes et des données catégorielles
- Capacité à capturer des relations non linéaires entre variables

**Limites :**
- Tendance au surapprentissage, particulièrement avec des arbres profonds
- Instabilité : de petites variations dans les données peuvent produire des arbres très différents
- Performance parfois inférieure à d'autres algorithmes plus complexes
- Difficulté à capturer certaines relations (comme les frontières de décision diagonales)

### Techniques d'amélioration

Pour surmonter certaines limitations, plusieurs techniques ont été développées :
- **[Élagage](https://fr.wikipedia.org/wiki/Élagage) (pruning)** : Réduction de la complexité de l'arbre pour éviter le surapprentissage
- **Ensembles d'arbres** : Combinaison de multiples arbres pour améliorer la robustesse et la précision
  - Random Forest : Utilise le bagging et la sélection aléatoire d'attributs
  - Gradient Boosting : Construction séquentielle d'arbres pour corriger les erreurs des précédents

### Applications pratiques

Les arbres de décision sont largement utilisés dans divers domaines :
- [Finance](https://fr.wikipedia.org/wiki/Finance) : évaluation des risques de crédit
- [Médecine](https://fr.wikipedia.org/wiki/Médecine) : aide au diagnostic
- Marketing : segmentation de clientèle
- Systèmes de recommandation
- Analyse de fiabilité et maintenance prédictive

Leur capacité à fournir des règles de décision claires en fait un outil précieux dans les contextes où l'interprétabilité est aussi importante que la précision des prédictions.