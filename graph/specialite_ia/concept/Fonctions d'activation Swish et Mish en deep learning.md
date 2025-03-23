---
title: Fonctions d'activation Swish et Mish en deep learning
type: concept
tags:
- deep learning
- fonctions d'activation
- Swish
- Mish
- réseaux de neurones
- Google Brain
- non-linéarité
- ReLU
- convergence
- apprentissage profond
date_creation: '2025-03-21'
date_modification: '2025-03-21'

- type: rdfs:subClassOf
  target: '[[Impact du choix des fonctions d''activation sur l''apprentissage profond]]'
---

## Généralité

Les fonctions d'activation Swish et Mish sont des fonctions non linéaires relativement récentes qui ont gagné en popularité dans les réseaux de neurones profonds. Introduites respectivement par Google Brain (Swish) en 2017 et par Diganta Misra (Mish) en 2019, ces fonctions représentent une alternative aux activations traditionnelles comme ReLU, en offrant des propriétés mathématiques avantageuses qui améliorent la performance et la convergence des modèles de deep learning.

## Points clés

- Swish est définie par f(x) = x · sigmoid(βx), combinant une multiplication par x et la fonction sigmoïde, où β est un paramètre ajustable
- Mish est définie par f(x) = x · tanh(softplus(x)), offrant une continuité C∞ et des dérivées non monotones
- Ces fonctions résolvent le problème du "dying ReLU" en permettant des gradients pour les valeurs négatives
- Swish et Mish sont auto-régularisantes et améliorent généralement la précision des modèles profonds sans coût computationnel significatif

## Détails

### Fonction Swish

Swish, développée par les chercheurs de Google Brain, est définie mathématiquement comme:

f(x) = x · sigmoid(βx) = x / (1 + e^(-βx))

Où β est un paramètre qui peut être fixe ou appris pendant l'entraînement. Lorsque β = 1, on parle simplement de Swish. Cette fonction possède plusieurs propriétés intéressantes:

- Elle est non bornée pour les valeurs positives (comme ReLU)
- Elle est légèrement négative pour certaines valeurs négatives d'entrée
- Elle est lisse et différentiable partout, contrairement à ReLU
- Sa dérivée ne souffre pas du problème de saturation comme la sigmoïde

Quand β tend vers l'infini, Swish se comporte comme ReLU, et quand β tend vers 0, elle se rapproche d'une fonction linéaire.

### Fonction Mish

Mish, proposée par Diganta Misra, est définie par:

f(x) = x · tanh(softplus(x)) = x · tanh(ln(1 + e^x))

Mish présente plusieurs avantages:

- Elle est continuellement différentiable (C∞)
- Elle préserve une légère information négative, ce qui aide à la régularisation
- Sa dérivée est non-monotone, permettant un meilleur flux de gradient
- Elle est bornée inférieurement mais non bornée supérieurement

### Comparaison et applications

Les expériences empiriques montrent que Swish et Mish surpassent généralement ReLU dans les architectures profondes comme ResNet, DenseNet et EfficientNet. Mish tend à offrir une légère amélioration par rapport à Swish dans plusieurs benchmarks.

Ces fonctions sont particulièrement efficaces dans:
- Les réseaux de neurones convolutifs profonds (CNN)
- Les tâches de classification d'images
- Les architectures avec de nombreuses couches

L'implémentation de ces fonctions est simple dans les frameworks modernes comme TensorFlow et PyTorch, avec un coût computationnel comparable à d'autres activations courantes, ce qui les rend pratiques pour une utilisation dans des applications réelles.