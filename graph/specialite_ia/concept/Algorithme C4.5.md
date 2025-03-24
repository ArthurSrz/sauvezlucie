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
date_creation: '2025-03-21'
date_modification: '2025-03-22'
follows: '[[Algorithme ID3]]'
isPartOf: '[[Arbre de décision]]'
---
## Généralité

L'[algorithme C4.5](https://fr.wikipedia.org/wiki/algorithme_C4.5) est une extension de l'algorithme ID3, développé par [Ross Quinlan](https://fr.wikipedia.org/wiki/Ross_Quinlan) en 1993 pour générer des arbres de décision. Il s'agit d'un algorithme d'apprentissage supervisé largement utilisé dans le domaine du data mining et de l'intelligence artificielle. C4.5 construit des arbres de décision à partir d'un ensemble de données d'entraînement en utilisant le concept d'entropie de l'information. Contrairement à son prédécesseur, C4.5 peut traiter des attributs continus et discrets, gérer les données manquantes et effectuer un élagage pour réduire les erreurs de classification.

## Points clés

- Extension de l'algorithme ID3 avec des améliorations significatives comme la gestion des attributs continus et des valeurs manquantes
- Utilise le ratio de gain (gain ratio) comme critère de division pour corriger le biais de l'ID3 envers les attributs à nombreuses valeurs
- Effectue un élagage post-construction pour améliorer la généralisation et réduire le surapprentissage
- Capable de convertir l'arbre de décision en ensemble de règles pour améliorer la lisibilité et l'interprétabilité

## Détails

### Fonctionnement de base

L'[algorithme C4.5](https://fr.wikipedia.org/wiki/algorithme_C4.5) construit un arbre de décision en divisant récursivement l'ensemble de données en sous-ensembles plus petits. À chaque nœud, il choisit l'attribut qui offre le meilleur ratio de gain d'information pour effectuer la division. Le processus se poursuit jusqu'à ce que tous les exemples d'un sous-ensemble appartiennent à la même classe ou qu'aucune autre division ne soit possible.

### Améliorations par rapport à ID3

1. **Traitement des attributs continus** : C4.5 peut discrétiser dynamiquement les attributs numériques en trouvant un seuil optimal pour la division.

2. **Gestion des valeurs manquantes** : Contrairement à ID3, C4.5 peut traiter les exemples avec des valeurs d'attributs manquantes en les pondérant proportionnellement à leur fréquence.

3. **Utilisation du ratio de gain** : Pour éviter le biais vers les attributs ayant de nombreuses valeurs, C4.5 normalise le gain d'information par l'entropie de l'attribut lui-même.

4. **[Élagage](https://fr.wikipedia.org/wiki/Élagage) de l'arbre** : C4.5 implémente une technique d'élagage pessimiste qui supprime les branches peu fiables après la construction de l'arbre, réduisant ainsi le surapprentissage.

### Formule du ratio de gain

Le ratio de gain est calculé comme suit :
```
Ratio de gain(S, A) = Gain(S, A) / SplitInfo(S, A)
```
où `Gain(S, A)` est le gain d'information standard et `SplitInfo(S, A)` représente l'information potentielle générée en divisant l'ensemble S en n sous-ensembles.

### Limitations

Malgré ses améliorations, C4.5 présente certaines limitations :
- Tendance au surapprentissage sur des données bruitées
- Préférence pour les attributs avec de nombreuses valeurs possibles, malgré la correction par le ratio de gain
- Coût computationnel élevé pour les grands ensembles de données

### Évolution

L'[algorithme C4.5](https://fr.wikipedia.org/wiki/algorithme_C4.5) a été suivi par C5.0 (ou See5), une version commerciale qui offre des améliorations en termes de vitesse, d'utilisation de la mémoire et d'efficacité. C5.0 introduit également le concept de "boosting" pour améliorer la précision de la classification.