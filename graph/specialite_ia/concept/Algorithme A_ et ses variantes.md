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
isPartOf:
- '[[Algorithmes de recherche heuristique en IA]]'
- '[[Approches exploratoires et de recherche d''espace]]'
subClassOf: '[[Algorithmes de recherche heuristique en IA]]'
---
## Généralité

L'[algorithme A*](https://fr.wikipedia.org/wiki/Algorithme_A*) (prononcé "A étoile") est un algorithme de recherche de chemin qui combine les avantages de l'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) et des algorithmes de recherche heuristique. Développé en 1968 par Peter Hart, Nils Nilsson et Bertram Raphael, il est largement utilisé dans les domaines de l'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle), de la robotique et des jeux vidéo pour trouver le chemin optimal entre deux points dans un graphe.

## Points clés

- Utilise une fonction d'évaluation f(n) = g(n) + h(n) combinant coût réel et estimation heuristique
- Garantit un chemin optimal lorsque l'heuristique est admissible et cohérente
- Maintient deux ensembles de nœuds : liste ouverte (à explorer) et liste fermée (déjà explorés)
- Dispose de plusieurs variantes adaptées à différents contextes (IDA*, D*, ARA*)
- Large application dans les jeux vidéo, navigation GPS, robotique et systèmes autonomes

## Détails

A* maintient une liste ouverte de nœuds à explorer, triée par ordre croissant de la fonction d'évaluation f(n). À chaque itération, l'algorithme sélectionne le nœud avec la valeur f(n) la plus basse, l'examine, puis ajoute ses voisins à la liste ouverte.

L'algorithme utilise deux structures principales :
- **Liste ouverte** : File de priorité basée sur f(n), souvent implémentée avec un [tas binaire](https://fr.wikipedia.org/wiki/Tas_binaire)
- **Liste fermée** : Table de hachage contenant les nœuds déjà explorés

La fonction d'évaluation f(n) = g(n) + h(n) combine :
- g(n): le coût réel du chemin depuis le nœud de départ jusqu'au nœud n
- h(n): une estimation heuristique du coût pour atteindre la destination depuis n (distance [euclidienne](https://fr.wikipedia.org/wiki/Distance_euclidienne) ou de [Manhattan](https://fr.wikipedia.org/wiki/Distance_de_Manhattan))

Pour garantir l'optimalité :
- **Heuristique admissible** : Ne jamais surestimer le coût réel
- **Heuristique cohérente** : Respecte l'inégalité triangulaire h(n) ≤ c(n,n') + h(n')

Les principales variantes incluent :
- **[IDA*](https://fr.wikipedia.org/wiki/IDA*)** (Iterative Deepening A*) qui utilise moins de mémoire via des recherches en profondeur itératives
- **D*** conçu pour les environnements dynamiques
- **ARA*** qui trouve rapidement une solution initiale puis l'améliore progressivement
- **Weighted A*** utilisant une heuristique pondérée
- **Bidirectional A*** effectuant deux recherches simultanées

A* et ses variantes trouvent des applications dans :
- Jeux vidéo (Civilization, Starcraft)
- Robotique (rovers martiens)
- Systèmes GPS ([Google Maps](https://fr.wikipedia.org/wiki/Google_Maps), Waze)
- Véhicules autonomes (Tesla, Waymo)
- Systèmes d'aide à la décision (logistique, transport)

La complexité temporelle dans le pire cas est exponentielle (O(b^d)), mais réduite significativement avec une bonne heuristique.