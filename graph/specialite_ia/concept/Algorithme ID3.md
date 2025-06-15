---
title: Algorithme ID3
type: concept
tags:
- algorithme
- ID3
- apprentissage supervisé
- arbre de décision
- Ross Quinlan
- entropie
- gain d'information
- classification
- machine learning
- data mining
date_creation: '2025-03-21'
date_modification: '2025-03-21'
isPartOf: '[[Arbre de décision]]'
precedes: '[[Algorithme C4.5]]'
---
## Généralité

L'[algorithme ID3](https://fr.wikipedia.org/wiki/ID3_(algorithme)) (Iterative Dichotomiser 3) est un algorithme d'[apprentissage supervisé](https://fr.wikipedia.org/wiki/Apprentissage_supervis%C3%A9) développé par [Ross Quinlan](https://fr.wikipedia.org/wiki/Ross_Quinlan) en 1986. Il s'agit d'une méthode fondamentale pour la construction d'[arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision), utilisée pour classer des instances en se basant sur leurs attributs.

## Points clés

- ID3 construit un arbre de décision de haut en bas en sélectionnant à chaque nœud l'attribut qui maximise le gain d'information
- L'algorithme utilise l'entropie comme mesure de l'impureté d'un ensemble de données
- ID3 est particulièrement efficace pour les attributs catégoriels et les problèmes de classification
- L'algorithme suit une approche gloutonne (greedy) sans backtracking
- ID3 a inspiré plusieurs algorithmes ultérieurs comme C4.5 et CART

## Détails

L'algorithme [ID3](https://fr.wikipedia.org/wiki/Algorithme_ID3) fonctionne de manière récursive en divisant l'ensemble de données en sous-ensembles de plus en plus homogènes. À chaque étape, il sélectionne l'attribut qui permet de réduire au maximum l'[entropie](https://fr.wikipedia.org/wiki/Entropie_de_Shannon) (ou augmenter le gain d'information) dans les sous-ensembles résultants.

L'entropie est une mesure de l'impureté ou du désordre dans un ensemble de données. Pour un ensemble S contenant des exemples de n classes différentes, l'entropie est calculée comme suit:

Entropie(S) = -Σ(p_i * log₂(p_i)) pour i de 1 à n

Le gain d'information pour un attribut A est calculé comme:

Gain(S, A) = Entropie(S) - Σ((|S_v|/|S|) * Entropie(S_v))

L'implémentation standard d'ID3 suit ces étapes précises:
1. Calculer l'entropie de l'ensemble de données actuel
2. Pour chaque attribut disponible, calculer le gain d'information
3. Sélectionner l'attribut avec le gain d'information maximal
4. Créer un nœud de décision basé sur cet attribut
5. Récursivement construire des sous-arbres pour chaque valeur de l'attribut
6. S'arrêter lorsque:
   - Tous les exemples d'un nœud appartiennent à la même classe
   - Il n'y a plus d'attributs disponibles
   - Tous les exemples restants ont les mêmes valeurs d'attribut

ID3 présente plusieurs limitations importantes:
- Biais en faveur des attributs avec de nombreuses valeurs distinctes
- Incapacité à traiter les attributs continus ou numériques sans discrétisation préalable
- Absence de mécanisme de traitement des valeurs manquantes
- Risque élevé de surapprentissage

Ces limitations ont conduit au développement de:
- [C4.5](https://fr.wikipedia.org/wiki/C4.5) qui introduit:
  - Le ratio de gain pour corriger le biais multi-valué
  - Le traitement des attributs continus
  - Des mécanismes d'élagage
- [CART](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision) qui:
  - Supporte classification et régression
  - Utilise l'indice de Gini
  - Implémente des techniques d'élagage sophistiquées

ID3 et ses dérivés sont largement utilisés dans divers domaines comme:
- **Le diagnostic médical**: Classification des maladies à partir de symptômes
- **L'analyse de risque financier**: Évaluation de la solvabilité des emprunteurs
- **La reconnaissance de formes**: Identification et classification d'objets dans des images
- **Les systèmes de recommandation**: Suggestion de produits ou contenus