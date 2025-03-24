---
title: LSTM (Long Short-Term Memory)
type: concept
tags:
- deep learning
- réseaux de neurones
- LSTM
- RNN
- traitement séquentiel
- mémoire à long terme
- Hochreiter
- Schmidhuber
- apprentissage automatique
- intelligence artificielle
date_creation: '2025-03-18'
date_modification: '2025-03-18'
isPartOf:
- '[[Réseaux de neurones récurrents (RNN)]]'
- '[[Réseaux récurrents bidirectionnels]]'
subClassOf: '[[Réseaux de neurones récurrents (RNN)]]'
solves: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
relatedTo: '[[GRU (Gated Recurrent Units)]]'
---
## Généralité

Les LSTM (Long Short-Term Memory) sont un type spécial de réseaux de neurones récurrents (RNN) conçus pour résoudre le problème de la disparition du gradient dans les RNN traditionnels. Introduits par Hochreiter et Schmidhuber en 1997, les LSTM permettent de capturer efficacement les dépendances à long terme dans les données séquentielles, ce qui les rend particulièrement adaptés pour des tâches comme la reconnaissance vocale, la traduction automatique, la génération de texte et la prédiction de séries temporelles.

## Points clés

- Les LSTM résolvent le problème de la disparition du gradient grâce à une architecture de cellule spéciale avec des mécanismes de portes (gates)
- Chaque cellule LSTM contient trois portes principales: la porte d'oubli (forget gate), la porte d'entrée (input gate) et la porte de sortie (output gate)
- Les LSTM maintiennent deux états: l'état de cellule (cell state) qui sert de "mémoire à long terme" et l'état caché (hidden state) qui fonctionne comme une "mémoire de travail"
- Ils excellent dans le traitement de séquences où les informations contextuelles à long terme sont importantes

## Détails

L'architecture d'une cellule LSTM est conçue autour d'un mécanisme de portes qui contrôle le flux d'information. Ces portes sont des couches de neurones avec une fonction d'activation sigmoïde qui produisent des valeurs entre 0 et 1, déterminant quelle proportion d'information doit passer.

La **porte d'oubli** décide quelles informations de l'état précédent doivent être conservées ou supprimées. Elle examine l'état caché précédent et l'entrée actuelle, puis génère un vecteur de valeurs entre 0 (oublier complètement) et 1 (conserver entièrement).

La **porte d'entrée** détermine quelles nouvelles informations seront stockées dans l'état de la cellule. Elle comprend deux parties: une couche sigmoïde qui décide quelles valeurs seront mises à jour, et une couche tanh qui crée un vecteur de nouvelles valeurs candidates.

La **porte de sortie** contrôle quelles parties de l'état de la cellule seront transmises à l'état caché. L'état de la cellule est d'abord passé à travers une fonction tanh, puis multiplié par la sortie d'une couche sigmoïde qui détermine quelles informations seront transmises.

L'**état de cellule** (cell state) est le composant clé qui permet aux LSTM de conserver l'information sur de longues séquences. Il agit comme une autoroute qui transporte l'information à travers la chaîne de cellules avec seulement quelques interactions mineures.

Mathématiquement, les opérations d'une cellule LSTM peuvent être représentées par:

1. Porte d'oubli: ft = σ(Wf·[ht-1, xt] + bf)
2. Porte d'entrée: it = σ(Wi·[ht-1, xt] + bi)
3. Candidats à l'état de cellule: C̃t = tanh(WC·[ht-1, xt] + bC)
4. Mise à jour de l'état de cellule: Ct = ft * Ct-1 + it * C̃t
5. Porte de sortie: ot = σ(Wo·[ht-1, xt] + bo)
6. [État](https://fr.wikipedia.org/wiki/État) caché: ht = ot * tanh(Ct)

Les LSTM ont inspiré de nombreuses variantes, dont les GRU (Gated Recurrent Units) qui simplifient l'architecture tout en conservant des performances similaires. Malgré l'émergence des modèles Transformer, les LSTM restent pertinents pour de nombreuses applications de traitement de séquences, particulièrement lorsque les ressources computationnelles sont limitées.