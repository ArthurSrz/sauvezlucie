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
date_creation: '2025-03-28'
date_modification: '2025-03-28'
seeAlso:
- '[[Recherche par essaim de particules (PSO)]]'
- '[[Algorithme A* et ses variantes]]'
hasPart: '[[Algorithme A* et ses variantes]]'
subClassOf: '[[Approches exploratoires et de recherche d''espace]]'
isPartOf: '[[Exploration vs exploitation dans l''apprentissage par renforcement]]'
---
## Généralité

Les algorithmes de [recherche heuristique](https://fr.wikipedia.org/wiki/Heuristique) sont des techniques fondamentales en [intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) qui permettent de trouver des solutions à des problèmes complexes en utilisant des connaissances ou des estimations pour guider la recherche. Contrairement aux algorithmes de recherche exhaustive, ces méthodes utilisent des "raccourcis" intelligents pour réduire l'espace de recherche et trouver des solutions acceptables plus rapidement, même si elles ne garantissent pas toujours l'optimalité.

## Points clés

- Utilisation de fonctions heuristiques qui fournissent une estimation du coût restant pour atteindre un objectif (comme la distance euclidienne dans le problème du [voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce))
- Compromis entre qualité de solution et temps de calcul, particulièrement utile dans des domaines comme la planification de trajectoires ou la résolution de jeux
- L'algorithme [A*](https://fr.wikipedia.org/wiki/Algorithme_A*) est un exemple célèbre qui combine le coût réel du chemin parcouru (g(n)) et une estimation heuristique du coût restant (h(n))
- Importance cruciale de la qualité de la fonction heuristique : plus elle est proche du coût réel (sans jamais le dépasser pour les heuristiques admissibles), meilleures sont les performances
- Applications variées allant des systèmes de navigation GPS aux jeux intelligents et à l'optimisation combinatoire

## Détails

Les fonctions heuristiques sont des fonctions d'évaluation qui estiment la distance ou le coût pour atteindre un objectif depuis un état donné. On distingue les heuristiques locales (basées sur l'état immédiat) et les heuristiques globales (qui considèrent l'ensemble du problème). Pour qu'un algorithme comme A* garantisse de trouver la solution optimale, l'heuristique utilisée doit être admissible (ne surestimer jamais le coût réel) et consistante (monotone). Une heuristique admissible classique est la distance en ligne droite pour les problèmes de cheminement.

Les principaux algorithmes incluent :
- **Algorithme A*** : Développé en 1968 par Peter Hart, Nils Nilsson et Bertram Raphael, il combine les informations g(n) et h(n) via la fonction f(n) = g(n) + h(n). Il est complet et optimal avec une heuristique admissible et consistante.
- **Recherche gloutonne (Greedy Best-First Search)** : Ne considère que l'heuristique h(n) pour choisir le prochain nœud à explorer. Plus rapide mais ne garantit pas l'optimalité.
- **Recherche à faisceau (Beam Search)** : Limite le nombre de nœuds explorés à chaque niveau à un nombre fixe ("faisceau"), réduisant la consommation mémoire.
- **IDA* (Iterative Deepening A*)** : Combinaison de A* avec l'approfondissement itératif pour économiser la mémoire.
- **Algorithmes génétiques** : Inspirés des mécanismes de l'évolution biologique (sélection, croisement, mutation).

Les applications pratiques sont nombreuses :
- **Systèmes de navigation GPS** : Utilisation d'A* pour calculer les itinéraires optimaux, combinant les avantages de [Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) et des approches gloutonnes.
- **IA dans les jeux** : Algorithmes comme [Minimax](https://fr.wikipedia.org/wiki/Algorithme_minimax) avec élagage alpha-bêta pour les jeux de stratégie.
- **Planification logistique** : Résolution des problèmes de voyageur de commerce avec des métaheuristiques (algorithmes génétiques, recuit simulé).
- **Diagnostic médical assisté** : Approches heuristiques pour évaluer les probabilités de diagnostics.
- **Optimisation des réseaux** : Conception et optimisation d'infrastructures télécoms.

Les limitations principales incluent le fait que les algorithmes heuristiques n'offrent pas toujours l'optimalité absolue, particulièrement dans les cas de problèmes complexes. Leur efficacité dépend fortement de la qualité de la fonction heuristique choisie. Un compromis doit être trouvé entre la précision de l'estimation et le coût de calcul de l'heuristique.