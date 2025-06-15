---
title: Réseaux génératifs pour la synthèse et manipulation d'images (au-delà des GANs)
type: concept
tags:
- réseaux génératifs
- synthèse d'images
- manipulation d'images
- GAN
- VAE
- apprentissage automatique
- IA générative
- modèles génératifs
date_creation: '2025-04-04'
date_modification: '2025-04-04'
relatedTo: '[[Auto-encodeurs adversariaux]]'
subClassOf: '[[Apprentissage non supervisé]]'
---
## Généralité

Les [réseaux génératifs](https://fr.wikipedia.org/wiki/R%C3%A9seau_g%C3%A9n%C3%A9ratif) désignent une famille de modèles d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) capables de créer ou modifier des images de manière réaliste. Ces systèmes, apparus dans les années 2010, reposent sur des architectures de [réseaux de neurones profonds](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels). Bien que les [GANs](https://fr.wikipedia.org/wiki/R%C3%A9seau_antagonistes_g%C3%A9n%C3%A9ratifs) soient les plus connus, d'autres architectures comme les [VAEs](https://fr.wikipedia.org/wiki/Autoencodeur_variationnel) ou les modèles de diffusion offrent des approches alternatives.

## Points clés

- **Diversité des architectures** : Plusieurs approches existent pour la génération d'images ([GANs](https://fr.wikipedia.org/wiki/R%C3%A9seaux_antagonistes_g%C3%A9n%C3%A9ratifs), [VAEs](https://fr.wikipedia.org/wiki/Autoencodeur_variationnel), Diffusion Models)
- **Contrôle avancé** : Possibilité de manipuler finement les attributs d'une image (style, couleur, structure)
- **Applications variées** : Utilisés dans l'art numérique, la médecine, l'industrie du divertissement et la mode
- **Défis éthiques** : Questions importantes concernant les [deepfakes](https://fr.wikipedia.org/wiki/Deepfake) et la propriété intellectuelle
- **Performances impressionnantes** : Systèmes comme [StyleGAN](https://fr.wikipedia.org/wiki/StyleGAN) ou [DALL-E](https://fr.wikipedia.org/wiki/DALL-E) produisent des images photoréalistes

## Détails

Les réseaux génératifs englobent plusieurs architectures principales. Les **GANs (Generative Adversarial Networks)**, introduits par Ian Goodfellow et al. en 2014, reposent sur un générateur et un discriminateur en compétition. Les **VAEs (Variational Autoencoders)**, introduits par Kingma et Welling en 2013, utilisent une approche probabiliste pour apprendre une représentation latente des données. Les **Diffusion Models**, popularisés par Ho et al. en 2020, transforment progressivement du bruit en images via un processus itératif.

Diverses techniques permettent une manipulation avancée des images générées. L'**interpolation latente** permet de naviguer dans l'espace latent comme dans [StyleGAN](https://fr.wikipedia.org/wiki/StyleGAN). Le **conditionnement multimodal** offre un contrôle par texte (via CLIP) ou par segmentation sémantique. L'**édition guidée** permet de transformer des esquisses en images photoréalistes (ex: GauGAN2).

Les applications concrètes sont nombreuses : dans l'**art numérique** avec la génération d'œuvres originales ("Portrait d'Edmond de Belamy" vendu chez Christie's), en **médecine** pour la synthèse d'images IRM aidant à la détection précoce de tumeurs, dans le **divertissement** pour la création de décors (comme dans ["The Mandalorian"](https://fr.wikipedia.org/wiki/The_Mandalorian)), et dans la **mode** pour la conception virtuelle de vêtements.

Les perspectives futures incluent l'hybridation entre différentes architectures, l'amélioration de l'efficacité énergétique, le développement de méthodes nécessitant moins de données, l'intégration de contraintes physiques pour des applications scientifiques, et la combinaison avec d'autres paradigmes comme les [réseaux neuronaux graphiques](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_graphes).