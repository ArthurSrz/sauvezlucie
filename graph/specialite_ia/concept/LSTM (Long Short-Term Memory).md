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

Les [LSTM](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_%C3%A0_m%C3%A9moire_%C3%A0_long_terme) (Long Short-Term Memory) sont un type spécial de [réseaux de neurones récurrents](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents) (RNN) conçus pour résoudre le problème de la disparition du gradient dans les RNN traditionnels. Introduits par Hochreiter et Schmidhuber en 1997, les LSTM se distinguent par leur architecture unique comprenant des "portes" qui régulent le flux d'information.

## Points clés

- Résolvent efficacement le problème de la [disparition du gradient](https://fr.wikipedia.org/wiki/Disparition_du_gradient) grâce à une architecture de cellule spéciale
- Architecture basée sur trois portes principales: porte d'oubli, porte d'entrée et porte de sortie
- Maintiennent deux états distincts: état de cellule (mémoire à long terme) et état caché (mémoire de travail)
- Excellents pour les tâches nécessitant des dépendances à long terme comme la [reconnaissance vocale](https://fr.wikipedia.org/wiki/Reconnaissance_automatique_de_la_parole) et la [traduction automatique](https://fr.wikipedia.org/wiki/Sequence_to_sequence_learning)
- Ont inspiré des architectures plus récentes comme les [GRU](https://fr.wikipedia.org/wiki/Unit%C3%A9_r%C3%A9currente_ferm%C3%A9e) et les [transformers](https://fr.wikipedia.org/wiki/Transformer_(machine_learning_model))

## Détails

L'architecture d'une [cellule LSTM](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_r%C3%A9current#LSTM) est conçue autour d'un mécanisme de portes qui contrôle le flux d'information. Ces portes sont des couches de neurones avec une [fonction d'activation sigmoïde](https://fr.wikipedia.org/wiki/Fonction_sigmo%C3%AFde) qui produisent des valeurs entre 0 et 1.

Les composants principaux comprennent:
- **Porte d'oubli**: Détermine quelles informations de l'état précédent doivent être conservées ou supprimées
- **Porte d'entrée**: Détermine quelles nouvelles informations seront stockées dans l'état de la cellule
- **Porte de sortie**: Contrôle quelles parties de l'état de la cellule seront transmises à l'état caché
- **État de cellule**: Composant clé permettant de conserver l'information sur de longues séquences
- **État caché**: Fonctionne comme une mémoire de travail pour les calculs immédiats

Les opérations mathématiques d'une cellule LSTM peuvent être représentées par:
1. Porte d'oubli: ft = σ(Wf·[ht-1, xt] + bf)
2. Porte d'entrée: it = σ(Wi·[ht-1, xt] + bi)
3. Candidats à l'état de cellule: C̃t = tanh(WC·[ht-1, xt] + bC)
4. Mise à jour de l'état de cellule: Ct = ft * Ct-1 + it * C̃t
5. Porte de sortie: ot = σ(Wo·[ht-1, xt] + bo)
6. État caché: ht = ot * tanh(Ct)

Les LSTM ont inspiré de nombreuses variantes:
- **LSTM bidirectionnelles (BiLSTM)**: Analysent les séquences dans les deux directions temporelles
- **LSTM empilées (stacked LSTM)**: Ajoutent des couches supplémentaires pour capturer des motifs plus complexes
- **GRU**: Simplifient l'architecture tout en conservant des performances comparables

Ces réseaux ont démontré leur efficacité dans de nombreux domaines:
- [Reconnaissance vocale](https://fr.wikipedia.org/wiki/Reconnaissance_automatique_de_la_parole)
- Traduction automatique ([Sequence to sequence learning](https://fr.wikipedia.org/wiki/Sequence_to_sequence_learning))
- Analyse de séries temporelles financières
- [Traitement automatique du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel)

Bien que les architectures transformer gagnent en popularité, les LSTM restent pertinents pour certaines applications, particulièrement dans des contextes où les ressources sont limitées ou lorsque la stabilité des gradients est importante.