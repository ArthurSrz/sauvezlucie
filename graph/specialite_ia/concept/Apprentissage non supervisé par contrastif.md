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

L'apprentissage non supervisé par contrastif est une technique d'apprentissage automatique qui permet à un modèle d'apprendre des représentations utiles des données sans nécessiter d'étiquettes explicites. Cette approche repose sur le principe de contraste entre des exemples similaires (positifs) et des exemples différents (négatifs). L'objectif est d'amener le modèle à rapprocher les représentations d'exemples similaires dans l'espace latent tout en éloignant celles d'exemples différents, créant ainsi une structure significative dans l'espace des caractéristiques.

## Points clés

- L'apprentissage contrastif crée des représentations en maximisant la similarité entre des paires positives et en minimisant celle entre des paires négatives
- Contrairement à l'apprentissage supervisé, il ne nécessite pas d'étiquettes manuelles, mais utilise la structure inhérente aux données
- Les fonctions de perte contrastives comme InfoNCE, NT-Xent ou le triplet loss sont au cœur de ces méthodes
- Cette approche est particulièrement efficace pour les tâches de vision par ordinateur et de traitement du langage naturel

## Détails

L'apprentissage contrastif fonctionne en créant des paires d'exemples positifs, généralement obtenues par des transformations ou des augmentations de données d'un même exemple original. Par exemple, en vision par ordinateur, on peut créer deux vues différentes d'une même image en appliquant des rotations, recadrages ou changements de couleur. Ces paires sont considérées comme similaires et le modèle doit apprendre à les reconnaître comme telles.

Les fonctions de perte contrastives sont essentielles à cette approche. La perte InfoNCE (Noise Contrastive Estimation) est l'une des plus utilisées et s'exprime généralement sous la forme:

```
L = -log[exp(sim(z_i, z_j)/τ) / Σ exp(sim(z_i, z_k)/τ)]
```

où `sim` est une fonction de similarité (souvent le cosinus), `z_i` et `z_j` sont des représentations d'une paire positive, `z_k` représente tous les autres exemples (négatifs), et τ est un paramètre de température qui contrôle la concentration de la distribution.

Plusieurs méthodes populaires ont émergé ces dernières années:

1. **SimCLR** (Simple Framework for Contrastive Learning of Visual Representations): utilise des augmentations de données et une architecture d'encodeur suivie d'une projection pour apprendre des représentations visuelles.

2. **MoCo** (Momentum Contrast): maintient une file d'attente de représentations négatives et utilise un encodeur avec mise à jour par momentum pour améliorer la cohérence des représentations.

3. **CLIP** ([Contrastive Language-Image Pre-training](https://fr.wikipedia.org/wiki/Contrastive_Language-Image_Pre-training)): applique l'apprentissage contrastif entre des images et des descriptions textuelles pour créer des représentations multimodales.

4. **SimSiam** et **BYOL**: variantes qui fonctionnent sans exemples négatifs explicites.

L'apprentissage contrastif présente plusieurs avantages: il permet d'apprendre des représentations robustes à partir de grandes quantités de données non étiquetées, il est moins sensible aux biais présents dans les étiquettes, et les représentations apprises se généralisent souvent bien à diverses tâches en aval. Ces caractéristiques en font une approche de plus en plus importante dans l'apprentissage auto-supervisé moderne.