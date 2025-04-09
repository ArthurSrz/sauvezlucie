---
title: Early stopping
type: concept
tags:
- machine learning
- early stopping
- surapprentissage
- optimisation
- validation
- apprentissage automatique
- régularisation
date_creation: '2025-04-08'
date_modification: '2025-04-08'
---
## Généralité

L'early stopping (ou arrêt précoce) est une technique d'optimisation utilisée en apprentissage automatique pour prévenir le surapprentissage (overfitting) lors de l'entraînement des modèles. Elle consiste à interrompre l'entraînement avant que le modèle ne commence à perdre en performance sur des données de validation.

## Points clés

- Technique de régularisation pour éviter le surapprentissage
- Surveille la performance sur un ensemble de validation pendant l'entraînement
- Arrête l'entraînement lorsque la performance se dégrade sur les données de validation
- Réduit le temps de calcul en évitant des itérations inutiles
- Peut être combinée avec d'autres techniques de régularisation

## Détails

L'early stopping fonctionne en divisant les données en trois ensembles : entraînement, validation et test. Pendant l'entraînement, le modèle est évalué périodiquement sur l'ensemble de validation. La technique implique généralement :

1. **Patience** : Nombre d'époques à attendre avant d'arrêter lorsque la performance ne s'améliore plus
2. **Delta minimum** : Seuil d'amélioration requis pour considérer qu'il y a progrès
3. **Restaurer les meilleurs poids** : Sauvegarde des paramètres du modèle au moment de sa meilleure performance

Les implémentations courantes incluent :
- Surveillance de la perte (loss) ou de la métrique de performance
- Critères d'arrêt basés sur des plateaux ou des dégradations
- Possibilité de reprendre l'entraînement (warm restart)

## Avantages et inconvénients

**Avantages :**
- Simple à implémenter
- Ne modifie pas le processus d'optimisation
- Économise du temps de calcul
- Fonctionne avec la plupart des architectures de modèles

**Inconvénients :**
- Nécessite un ensemble de validation séparé
- Peut arrêter trop tôt si la patience est mal configurée
- Moins efficace pour les problèmes où la perte fluctue naturellement

## Bonnes pratiques

- Choisir une métrique de validation pertinente pour le problème
- Ajuster la patience en fonction de la complexité du modèle
- Combiner avec d'autres techniques comme la réduction du taux de apprentissage
- Visualiser les courbes d'apprentissage pour choisir les paramètres