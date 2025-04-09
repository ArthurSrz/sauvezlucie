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
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

Les fonctions d'activation sigmoïde et tangente hyperbolique (tanh) sont des fonctions non linéaires essentielles dans les réseaux de neurones artificiels. Elles permettent de transformer la somme pondérée des entrées d'un neurone en une sortie bornée, ce qui est crucial pour apprendre des relations complexes et non linéaires entre les variables. Leur nature différentiable est fondamentale pour l'algorithme de rétropropagation du gradient.

## Points clés

- **Sigmoïde** ([Wikipedia](https://fr.wikipedia.org/wiki/Sigmo%C3%AFde_(math%C3%A9matiques))) : Transforme les entrées en valeurs entre 0 et 1 (utile pour les probabilités)
- **Tanh** ([Wikipedia](https://fr.wikipedia.org/wiki/Tangente_hyperbolique)) : Produit des sorties entre -1 et 1 (convergence souvent plus rapide)
- **Problème de vanishing gradient** : Dérivées très petites pour les valeurs extrêmes (limite l'apprentissage profond)
- **Applications contemporaines** : Toujours utilisées dans les LSTM et pour les couches de sortie probabilistes
- **Historique** : Sigmoïde associée à Frank Rosenblatt (perceptron), tanh popularisée avec la rétropropagation

## Détails

### Fonction sigmoïde

La fonction [sigmoïde](https://fr.wikipedia.org/wiki/Sigmo%C3%AFde_(math%C3%A9matiques)) est définie mathématiquement par :

σ(x) = 1/(1 + e^(-x))

Ses caractéristiques principales sont :
- Continue et différentiable sur tout ℝ
- Dérivée : σ'(x) = σ(x)(1 - σ(x)) (gradient maximum de 0.25)
- Compresse les valeurs entre 0 et 1
- Forme en "S" caractéristique (monotone croissante)

Historiquement utilisée par [Frank Rosenblatt](https://fr.wikipedia.org/wiki/Frank_Rosenblatt) pour le [perceptron](https://fr.wikipedia.org/wiki/Perceptron) dans les années 1950.

### Fonction tangente hyperbolique (tanh)

La fonction [tanh](https://fr.wikipedia.org/wiki/Tangente_hyperbolique) est définie par :

tanh(x) = (e^x - e^(-x))/(e^x + e^(-x)) = 2σ(2x) - 1

Ses propriétés principales sont :
- Valeurs entre -1 et 1
- Dérivée : tanh'(x) = 1 - tanh²(x)
- Symétrique par rapport à l'origine
- Gradient maximum de 1 (pente plus forte que sigmoïde)

Popularisée par [Paul Werbos](https://fr.wikipedia.org/wiki/Paul_Werbos) dans les années 1970 pour la [rétropropagation](https://fr.wikipedia.org/wiki/R%C3%A9tropropagation_du_gradient).

### Limitations communes

1. **Gradient qui s'évanouit** : Dérivées proches de zéro pour les valeurs extrêmes
2. **Coût computationnel** : Calcul des exponentielles plus coûteux que ReLU
3. **Non-centrées sur zéro** (sauf tanh) : Peut compliquer la convergence

### Applications contemporaines

- Cellules de mémoire des réseaux récurrents ([LSTM](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_m%C3%A9moire_%C3%A0_long_terme))
- Couches de sortie pour classification binaire (sigmoïde)
- Réseaux de neurones probabilistes