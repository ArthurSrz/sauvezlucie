---
title: Apprentissage continu (Continual Learning)
type: concept
tags:
- intelligence artificielle
- apprentissage automatique
- continual learning
- IA
- machine learning
- apprentissage continu
- modèles adaptatifs
date_creation: '2025-03-29'
date_modification: '2025-03-29'
relatedTo:
- '[[Fonctions de perte en apprentissage profond]]'
- '[[Apprentissage par renforcement]]'
uses: '[[Véhicules autonomes et systèmes de navigation IA]]'
subClassOf: '[[Apprentissage non supervisé]]'
---
## Généralité

L'apprentissage continu (Continual Learning) est un domaine de l'intelligence artificielle qui se concentre sur la capacité d'un système d'apprentissage automatique à acquérir de nouvelles connaissances tout en conservant les compétences précédemment apprises, sans oublier ces dernières. Contrairement aux approches traditionnelles d'apprentissage automatique où les modèles sont entraînés une seule fois sur un ensemble de données statique, l'apprentissage continu vise à développer des systèmes capables d'apprendre de manière incrémentale à partir de flux de données en évolution, tout comme les humains apprennent tout au long de leur vie.

## Points clés

- L'apprentissage continu cherche à résoudre le problème de l'oubli catastrophique (catastrophic forgetting), où les modèles perdent leurs connaissances antérieures lorsqu'ils sont entraînés sur de nouvelles données.
- Il permet aux systèmes d'IA d'adapter leurs connaissances dans des environnements dynamiques et de s'améliorer progressivement sans nécessiter un réentraînement complet.
- Les applications incluent la robotique, les assistants personnels, les systèmes de recommandation et tout système d'IA devant évoluer avec le temps.
- Différentes stratégies sont employées, comme la régularisation, la répétition d'expériences passées, et l'architecture modulaire.

## Détails

### Défis de l'apprentissage continu

Le principal défi de l'apprentissage continu est l'oubli catastrophique. Lorsqu'un réseau neuronal est entraîné sur de nouvelles données, les poids du réseau sont ajustés pour minimiser l'erreur sur ces nouvelles données, ce qui peut effacer ou altérer significativement les connaissances précédemment acquises. Ce phénomène est particulièrement problématique dans les environnements réels où les données et les tâches évoluent constamment.

### Approches principales

Plusieurs approches ont été développées pour aborder ces défis :

1. **Méthodes basées sur la régularisation** : Elles ajoutent des contraintes lors de l'apprentissage de nouvelles tâches pour préserver les connaissances importantes des tâches précédentes. Des exemples incluent Elastic Weight Consolidation (EWC) et Synaptic Intelligence.

2. **Méthodes basées sur la mémoire** : Elles maintiennent un ensemble d'exemples représentatifs des tâches précédentes (replay buffer) et les réutilisent lors de l'apprentissage de nouvelles tâches. Des techniques comme iCaRL et Experience Replay entrent dans cette catégorie.

3. **Méthodes architecturales** : Elles modifient l'architecture du réseau pour accommoder de nouvelles tâches sans perturber les connaissances existantes. Progressive Neural Networks et PathNet sont des exemples de cette approche.

4. **Méthodes hybrides** : Elles combinent plusieurs des approches ci-dessus pour obtenir de meilleures performances.

### Applications pratiques

L'apprentissage continu est crucial pour les systèmes d'IA déployés dans le monde réel qui doivent s'adapter à des environnements changeants :

- Les robots qui doivent apprendre de nouvelles tâches sans oublier les précédentes
- Les assistants virtuels qui s'améliorent avec l'interaction utilisateur
- Les systèmes de diagnostic médical qui intègrent de nouvelles connaissances médicales
- Les véhicules autonomes qui doivent s'adapter à de nouvelles conditions routières

L'apprentissage continu représente une étape importante vers des systèmes d'IA plus adaptatifs et autonomes, capables d'apprendre et d'évoluer de manière similaire aux humains, en accumulant des connaissances tout au long de leur "vie".