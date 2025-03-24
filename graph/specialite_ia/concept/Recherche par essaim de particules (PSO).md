---
title: Recherche par essaim de particules (PSO)
type: concept
tags:
- optimisation
- métaheuristique
- intelligence collective
- PSO
- algorithme
- biomimétisme
- intelligence artificielle
- optimisation globale
- Kennedy et Eberhart
date_creation: '2025-03-22'
date_modification: '2025-03-22'
subClassOf:
- '[[Techniques bio-inspirées en IA]]'
- '[[Algorithmes de recherche heuristique en IA]]'
isPartOf: '[[Entraînement d''un modèle d''IA]]'
---
## Généralité

La Recherche par Essaim de Particules (Particle Swarm Optimization ou PSO) est une technique d'optimisation métaheuristique inspirée par le comportement social des oiseaux en vol ou des bancs de poissons. Développée en 1995 par Kennedy et Eberhart, cette méthode simule l'intelligence collective d'un groupe d'agents simples (particules) qui se déplacent dans un espace de recherche multidimensionnel pour trouver une solution optimale à un problème d'optimisation.

## Points clés

- [Algorithme](https://fr.wikipedia.org/wiki/Algorithme) bio-inspiré qui exploite l'intelligence collective d'un groupe de particules pour explorer efficacement un espace de solutions
- Chaque particule ajuste sa position en fonction de sa propre expérience (meilleure position personnelle) et de l'expérience du groupe (meilleure position globale)
- Particulièrement efficace pour les problèmes d'optimisation non linéaires et dans les espaces de recherche continus
- Facile à implémenter avec peu de paramètres à ajuster (vitesse d'inertie, coefficients d'apprentissage personnel et social)
- [Converge](https://fr.wikipedia.org/wiki/Converge) généralement plus rapidement que d'autres algorithmes évolutionnaires pour de nombreux problèmes d'optimisation

## Détails

Le fonctionnement de PSO repose sur un ensemble de particules qui se déplacent dans l'espace de recherche. Chaque particule possède une position (représentant une solution candidate) et une vitesse (direction et amplitude du déplacement). À chaque itération, les particules ajustent leur trajectoire en fonction de deux informations principales:

1. **La meilleure position personnelle (pbest)**: la meilleure solution que la particule a trouvée jusqu'à présent
2. **La meilleure position globale (gbest)**: la meilleure solution trouvée par l'ensemble de l'essaim

La mise à jour de la vitesse de chaque particule est calculée selon l'équation:

```
v_i(t+1) = w*v_i(t) + c1*r1*(pbest_i - x_i(t)) + c2*r2*(gbest - x_i(t))
```

Où:
- w est le coefficient d'inertie
- c1 et c2 sont les coefficients d'apprentissage personnel et social
- r1 et r2 sont des nombres aléatoires entre 0 et 1
- x_i(t) est la position actuelle de la particule

La position est ensuite mise à jour par:

```
x_i(t+1) = x_i(t) + v_i(t+1)
```

L'algorithme PSO présente plusieurs variantes, notamment:

- **PSO avec topologie en anneau**: où chaque particule n'est influencée que par ses voisines immédiates
- **PSO avec coefficient d'inertie adaptatif**: où le coefficient d'inertie varie au cours de l'optimisation
- **PSO multi-essaims**: utilisant plusieurs sous-essaims qui évoluent indépendamment et échangent des informations périodiquement

Les applications de PSO sont nombreuses et variées, incluant l'optimisation de fonctions mathématiques, l'entraînement de réseaux de neurones, la planification de trajectoires robotiques, l'optimisation de portefeuilles financiers, et la conception de systèmes d'ingénierie complexes.

Comparé à d'autres algorithmes d'optimisation comme les algorithmes génétiques, PSO est généralement plus simple à implémenter et nécessite moins de paramètres à régler, tout en offrant une convergence rapide pour de nombreux problèmes pratiques.