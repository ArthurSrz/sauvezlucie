---
title: Réseaux de neurones récurrents (RNN)
type: concept
tags:
- intelligence artificielle
- deep learning
- RNN
- réseaux de neurones
- données séquentielles
- séries temporelles
- traitement du langage
- mémoire artificielle
date_creation: '2025-03-18'
date_modification: '2025-03-18'
seeAlso:
- '[[LSTM (Long Short-Term Memory)]]'
- '[[GRU (Gated Recurrent Units)]]'
- '[[Réseaux récurrents bidirectionnels]]'
hasPart:
- '[[Problème du gradient évanescent dans les réseaux récurrents]]'
- '[[LSTM (Long Short-Term Memory)]]'
- '[[GRU (Gated Recurrent Units)]]'
isPartOf: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
relatedTo: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
subClassOf:
- '[[Apprentissage profond (Deep Learning)]]'
- '[[Réseaux neuronaux en IA]]'
---
où f et g sont des fonctions d'activation, W représente les matrices de poids et b les biais. L'état caché h_t encode ainsi l'information des étapes précédentes.

Le principal défi des RNN classiques est leur difficulté à capturer les dépendances à long terme dans les séquences. Ce phénomène, connu sous le nom de problème de disparition ou d'explosion du gradient, se produit lors de la rétropropagation du gradient à travers de nombreuses couches temporelles.

Parmi les variantes avancées des RNN, on trouve :
- **LSTM** : Introduit par Hochreiter et Schmidhuber en 1997, utilise des portes (d'entrée, d'oubli et de sortie) qui contrôlent le flux d'information
- **GRU** : Version simplifiée du LSTM avec moins de paramètres, proposé par Cho et al. en 2014
- **Réseaux bidirectionnels (Bi-RNN)** : Traitent les séquences dans les deux directions pour capturer des contextes plus riches

Les RNN et leurs variantes sont utilisés dans de nombreux domaines:
- **[Traitement du langage](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel)** : Traduction automatique, génération de texte, analyse de sentiments
- **Traitement du signal** : Reconnaissance vocale, synthèse vocale
- **Séries temporelles** : Prédiction boursière, modélisation météorologique
- **Bioinformatique** : Prédiction de structure protéique, analyse de séquences ADN
- **Création de contenu** : Génération de musique, reconnaissance d'écriture manuscrite
- **Systèmes de recommandation** contextuels

Bien que d'autres architectures comme les Transformers soient désormais souvent préférées pour certaines tâches, les principes fondamentaux des RNN restent essentiels pour comprendre l'évolution des architectures de deep learning pour les données séquentielles.