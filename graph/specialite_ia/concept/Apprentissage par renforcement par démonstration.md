---
title: Apprentissage par renforcement par démonstration
type: concept
tags:
- Apprentissage par Renforcement
- Apprentissage par Imitation
- RL
- IL
- Intelligence Artificielle
- Machine Learning
- Hybrid Learning
date_creation: '2025-04-08'
date_modification: '2025-04-09'
subClassOf:
- '[[Apprentissage par renforcement]]'
- '[[Apprentissage par imitation (Imitation Learning)]]'
---
## Généralité

L'[apprentissage par renforcement](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement) par démonstration (Apprentissage par Renforcement par Imitation, ou Apprentissage par Renforcement Guidé) est une approche hybride qui combine les techniques de l'apprentissage par renforcement (RL) et de l'[apprentissage par imitation](https://fr.wikipedia.org/wiki/Apprentissage_par_imitation) (IL). Cette méthode permet à un agent d'apprendre à partir d'exemples de comportements experts, tout en optimisant sa politique de décision pour maximiser une récompense cumulée.

L'objectif principal est de bénéficier des avantages de l'apprentissage par imitation pour accélérer le processus d'apprentissage et de l'apprentissage par renforcement pour améliorer les performances finales, tout en réduisant les risques liés à une exploration aléatoire inefficace ou à des biais dans les données de démonstration.

## Points clés

- **Combinaison d'approches** : Intègre les techniques de l'[apprentissage par imitation](https://fr.wikipedia.org/wiki/Apprentissage_par_imitation) (IL) et de l'[apprentissage par renforcement](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement) (RL), une méthode parfois appelée "Apprentissage par Renforcement Guidé".
- **Accélération de l'apprentissage** : Utilise des démonstrations expertes pour initialiser l'apprentissage, réduisant considérablement le temps d'exploration aléatoire.
- **Optimisation de la politique** : Améliore la politique de l'agent en combinant deux mécanismes : 1) l'imitation de comportements experts (comme dans [AlphaGo](https://fr.wikipedia.org/wiki/AlphaGo)) et 2) l'optimisation par renforcement via des fonctions de récompense.
- **Applications pratiques** : Ces techniques sont effectivement utilisées en [robotique](https://fr.wikipedia.org/wiki/Robotique), dans les systèmes autonomes (voitures sans conducteur) et les jeux vidéo (comme DeepMind's AlphaStar).
- **Variantes avancées** : Inclut des méthodes comme l'[Apprentissage par Renforcement Inverse](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement_inverse) et GAIL (Generative Adversarial Imitation Learning).

## Détails

### Processus d'Apprentissage

1. **Collecte de démonstrations** : Des experts fournissent des démonstrations de comportements souhaités dans l'environnement. Ces démonstrations peuvent être des séquences d'actions, des trajectoires d'états, ou des paires d'état-action.

2. **Apprentissage par imitation** : L'agent apprend une politique initiale en imitant les démonstrations. Cette étape peut être réalisée à l'aide de méthodes telles que le Clonage Comportemental (Behavioral Cloning) ou l'Apprentissage Inverse de la Politique.

3. **Apprentissage par renforcement** : L'agent utilise la politique initiale comme point de départ pour l'apprentissage par renforcement. Il interagit avec l'environnement, reçoit des récompenses, et ajuste sa politique pour maximiser la récompense cumulée.

### Avantages

- **Accélération de l'apprentissage** : Les démonstrations fournissent un point de départ solide, réduisant considérablement le temps nécessaire pour atteindre des performances acceptables.
- **Réduction du risque de sous-optimisation** : En utilisant des démonstrations, l'agent est moins susceptible de converger vers des politiques sous-optimales.
- **Flexibilité** : L'agent peut continuer à apprendre et à s'adapter à des situations non couvertes par les démonstrations.
- **Surpassement des experts** : L'agent peut finalement surpasser les performances des démonstrateurs humains grâce à la combinaison d'imitation et d'exploration.

### Défis

- **Qualité des démonstrations** : La performance de l'agent dépend fortement de la qualité et de la pertinence des démonstrations fournies.
- **Généralisation** : L'agent doit être capable de généraliser les comportements appris à des situations nouvelles et inconnues.
- **Équilibrage entre imitation et exploration** : Il est crucial de trouver le bon équilibre entre l'imitation des démonstrations et l'exploration de nouveaux comportements.
- **Biais humains** : Les démonstrations peuvent incorporer des biais ou limites humaines que l'agent risque de reproduire.

### Applications

- **Robotique** : Formation de robots pour effectuer des tâches complexes, telles que la manipulation d'objets ou la navigation dans des environnements dynamiques.
- **Jeux** : Amélioration des performances des agents dans des jeux vidéo (StarCraft II avec AlphaStar).
- **Systèmes de recommandation** : Optimisation des recommandations en intégrant des préférences utilisateur observées.
- **Véhicules autonomes** : Apprentissage de politiques de conduite à partir de démonstrations humaines combinées avec un apprentissage par renforcement.