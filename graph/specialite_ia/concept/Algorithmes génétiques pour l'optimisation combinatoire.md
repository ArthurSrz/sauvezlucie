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
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

Les [algorithmes génétiques](https://fr.wikipedia.org/wiki/Algorithme_g%C3%A9n%C3%A9tique) (AG) appliqués à l'[optimisation combinatoire](https://fr.wikipedia.org/wiki/Optimisation_combinatoire) constituent une approche bio-inspirée pour résoudre des problèmes complexes où l'espace de recherche est discret et généralement très vaste. Développés initialement par [John Holland](https://fr.wikipedia.org/wiki/John_Henry_Holland) dans les années 1970, ces algorithmes s'inspirent des principes de l'évolution naturelle selon Darwin.

## Points clés

- Les algorithmes génétiques permettent d'explorer efficacement des espaces de recherche vastes et discontinus où les méthodes exactes échouent
- Leur efficacité repose sur un équilibre entre exploration (diversification) et exploitation (intensification) de l'espace de recherche
- La conception du codage génétique et des opérateurs est cruciale et spécifique au problème d'optimisation combinatoire traité
- Les AG sont souvent appliqués aux problèmes [NP-difficiles](https://fr.wikipedia.org/wiki/Probl%C3%A8me_NP-difficile) comme le voyageur de commerce ou le problème du sac à dos
- Ils peuvent traiter certaines fonctions objectif non différentiables ou discontinues, avec une relative robustesse face au bruit

## Détails

Basés sur les mécanismes de sélection naturelle, de croisement (recombinaison) et de mutation, ces algorithmes manipulent des populations de solutions candidates (ou chromosomes) encodées dans une structure de données, généralement des chaînes binaires. À chaque génération, les solutions les plus performantes sont sélectionnées (par exemple via la méthode de la roulette biaisée ou le tournoi) puis recombinées pour produire une nouvelle génération de solutions.

Les AG se sont révélés particulièrement efficaces pour des problèmes NP-difficiles comme le [voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce), l'ordonnancement et la conception de circuits électroniques.

L'application aux problèmes d'optimisation combinatoire nécessite plusieurs adaptations:

- **Codage des solutions**: requiert souvent des représentations spécialisées comme des permutations, des ensembles ou des graphes. Pour le TSP, une solution est généralement codée comme une permutation des villes.

- **Opérateurs spécialisés**: comme le croisement OX (Order Crossover) ou PMX (Partially Mapped Crossover) qui doivent préserver l'intégrité des solutions. 

- **Fonction d'évaluation**: quantifie la qualité des solutions. Pour le TSP, c'est la distance totale parcourue, avec éventuelles pénalités pour contraintes supplémentaires.

- **Gestion des contraintes**: soit par pénalisation dans la fonction fitness, soit par conception d'opérateurs produisant uniquement des solutions valides.

Parmi les améliorations et variantes notables, on trouve:
- Les algorithmes mémétiques qui combinent AG avec des méthodes de recherche locale comme la [recherche tabou](https://fr.wikipedia.org/wiki/Recherche_tabou)
- L'auto-adaptation des paramètres (taille de population, taux de croisement et mutation)
- Les variantes comme les algorithmes génétiques à populations restreintes (CHC)

Les paramètres typiques incluent:
- Taille de population: généralement entre 50 et 500 individus
- Taux de croisement: 60-90%
- Taux de mutation: 0,5-1%