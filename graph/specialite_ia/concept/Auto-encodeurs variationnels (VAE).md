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

Les Auto-encodeurs Variationnels (VAE) sont des modèles génératifs probabilistes qui étendent le concept d'auto-encodeurs traditionnels en introduisant une composante stochastique. Proposés par Kingma et Welling en 2013, les VAE apprennent à encoder des données dans un espace latent probabiliste et à les reconstruire à partir de cet espace, permettant ainsi la génération de nouvelles données similaires à celles de l'ensemble d'apprentissage. Contrairement aux auto-encodeurs classiques, les VAE ne se contentent pas de compresser l'information, mais modélisent une distribution de probabilité sur l'espace latent.

## Points clés

- Les VAE encodent les entrées en distributions (généralement gaussiennes) dans l'espace latent plutôt qu'en points fixes
- Ils utilisent une fonction de perte combinant un terme de reconstruction et un terme de régularisation (divergence KL)
- L'astuce de reparamétrisation permet l'entraînement par rétropropagation malgré la nature stochastique du modèle
- Les VAE peuvent générer de nouvelles données en échantillonnant l'espace latent et en décodant les échantillons

## Détails

L'architecture d'un VAE comprend deux composants principaux : un encodeur et un décodeur. L'encodeur transforme une donnée d'entrée x en paramètres (μ et σ) d'une distribution gaussienne dans l'espace latent. Le décodeur prend un point z échantillonné de cette distribution et tente de reconstruire la donnée originale.

La fonction de perte d'un VAE se compose de deux termes :
1. **Terme de reconstruction** : mesure la différence entre l'entrée originale et sa reconstruction (souvent une erreur quadratique moyenne ou une log-vraisemblance négative)
2. **Terme de régularisation** : divergence de Kullback-Leibler entre la distribution latente encodée et une distribution gaussienne standard N(0,I), encourageant l'espace latent à être bien structuré

L'astuce de reparamétrisation est cruciale pour l'entraînement des VAE. Au lieu d'échantillonner directement z ~ N(μ, σ²), on calcule z = μ + σ ⊙ ε où ε ~ N(0,I). Cette formulation permet la propagation du gradient à travers l'opération d'échantillonnage.

Les VAE présentent plusieurs avantages par rapport à d'autres modèles génératifs :
- Ils ont une base théorique solide dans l'inférence variationnelle
- L'entraînement est généralement stable
- L'espace latent est continu et structuré, permettant des interpolations significatives

Cependant, ils souffrent aussi de limitations :
- Les reconstructions peuvent être floues, particulièrement pour des données complexes comme les images
- Le compromis entre qualité de reconstruction et régularisation de l'espace latent est parfois difficile à équilibrer
- La capacité générative peut être inférieure à celle d'autres modèles comme les GANs

Les VAE ont trouvé de nombreuses applications en génération d'images, traitement du langage naturel, découverte de médicaments, et même en musique. Des variantes comme les β-VAE, VQ-VAE et VAE conditionnels ont été développées pour améliorer leurs performances ou les adapter à des tâches spécifiques.