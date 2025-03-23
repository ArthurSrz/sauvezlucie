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
rdfs:seeAlso: '[[LSTM (Long Short-Term Memory)]]'
rdfs:seeAlso: '[[GRU (Gated Recurrent Units)]]'
rdfs:seeAlso: '[[Réseaux récurrents bidirectionnels]]'
hasPart: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
isPartOf: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
hasPart: '[[LSTM (Long Short-Term Memory)]]'
hasPart: '[[GRU (Gated Recurrent Units)]]'
relatedTo: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
rdfs:subClassOf: '[[Apprentissage profond (Deep Learning)]]'
rdfs:subClassOf: '[[Réseaux neuronaux en IA]]'
---

## Généralité

Les Réseaux de Neurones Récurrents (RNN) sont une classe de réseaux de neurones artificiels spécialement conçus pour traiter des données séquentielles. Contrairement aux réseaux de neurones traditionnels qui traitent les entrées de manière indépendante, les RNN possèdent une "mémoire" qui leur permet de prendre en compte les informations précédemment traitées. Cette caractéristique les rend particulièrement adaptés pour l'analyse de séries temporelles, le traitement du langage naturel, la reconnaissance vocale et d'autres tâches où le contexte temporel est important.

## Points clés

- Les RNN possèdent des connexions récurrentes qui forment des cycles dans le réseau, permettant à l'information de persister
- Ils souffrent du problème de disparition ou d'explosion du gradient lors de l'apprentissage de dépendances à long terme
- Des variantes comme LSTM (Long Short-Term Memory) et GRU (Gated Recurrent Unit) ont été développées pour résoudre ces problèmes
- Les RNN sont fondamentaux pour de nombreuses applications modernes comme la traduction automatique, la génération de texte et la prédiction de séries temporelles

## Détails

### Architecture de base

Un RNN standard possède une boucle interne qui permet à l'information de circuler d'une étape de temps à la suivante. À chaque pas de temps t, le réseau reçoit une entrée x_t et produit une sortie y_t, tout en mettant à jour son état caché h_t qui sera utilisé à l'étape suivante. Mathématiquement, cela peut être représenté par:

h_t = f(W_hh · h_{t-1} + W_xh · x_t + b_h)
y_t = g(W_hy · h_t + b_y)

où f et g sont des fonctions d'activation, W représente les matrices de poids et b les biais.

### Problèmes et limitations

Le principal défi des RNN classiques est leur difficulté à capturer les dépendances à long terme dans les séquences. Ce phénomène, connu sous le nom de problème de disparition ou d'explosion du gradient, se produit lors de la rétropropagation du gradient à travers de nombreuses couches temporelles. Lorsque les gradients deviennent trop petits, l'apprentissage devient inefficace; lorsqu'ils explosent, les poids oscillent de manière chaotique.

### Variantes avancées

Pour surmonter ces limitations, plusieurs architectures avancées ont été développées:

- **LSTM (Long Short-Term Memory)**: Introduit des portes (d'entrée, d'oubli et de sortie) qui contrôlent le flux d'information, permettant au réseau de mémoriser ou d'oublier sélectivement des informations sur de longues périodes.
- **GRU (Gated Recurrent Unit)**: Une version simplifiée du LSTM avec moins de paramètres, combinant les portes d'entrée et d'oubli en une seule "porte de mise à jour".
- **Réseaux bidirectionnels**: Traitent les séquences dans les deux directions (avant et arrière) pour capturer des contextes plus riches.

### Applications

Les RNN et leurs variantes sont utilisés dans de nombreux domaines:
- Traduction automatique (séquence à séquence)
- Reconnaissance et synthèse vocale
- Génération de texte et de musique
- Prédiction de séries temporelles financières ou météorologiques
- Analyse de sentiments et classification de textes
- Systèmes de recommandation contextuels

Avec l'avènement des modèles d'attention et des transformers, les RNN purs sont moins utilisés dans certaines applications de pointe, mais leurs principes fondamentaux restent essentiels pour comprendre l'évolution des architectures de deep learning pour les données séquentielles.