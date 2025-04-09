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
isPartOf:
- '[[Réseaux de neurones récurrents (RNN)]]'
- '[[Réseaux récurrents bidirectionnels]]'
relatedTo:
- '[[LSTM (Long Short-Term Memory)]]'
- '[[Problème du gradient évanescent dans les réseaux récurrents]]'
subClassOf: '[[Réseaux de neurones récurrents (RNN)]]'
---
## Généralité

Les [GRU](https://fr.wikipedia.org/wiki/Gated_recurrent_unit) (Gated Recurrent Units) sont un type de [réseau de neurones récurrents](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents) (RNN) introduit comme alternative simplifiée aux [LSTM](https://fr.wikipedia.org/wiki/Long_short-term_memory). Conçus pour résoudre le problème de disparition du gradient dans les RNN traditionnels, les GRU maintiennent une architecture plus légère que les LSTM avec seulement deux portes (update gate et reset gate) [Source: Wikipedia - Gated Recurrent Unit].

## Points clés

- Architecture simplifiée avec seulement 2 portes (contre 3 pour les LSTM) et environ 30% de paramètres en moins
- Résolution efficace du problème de [disparition du gradient](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_gradient_disparaisant) dans les RNN
- Performance souvent comparable aux LSTM tout en étant plus rapides à entraîner
- Applications étendues en [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel), traduction automatique et analyse de séries temporelles
- Flexibilité pour apprendre différentes dépendances temporelles (court et long terme)

## Détails

L'architecture [GRU](https://fr.wikipedia.org/wiki/Unit%C3%A9_r%C3%A9currente_%C3%A0_grille) repose sur deux mécanismes de porte :

1. **Porte de mise à jour (z)** : Détermine la proportion d'information précédente à conserver et de nouvelle information à intégrer, cruciale pour mémoriser des informations sur de longues séquences.

2. **Porte de réinitialisation (r)** : Contrôle la quantité d'information passée à oublier, permettant aux GRU d'apprendre différents types de dépendances temporelles.

Les équations gouvernant une cellule GRU sont :

- z_t = σ(W_z·[h_{t-1}, x_t] + b_z)
- r_t = σ(W_r·[h_{t-1}, x_t] + b_r)
- h̃_t = tanh(W·[r_t * h_{t-1}, x_t] + b)
- h_t = (1 - z_t) * h_{t-1} + z_t * h̃_t

Contrairement aux [LSTM](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9current_%C3%A0_m%C3%A9moire_long_terme), les GRU intègrent la fonction de mémoire directement dans leur état caché, simplifiant le flux d'information tout en maintenant une capacité similaire à capturer des motifs complexes [Source: Wikipedia - Gated Recurrent Unit].

Les avantages principaux des GRU par rapport aux LSTM incluent :

- **Simplicité** : Architecture réduite avec moins de paramètres
- **Efficacité computationnelle** : Moins de mémoire et calculs nécessaires
- **Convergence rapide** : Jusqu'à 30% plus rapide sur certaines tâches comme la modélisation de langage

Les GRU sont largement utilisés dans de nombreuses applications, notamment :

- Traitement du langage naturel (traduction automatique, génération de texte)
- Reconnaissance vocale
- Analyse de séries temporelles
- Prédiction de séquences biologiques

Le choix entre GRU et LSTM dépend souvent de la tâche spécifique et des contraintes de ressources, avec des performances globalement comparables sur de nombreuses applications [Source: Wikipedia - Long short-term memory].