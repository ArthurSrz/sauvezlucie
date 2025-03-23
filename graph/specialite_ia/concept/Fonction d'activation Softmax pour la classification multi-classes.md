---
title: Fonction d'activation Softmax pour la classification multi-classes
type: concept
tags:
- machine learning
- réseaux de neurones
- classification
- softmax
- fonction d'activation
- probabilités
- multi-classes
- deep learning
- couche de sortie
- distribution de probabilités
date_creation: '2025-03-21'
date_modification: '2025-03-21'

- type: rdfs:subClassOf
  target: '[[Impact du choix des fonctions d''activation sur l''apprentissage profond]]'
---

## Généralité

La fonction d'activation Softmax est une généralisation de la fonction logistique pour les problèmes de classification multi-classes. Elle transforme un vecteur de valeurs réelles en une distribution de probabilités sur plusieurs classes, où la somme des probabilités est égale à 1. Softmax est particulièrement utilisée dans la couche de sortie des réseaux de neurones pour les tâches de classification où chaque entrée doit être classée dans une seule catégorie parmi plusieurs options possibles.

## Points clés

- Softmax convertit un vecteur de scores (logits) en probabilités normalisées entre 0 et 1 dont la somme est égale à 1
- Elle accentue les différences entre les valeurs d'entrée, rendant la classe la plus probable encore plus dominante
- Contrairement à d'autres fonctions d'activation, Softmax prend en compte les relations entre toutes les classes simultanément
- Elle est différentiable, ce qui la rend compatible avec les algorithmes d'apprentissage par rétropropagation du gradient

## Détails

La fonction Softmax est définie mathématiquement comme suit:

Pour un vecteur z = [z₁, z₂, ..., zₙ], la fonction Softmax calcule:

σ(z)ᵢ = e^(zᵢ) / Σⱼ e^(zⱼ)

Où σ(z)ᵢ représente la probabilité de la classe i, e est la base du logarithme naturel, et le dénominateur est la somme des exponentielles de toutes les composantes du vecteur z.

Lorsque Softmax est appliquée, les valeurs les plus élevées du vecteur d'entrée sont amplifiées de manière exponentielle, tandis que les valeurs plus faibles sont réduites, créant ainsi un contraste plus marqué entre les classes. Cette propriété est particulièrement utile pour la classification, car elle permet d'identifier clairement la classe la plus probable.

Dans un réseau de neurones pour la classification multi-classes, l'architecture typique comprend:
1. Une couche de sortie avec autant de neurones que de classes possibles
2. L'application de la fonction Softmax sur les sorties brutes (logits) de cette couche
3. L'utilisation de l'entropie croisée comme fonction de perte pour mesurer l'écart entre les probabilités prédites et les étiquettes réelles

La dérivée de la fonction Softmax est également importante pour l'apprentissage par rétropropagation. Elle présente une forme particulière qui permet un calcul efficace du gradient lors de l'entraînement.

Une propriété intéressante de Softmax est sa sensibilité à l'échelle: l'ajout d'une constante à toutes les entrées ne change pas le résultat final, mais la multiplication de toutes les entrées par un facteur peut modifier significativement la distribution des probabilités, rendant la distribution plus ou moins "pointue".

## Applications

Softmax est utilisée dans de nombreuses applications de deep learning, notamment:
- La reconnaissance d'images (classification d'objets)
- Le traitement du langage naturel (classification de textes, analyse de sentiments)
- La reconnaissance vocale
- Les systèmes de recommandation basés sur la classification