---
title: 'CHAID (CHi-squared Automatic Interaction Detector) '
type: concept
tags:
- CHAID
- arbres de décision
- analyse prédictive
- segmentation
- chi-carré
- statistiques
- data mining
- Gordon V. Kass
- variables catégorielles
- classification
date_creation: '2025-03-21'
date_modification: '2025-03-21'
isPartOf: '[[Arbre de décision]]'
---
## Généralité

[CHAID](https://fr.wikipedia.org/wiki/CHAID) (CHi-squared Automatic Interaction Detector) est une technique d'analyse prédictive et de segmentation qui appartient à la famille des arbres de décision. Développée par Gordon V. Kass en 1980, cette méthode permet d'identifier les relations entre variables catégorielles et de créer des segments homogènes en fonction de la variable cible. CHAID utilise le test du chi-carré (χ²) comme critère statistique pour déterminer les meilleures divisions dans l'arbre, ce qui le rend particulièrement adapté aux variables qualitatives.

## Points clés

- CHAID est spécialement conçu pour traiter des variables catégorielles (nominales ou ordinales), contrairement à d'autres algorithmes d'arbres de décision qui privilégient les variables continues
- L'algorithme utilise le test du chi-carré pour évaluer l'indépendance entre variables et déterminer les divisions optimales
- CHAID peut produire des arbres à divisions multiples (non binaires), où un nœud peut se diviser en plus de deux branches
- Particulièrement utilisé en marketing, études de marché et sciences sociales pour la segmentation de population

## Détails

### Fonctionnement de l'algorithme

Le processus CHAID se déroule en trois étapes principales :

1. **Fusion** : Pour chaque prédicteur, l'algorithme regroupe les catégories non significativement différentes par rapport à la variable cible. Cette étape réduit la complexité en fusionnant les catégories similaires.

2. **Division** : CHAID sélectionne le prédicteur ayant la plus forte interaction avec la variable cible (selon la p-value du test du chi-carré) pour créer une division.

3. **Arrêt** : Le processus continue récursivement sur chaque [sous-groupe](https://fr.wikipedia.org/wiki/sous-groupe) jusqu'à ce qu'aucune division significative ne puisse être trouvée ou que les critères d'arrêt soient atteints (profondeur maximale, taille minimale des nœuds, etc.).

### Avantages et limites

**Avantages :**
- Interprétabilité élevée des résultats, facilement visualisables sous forme d'arbre
- Gestion naturelle des valeurs manquantes, qui peuvent être traitées comme une catégorie distincte
- Capacité à détecter automatiquement les interactions non linéaires entre variables
- Production de segments mutuellement exclusifs et exhaustifs

**Limites :**
- Moins performant avec des variables continues (nécessite une discrétisation préalable)
- Sensibilité aux petits échantillons où le test du chi-carré peut être moins fiable
- [Risque](https://fr.wikipedia.org/wiki/Risque) de surapprentissage si les critères d'arrêt ne sont pas bien paramétrés
- Instabilité potentielle : de petits changements dans les données peuvent produire des arbres très différents

### Applications pratiques

CHAID est largement utilisé dans :
- La segmentation de clientèle en marketing
- L'analyse de comportement d'achat
- Les études socio-démographiques
- L'évaluation des risques en assurance
- La recherche médicale pour identifier les facteurs de risque

Sa capacité à produire des segments facilement interprétables en fait un outil précieux pour les analyses exploratoires et la prise de décision basée sur des données catégorielles.