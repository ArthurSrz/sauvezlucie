---
title: Apprentissage par renforcement hiérarchique
type: concept
tags:
- Apprentissage par Renforcement
- ARH
- Tâches Hiérarchiques
- Optimisation de Décision
- Environnements Complexes
date_creation: '2025-04-08'
date_modification: '2025-04-09'
subClassOf: '[[Apprentissage par renforcement]]'
---
## Généralité

L'[apprentissage par renforcement hiérarchique](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement_hi%C3%A9rarchique) (ARH) est une approche avancée de l'[apprentissage par renforcement](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement) qui structure les tâches complexes en sous-tâches hiérarchiques organisées. Inspiré des travaux de [Richard S. Sutton](https://fr.wikipedia.org/wiki/Richard_S._Sutton) et [Andrew G. Barto](https://fr.wikipedia.org/wiki/Andrew_Barto), cette méthode permet de gérer des problèmes difficiles en les décomposant en tâches plus simples, facilitant ainsi l'apprentissage et l'optimisation des politiques de décision.

## Points clés

- **Décomposition hiérarchique** : Les tâches complexes sont décomposées en sous-tâches plus simples formant une [hiérarchie](https://fr.wikipedia.org/wiki/Hi%C3%A9rarchie), inspirée des travaux sur les options (actions temporellement étendues)
- **Structure duale** : Utilisation de macropolitiques (gestion des sous-tâches) et micropolitiques (actions locales), analogue aux principes de [modularité](https://fr.wikipedia.org/wiki/Modularit%C3%A9_(informatique))
- **Réutilisation de connaissances** : Les sous-tâches apprises peuvent être réutilisées via des mécanismes de [transfer learning](https://fr.wikipedia.org/wiki/Apprentissage_par_transfert)
- **Algorithmes modernes** : Implémentations comme [HiPPO](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement) et MAXQ combinant méta-apprentissage et adaptation dynamique
- **Applications variées** : Utilisation en [robotique](https://fr.wikipedia.org/wiki/Robotique), systèmes de recommandation et jeux comme le [jeu de Go](https://fr.wikipedia.org/wiki/Go_(jeu))

## Détails

### Structure Hiérarchique

La hiérarchie dans l'ARH est généralement représentée par un arbre où :
- Le nœud racine correspond à la tâche principale
- Les nœuds intermédiaires gèrent des sous-tâches abstraites
- Les nœuds feuilles représentent les actions primitives

Cette structure réduit la complexité computationnelle en limitant l'espace de recherche, avec des gains d'efficacité significatifs dans certains environnements simulés.

### Fonctionnement des Politiques

**Macropolitiques** :
- Déterminent la séquence de sous-tâches
- Opèrent à un niveau abstrait
- Choisissent les sous-tâches selon l'état environnemental

**Micropolitiques** :
- Gèrent les actions primitives
- Opèrent au sein de chaque sous-tâche
- Différentes granularités et horizons temporels

### Méthodes et Algorithmes

1. **Options Framework** (Sutton, Precup et Singh - 1999) :
   - Définit des politiques de sous-tâches avec points de départ/fin

2. **HIRO** :
   - Utilise des options pour apprendre des politiques hiérarchiques

3. **FeUdal Networks** ([Google DeepMind](https://fr.wikipedia.org/wiki/DeepMind) - 2017) :
   - Architecture neuronale hiérarchique multi-niveaux

4. **MAXQ** (Dietterich - 2000) :
   - Permet une réutilisation efficace des sous-tâches apprises

### Applications Concrètes

- **Robotique** :
  - Planification de mouvements complexes
  - Navigation et locomotion robotique

- **Jeux** :
  - Prise de décision à long terme
  - Stratégies complexes (ex: jeu de Go)

- **Systèmes intelligents** :
  - Personnalisation des recommandations
  - Gestion de processus décisionnels complexes

### Avantages Principaux

1. **Efficacité accrue** :
   - Réduction de l'espace d'états/actions
   - Convergence plus rapide dans certains cas

2. **Modularité** :
   - Séparation claire des responsabilités
   - Maintenance et évolution simplifiées

3. **Généralisation** :
   - Adaptation à des tâches similaires
   - Transfert de connaissances entre domaines

L'ARH combine donc puissance théorique et applicabilité pratique, avec des développements récents intégrant de plus en plus le méta-apprentissage pour une adaptabilité accrue.