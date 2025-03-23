---
title: Algorithmes de recherche heuristique en IA
type: concept
tags:
- intelligence artificielle
- algorithmes
- heuristique
- recherche
- optimisation
- IA
- résolution de problèmes
- informatique
date_creation: '2025-03-22'
date_modification: '2025-03-22'
rdfs:seeAlso: '[[Recherche par essaim de particules (PSO)]]'
rdfs:seeAlso: '[[Algorithme A* et ses variantes]]'
hasPart: '[[Algorithme A* et ses variantes]]'
rdfs:subClassOf: '[[Approches exploratoires et de recherche d''espace]]'
---

## Généralité

Les algorithmes de recherche heuristique sont des techniques fondamentales en intelligence artificielle qui permettent de trouver des solutions à des problèmes complexes en utilisant des connaissances ou des estimations pour guider la recherche. Contrairement aux algorithmes de recherche exhaustive, les méthodes heuristiques utilisent des "raccourcis" intelligents pour réduire l'espace de recherche et trouver des solutions acceptables plus rapidement, même si elles ne garantissent pas toujours l'optimalité.

## Points clés

- Les heuristiques sont des fonctions d'évaluation qui estiment la distance ou le coût pour atteindre un objectif depuis un état donné
- Les algorithmes heuristiques permettent de résoudre des problèmes dont l'espace de recherche est trop vaste pour une exploration exhaustive
- L'efficacité d'un algorithme heuristique dépend fortement de la qualité de sa fonction heuristique
- Les heuristiques admissibles (qui ne surestiment jamais le coût réel) garantissent l'optimalité dans certains algorithmes comme A*

## Détails

Les algorithmes de recherche heuristique sont essentiels pour résoudre des problèmes d'IA où l'espace de recherche est trop vaste pour être exploré de manière exhaustive. Ils utilisent des fonctions heuristiques qui fournissent une estimation du coût ou de la distance restante jusqu'à l'objectif.

L'algorithme A* est l'un des plus célèbres algorithmes de recherche heuristique. Il combine deux informations : le coût réel du chemin parcouru depuis l'état initial (g(n)) et une estimation heuristique du coût restant jusqu'à l'objectif (h(n)). La fonction d'évaluation totale f(n) = g(n) + h(n) permet de sélectionner le nœud le plus prometteur à explorer à chaque étape.

Pour qu'un algorithme comme A* garantisse de trouver la solution optimale, l'heuristique utilisée doit être admissible, c'est-à-dire qu'elle ne doit jamais surestimer le coût réel pour atteindre l'objectif. Une heuristique est également dite consistante (ou monotone) si son estimation est toujours inférieure ou égale au coût pour atteindre un nœud successeur plus l'estimation heuristique de ce successeur.

D'autres algorithmes heuristiques importants incluent :

- La recherche gloutonne (Greedy Best-First Search) : ne considère que l'heuristique h(n) pour choisir le prochain nœud à explorer
- La recherche à faisceau (Beam Search) : limite le nombre de nœuds explorés à chaque niveau
- L'algorithme IDA* (Iterative Deepening A*) : combine A* avec l'approfondissement itératif pour économiser la mémoire
- Les algorithmes génétiques : utilisent des principes inspirés de l'évolution pour explorer l'espace de recherche

Les domaines d'application des algorithmes heuristiques sont nombreux : planification de trajectoires pour les robots, jeux (échecs, Go), problèmes d'optimisation combinatoire (voyageur de commerce), planification automatique, et bien d'autres.

Le principal défi dans la conception d'un algorithme heuristique efficace réside dans la création d'une bonne fonction heuristique. Une heuristique trop simpliste peut conduire à explorer presque autant de nœuds qu'une recherche exhaustive, tandis qu'une heuristique trop complexe peut nécessiter trop de calculs pour être pratique.

## Applications pratiques

Les algorithmes de recherche heuristique sont utilisés dans les systèmes de navigation GPS, les jeux vidéo, la planification logistique, la conception de circuits intégrés, et de nombreux autres domaines où l'optimisation et la prise de décision automatisée sont nécessaires.