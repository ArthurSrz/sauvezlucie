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
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

La [Recherche par Essaim de Particules](https://fr.wikipedia.org/wiki/Optimisation_par_essaim_particolaire) (Particle Swarm Optimization ou PSO) est une technique d'[optimisation métaheuristique](https://fr.wikipedia.org/wiki/M%C3%A9taheuristique) inspirée par le comportement social des oiseaux en vol ou des bancs de poissons. Développée en 1995 par James Kennedy et Russell Eberhart, cette méthode simule l'[intelligence collective](https://fr.wikipedia.org/wiki/Intelligence_collective) d'un groupe d'agents simples (particules) qui se déplacent dans un espace de recherche multidimensionnel pour trouver une solution optimale à un problème d'optimisation.

## Points clés

- [Algorithme bio-inspiré](https://fr.wikipedia.org/wiki/Algorithme_bio-inspir%C3%A9) qui exploite l'intelligence collective d'un groupe de particules, initialement inspiré par le comportement des oiseaux et bancs de poissons ([comportement stigmergique](https://fr.wikipedia.org/wiki/Stigmergie))
- Chaque particule ajuste sa position en fonction de sa propre expérience (meilleure position personnelle historique) et de l'expérience du groupe (meilleure position globale)
- Particulièrement efficace pour les problèmes d'optimisation non linéaires, non convexes et dans les espaces de recherche continus multidimensionnels
- Facile à implémenter avec peu de paramètres à ajuster (vitesse d'inertie ω, coefficients d'apprentissage personnel et social)
- Applications étendues dans divers domaines : conception aérodynamique, [réseaux de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels), planification de trajectoires, et arts génératifs

## Détails

Le fonctionnement de [PSO](https://fr.wikipedia.org/wiki/Optimisation_par_essaim_particulaire) repose sur un ensemble de particules qui se déplacent dans l'espace de recherche. Chaque particule possède une position (représentant une solution candidate) et une vitesse (direction et amplitude du déplacement). À chaque itération, les particules ajustent leur trajectoire en fonction de deux informations principales: la meilleure position personnelle (pbest) qui est la meilleure solution que la particule a trouvée jusqu'à présent, et la meilleure position globale (gbest) qui est la meilleure solution trouvée par l'ensemble de l'essaim.

La mise à jour de la vitesse de chaque particule est calculée selon l'équation: