---
title: Apprentissage par imitation (Imitation Learning)
type: concept
tags:
  - intelligence
  - artificielle
  - apprentissage
  - automatique
  - imitation
  - learning
  - démonstration
  - d'experts
  - supervision
  - apprentissage
  - par
  - renforcement
  - comportement
  - d'agent
  - IA
  - algorithmes
  - d'apprentissage
  - modélisation
  - comportementale
date_creation: 2025-03-20
date_modification: 2025-03-20
relatedTo:
  - "[[Réseaux antagonistes génératifs (GANs)]]"
  - "[[Apprentissage par renforcement_]]"
isPartOf: "[[Entraînement d'un modèle d'IA]]"
---
## Généralité

L'apprentissage par imitation (Imitation Learning) est une approche en intelligence artificielle où un agent apprend à effectuer une tâche en observant et en reproduisant les comportements d'un expert. Contrairement à l'apprentissage par renforcement qui nécessite une fonction de récompense explicite, l'apprentissage par imitation utilise des démonstrations d'experts comme signal de supervision. Cette méthode est particulièrement utile lorsqu'il est difficile de définir une fonction de récompense précise ou lorsque l'exploration de l'environnement est coûteuse ou dangereuse.

## Points clés

- L'apprentissage par imitation permet à un agent d'acquérir des compétences en observant et en reproduisant les actions d'un expert humain ou artificiel
- Cette approche est particulièrement efficace pour les tâches complexes où la définition d'une fonction de récompense est difficile
- Les principales techniques incluent l'apprentissage supervisé comportemental, l'apprentissage par démonstration inverse (IRL) et l'apprentissage génératif antagoniste (GAIL)
- Un défi majeur est le problème de "distribution shift" où l'agent rencontre des situations non observées dans les démonstrations

## Détails

L'apprentissage par imitation se décline en plusieurs approches principales :

**Behavioral Cloning (BC)** : La méthode la plus simple qui traite l'imitation comme un problème d'apprentissage supervisé. L'agent apprend directement une correspondance entre les états et les actions en imitant les démonstrations de l'expert. Bien que simple à mettre en œuvre, cette approche souffre du problème de "distribution shift" - l'agent peut dévier de la trajectoire optimale et se retrouver dans des états jamais rencontrés pendant l'entraînement.

**[Inverse Reinforcement Learning](https://fr.wikipedia.org/wiki/Inverse_Reinforcement_Learning) (IRL)** : Cette approche tente d'abord d'inférer la fonction de récompense implicite que l'expert optimise, puis utilise cette récompense reconstruite pour entraîner un agent par apprentissage par renforcement. L'IRL permet une meilleure généralisation mais est computationnellement plus intensive.

**Generative Adversarial Imitation Learning (GAIL)** : Inspiré des réseaux antagonistes génératifs (GANs), GAIL entraîne simultanément un discriminateur qui distingue les comportements de l'expert de ceux de l'agent, et un générateur (l'agent) qui tente de produire des comportements indiscernables de ceux de l'expert. Cette méthode offre souvent de meilleures performances que le BC simple.

**Dataset Aggregation (DAgger)** : Cette technique itérative aborde le problème de distribution shift en collectant de nouvelles données d'expert dans les états visités par la politique apprise, puis en réentraînant la politique avec ces nouvelles données.

L'apprentissage par imitation trouve des applications dans de nombreux domaines :
- La robotique, où les robots apprennent des mouvements complexes à partir de démonstrations humaines
- La conduite autonome, où les véhicules apprennent à conduire en observant des conducteurs humains
- Les jeux vidéo, où les agents apprennent des stratégies complexes en observant des joueurs experts

Malgré ses avantages, l'apprentissage par imitation présente des limitations, notamment la dépendance à la qualité et à la quantité des démonstrations d'experts, ainsi que la difficulté à surpasser les performances de l'expert (plafond de performance). Les approches hybrides combinant imitation et apprentissage par renforcement sont souvent utilisées pour surmonter ces limitations.