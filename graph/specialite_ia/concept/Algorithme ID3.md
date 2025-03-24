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

L'algorithme ID3 (Iterative Dichotomiser 3) est un algorithme d'apprentissage supervisé développé par [Ross Quinlan](https://fr.wikipedia.org/wiki/Ross_Quinlan) en 1986. Il s'agit d'une méthode fondamentale pour la construction d'arbres de décision, utilisée pour classer des instances en se basant sur leurs attributs. ID3 utilise l'entropie et le gain d'information pour sélectionner les attributs les plus discriminants à chaque étape de la construction de l'arbre, ce qui permet de créer un modèle prédictif efficace à partir de données d'entraînement.

## Points clés

- ID3 construit un arbre de décision de haut en bas en sélectionnant à chaque nœud l'attribut qui maximise le gain d'information
- L'algorithme utilise l'entropie comme mesure de l'impureté d'un ensemble de données
- ID3 s'arrête lorsque tous les exemples d'un nœud appartiennent à la même classe ou lorsqu'il n'y a plus d'attributs disponibles
- Il est particulièrement efficace pour les attributs catégoriels et les problèmes de classification

## Détails

### Principe de fonctionnement

L'algorithme ID3 fonctionne de manière récursive en divisant l'ensemble de données en sous-ensembles de plus en plus homogènes. À chaque étape, il sélectionne l'attribut qui permet de réduire au maximum l'entropie (ou augmenter le gain d'information) dans les sous-ensembles résultants.

L'entropie est une mesure de l'impureté ou du désordre dans un ensemble de données. Pour un ensemble S contenant des exemples de n classes différentes, l'entropie est calculée comme suit:

Entropie(S) = -Σ(p_i * log₂(p_i)) pour i de 1 à n

où p_i est la proportion d'exemples appartenant à la classe i dans l'ensemble S.

Le gain d'information pour un attribut A est calculé comme la différence entre l'entropie de l'ensemble initial et la somme pondérée des entropies des sous-ensembles créés en divisant selon les valeurs de A:

Gain(S, A) = Entropie(S) - Σ((|S_v|/|S|) * Entropie(S_v))

où S_v est le sous-ensemble de S pour lequel l'attribut A a la valeur v.

### Algorithme

1. Calculer l'entropie de l'ensemble de données actuel
2. Pour chaque attribut, calculer le gain d'information obtenu en divisant l'ensemble selon cet attribut
3. Sélectionner l'attribut avec le gain d'information maximal
4. Créer un nœud de décision basé sur cet attribut
5. Récursivement construire des sous-arbres pour chaque valeur de l'attribut sélectionné
6. S'arrêter lorsque tous les exemples d'un nœud appartiennent à la même classe ou lorsqu'il n'y a plus d'attributs disponibles

### Limites et extensions

ID3 présente certaines limitations:
- Il a tendance à favoriser les attributs avec de nombreuses valeurs distinctes
- Il ne gère pas naturellement les attributs continus
- Il peut créer des arbres trop complexes (surapprentissage)
- Il ne traite pas les valeurs manquantes

Ces limitations ont conduit au développement d'algorithmes plus avancés comme C4.5 (successeur direct d'ID3) et CART, qui intègrent des mécanismes comme l'élagage, la gestion des attributs continus et le traitement des valeurs manquantes.

## Applications

ID3 et ses dérivés sont largement utilisés dans divers domaines comme:
- Le diagnostic médical
- L'analyse de risque financier
- La reconnaissance de formes
- Les systèmes de recommandation
- L'analyse de données marketing