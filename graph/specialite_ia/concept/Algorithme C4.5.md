---
title: Algorithme C4.5
type: concept
tags:
- machine learning
- arbres de décision
- data mining
- Ross Quinlan
- apprentissage supervisé
- intelligence artificielle
- entropie
- algorithmes
date_creation: '2025-04-08'
date_modification: '2025-04-08'
follows: '[[Algorithme ID3]]'
isPartOf: '[[Arbre de décision]]'
hasPart: '[[Causalité et inférence causale]]'
---
## Généralité

L'algorithme [C4.5](https://fr.wikipedia.org/wiki/C4.5) est une extension de l'algorithme [ID3](https://fr.wikipedia.org/wiki/Algorithme_ID3), développé par Ross Quinlan en 1993 pour générer des [arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision). Il s'agit d'un algorithme d'apprentissage supervisé largement utilisé dans le domaine du [data mining](https://fr.wikipedia.org/wiki/Exploration_de_donn%C3%A9es) et de l'intelligence artificielle, particulièrement apprécié pour sa capacité à traiter des problèmes de classification complexes.

## Points clés

- Extension majeure de l'algorithme ID3 avec gestion des attributs continus et des valeurs manquantes
- Utilisation du ratio de gain d'information normalisé (gain ratio) pour éviter les biais
- Capacité à effectuer un élagage post-construction pour réduire le surapprentissage
- Conversion possible de l'arbre de décision en règles interprétables
- Complexité temporelle de O(n log n) pour n instances d'entraînement

## Détails

L'algorithme [C4.5](https://fr.wikipedia.org/wiki/C4.5) construit un [arbre de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision) en divisant récursivement l'ensemble de données en sous-ensembles plus petits. À chaque nœud, il choisit l'attribut qui offre le meilleur ratio de gain d'information pour effectuer la division.

**Améliorations par rapport à ID3** :  
1. **Traitement des attributs continus** : C4.5 peut discrétiser dynamiquement les attributs numériques en trouvant un seuil optimal pour la division.  
2. **Gestion des valeurs manquantes** : C4.5 peut traiter les exemples avec des valeurs d'attributs manquantes en les pondérant proportionnellement à leur fréquence.  
3. **Utilisation du ratio de gain** : Pour éviter le biais vers les attributs ayant de nombreuses valeurs, C4.5 normalise le gain d'information par l'[entropie](https://fr.wikipedia.org/wiki/Entropie_de_Shannon) de l'attribut lui-même.  
4. **Élagage de l'arbre** : C4.5 implémente une technique d'élagage pessimiste qui supprime les branches peu fiables après la construction de l'arbre.

Le ratio de gain est calculé comme suit :