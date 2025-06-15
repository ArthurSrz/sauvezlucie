---
title: Réseaux récurrents bidirectionnels
type: concept
tags:
- deep learning
- réseaux de neurones
- BiRNN
- traitement de séquences
- apprentissage automatique
- RNN
- modèles bidirectionnels
- NLP
- intelligence artificielle
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Réseaux de neurones récurrents (RNN)]]'
hasPart:
- '[[LSTM (Long Short-Term Memory)]]'
- '[[GRU (Gated Recurrent Units)]]'
isPartOf: '[[Architectures modulaires à commutation pour LLM spécialisés]]'
---
## Généralité

Les réseaux récurrents bidirectionnels ([Bidirectional Recurrent Neural Networks](https://fr.wikipedia.org/wiki/Réseau_de_neurones_récurrents) ou BiRNN) sont une extension des [réseaux de neurones récurrents](https://fr.wikipedia.org/wiki/Réseau_de_neurones_récurrents) (RNN) traditionnels qui permettent de traiter les séquences de données dans les deux directions : de gauche à droite et de droite à gauche. Cette architecture, introduite en 1997 par Schuster et Paliwal pour améliorer le [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel), combine deux couches récurrentes distinctes : une qui traite la séquence dans l'ordre chronologique et une autre dans l'ordre inverse.

## Points clés

- Les BiRNN utilisent deux couches RNN distinctes qui traitent les données dans des directions opposées (avant et arrière), puis combinent leurs sorties
- Ils capturent le contexte complet d'une séquence en intégrant les informations passées et futures pour chaque élément
- Ils sont particulièrement efficaces pour les tâches de [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) où le contexte bidirectionnel est crucial
- Ils constituent souvent la base des architectures [BiLSTM](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9current_%C3%A0_m%C3%A9moire_long_terme) et BiGRU
- Comparés aux RNN unidirectionnels, les BiRNN nécessitent environ deux fois plus de paramètres et de puissance de calcul

## Détails

Un [réseau récurrent bidirectionnel](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9current_bidirectionnel) (BiRNN) se compose de deux [RNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9current) indépendants : un réseau "forward" qui traite la séquence dans l'ordre chronologique (de gauche à droite) et un réseau "backward" qui traite la séquence dans l'ordre inverse (de droite à gauche).

Formellement, si nous avons une séquence d'entrée x = (x₁, x₂, ..., xₙ), le BiRNN calcule :
- Une séquence d'états cachés avant (forward) : h⃗ = (h⃗₁, h⃗₂, ..., h⃗ₙ)
- Une séquence d'états cachés arrière (backward) : h⃖ = (h⃖₁, h⃖₂, ..., h⃖ₙ)
- La sortie finale pour chaque position i est typiquement : yᵢ = f(h⃗ᵢ, h⃖ᵢ)

Les BiRNN sont particulièrement utiles pour des tâches comme la reconnaissance de la parole (où le contexte futur peut aider à désambiguïser les phonèmes), la traduction automatique (pour mieux comprendre la structure syntaxique), l'analyse de texte (comme dans les modèles BIOES pour la reconnaissance d'entités nommées), la reconnaissance d'entités nommées (modèles BIOES) et l'analyse de sentiment (pour capturer le contexte global d'une phrase).

Les versions modernes comme BiLSTM (Bidirectional Long Short-Term Memory) ont effectivement montré des performances améliorées dans divers domaines du traitement automatique du langage. Ces variantes résolvent le problème de la disparition du gradient et permettent de mieux modéliser les dépendances à long terme. Dans les implémentations modernes, les BiRNN sont souvent combinés avec des mécanismes d'attention pour améliorer encore leur capacité à se concentrer sur les parties pertinentes de la séquence d'entrée.