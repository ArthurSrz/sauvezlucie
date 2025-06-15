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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Arbre de décision]]'
---
## Généralité

[CHAID](https://fr.wikipedia.org/wiki/CHAID) (CHi-squared Automatic Interaction Detector) est une technique d'[analyse prédictive](https://fr.wikipedia.org/wiki/Analyse_pr%C3%A9dictive) et de segmentation qui appartient à la famille des [arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision). Développée par Gordon V. Kass en 1980, cette méthode permet d'identifier les relations entre variables catégorielles et de créer des segments homogènes en fonction de la variable cible.

## Points clés

- Spécialement conçu pour traiter des variables catégorielles (nominales ou ordinales), contrairement à d'autres algorithmes d'arbres de décision
- Utilise principalement le [test du chi-carré](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2) ou le test exact de Fisher pour déterminer les divisions optimales
- Peut produire des arbres à divisions multiples (non binaires), offrant une plus grande flexibilité
- Gère automatiquement les valeurs manquantes en les traitant comme une catégorie distincte
- Intègre un mécanisme de pré-élagage pour éviter le sur-apprentissage

## Détails

Le processus CHAID se déroule en trois étapes principales : fusion des catégories non significativement différentes, sélection du prédicteur ayant la plus forte interaction avec la variable cible pour créer une division, et arrêt lorsque aucune division significative ne peut être trouvée.

Les principaux avantages incluent une interprétabilité élevée des résultats, une gestion naturelle des valeurs manquantes, et la capacité à détecter automatiquement les interactions non linéaires. Cependant, la méthode présente des limites comme une performance réduite avec des variables continues, une sensibilité aux petits échantillons, et un risque de surapprentissage si les critères d'arrêt ne sont pas bien paramétrés.

Les applications pratiques de CHAID sont nombreuses : segmentation de clientèle en marketing, analyse de comportement d'achat, études socio-démographiques, évaluation des risques en assurance et banque, recherche médicale et épidémiologique, ainsi que dans les sciences sociales. Cette méthode est particulièrement utile dans les domaines où l'explicabilité prime sur la pure performance prédictive.