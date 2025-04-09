---
title: Dropout
type: concept
tags:
- deep learning
- régularisation
- surapprentissage
- réseaux de neurones
- apprentissage automatique
- dropout
- optimisation
date_creation: '2025-04-08'
date_modification: '2025-04-08'
---
## Généralité

Le dropout est une technique de régularisation utilisée en apprentissage profond pour prévenir le surapprentissage (overfitting). Il consiste à désactiver aléatoirement un certain pourcentage de neurones pendant l'entraînement, ce qui force le réseau à apprendre des représentations plus robustes.

## Points clés

- Technique de régularisation efficace contre le surapprentissage
- Désactive aléatoirement des neurones pendant l'entraînement (mais pas pendant l'inférence)
- Force le réseau à ne pas dépendre excessivement de neurones spécifiques
- Améliore souvent la généralisation du modèle
- Paramétré par un taux de dropout (généralement entre 0.2 et 0.5)

## Détails

Le dropout fonctionne en "éteignant" temporairement chaque neurone avec une probabilité p (taux de dropout) à chaque étape d'entraînement. Les neurones désactivés ne contribuent pas à la propagation avant (forward pass) ni ne reçoivent de gradients pendant la rétropropagation (backward pass).

Pendant l'inférence (phase de test), tous les neurones sont actifs, mais leurs poids sont multipliés par p pour maintenir l'échelle des activations. Cette approche est appelée "inverted dropout" et est la plus couramment implémentée.

Le dropout peut être vu comme:
- Une forme d'ensembling: à chaque batch, le réseau voit une architecture légèrement différente, ce qui équivaut approximativement à entraîner un ensemble de réseaux
- Un régularisateur qui empêche la co-adaptation excessive des neurones

Variantes notables:
- Spatial Dropout: désactive des canaux entiers dans les couches convolutives
- DropConnect: désactive des connexions de poids plutôt que des neurones
- Alpha Dropout: conçu pour les réseaux à normalisation SELU, préserve les propriétés d'auto-normalisation

## Applications pratiques

Le dropout est particulièrement utile:
- Dans les grands réseaux avec beaucoup de paramètres
- Lorsque la quantité de données d'entraînement est limitée
- Combiné avec d'autres techniques de régularisation comme la normalisation par lots

Il est moins efficace pour les petits réseaux ou lorsque le surapprentissage n'est pas un problème majeur. Le choix du taux de dropout optimal dépend de l'architecture et du problème, nécessitant souvent une validation croisée.