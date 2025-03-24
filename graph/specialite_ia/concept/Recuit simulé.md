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
##Généralité

Le recuit simulé est une méthode d'optimisation stochastique inspirée du processus métallurgique de recuit, où un métal est chauffé puis refroidi lentement pour réduire ses défauts. En informatique, cette technique permet de résoudre des problèmes d'optimisation combinatoire complexes en évitant les minimums locaux. Contrairement aux méthodes de descente de gradient classiques, le recuit simulé accepte occasionnellement des solutions qui dégradent temporairement la fonction objectif, ce qui lui permet d'explorer plus largement l'espace des solutions.

## Points clés

- Méthode d'optimisation stochastique inspirée d'un processus physique de métallurgie
- Capable d'échapper aux minimums locaux grâce à l'acceptation probabiliste de solutions moins bonnes
- Contrôlé par un paramètre de température qui diminue progressivement, réduisant la probabilité d'accepter des solutions dégradantes
- Particulièrement efficace pour les problèmes NP-difficiles comme le voyageur de commerce ou le placement de circuits

## Détails

### Principe de fonctionnement

Le recuit simulé fonctionne en simulant le processus physique de recuit des métaux. L'algorithme commence avec une température élevée, permettant d'explorer largement l'espace des solutions, puis la température diminue progressivement, favorisant l'exploitation locale et la convergence vers un optimum.

À chaque itération, une solution voisine de la solution courante est générée aléatoirement. Si cette nouvelle solution améliore la fonction objectif, elle est automatiquement acceptée. Si elle la dégrade, elle peut néanmoins être acceptée avec une probabilité qui dépend de :
- L'ampleur de la dégradation
- La température actuelle

Cette probabilité est généralement calculée selon la formule de Metropolis : P(accepter) = exp(-ΔE/T), où ΔE représente la différence d'énergie (ou de coût) entre les deux solutions et T la température.

### [Algorithme](https://fr.wikipedia.org/wiki/Algorithme) de base

1. Initialiser une solution aléatoire S et une température initiale T élevée
2. Tant que le critère d'arrêt n'est pas atteint :
   - Générer une solution voisine S'
   - Calculer ΔE = f(S') - f(S) où f est la fonction objectif
   - Si ΔE < 0 (amélioration), accepter S' comme nouvelle solution courante
   - [Sinon](https://fr.wikipedia.org/wiki/Sinon), accepter S' avec une probabilité exp(-ΔE/T)
   - Réduire la température T selon un schéma de refroidissement prédéfini
3. Retourner la meilleure solution trouvée

### Paramètres critiques

Le succès du recuit simulé dépend fortement de plusieurs paramètres :
- La température initiale (suffisamment élevée pour explorer l'espace)
- Le schéma de refroidissement (linéaire, géométrique, adaptatif)
- La fonction de voisinage (génération de solutions proches)
- Le critère d'arrêt (nombre d'itérations, température minimale)

### Applications

Le recuit simulé est particulièrement adapté aux problèmes d'optimisation combinatoire difficiles :
- Problème du voyageur de commerce
- Placement de circuits électroniques
- Ordonnancement de tâches
- Conception de réseaux
- Problèmes d'allocation de ressources

### Avantages et inconvénients

**Avantages :**
- Simple à implémenter
- Capable de traiter des fonctions objectif non différentiables ou discontinues
- Peut échapper aux minimums locaux

**Inconvénients :**
- Convergence lente par rapport à certaines méthodes déterministes
- Résultats non reproductibles (nature stochastique)
- Sensible au réglage des paramètres

Le recuit simulé reste une méthode de référence pour l'optimisation globale et continue d'inspirer de nombreuses variantes et hybridations avec d'autres techniques d'optimisation.