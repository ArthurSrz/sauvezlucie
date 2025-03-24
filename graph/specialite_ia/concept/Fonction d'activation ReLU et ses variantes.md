---
title: Fonction d'activation ReLU et ses variantes
type: concept
tags:
- deep learning
- réseaux de neurones
- ReLU
- fonction d'activation
- apprentissage profond
- gradient
- IA
- machine learning
- neural networks
date_creation: '2025-03-21'
date_modification: '2025-03-21'
isPartOf: '[[Impact du choix des fonctions d''activation sur l''apprentissage profond]]'
solves: '[[Problème du gradient évanescent dans les réseaux récurrents]]'
relatedTo: '[[Fonctions d''activation Swish et Mish en deep learning]]'
---
## Généralité

La fonction d'activation ReLU (Rectified Linear Unit) est l'une des fonctions d'activation les plus populaires dans les réseaux de neurones profonds. Introduite pour résoudre le problème de disparition du gradient rencontré avec les fonctions sigmoïde et tangente hyperbolique, ReLU est définie mathématiquement comme f(x) = max(0, x). Elle renvoie simplement la valeur d'entrée si celle-ci est positive, sinon elle renvoie zéro. Sa simplicité computationnelle et son efficacité ont conduit au développement de plusieurs variantes pour surmonter certaines de ses limitations.

## Points clés

- ReLU est définie par f(x) = max(0, x), ce qui signifie qu'elle produit 0 pour toute entrée négative et conserve les valeurs positives telles quelles
- Le principal avantage de ReLU est sa capacité à accélérer la convergence des réseaux profonds grâce à sa non-saturation pour les valeurs positives
- Le "problème des neurones morts" est la principale limitation de ReLU, où les neurones peuvent cesser d'apprendre si trop d'activations deviennent négatives
- Plusieurs variantes comme Leaky ReLU, PReLU, ELU et SELU ont été développées pour résoudre les limitations de la ReLU originale

## Détails

### ReLU standard

La ReLU standard présente plusieurs avantages majeurs. Sa dérivée est soit 0 (pour les entrées négatives), soit 1 (pour les entrées positives), ce qui permet d'éviter la saturation du gradient pour les valeurs positives. Cette propriété accélère considérablement l'apprentissage par rapport aux fonctions sigmoïde ou tangente hyperbolique. De plus, sa mise en œuvre computationnelle est extrêmement efficace.

Cependant, ReLU souffre du "problème des neurones morts" : lorsqu'un neurone produit systématiquement des sorties négatives, sa dérivée devient nulle, empêchant toute mise à jour des poids pendant la rétropropagation. Ce neurone devient alors "mort" et inutile pour le réseau.

### Variantes principales

**Leaky ReLU** : Définie par f(x) = max(αx, x) où α est un petit coefficient positif (typiquement 0.01). Elle permet une petite pente pour les valeurs négatives, évitant ainsi les neurones morts.

**Parametric ReLU (PReLU)** : Similaire à Leaky ReLU, mais le coefficient α devient un paramètre appris pendant l'entraînement, permettant au réseau de déterminer la pente optimale pour les valeurs négatives.

**Exponential Linear Unit (ELU)** : Définie par f(x) = x si x ≥ 0, sinon α(e^x - 1). ELU utilise une fonction exponentielle pour les valeurs négatives, ce qui peut aider à rapprocher la moyenne des activations vers zéro, accélérant l'apprentissage.

**Scaled Exponential Linear Unit (SELU)** : Une version d'ELU avec des paramètres spécifiques qui garantissent l'auto-normalisation des activations, réduisant le besoin de techniques comme la normalisation par lots.

**Swish** : Proposée par Google, définie par f(x) = x·sigmoid(βx), où β est un paramètre. Cette fonction a montré des performances supérieures dans certains réseaux profonds.

### Choix de la fonction d'activation

Le choix entre ReLU et ses variantes dépend souvent de l'architecture du réseau et de la tâche à accomplir. ReLU reste le choix par défaut pour de nombreuses applications en raison de sa simplicité et de son efficacité. Cependant, pour les réseaux très profonds ou les tâches où le problème des neurones morts est critique, les variantes comme Leaky ReLU ou ELU peuvent offrir de meilleures performances.