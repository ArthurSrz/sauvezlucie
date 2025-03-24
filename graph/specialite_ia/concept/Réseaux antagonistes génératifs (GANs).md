---
title: Réseaux antagonistes génératifs (GANs)
type: concept
tags:
- intelligence artificielle
- apprentissage automatique
- GANs
- réseaux de neurones
- génération de données
- Ian Goodfellow
- modèles génératifs
- deep learning
- données synthétiques
- algorithmes
date_creation: '2025-03-20'
date_modification: '2025-03-20'
subClassOf:
- '[[Apprentissage profond (Deep Learning)]]'
- '[[Apprentissage non supervisé]]'
---
## Généralité

Les Réseaux Antagonistes Génératifs (GANs, [Generative Adversarial Networks](https://fr.wikipedia.org/wiki/Generative_Adversarial_Networks)) sont une architecture d'apprentissage automatique introduite par [Ian Goodfellow](https://fr.wikipedia.org/wiki/Ian_Goodfellow) et ses collègues en 2014. Ce cadre innovant met en compétition deux réseaux de neurones : un générateur qui crée des données synthétiques et un discriminateur qui tente de distinguer les données réelles des données générées. Cette approche antagoniste permet de produire des données artificielles d'une qualité remarquable, capables de capturer la distribution des données réelles.

## Points clés

- Les GANs sont composés de deux réseaux en compétition : un générateur qui crée des données et un discriminateur qui les évalue
- L'entraînement des GANs repose sur un jeu à somme nulle où le générateur s'améliore pour tromper le discriminateur
- Les GANs excellent dans la génération d'images, de textes, de musique et d'autres types de contenus créatifs
- Malgré leur puissance, les GANs souffrent de problèmes comme l'instabilité d'entraînement et le mode collapse

## Détails

Le fonctionnement des GANs repose sur une dynamique d'apprentissage unique. Le générateur prend en entrée un vecteur de bruit aléatoire et produit des données synthétiques (par exemple, des images). Le discriminateur, quant à lui, reçoit soit des données réelles, soit des données générées, et doit déterminer leur origine. L'objectif du générateur est de créer des données si convaincantes que le discriminateur ne peut les distinguer des données réelles.

Mathématiquement, les GANs optimisent une fonction minimax où le discriminateur maximise sa capacité à identifier correctement les données réelles et générées, tandis que le générateur minimise la capacité du discriminateur à détecter ses créations. Cette compétition pousse les deux réseaux à s'améliorer continuellement.

Les applications des GANs sont vastes et en constante expansion :
- Génération d'images photoréalistes
- Conversion d'images (style transfer, image-to-image translation)
- [Super-résolution](https://fr.wikipedia.org/wiki/Super-résolution) d'images
- Complétion d'images (inpainting)
- Synthèse de visages et manipulation faciale
- Génération de texte et de musique
- Création de données synthétiques pour l'augmentation de jeux de données

Plusieurs variantes de GANs ont été développées pour résoudre des problèmes spécifiques ou améliorer les performances :
- DCGANs (Deep Convolutional GANs) pour la génération d'images
- CycleGANs pour la traduction d'images sans paires d'entraînement
- StyleGANs pour le contrôle précis des attributs générés
- BigGANs pour la génération d'images à haute résolution
- StackGANs pour la génération d'images à partir de descriptions textuelles

Malgré leurs succès, les GANs présentent des défis significatifs. L'entraînement est souvent instable, avec des oscillations qui empêchent la convergence. Le mode collapse, où le générateur produit seulement un sous-ensemble limité de la distribution cible, reste un problème persistant. De plus, l'évaluation objective de la qualité des GANs demeure complexe, nécessitant souvent des métriques spécifiques comme l'Inception Score ou le Fréchet Inception Distance.