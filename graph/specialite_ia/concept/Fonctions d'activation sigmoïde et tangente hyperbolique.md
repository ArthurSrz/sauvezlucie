---
title: Fonctions d'activation sigmoïde et tangente hyperbolique
type: concept
tags:
- réseaux de neurones
- fonctions d'activation
- sigmoïde
- tanh
- non-linéarité
- apprentissage automatique
- deep learning
- neurone artificiel
date_creation: '2025-03-21'
date_modification: '2025-03-21'
relatedTo: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
isPartOf: '[[Impact du choix des fonctions d''activation sur l''apprentissage profond]]'
---
## Généralité

Les fonctions d'activation sigmoïde et tangente hyperbolique (tanh) sont des fonctions non linéaires essentielles dans les réseaux de neurones artificiels. Elles transforment la somme pondérée des entrées d'un neurone en une sortie bornée, permettant au réseau d'apprendre des relations complexes et non linéaires entre les variables. Ces fonctions ont joué un rôle historique majeur dans le développement des réseaux de neurones avant l'avènement des fonctions d'activation plus modernes comme ReLU.

## Points clés

- La fonction sigmoïde transforme les valeurs d'entrée en une sortie comprise entre 0 et 1, ce qui la rend particulièrement adaptée pour modéliser des probabilités
- La fonction tangente hyperbolique (tanh) est similaire à la sigmoïde mais produit des valeurs entre -1 et 1, offrant une symétrie autour de l'origine
- Ces deux fonctions souffrent du problème de "vanishing gradient" lors de l'entraînement de réseaux profonds, limitant leur utilisation dans les architectures modernes
- Elles restent pertinentes dans certaines architectures spécifiques comme les LSTM et les GRU pour les problèmes de séquences

## Détails

### Fonction sigmoïde

La fonction sigmoïde est définie mathématiquement par :

σ(x) = 1/(1 + e^(-x))

Ses caractéristiques principales sont :
- Elle est continue et différentiable sur tout son domaine
- Sa dérivée est facilement calculable : σ'(x) = σ(x)(1 - σ(x))
- Elle compresse les valeurs d'entrée entre 0 et 1
- Elle présente une pente maximale autour de x = 0

Historiquement, la sigmoïde était très utilisée dans les couches de sortie pour les problèmes de classification binaire, où la sortie peut être interprétée comme une probabilité.

### Fonction tangente hyperbolique (tanh)

La fonction tanh est définie par :

tanh(x) = (e^x - e^(-x))/(e^x + e^(-x))

Ou alternativement : tanh(x) = 2σ(2x) - 1

Ses propriétés principales sont :
- Elle produit des valeurs entre -1 et 1
- Sa dérivée est : tanh'(x) = 1 - tanh²(x)
- Elle est symétrique par rapport à l'origine (tanh(0) = 0)
- Elle a une pente plus forte que la sigmoïde autour de zéro

### Limitations communes

Ces deux fonctions présentent des inconvénients significatifs :

1. **Problème du gradient qui s'évanouit** : Pour les valeurs d'entrée élevées (positives ou négatives), les dérivées de ces fonctions sont proches de zéro, ce qui ralentit considérablement l'apprentissage dans les couches profondes.

2. **Coût computationnel** : Le calcul des exponentielles est relativement coûteux comparé à des fonctions plus simples comme ReLU.

3. **Non-centrées sur zéro** : La sigmoïde n'est pas centrée sur zéro, ce qui peut compliquer la convergence lors de l'optimisation.

Malgré ces limitations, ces fonctions restent importantes dans certains contextes spécifiques, notamment dans les cellules de mémoire des réseaux récurrents où leur capacité à "saturer" les signaux est exploitée pour contrôler le flux d'information.