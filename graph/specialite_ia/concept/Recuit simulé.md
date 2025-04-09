---
title: Recuit simulé
type: concept
tags:
- algorithme
- optimisation
- intelligence artificielle
- métaheuristique
- recherche opérationnelle
- simulation
date_creation: '2025-03-16'
date_modification: '2025-03-16'
isPartOf: '[[Approches exploratoires et de recherche d''espace]]'
---
## Généralité

Le [recuit simulé](https://fr.wikipedia.org/wiki/Recuit_simul%C3%A9) est une méthode d'optimisation stochastique inspirée du processus métallurgique de recuit, où un métal est chauffé puis refroidi lentement pour réduire ses défauts cristallins. En informatique, cette analogie est utilisée pour résoudre des problèmes d'optimisation complexes en permettant des solutions temporairement moins bonnes pour échapper aux minima locaux.

## Points clés

- Méthode d'[optimisation stochastique](https://fr.wikipedia.org/wiki/Optimisation_stochastique) inspirée d'un processus physique
- Capable d'échapper aux minima locaux grâce à l'acceptation probabiliste
- Contrôlé par un paramètre de température qui diminue progressivement
- Particulièrement efficace pour les problèmes [NP-difficiles](https://fr.wikipedia.org/wiki/Problème_NP-difficile)
- Applications étendues en optimisation combinatoire et au-delà

## Détails

### Principe de fonctionnement

Le recuit simulé simule le processus physique de recuit des métaux. L'algorithme commence avec une température élevée, permettant une large exploration de l'espace des solutions, puis la température diminue progressivement selon une loi de refroidissement.

À chaque itération :
1. Une solution voisine est générée aléatoirement
2. Si elle améliore la fonction objectif, elle est acceptée
3. Sinon, elle peut être acceptée avec probabilité exp(-ΔE/T)

### Algorithme de base

1. Initialiser une solution aléatoire S et température T
2. Tant que critère d'arrêt non atteint :
   - Pour N itérations à température constante :
     - Générer solution voisine S'
     - Calculer ΔE = f(S') - f(S)
     - Accepter selon critère de Metropolis
   - Réduire T selon schéma de refroidissement
3. Retourner meilleure solution trouvée

### Paramètres critiques

- Température initiale
- Schéma de refroidissement (géométrique, logarithmique, adaptatif)
- Fonction de voisinage
- Longueur de la [chaîne de Markov](https://fr.wikipedia.org/wiki/Cha%C3%AEne_de_Markov)
- Critère d'arrêt

### Applications

- [Problème du voyageur de commerce](https://fr.wikipedia.org/wiki/Problème_du_voyageur_de_commerce)
- Placement de circuits électroniques
- Ordonnancement de tâches
- Conception de réseaux
- [Repliement des protéines](https://fr.wikipedia.org/wiki/Repliement_des_prot%C3%A9ines)

### Avantages et inconvénients

**Avantages :**
- Simple à implémenter
- Traite fonctions non différentiables
- Peut échapper aux minima locaux
- Convergence garantie sous certaines conditions

**Inconvénients :**
- Convergence lente
- Résultats non reproductibles exactement
- Sensibilité au choix des paramètres
- Nécessite un réglage minutieux de la température initiale