---
title: Architectures résiduelles (ResNets)
type: concept
tags:
- ResNets
- Réseaux de neurones
- Deep Learning
- Connexions résiduelles
- Apprentissage profond
- Microsoft Research
- Réseaux convolutifs
date_creation: '2025-04-08'
date_modification: '2025-04-08'
solves: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
uses: '[[Optimiseurs adaptatifs]]'
appliedIn: '[[Techniques d''augmentation de données pour la vision]]'
subClassOf: '[[Réseau neuronal convolutif]]'
---
## Généralité

Les architectures résiduelles (ResNets) sont un type de réseau de neurones convolutifs profonds introduits par Microsoft Research en 2015. Elles résolvent le problème de la disparition du gradient dans les réseaux très profonds grâce à des connexions résiduelles (ou "skip connections").

## Points clés

- **Connexions résiduelles** : Mécanisme permettant de contourner des couches via des connexions directes, facilitant l'apprentissage de fonctions identité.
- **Résolution du problème de gradient** : Permettent d'entraîner des réseaux extrêmement profonds (100+ couches) sans dégradation des performances.
- **Blocs résiduels** : Structure de base des ResNets, composée de couches convolutives avec une connexion résiduelle additive.

## Détails

Les ResNets ont révolutionné l'apprentissage profond en permettant la construction de réseaux avec des centaines de couches. Leur innovation principale réside dans les blocs résiduels, où la sortie d'un groupe de couches est additionnée à leur entrée avant d'être passée à travers une fonction d'activation.

Mathématiquement, un bloc résiduel implémente :
H(x) = F(x) + x
où F(x) représente les transformations apprises et x est l'entrée originale.

Cette architecture présente plusieurs avantages :
1. **Stabilité de l'entraînement** : Le gradient peut circuler directement à travers les connexions résiduelles
2. **Performance accrue** : Meilleures résultats sur des benchmarks comme ImageNet
3. **Extensibilité** : Variantes comme ResNeXt et Wide ResNets ont émergé

Les ResNets standards incluent des versions avec 18, 34, 50, 101 et 152 couches, chacune adaptée à différents besoins en termes de capacité et de ressources computationnelles.

## Applications

Les ResNets sont largement utilisés pour :
- Classification d'images
- Détection d'objets
- Segmentation sémantique
- Transfer learning

Leur conception a inspiré de nombreuses architectures ultérieures et reste une référence en vision par ordinateur.