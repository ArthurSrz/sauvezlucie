---
title: Optimisation par mimétisme bactérien
type: concept
tags:
- optimisation
- algorithmes bio-inspirés
- intelligence artificielle
- recherche opérationnelle
- modélisation biologique
- ingénierie
- finance
date_creation: '2025-04-03'
date_modification: '2025-04-04'
relatedTo: '[[Optimisation stigmergique : modélisation des comportements collectifs
  dans les systèmes complexes]]'
seeAlso: '[[Algorithmes de recherche heuristique en IA]]'
subClassOf:
- '[[Techniques bio-inspirées en IA]]'
- '[[Approches exploratoires et de recherche d''espace]]'
---
## Généralité

L'[optimisation par mimétisme bactérien](https://fr.wikipedia.org/wiki/Optimisation_par_colonie_de_bact%C3%A9ries) (Bacterial Foraging Optimization - BFO) est un algorithme d'optimisation inspirationnelle développé en 2002 par Kevin M. Passino. Il s'inspire du comportement collectif des bactéries [Escherichia coli](https://fr.wikipedia.org/wiki/Escherichia_coli), notamment leur capacité à chercher de la nourriture (chimiotaxie) et à éviter les substances nocives (répulsion chimique). Cette méthode métaheuristique appartient à la famille des algorithmes d'optimisation par essaims et est particulièrement adaptée aux problèmes d'optimisation non linéaires et multimodaux.

## Points clés

- **Inspiration biologique** : Basé sur le comportement de recherche de nourriture des bactéries *[E. coli](https://fr.wikipedia.org/wiki/Escherichia_coli)* et leur stratégie de [chimiotaxie](https://fr.wikipedia.org/wiki/Chimiotaxie)
- **Trois mécanismes principaux** : 
  - Chimiotaxie (mouvement vers les nutriments)
  - Reproduction (sélection des bactéries les plus performantes)
  - Élimination-dispersion (événements probabilistes pour éviter les optima locaux)
- **Applications majeures** :
  - [Ingénierie](https://fr.wikipedia.org/wiki/Ing%C3%A9nierie) (conception de réseaux électriques)
  - [Finance](https://fr.wikipedia.org/wiki/Finance) (optimisation de portefeuilles)
  - [Intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) (paramétrage de réseaux de neurones)

## Détails

L'algorithme [BFO](https://fr.wikipedia.org/wiki/Optimisation_par_forage_bact%C3%A9rien) simule le processus de recherche de nourriture des bactéries avec trois étapes clés :

1. **Chimiotaxie** :  
   Les bactéries se déplacent en alternant mouvements linéaires ("course") et rotations aléatoires ("tumbling") pour maximiser leur découverte de nutriments. Ce comportement est modélisé mathématiquement pour converger vers des solutions optimales.

2. **Reproduction** :  
   Les individus les plus performants (ayant trouvé de meilleures solutions) se reproduisent, tandis que les moins performants sont éliminés. Ce processus de [sélection naturelle](https://fr.wikipedia.org/wiki/S%C3%A9lection_naturelle) est analogue à la fitness dans les algorithmes génétiques.

3. **Élimination-dispersion** :  
   Certaines bactéries sont éliminées ou dispersées aléatoirement selon un mécanisme probabiliste, ce qui permet d'éviter la stagnation dans des optima locaux.

Dans le domaine de l'ingénierie, ce modèle est utilisé pour optimiser la conception de systèmes mécaniques ou électriques, notamment pour réduire les pertes énergétiques dans les réseaux électriques. En finance, il sert à l'optimisation de portefeuilles et à la gestion des risques, pour calibrer des modèles financiers complexes. Pour les réseaux neuronaux, il permet l'ajustement des poids dans les modèles d'apprentissage automatique.

Des versions hybrides de BFO ont été développées pour améliorer ses performances, notamment :
- **BFO-GA** : Combinaison avec des [algorithmes génétiques](https://fr.wikipedia.org/wiki/Algorithme_g%C3%A9n%C3%A9tique)
- **BFO-PSO** : Hybridation avec l'[optimisation par essaims particulaires](https://fr.wikipedia.org/wiki/Optimisation_par_essaim_particulaire) (PSO)
- **Adaptive BFO** : Version avec des pas de déplacement adaptatifs
- **mBFO** : Version modifiée avec mécanisme de chimiotaxie amélioré
- **Quantum-inspired BFO** : Utilisant des principes de calcul quantique

Parmi ses principaux avantages, on note sa robustesse face aux bruits et perturbations, sa capacité à explorer efficacement un large espace de recherche et son adaptabilité à différents types de problèmes d'optimisation. Cependant, l'algorithme présente certaines limites comme un temps de calcul potentiellement élevé pour des problèmes complexes, des paramètres sensibles nécessitant un calibrage précis, et une efficacité moindre que certaines métaheuristiques modernes pour les problèmes à très haute dimension.