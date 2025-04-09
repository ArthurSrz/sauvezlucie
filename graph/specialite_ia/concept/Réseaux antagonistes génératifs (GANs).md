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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf:
- '[[Apprentissage profond (Deep Learning)]]'
- '[[Apprentissage non supervisé]]'
---
## Généralité

Les [Réseaux Antagonistes Génératifs](https://fr.wikipedia.org/wiki/R%C3%A9seau_antagoniste_g%C3%A9n%C3%A9ratif) (GANs, Generative Adversarial Networks) sont une architecture d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) introduite par Ian Goodfellow et ses collègues en 2014. Ils mettent en compétition deux réseaux de neurones : un générateur qui crée des données synthétiques et un discriminateur qui tente de distinguer les données réelles des données générées. [Source: Wikipedia "Generative adversarial network"]

## Points clés

- Composés de deux réseaux en compétition : un générateur (crée des données) et un discriminateur (les évalue)
- Inspirés de la [théorie des jeux](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_jeux) et du concept d'[équilibre de Nash](https://fr.wikipedia.org/wiki/%C3%89quilibre_de_Nash)
- Applications variées : génération d'images réalistes, transfert de style artistique, super-résolution d'images
- Défis techniques : instabilité d'entraînement et mode collapse (faible diversité des sorties)
- Variantes architecturales : DCGANs, WGANs, CycleGANs parmi les plus influentes

## Détails

Le fonctionnement des GANs repose sur une dynamique d'apprentissage unique. Le générateur prend en entrée un vecteur de bruit aléatoire et produit des données synthétiques. Le discriminateur reçoit soit des données réelles, soit des données générées, et doit déterminer leur origine.

Mathématiquement, les GANs optimisent une fonction minimax où :
- Le discriminateur maximise sa capacité à identifier correctement les données
- Le générateur minimise la capacité du discriminateur à détecter les fausses données

Les GANs ont trouvé des applications dans de nombreux domaines :
- Génération d'images (comme les visages synthétiques de This Person Does Not Exist)
- Transfert de style artistique
- Super-résolution d'images
- Découverte de molécules en chimie médicinale (applications encore expérimentales)

L'architecture de base a donné naissance à de nombreuses variantes :
- DCGANs (Deep Convolutional GANs)
- WGANs (Wasserstein GANs) 
- CycleGANs

Ces variantes apportent des améliorations en termes de stabilité d'entraînement ou de qualité des résultats, bien qu'aucune n'ait complètement résolu tous les défis des GANs originaux.

[Source: Wikipedia "Generative adversarial network#Applications"]
[Source: Wikipedia "Generative adversarial network#Variations"]