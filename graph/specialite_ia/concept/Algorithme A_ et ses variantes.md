---
title: Algorithme A* et ses variantes
type: concept
tags:
- algorithme
- recherche de chemin
- A*
- intelligence artificielle
- optimisation
- graphes
- Dijkstra
- heuristique
- pathfinding
- informatique
date_creation: '2025-03-22'
date_modification: '2025-03-22'
isPartOf: '[[Algorithmes de recherche heuristique en IA]]'
rdfs:subClassOf: '[[Algorithmes de recherche heuristique en IA]]'
isPartOf: '[[Approches exploratoires et de recherche d''espace]]'
---

## Généralité

L'algorithme A* (prononcé "A étoile") est un algorithme de recherche de chemin qui combine les avantages de l'algorithme de Dijkstra et des algorithmes de recherche heuristique. Développé en 1968 par Peter Hart, Nils Nilsson et Bertram Raphael, A* est largement utilisé dans les domaines de l'intelligence artificielle, de la robotique et des jeux vidéo pour trouver le chemin optimal entre deux points dans un graphe. Sa popularité vient de son efficacité et de sa complétude, garantissant de trouver le chemin le plus court lorsqu'une heuristique admissible est utilisée.

## Points clés

- A* utilise une fonction d'évaluation f(n) = g(n) + h(n), où g(n) est le coût réel du chemin depuis le départ jusqu'au nœud n, et h(n) est une heuristique estimant le coût du chemin de n jusqu'à la destination
- L'algorithme est optimal lorsque l'heuristique est admissible (ne surestime jamais le coût réel) et cohérente (respecte l'inégalité triangulaire)
- Plusieurs variantes d'A* ont été développées pour améliorer ses performances dans différents contextes, comme IDA*, D*, ARA* et autres
- A* maintient deux ensembles de nœuds: une liste ouverte (nœuds à explorer) et une liste fermée (nœuds déjà explorés)

## Détails

### Fonctionnement de base d'A*

A* maintient une liste ouverte de nœuds à explorer, triée par ordre croissant de la fonction d'évaluation f(n). À chaque itération, l'algorithme sélectionne le nœud avec la valeur f(n) la plus basse, l'examine, puis ajoute ses voisins à la liste ouverte s'ils n'y sont pas déjà ou s'ils peuvent être atteints par un chemin moins coûteux.

La fonction d'évaluation f(n) = g(n) + h(n) combine:
- g(n): le coût réel du chemin depuis le nœud de départ jusqu'au nœud n
- h(n): une estimation heuristique du coût pour atteindre la destination depuis n

### Principales variantes d'A*

1. **IDA* (Iterative Deepening A*)**: Utilise moins de mémoire en effectuant des recherches en profondeur itératives avec des limites de coût croissantes. Particulièrement utile pour les problèmes avec un grand espace d'états.

2. **D* (Dynamic A*)**: Conçu pour la planification de chemin dans des environnements dynamiques où les coûts peuvent changer. Très utilisé en robotique mobile.

3. **ARA* (Anytime Repairing A*)**: Un algorithme "anytime" qui trouve rapidement une solution initiale, puis l'améliore progressivement si du temps supplémentaire est disponible.

4. **Weighted A***: Utilise une heuristique pondérée (w × h(n)) pour accélérer la recherche au détriment de l'optimalité. Plus w est grand, plus la recherche est rapide mais moins optimale.

5. **Bidirectional A***: Effectue deux recherches simultanées, une depuis le point de départ et une depuis la destination, pour accélérer la découverte du chemin.

### Applications

A* et ses variantes sont largement utilisés dans:
- Les jeux vidéo pour la navigation des personnages
- La robotique pour la planification de trajectoires
- Les systèmes GPS et de navigation
- La planification de missions pour les véhicules autonomes
- Les systèmes d'aide à la décision

Le choix de la variante appropriée dépend des contraintes spécifiques du problème, comme les limitations de mémoire, les exigences de temps réel, ou la nature dynamique de l'environnement.