---
title: Algorithmes génétiques pour l'optimisation combinatoire
type: concept
tags:
- algorithmes génétiques
- optimisation combinatoire
- bio-inspiration
- évolution
- recherche heuristique
- intelligence artificielle
- problèmes discrets
- métaheuristiques
date_creation: '2025-03-22'
date_modification: '2025-03-22'
subClassOf:
- '[[Algorithmes génétiques en IA]]'
- '[[Techniques bio-inspirées en IA]]'
---
## Généralité

Les algorithmes génétiques (AG) appliqués à l'optimisation combinatoire constituent une approche bio-inspirée pour résoudre des problèmes complexes où l'espace de recherche est discret et généralement très vaste. Basés sur les principes de l'évolution naturelle, ces algorithmes manipulent des populations de solutions candidates qui évoluent progressivement vers des solutions optimales ou quasi-optimales à travers des mécanismes de sélection, croisement et mutation.

## Points clés

- Les algorithmes génétiques permettent d'explorer efficacement des espaces de recherche vastes et discontinus où les méthodes exactes échouent
- Leur efficacité repose sur un équilibre entre exploration (diversification) et exploitation (intensification) de l'espace de recherche
- La conception du codage génétique et des opérateurs est cruciale et spécifique au problème d'optimisation combinatoire traité
- Les AG sont particulièrement adaptés aux problèmes NP-difficiles comme le voyageur de commerce, le problème du sac à dos ou l'ordonnancement

## Détails

L'application des algorithmes génétiques aux problèmes d'optimisation combinatoire nécessite plusieurs adaptations spécifiques. Le codage des solutions est la première étape critique : contrairement aux problèmes continus où un codage binaire ou réel peut suffire, les problèmes combinatoires requièrent souvent des représentations spécialisées comme des permutations, des ensembles ou des graphes.

Pour le problème du voyageur de commerce (TSP) par exemple, une solution est généralement codée comme une permutation des villes à visiter. Les opérateurs génétiques doivent alors préserver la validité des solutions : un croisement classique à un point ne fonctionne pas car il produirait des doublons ou des omissions de villes. Des opérateurs spécifiques comme le croisement OX (Order Crossover) ou PMX (Partially Mapped Crossover) ont été développés pour maintenir l'intégrité des permutations.

La fonction d'évaluation (fitness) quantifie la qualité des solutions et guide le processus évolutif. Pour le TSP, elle correspond typiquement à la distance totale parcourue. La sélection des individus pour la reproduction favorise les solutions de meilleure qualité tout en maintenant une diversité suffisante, souvent via des mécanismes comme la sélection par tournoi ou la sélection proportionnelle à la fitness.

Les contraintes inhérentes aux problèmes combinatoires peuvent être gérées soit par pénalisation dans la fonction fitness, soit par conception d'opérateurs qui produisent uniquement des solutions valides. Par exemple, dans un problème d'affectation de ressources, les contraintes de capacité peuvent être intégrées directement dans les opérateurs de croisement et mutation.

L'hybridation avec des méthodes de recherche locale (comme la recherche tabou ou le recuit simulé) a démontré son efficacité pour améliorer les performances des AG sur les problèmes combinatoires. Ces approches hybrides, parfois appelées algorithmes mémétiques, permettent d'intensifier la recherche dans des régions prometteuses identifiées par l'algorithme génétique.

Les paramètres comme la taille de population, les taux de croisement et mutation, et les critères d'arrêt doivent être soigneusement ajustés en fonction du problème. Des techniques d'auto-adaptation de ces paramètres pendant l'exécution peuvent améliorer la robustesse de l'algorithme face à différentes instances du problème.