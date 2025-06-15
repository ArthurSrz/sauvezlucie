---
title: Apprentissage par imitation (Imitation Learning)
type: concept
tags:
- intelligence artificielle
- apprentissage automatique
- imitation learning
- démonstration d'experts
- supervision
- apprentissage par renforcement
- comportement d'agent
- IA
- algorithmes d'apprentissage
- modélisation comportementale
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

L'[apprentissage par imitation](https://fr.wikipedia.org/wiki/Apprentissage_par_imitation) (Imitation Learning) est une approche en [intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) où un agent apprend à effectuer une tâche en observant et en reproduisant les comportements d'un expert. Contrairement à l'[apprentissage par renforcement](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement) qui nécessite une fonction de récompense explicite, l'apprentissage par imitation utilise des démonstrations d'experts comme signal de supervision.

## Points clés

- Permet d'acquérir des compétences complexes sans fonction de récompense explicite
- Deux catégories principales : apprentissage supervisé par imitation et apprentissage par renforcement inverse
- Applications en [robotique](https://fr.wikipedia.org/wiki/Robotique), systèmes autonomes et jeux vidéo
- Algorithmes courants : DAgger, Behavioral Cloning, GAIL
- Défis majeurs : dérive comportementale et dépendance à la qualité des démonstrations

## Détails

L'apprentissage par imitation comprend plusieurs approches principales :

**Behavioral Cloning (BC)** :  
Méthode la plus simple qui traite l'imitation comme un problème d'[apprentissage supervisé](https://fr.wikipedia.org/wiki/Apprentissage_supervis%C3%A9). Souffre du problème de "distribution shift". Initialement développé pour des systèmes de [conduite autonome](https://fr.wikipedia.org/wiki/V%C3%A9hicule_autonome).

**Inverse Reinforcement Learning (IRL)** :  
Tente d'inférer la fonction de récompense implicite que l'expert optimise. Popularisé par les travaux de Andrew Ng et Stuart Russell en 2000. Applications en robotique médicale.

**Generative Adversarial Imitation Learning (GAIL)** :  
Inspiré des réseaux antagonistes génératifs (GANs). Introduit par Ho et Ermon en 2016. Offre de meilleures performances que le BC simple.

**Dataset Aggregation (DAgger)** :  
Spécifiquement développé pour atténuer le problème de "distribution shift".

Les principaux domaines d'application incluent :
- Robotique (manipulation d'objets fragiles, marche bipède)
- Systèmes autonomes (conduite de véhicules)
- Jeux vidéo (comportements d'IA réalistes)

Cependant, cette approche présente certaines limitations :
- Problème de "distribution shift"/"covariate shift"
- Dépendance à la qualité des démonstrations ("problème de l'enseignant")
- Accumulation d'erreurs au fil du temps

Les recherches récentes explorent des solutions comme :
- L'apprentissage actif
- L'utilisation de démonstrations multiples
- La combinaison avec d'autres approches d'apprentissage