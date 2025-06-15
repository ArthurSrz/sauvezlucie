---
title: Optimisation par essaim de lucioles
type: concept
tags:
- Optimisation
- Métaheuristique
- Algorithmes bio-inspirés
- Intelligence artificielle
- Recherche opérationnelle
- Firefly Algorithm
- Xin-She Yang
date_creation: '2025-04-03'
date_modification: '2025-04-04'
relatedTo: '[[Recherche par essaim de particules (PSO)]]'
subClassOf:
- '[[Approches exploratoires et de recherche d''espace]]'
- '[[Techniques bio-inspirées en IA]]'
---
## Généralité

L'[optimisation par essaim de lucioles](https://fr.wikipedia.org/wiki/Algorithme_des_lucioles) (Firefly Algorithm - FA) est une [métaheuristique](https://fr.wikipedia.org/wiki/M%C3%A9taheuristique) inspirée du comportement bioluminescent des lucioles. Développée par Xin-She Yang en 2008, cette méthode simule le comportement des lucioles dans la nature, un phénomène observé chez environ 2000 espèces de coléoptères [Lampyridae](https://fr.wikipedia.org/wiki/Lampyridae). Elle est utilisée pour résoudre des problèmes d'optimisation complexes dans divers domaines comme l'[ingénierie](https://fr.wikipedia.org/wiki/Ing%C3%A9nierie), l'informatique et la [recherche opérationnelle](https://fr.wikipedia.org/wiki/Recherche_op%C3%A9rationnelle).

## Points clés

- **Attraction lumineuse** : Les lucioles les plus brillantes attirent les autres (attraction proportionnelle à l'intensité lumineuse)
- **Décroissance avec distance** : L'attractivité diminue avec la distance suivant une loi exponentielle
- **Bioluminescence optimisée** : La luminosité est déterminée par la fonction objectif à optimiser
- **Efficacité prouvée** : Particulièrement efficace pour les problèmes non linéaires et multimodaux (comme la [fonction de Rastrigin](https://fr.wikipedia.org/wiki/Fonction_de_Rastrigin))
- **Variantes améliorées** : Existence de plusieurs versions adaptatives et hybrides de l'algorithme

## Détails

L'algorithme FA s'inspire de trois caractéristiques biologiques vérifiées : l'attraction proportionnelle à l'intensité lumineuse (coefficient généralement entre 0 et 1), l'attractivité qui diminue avec la distance (coefficient γ) et le mouvement aléatoire (paramètre α) avec complexité temporelle de O(n²) par itération.

Dans le domaine du génie électrique, l'algorithme a été utilisé pour l'optimisation de réseaux avec des résultats confirmés par des études de cas. En intelligence artificielle, son usage est documenté mais moins répandu, principalement pour l'apprentissage automatique. Des applications plus limitées existent aussi en économie pour la modélisation de systèmes complexes.

Plusieurs extensions ont été développées pour améliorer les performances : la FA avec attraction adaptative qui ajuste dynamiquement γ et α (amélioration de convergence de 15-25%), des versions hybrides combinées avec [PSO](https://fr.wikipedia.org/wiki/Optimisation_par_essaim_particulaire) ou [algorithmes génétiques](https://fr.wikipedia.org/wiki/Algorithme_g%C3%A9n%C3%A9tique), des approches multi-objectifs utilisant des techniques de pondération ou approches Pareto-front, la FA avec Lévy Flight qui remplace le mouvement aléatoire par des pas de [Lévy](https://fr.wikipedia.org/wiki/Processus_de_L%C3%A9vy), et des implémentations parallèles suivant les principes du [calcul parallèle](https://fr.wikipedia.org/wiki/Calcul_parall%C3%A8le).

D'après les études comparatives, l'algorithme montre une convergence 20-30% plus rapide que certains algorithmes sur des problèmes non linéaires, un meilleur évitement des optima locaux grâce à son mécanisme d'attraction aléatoire, bien que son efficacité relative dépende fortement du problème spécifique et des paramètres choisis.