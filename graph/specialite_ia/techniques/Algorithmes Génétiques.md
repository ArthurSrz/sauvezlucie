---
title: "Algorithmes Génétiques"
type: "technique"
tags: ["évolution", "optimisation", "métaheuristique", "sélection naturelle", "génétique"]
relations:
  - type: "rdfs:subClassOf"
    target: "[[Techniques de l'intelligence artificielle]]"
  - type: "rdfs:seeAlso"
    target: ["[[Approche exploratoires et de recherche d'espace]]", "[[Approches Hybrides en IA]]"]
---

## Généralité

Les algorithmes génétiques sont des méthodes d'optimisation s'inspirant des mécanismes de l'évolution biologique pour résoudre des problèmes complexes grâce à des processus de sélection, de croisement et de mutation.

## Points clés

- S'inspirent directement des principes de la sélection naturelle de Darwin
- Particulièrement efficaces pour explorer de vastes espaces de solutions
- Fonctionnent sans connaissance préalable du domaine du problème
- Utilisent des opérateurs de sélection, croisement et mutation pour faire évoluer les solutions

## Détails

Les algorithmes génétiques, développés initialement par John Holland dans les années 1960-1970, représentent une approche bio-inspirée de résolution de problèmes et d'optimisation. Ils appartiennent à la famille des métaheuristiques et s'avèrent particulièrement efficaces pour traiter des problèmes où l'espace de recherche est vaste, non linéaire, ou mal défini.

**Principe de fonctionnement:**

Le processus d'un algorithme génétique s'articule autour de plusieurs étapes clés, mimant le processus de l'évolution naturelle:

1. **Initialisation**: Création d'une population initiale d'individus (solutions potentielles) généralement de façon aléatoire.

2. **Évaluation**: Chaque individu est évalué selon une fonction d'aptitude (fitness) qui mesure sa qualité en tant que solution au problème posé.

3. **Sélection**: Les individus les plus performants sont sélectionnés pour la reproduction, avec une probabilité proportionnelle à leur fitness.

4. **Reproduction**: De nouveaux individus sont créés par:
   - **Croisement** (crossover): combinaison de fragments génétiques de deux parents
   - **Mutation**: modification aléatoire de certains gènes pour maintenir la diversité

5. **Remplacement**: La nouvelle génération remplace partiellement ou totalement l'ancienne.

Ces étapes sont répétées sur plusieurs générations jusqu'à ce qu'un critère d'arrêt soit atteint (nombre maximal de générations, convergence, seuil de fitness).

**Applications:**

Les algorithmes génétiques ont été appliqués avec succès dans de nombreux domaines:
- Optimisation de conception en ingénierie (aérodynamique, structures)
- Planification et ordonnancement (emplois du temps, logistique)
- Apprentissage automatique (optimisation d'hyperparamètres, feature selection)
- Finance (optimisation de portefeuille)
- Bioinformatique (alignement de séquences)
- Conception de jeux vidéo (génération procédurale, IA des PNJ)

Leur principal avantage réside dans leur capacité à explorer efficacement des espaces de recherche complexes sans nécessiter de connaissances spécifiques du domaine, tout en évitant souvent les minimums locaux qui piègent les méthodes d'optimisation traditionnelles.

## Liens complémentaires

### [[Programmation évolutionnaire]]
### [[Optimisation par essaims particulaires]]
### [[Approche exploratoires et de recherche d'espace]]
### [[Applications des algorithmes génétiques]]
