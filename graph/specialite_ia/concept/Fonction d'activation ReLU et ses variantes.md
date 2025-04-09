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

La fonction d'activation [ReLU](https://fr.wikipedia.org/wiki/Fonction_d%27activation#ReLU_(Rectified_Linear_Unit)) (Rectified Linear Unit) est l'une des fonctions d'activation les plus populaires dans les [réseaux de neurones profonds](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_profond). Introduite pour résoudre le problème de [disparition du gradient](https://fr.wikipedia.org/wiki/Disparition_du_gradient) rencontré avec les fonctions sigmoïde et tangente hyperbolique, ReLU est définie mathématiquement comme f(x) = max(0, x). Elle renvoie simplement la valeur d'entrée si celle-ci est positive, sinon elle renvoie zéro.

## Points clés

- [ReLU](https://fr.wikipedia.org/wiki/Fonction_d%27activation#ReLU) est définie par f(x) = max(0, x), ce qui signifie qu'elle produit 0 pour toute entrée négative et conserve les valeurs positives telles quelles
- Le principal avantage de ReLU est sa capacité à accélérer la convergence des réseaux profonds grâce à sa non-saturation pour les valeurs positives
- Le "problème des neurones morts" est une limitation connue de ReLU, où les neurones peuvent cesser d'apprendre si trop d'activations deviennent négatives
- Plusieurs variantes comme Leaky ReLU, PReLU, ELU et SELU ont été développées pour résoudre les limitations de la ReLU originale
- Historiquement, ReLU a été proposée dès 1969 par [Kunihiko Fukushima](https://fr.wikipedia.org/wiki/Kunihiko_Fukushima) mais popularisée après 2012

## Détails

La ReLU standard présente plusieurs avantages majeurs. Sa dérivée est soit 0 (pour les entrées négatives), soit 1 (pour les entrées positives), ce qui permet d'éviter la saturation du gradient pour les valeurs positives. 

Cette propriété accélère considérablement l'apprentissage par rapport aux fonctions [sigmoïde](https://fr.wikipedia.org/wiki/Sigmo%C3%AFde_(math%C3%A9matiques)) ou [tangente hyperbolique](https://fr.wikipedia.org/wiki/Tangente_hyperbolique). De plus, sa mise en œuvre computationnelle est extrêmement efficace. Cependant, ReLU souffre du "problème des neurones morts" (Dying ReLU) : lorsqu'un neurone produit systématiquement des sorties négatives, sa dérivée devient nulle, empêchant toute mise à jour des poids pendant la rétropropagation.

Parmi les variantes principales, on trouve :
- **Leaky ReLU** : f(x) = max(αx, x) où α est un petit coefficient positif
- **Parametric ReLU (PReLU)** : Similaire à Leaky ReLU, mais avec α appris pendant l'entraînement
- **Exponential Linear Unit (ELU)** : f(x) = x si x ≥ 0, sinon α(e^x - 1)
- **Scaled Exponential Linear Unit (SELU)** : Version d'ELU avec auto-normalisation
- **Swish** : f(x) = x·sigmoid(βx)
- **GELU** : xΦ(x), populaire dans les modèles comme [GPT](https://fr.wikipedia.org/wiki/Generative_Pre-trained_Transformer)

Le choix entre ReLU et ses variantes dépend de l'architecture du réseau et de la tâche. ReLU reste le choix par défaut pour sa simplicité et efficacité, tandis que ses variantes peuvent offrir de meilleures performances dans certains cas spécifiques.