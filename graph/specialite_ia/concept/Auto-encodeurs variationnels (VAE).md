---
title: Auto-encodeurs variationnels (VAE)
type: concept
tags:
- machine learning
- deep learning
- VAE
- modèles génératifs
- auto-encodeurs
- espace latent
- Kingma
- probabiliste
- génération de données
- compression
date_creation: '2025-03-18'
date_modification: '2025-03-18'
subClassOf: '[[Les auto-encodeurs]]'
---
## Généralité

Les [Auto-encodeurs Variationnels](https://fr.wikipedia.org/wiki/Auto-encodeur_variationnel) (VAE) sont des modèles génératifs probabilistes qui étendent le concept d'[auto-encodeurs](https://fr.wikipedia.org/wiki/Auto-encodeur) traditionnels en introduisant une composante stochastique. Proposés par Diederik P. Kingma et Max Welling dans leur article fondateur "Auto-Encoding Variational Bayes" (2013), les VAE représentent une avancée majeure dans l'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) génératif. Ces modèles apprennent à encoder des données dans un espace latent probabiliste et à les reconstruire à partir de cet espace, permettant ainsi la génération de nouvelles données similaires à celles de l'ensemble d'apprentissage.

## Points clés

- Les VAE encodent les entrées en distributions (généralement gaussiennes) dans l'espace latent plutôt qu'en points fixes, permettant une meilleure généralisation et interpolation
- Ils utilisent une fonction de perte combinant un terme de reconstruction et un terme de régularisation (divergence KL) qui mesure l'écart entre la distribution apprise et une distribution a priori
- L'astuce de reparamétrisation permet l'entraînement par rétropropagation malgré la nature stochastique du modèle
- Les VAE peuvent générer de nouvelles données en échantillonnant l'espace latent et en décodant les échantillons
- Ils se distinguent des autres modèles génératifs comme les GAN par leur approche probabiliste explicite

## Détails

L'architecture d'un [VAE](https://fr.wikipedia.org/wiki/Autoencodeur_variationnel) comprend deux composants principaux : un **encodeur** qui transforme une donnée d'entrée en paramètres (μ et σ) d'une distribution gaussienne dans l'espace latent, et un **décodeur** qui prend un point échantillonné de cette distribution et tente de reconstruire la donnée originale. Le choix d'une distribution gaussienne est motivé par sa simplicité mathématique et la possibilité de calculer analytiquement la [divergence KL](https://fr.wikipedia.org/wiki/Divergence_de_Kullback-Leibler).

La fonction de perte d'un VAE se compose de deux termes : un **terme de reconstruction** qui mesure la différence entre l'entrée originale et sa reconstruction (erreur quadratique moyenne ou log-vraisemblance négative), et un **terme de régularisation** (divergence de Kullback-Leibler entre la distribution latente encodée et une distribution gaussienne standard N(0,I)).

L'astuce de reparamétrisation est cruciale pour l'entraînement des VAE. Au lieu d'échantillonner directement z ~ N(μ, σ²), on calcule z = μ + σ ⊙ ε où ε ~ N(0,I). Cette technique permet de rendre le processus d'échantillonnage différenciable en exprimant l'échantillon aléatoire comme une transformation déterministe des paramètres du modèle et d'une variable aléatoire auxiliaire, facilitant ainsi le calcul des gradients par [rétropropagation](https://fr.wikipedia.org/wiki/R%C3%A9tropropagation_du_gradient).

Les VAE présentent plusieurs avantages : base théorique solide dans l'inférence variationnelle, entraînement généralement stable, espace latent continu et structuré permettant des interpolations significatives, et capacité à fournir une mesure quantitative de la vraisemblance des données. Cependant, ils souffrent aussi de limitations comme des reconstructions parfois floues, un compromis difficile entre qualité de reconstruction et régularisation de l'espace latent, une capacité générative parfois inférieure à d'autres modèles comme les GANs, et des performances parfois limitées sur des données multimodales complexes.

Les VAE ont trouvé de nombreuses applications en génération d'images (visages réalistes), traitement du langage naturel, découverte de médicaments et musique (composition algorithmique). Des variantes ont été développées comme les β-VAE (contrôle de la régularisation), VQ-VAE (espace latent discret) et VAE conditionnels (contrôle sur la génération).

[Plus d'informations sur Wikipédia](https://fr.wikipedia.org/wiki/Auto-encodeur_variationnel)