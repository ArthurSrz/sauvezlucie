---
title: Auto-encodeurs adversariaux
type: concept
tags:
- deep learning
- auto-encodeurs
- GAN
- réseaux de neurones
- apprentissage non supervisé
- génération de données
- représentation latente
- Makhzani
- intelligence artificielle
date_creation: '2025-03-18'
date_modification: '2025-03-18'
subClassOf: '[[Les auto-encodeurs]]'
---
## Généralité

Les auto-encodeurs adversariaux (AAE - Adversarial Autoencoders) sont une architecture de réseau neuronal qui combine les principes des auto-encodeurs traditionnels avec ceux des réseaux antagonistes génératifs (GAN). Introduits par Makhzani et al. en 2015, ils permettent d'apprendre des représentations latentes structurées tout en imposant une distribution préalable arbitraire sur l'espace latent. Cette approche hybride offre un cadre puissant pour la génération de données, l'apprentissage de représentations et diverses tâches d'apprentissage non supervisé.

## Points clés

- Les AAE combinent un [auto-encodeur](https://fr.wikipedia.org/wiki/auto-encodeur) traditionnel avec un mécanisme adversarial inspiré des GANs
- Ils permettent de contraindre l'espace latent à suivre une distribution spécifique (souvent gaussienne)
- Contrairement aux auto-encodeurs variationnels (VAE), les AAE utilisent un discriminateur pour imposer la distribution latente
- Ils sont particulièrement efficaces pour la génération de données et l'apprentissage de représentations disentangled
- Les AAE peuvent être adaptés pour l'apprentissage semi-supervisé et le clustering

## Détails

L'architecture d'un auto-encodeur adversarial comprend trois composants principaux : un encodeur, un décodeur et un discriminateur. L'encodeur transforme les données d'entrée en vecteurs dans l'espace latent, tandis que le décodeur tente de reconstruire les données originales à partir de ces vecteurs latents. Le discriminateur, quant à lui, essaie de distinguer les vecteurs latents générés par l'encodeur des échantillons tirés d'une distribution préalable spécifiée.

L'entraînement d'un AAE se déroule en deux phases alternées :
1. **Phase de reconstruction** : l'encodeur et le décodeur sont entraînés ensemble pour minimiser l'erreur de reconstruction, comme dans un auto-encodeur classique.
2. **Phase adversariale** : l'encodeur est entraîné pour tromper le discriminateur, tandis que le discriminateur est entraîné pour distinguer les vecteurs latents encodés des échantillons de la distribution préalable.

Cette approche présente plusieurs avantages par rapport aux auto-encodeurs variationnels (VAE). Alors que les VAE imposent une distribution gaussienne sur l'espace latent via une divergence KL, les AAE peuvent imposer pratiquement n'importe quelle distribution préalable grâce au mécanisme adversarial. De plus, les AAE produisent généralement des reconstructions plus nettes que les VAE.

Les applications des auto-encodeurs adversariaux sont nombreuses :
- Génération d'images réalistes
- [Apprentissage](https://fr.wikipedia.org/wiki/Apprentissage) de représentations disentangled (où différentes dimensions de l'espace latent capturent des facteurs de variation indépendants)
- Clustering non supervisé
- [Apprentissage](https://fr.wikipedia.org/wiki/Apprentissage) semi-supervisé
- Traduction entre domaines (style transfer)
- Imputation de données manquantes

Des variantes des AAE ont été développées, comme les AAE conditionnels qui permettent de contrôler le processus de génération, ou les AAE supervisés qui intègrent des informations d'étiquettes pour améliorer les représentations apprises.

## Comparaison avec d'autres modèles génératifs

Comparés aux GANs classiques, les AAE offrent l'avantage d'apprendre explicitement une représentation latente des données, ce qui facilite certaines tâches comme l'interpolation ou la manipulation sémantique. Par rapport aux VAE, ils produisent généralement des échantillons de meilleure qualité tout en offrant plus de flexibilité dans le choix de la distribution préalable.