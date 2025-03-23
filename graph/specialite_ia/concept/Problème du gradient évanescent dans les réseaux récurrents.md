---
title: Problème du gradient évanescent dans les réseaux récurrents
type: concept
tags:
- deep learning
- réseaux de neurones récurrents
- RNN
- gradient évanescent
- rétropropagation
- BPTT
- apprentissage profond
- optimisation
- entraînement
date_creation: '2025-03-18'
date_modification: '2025-03-18'
isPartOf: '[[Réseaux de neurones récurrents (RNN)]]'
solvedBy: '[[LSTM (Long Short-Term Memory)]]'
hasPart: '[[Réseaux de neurones récurrents (RNN)]]'
---

## Généralité

Le problème du gradient évanescent est un obstacle majeur dans l'entraînement des réseaux de neurones récurrents (RNN). Ce phénomène se produit lorsque les gradients calculés lors de la rétropropagation du temps (BPTT) deviennent exponentiellement petits à mesure qu'ils sont propagés en arrière à travers les couches temporelles. En conséquence, les poids des connexions éloignées dans le temps ne sont pratiquement pas mis à jour, ce qui empêche le réseau d'apprendre les dépendances à long terme dans les séquences de données.

## Points clés

- Les gradients diminuent exponentiellement avec le nombre d'étapes temporelles, rendant l'apprentissage des dépendances à long terme difficile
- Ce problème est intrinsèquement lié à l'architecture des RNN classiques et à leur fonction d'activation
- Les solutions incluent les architectures LSTM, GRU, et d'autres techniques comme l'initialisation orthogonale et le gradient clipping
- Le problème dual du gradient explosif peut également survenir dans les RNN

## Détails

Dans un RNN standard, lors de la rétropropagation du temps, le gradient est multiplié par la matrice des poids récurrents à chaque étape temporelle. Mathématiquement, si la plus grande valeur propre de cette matrice est inférieure à 1, le gradient diminuera exponentiellement avec le nombre d'étapes temporelles. Pour une séquence longue, le gradient devient si petit qu'il est pratiquement nul, ce qui rend l'apprentissage inefficace.

Ce problème a été formellement identifié par Sepp Hochreiter et Jürgen Schmidhuber en 1991, qui ont ensuite proposé les Long Short-Term Memory (LSTM) comme solution en 1997. Les LSTM introduisent un mécanisme de "portes" qui permet au réseau de décider quelles informations doivent être conservées ou oubliées à chaque étape temporelle, créant ainsi des "autoroutes de gradient" qui facilitent la propagation des erreurs sur de longues séquences.

Les Gated Recurrent Units (GRU), proposées par Cho et al. en 2014, offrent une alternative plus légère aux LSTM tout en conservant leur capacité à atténuer le problème du gradient évanescent.

D'autres approches pour contrer ce problème incluent:

1. L'initialisation orthogonale des matrices de poids, qui aide à préserver la norme des gradients
2. Le gradient clipping, qui empêche les gradients de devenir trop grands (résolvant le problème dual du gradient explosif)
3. L'utilisation de connexions résiduelles (skip connections), comme dans les architectures ResNet
4. Les fonctions d'activation comme ReLU qui ne saturent pas pour les valeurs positives

Il est important de noter que le problème du gradient évanescent n'est pas unique aux RNN. Il peut également affecter les réseaux de neurones profonds feedforward, mais il est particulièrement sévère dans les RNN en raison du partage des poids à travers les étapes temporelles.

La compréhension de ce problème et de ses solutions a été cruciale pour les avancées dans le traitement des séquences, permettant des applications comme la traduction automatique, la reconnaissance vocale et la génération de texte qui nécessitent la capture de dépendances à long terme.