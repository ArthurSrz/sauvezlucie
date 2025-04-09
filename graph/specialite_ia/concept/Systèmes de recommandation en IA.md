---
title: Systèmes de recommandation en IA
type: concept
tags:
- intelligence artificielle
- recommandation
- personnalisation
- expérience utilisateur
- algorithmes
- Netflix
- Amazon
- Spotify
- apprentissage automatique
date_creation: '2025-03-29'
date_modification: '2025-03-29'
isPartOf:
- '[[Les applications de l''intelligence artificielle]]'
- '[[Apprentissage automatique (Machine Learning)]]'
uses:
- '[[Apprentissage profond (Deep Learning)]]'
- '[[Entreprises technologiques et géants du numérique dans le domaine de l''intelligence
  artificielle]]'
relatedTo: '[[Éthique de l''intelligence artificielle]]'
seeAlso:
- '[[Systèmes de recommandation personnalisée]]'
- '[[Systèmes de recommandation et filtrage collaboratif]]'
---
## Généralité

Les systèmes de recommandation sont des applications d'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) qui suggèrent des produits, services ou contenus pertinents aux utilisateurs en fonction de leurs préférences, comportements passés ou similitudes avec d'autres utilisateurs. Apparus dans les années 1990 avec les premiers [filtres collaboratifs](https://fr.wikipedia.org/wiki/Filtrage_collaboratif), ils constituent aujourd'hui un élément fondamental des plateformes comme [Netflix](https://fr.wikipedia.org/wiki/Netflix), [Amazon](https://fr.wikipedia.org/wiki/Amazon), Spotify ou YouTube, transformant les données utilisateur en suggestions personnalisées tout en soulevant des questions éthiques importantes.

## Points clés

- **Approches principales**: [Filtrage collaboratif](https://fr.wikipedia.org/wiki/Filtrage_collaboratif), filtrage basé sur le contenu et méthodes hybrides combinant ces approches
- **Impact économique**: Génèrent 35% des revenus d'Amazon, influencent 80% du contenu visionné sur Netflix, augmentent de 20-30% le panier moyen sur les sites [e-commerce](https://fr.wikipedia.org/wiki/Commerce_%C3%A9lectronique)
- **Technologies clés**: [Apprentissage profond](https://fr.wikipedia.org/wiki/Apprentissage_profond), modèles d'embedding, algorithmes de bandits multi-bras et factorisation matricielle

## Détails

Les systèmes de recommandation utilisent principalement trois approches techniques. Le **filtrage collaboratif** se divise en deux catégories: basé sur l'utilisateur (comme les suggestions "Les clients ayant acheté ce produit..." sur [Amazon](https://fr.wikipedia.org/wiki/Amazon)) et basé sur les items (comme "Parce que vous avez regardé..." sur [Netflix](https://fr.wikipedia.org/wiki/Netflix)). 

Le **filtrage basé sur le contenu** analyse les caractéristiques des items (genres, acteurs, etc.), efficace contre le problème du "cold item" mais pouvant causer une sur-spécialisation. Les **approches hybrides** compensent les faiblesses des autres méthodes. Par exemple, [Spotify](https://fr.wikipedia.org/wiki/Spotify) combine filtrage collaboratif pour Discover Weekly et analyse de contenu pour les recommandations par genre.

Les technologies avancées incluent les réseaux de neurones profonds (utilisés par YouTube), les modèles d'embedding comme Word2Vec (Amazon), les algorithmes de bandits multi-bras ([LinkedIn](https://fr.wikipedia.org/wiki/LinkedIn)) et la factorisation matricielle (SVD dans le Netflix Prize). Les systèmes modernes intègrent également des données contextuelles (localisation, moment, appareil) et des techniques de reinforcement learning.

Parmi les principaux défis et considérations éthiques, on note:
- **Bulles de filtre**: Limitation de l'exposition à des contenus diversifiés (étudié sur [Facebook](https://fr.wikipedia.org/wiki/Facebook))
- **Biais algorithmiques**: Amplification des préjugés existants
- **Confidentialité**: Réglementée par le [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es) en Europe
- **Explicabilité**: Nécessité d'expliquer les recommandations

L'évolution future tend vers la personnalisation contextuelle (heure, localisation), la détection d'émotions (applications expérimentales) et l'adaptation aux objectifs à long terme des utilisateurs.