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
subClassOf: '[[Impact du choix des fonctions d''activation sur l''apprentissage profond]]'
---
## Généralité

Les fonctions d'activation [Swish](https://fr.wikipedia.org/wiki/Fonction_d%27activation#Swish) et [Mish](https://fr.wikipedia.org/wiki/Fonction_d%27activation) sont des fonctions non linéaires relativement récentes utilisées dans les [réseaux de neurones profonds](https://fr.wikipedia.org/wiki/Réseau_de_neurones_artificiels).

## Points clés

- Fonctions d'activation modernes dérivables partout
- Améliorent la propagation du gradient lors de l'apprentissage
- Offrent de meilleures performances que ReLU dans certains cas
- Combinaison de propriétés linéaires et non-linéaires
- Auto-gated: la sortie dépend dynamiquement de l'entrée

## Détails

La fonction Swish, proposée par Google en 2017, est définie par f(x) = x * sigmoïde(βx). Elle présente plusieurs avantages:
- Conserve l'information pour les entrées positives (comme ReLU)
- Permet une légère rétropropagation pour les entrées négatives (contrairement à ReLU)
- Paramètre β apprenable qui permet d'adapter la non-linéarité

La fonction Mish, introduite en 2019, est définie par f(x) = x * tanh(softplus(x)). Ses caractéristiques incluent:
- Continuité différentiable sur tout son domaine
- Minorée pour éviter l'évanouissement du gradient
- Meilleure conservation de l'information que Swish dans les couches profondes

Ces fonctions sont particulièrement efficaces pour:
- Les architectures profondes (>50 couches)
- Les tâches de classification complexe
- Les problèmes où ReLU montre des limitations

Comparaison avec ReLU:
- Meilleure propagation du gradient
- Moins sensible à l'initialisation des poids
- Réduction des neurones "morts"
- Coût computationnel légèrement supérieur

Applications typiques:
- Vision par ordinateur (classification d'images)
- Traitement du langage naturel
- Réseaux génératifs profonds