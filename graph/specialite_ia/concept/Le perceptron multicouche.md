---
title: Le perceptron multicouche
type: concept
tags:
- perceptron multicouche
- intelligence artificielle
- réseaux de neurones
- apprentissage automatique
- deep learning
- modèles computationnels
date_creation: '2025-03-17'
date_modification: '2025-03-17'
subClassOf: '[[Réseaux neuronaux en IA]]'
uses: '[[L''algorithme du gradient]]'
isPartOf: '[[Apprentissage profond (Deep Learning)]]'
---
##Généralité

Le perceptron multicouche (PMC ou MLP pour Multi-Layer Perceptron en anglais) est un type de réseau de neurones artificiels composé de plusieurs couches de neurones interconnectés. Contrairement au perceptron simple qui ne peut résoudre que des problèmes linéairement séparables, le perceptron multicouche peut modéliser des relations complexes et non linéaires entre les entrées et les sorties, ce qui en fait un outil puissant pour l'apprentissage automatique et la reconnaissance de formes.

## Points clés

- Architecture composée d'une couche d'entrée, une ou plusieurs couches cachées, et une couche de sortie
- Utilise des fonctions d'activation non linéaires (comme la sigmoïde, tanh ou ReLU) pour traiter les données
- Apprentissage par rétropropagation du gradient pour ajuster les poids des connexions
- Capable de résoudre des problèmes non linéairement séparables, contrairement au perceptron simple
- Forme la base de l'apprentissage profond moderne lorsqu'il comporte de nombreuses couches cachées

## Détails

### Architecture et fonctionnement

Un perceptron multicouche est structuré en couches successives de neurones. Chaque neurone d'une couche est connecté à tous les neurones de la couche suivante, formant ainsi un réseau entièrement connecté (fully connected). L'information circule de la couche d'entrée vers la couche de sortie en passant par les couches cachées intermédiaires.

Chaque connexion entre deux neurones possède un poids qui détermine l'importance du signal transmis. Chaque neurone applique une fonction d'activation à la somme pondérée de ses entrées pour produire sa sortie. Les fonctions d'activation non linéaires comme la sigmoïde, la tangente hyperbolique (tanh) ou la ReLU (Rectified Linear Unit) permettent au réseau de modéliser des relations complexes.

### Apprentissage par rétropropagation

L'apprentissage d'un perceptron multicouche se fait généralement par l'algorithme de rétropropagation du gradient (backpropagation). Ce processus comporte deux phases principales :

1. **Propagation avant** : Les données d'entrée sont transmises à travers le réseau pour générer une prédiction.
2. **Rétropropagation** : L'erreur entre la prédiction et la valeur attendue est calculée, puis propagée en arrière à travers le réseau pour ajuster les poids des connexions.

L'objectif est de minimiser une fonction de coût (ou fonction de perte) qui mesure l'écart entre les prédictions du réseau et les valeurs réelles. Cette minimisation est généralement réalisée par descente de gradient.

### Applications

Le perceptron multicouche est utilisé dans de nombreux domaines :

- Classification d'images et reconnaissance de formes
- Prévision de séries temporelles
- Traitement du langage naturel
- Approximation de fonctions complexes
- Systèmes de recommandation

### Limites et évolutions

Malgré sa puissance, le perceptron multicouche présente certaines limitations :
- Risque de surapprentissage (overfitting) sur des données d'entraînement limitées
- Difficulté à déterminer l'architecture optimale (nombre de couches et de neurones)
- Problèmes de disparition ou d'explosion du gradient dans les réseaux profonds

Ces limitations ont conduit au développement d'architectures plus avancées comme les réseaux convolutifs (CNN), les réseaux récurrents (RNN) et les transformers, qui sont mieux adaptés à certains types de données et de problèmes spécifiques.