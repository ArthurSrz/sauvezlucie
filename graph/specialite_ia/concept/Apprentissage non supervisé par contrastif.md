---
title: Apprentissage non supervisé par contrastif
type: concept
tags:
- apprentissage automatique
- non supervisé
- contrastif
- représentation
- espace latent
- similarité
- exemples positifs
- exemples négatifs
- IA
- deep learning
date_creation: '2025-03-29'
date_modification: '2025-03-29'
hasPart: '[[Fonctions de perte en apprentissage profond]]'
subClassOf: '[[Apprentissage auto-supervisé (Self-supervised Learning)]]'
---
## Généralité

L'[apprentissage non supervisé](https://fr.wikipedia.org/wiki/Apprentissage_non_supervis%C3%A9) par contrastif est une technique d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui permet à un modèle d'apprendre des représentations utiles des données sans nécessiter d'étiquettes explicites. Cette approche repose sur le principe de contraste entre des exemples similaires (positifs) et des exemples différents (négatifs). L'objectif est d'amener le modèle à rapprocher les représentations d'exemples similaires dans l'espace latent tout en éloignant celles d'exemples différents, créant ainsi une structure significative dans l'espace des caractéristiques.

## Points clés

- L'[apprentissage contrastif](https://fr.wikipedia.org/wiki/Apprentissage_par_contraste) crée des représentations en maximisant la similarité entre des paires positives et en minimisant celle entre des paires négatives.
- Contrairement à l'[apprentissage supervisé](https://fr.wikipedia.org/wiki/Apprentissage_automatique#Apprentissage_supervis%C3%A9), il ne nécessite pas d'étiquettes manuelles explicites, mais utilise la structure inhérente aux données.
- Les fonctions de perte contrastives comme InfoNCE, NT-Xent ou le triplet loss sont au cœur de ces méthodes.
- Cette approche est particulièrement efficace pour les tâches de [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur) et de [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel).
- L'apprentissage contrastif bénéficie particulièrement des architectures de [réseaux neuronaux profonds](https://fr.wikipedia.org/wiki/Apprentissage_profond) et des grandes quantités de données.

## Détails

L'[apprentissage contrastif](https://fr.wikipedia.org/wiki/Apprentissage_contrastif) fonctionne en créant des paires d'exemples positifs, généralement obtenues par des transformations ou des augmentations de données d'un même exemple original. Par exemple, en vision par ordinateur, on peut créer deux vues différentes d'une même image en appliquant des rotations, recadrages ou changements de couleur.

Les fonctions de perte contrastives sont essentielles à cette approche. La perte InfoNCE (Noise Contrastive Estimation) est l'une des plus utilisées et s'exprime généralement sous la forme: