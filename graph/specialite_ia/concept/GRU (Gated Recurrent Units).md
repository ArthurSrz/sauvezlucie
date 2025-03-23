---
title: GRU (Gated Recurrent Units)
type: concept
tags:
- deep learning
- réseaux de neurones
- RNN
- GRU
- LSTM
- traitement de séquences
- apprentissage automatique
- dépendances temporelles
- Cho et al.
date_creation: '2025-03-18'
date_modification: '2025-03-18'
isPartOf: '[[Réseaux de neurones récurrents (RNN)]]'
isPartOf: '[[Réseaux récurrents bidirectionnels]]'
relatedTo: '[[LSTM (Long Short-Term Memory)]]'
rdfs:subClassOf: '[[Réseaux de neurones récurrents (RNN)]]'
relatedTo: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
---

## Généralité

Les GRU (Gated Recurrent Units) sont un type de réseau de neurones récurrents (RNN) introduit par Cho et al. en 2014 comme une alternative simplifiée aux LSTM (Long Short-Term Memory). Les GRU sont conçus pour résoudre le problème de disparition du gradient dans les RNN traditionnels tout en maintenant une architecture plus légère que les LSTM. Cette architecture permet aux GRU de modéliser efficacement des dépendances temporelles à long terme dans des séquences de données, ce qui les rend particulièrement utiles pour le traitement du langage naturel, la reconnaissance vocale et d'autres tâches impliquant des données séquentielles.

## Points clés

- Les GRU utilisent deux portes principales (gates) : la porte de mise à jour (update gate) et la porte de réinitialisation (reset gate), contrairement aux LSTM qui en utilisent trois.
- Ils sont généralement plus rapides à entraîner que les LSTM tout en offrant des performances comparables sur de nombreuses tâches.
- Les GRU peuvent mémoriser des informations sur de longues séquences sans souffrir du problème de disparition du gradient.
- Leur architecture simplifiée nécessite moins de paramètres, ce qui réduit les besoins en mémoire et en puissance de calcul.
- Ils sont particulièrement efficaces pour les tâches de modélisation de séquences où les dépendances à long terme sont importantes.

## Détails

### Architecture et fonctionnement

L'architecture GRU repose sur deux mécanismes de porte qui contrôlent le flux d'information :

1. **Porte de mise à jour (z)** : Détermine quelle proportion de l'information précédente doit être conservée et quelle proportion de la nouvelle information doit être intégrée. Elle fonctionne comme un mécanisme de mémoire à long terme.

2. **Porte de réinitialisation (r)** : Contrôle combien d'information passée doit être oubliée. Lorsque cette porte est proche de 0, l'unité est forcée d'ignorer l'état précédent et de se réinitialiser.

Les équations qui régissent le fonctionnement d'une cellule GRU sont :

- z_t = σ(W_z·[h_{t-1}, x_t] + b_z)
- r_t = σ(W_r·[h_{t-1}, x_t] + b_r)
- h̃_t = tanh(W·[r_t * h_{t-1}, x_t] + b)
- h_t = (1 - z_t) * h_{t-1} + z_t * h̃_t

Où σ est la fonction sigmoïde, * représente la multiplication élément par élément, et h_t est l'état caché à l'instant t.

### Avantages par rapport aux LSTM

Les GRU présentent plusieurs avantages par rapport aux LSTM :

- **Simplicité** : Avec moins de paramètres à apprendre, les GRU sont généralement plus rapides à entraîner.
- **Efficacité computationnelle** : Ils nécessitent moins de mémoire et de calculs.
- **Convergence plus rapide** : Sur certaines tâches, les GRU peuvent converger plus rapidement que les LSTM.

### Applications courantes

Les GRU sont largement utilisés dans :

- Le traitement du langage naturel (NLP)
- La traduction automatique
- La génération de texte
- La reconnaissance vocale
- L'analyse de séries temporelles
- La prédiction de séquences biologiques

Dans la pratique, le choix entre GRU et LSTM dépend souvent de la tâche spécifique et des contraintes de ressources, les deux architectures offrant des performances similaires sur de nombreuses applications.