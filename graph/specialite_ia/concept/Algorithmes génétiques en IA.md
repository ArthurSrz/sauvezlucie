---
title: Algorithmes génétiques en IA
type: concept
tags:
- intelligence artificielle
- algorithmes génétiques
- optimisation
- John Holland
- évolution
- sélection naturelle
- algorithmes évolutionnaires
- recherche
date_creation: '2025-03-29'
date_modification: '2025-03-29'
relatedTo: '[[Apprentissage automatique (Machine Learning)]]'
subClassOf: '[[Techniques bio-inspirées en IA]]'
seeAlso: '[[Algorithmes génétiques pour l''optimisation combinatoire]]'
isPartOf: '[[Distillation de connaissances en IA]]'
---
## Généralité

Les algorithmes génétiques (AG) sont des méthodes d'optimisation et de recherche inspirées par le processus d'évolution naturelle et la sélection naturelle. Développés initialement par John Holland dans les années 1970, ces algorithmes appartiennent à la famille plus large des algorithmes évolutionnaires en intelligence artificielle. Ils utilisent des mécanismes biologiques comme la sélection, le croisement et la mutation pour faire évoluer une population de solutions candidates vers une solution optimale ou proche de l'optimale pour un problème donné.

## Points clés

- Les algorithmes génétiques s'inspirent de la théorie de l'évolution de Darwin pour résoudre des problèmes d'optimisation complexes
- Ils opèrent sur une population de solutions potentielles qui évoluent à travers des générations successives
- Les trois opérateurs principaux sont la sélection (choix des individus les plus adaptés), le croisement (combinaison de solutions) et la mutation (introduction de variations aléatoires)
- Particulièrement efficaces pour explorer de vastes espaces de recherche où les méthodes traditionnelles échouent

## Détails

### Structure et fonctionnement

Un algorithme génétique typique fonctionne selon les étapes suivantes:

1. **Initialisation**: Création d'une population initiale de solutions candidates (individus) généralement de façon aléatoire.
2. **[Évaluation](https://fr.wikipedia.org/wiki/Évaluation)**: Calcul de la valeur d'adaptation (fitness) de chaque individu selon une fonction objectif.
3. **Sélection**: Choix des individus qui participeront à la reproduction, avec une probabilité proportionnelle à leur fitness.
4. **Croisement**: Combinaison de paires d'individus pour créer de nouveaux individus (enfants).
5. **Mutation**: Modification aléatoire de certains gènes pour maintenir la diversité génétique.
6. **Remplacement**: Formation d'une nouvelle génération à partir des enfants et éventuellement de certains parents.
7. **Itération**: Répétition des étapes 2 à 6 jusqu'à atteindre un critère d'arrêt.

### Représentation génétique

Les solutions sont encodées sous forme de "chromosomes", généralement des chaînes binaires, des nombres réels, des permutations ou des structures de données plus complexes selon le problème. Chaque élément du chromosome est appelé "gène" et représente une caractéristique de la solution.

### Applications en IA

Les algorithmes génétiques sont utilisés dans de nombreux domaines de l'IA:

- **Apprentissage automatique**: Optimisation des hyperparamètres des modèles
- **Réseaux de neurones**: Détermination des poids et de l'architecture optimale
- **[Planification](https://fr.wikipedia.org/wiki/Planification) et ordonnancement**: Résolution de problèmes comme le voyageur de commerce
- **Conception assistée par ordinateur**: Optimisation de structures et de systèmes
- **[Robotique](https://fr.wikipedia.org/wiki/Robotique)**: Développement de comportements adaptatifs et évolutifs

### Avantages et limitations

**Avantages**:
- Capacité à traiter des problèmes avec des espaces de recherche vastes et complexes
- Robustesse face aux optima locaux
- Parallélisation naturelle du processus de recherche

**Limitations**:
- Difficulté à définir une fonction de fitness appropriée
- Convergence parfois prématurée vers des solutions sous-optimales
- Coût computationnel potentiellement élevé pour certains problèmes

Les algorithmes génétiques continuent d'évoluer avec des variantes comme les stratégies d'évolution, la programmation génétique et les algorithmes à estimation de distribution, élargissant encore leur champ d'application en intelligence artificielle.