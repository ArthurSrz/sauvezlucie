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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Réseaux neuronaux en IA]]'
uses: '[[L''algorithme du gradient]]'
isPartOf: '[[Apprentissage profond (Deep Learning)]]'
seeAlso: '[[Architecture d''un réseau neuronal ]]'
---
## Généralité

Le [perceptron multicouche](https://fr.wikipedia.org/wiki/Perceptron_multicouche) (PMC ou MLP pour Multi-Layer Perceptron en anglais) est un type de [réseau de neurones artificiels](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) composé de plusieurs couches de neurones interconnectés. Contrairement au perceptron simple qui ne peut résoudre que des problèmes linéairement séparables, le perceptron multicouche peut modéliser des relations complexes et non linéaires entre les entrées et les sorties, ce qui en fait un outil puissant pour l'apprentissage automatique et la reconnaissance de formes.

## Points clés

- Architecture composée d'une couche d'entrée, une ou plusieurs couches cachées, et une couche de sortie (selon [Wikipédia](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels), cette structure minimale à 3 couches est nécessaire pour obtenir une capacité d'approximation universelle, comme démontré par [Cybenko](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_d%27approximation_universelle) en 1989 et [Hornik](https://fr.wikipedia.org/wiki/Kurt_Hornik) en 1991)
- Utilise des [fonctions d'activation](https://fr.wikipedia.org/wiki/Fonction_d%27activation) non linéaires (comme la sigmoïde, tanh ou ReLU) pour traiter les données - la [ReLU](https://fr.wikipedia.org/wiki/Rectified_linear_unit) (Rectified Linear Unit) est particulièrement populaire dans les réseaux profonds pour sa capacité à éviter le problème de gradient disparaissant
- Apprentissage par [rétropropagation du gradient](https://fr.wikipedia.org/wiki/R%C3%A9tropropagation_du_gradient) pour ajuster les poids des connexions (algorithme popularisé dans les années 1980 par Rumelhart et Hinton)
- Capable de résoudre des problèmes non linéairement séparables, contrairement au perceptron simple (grâce au théorème d'approximation universelle)

## Détails

Un [perceptron multicouche](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels#Perceptron_multicouche) (PMC ou MLP) est structuré en couches successives de neurones, comprenant au minimum une couche d'entrée, une ou plusieurs couches cachées et une couche de sortie. Chaque neurone d'une couche est connecté à tous les neurones de la couche suivante (architecture dite "fully connected"), formant ainsi un réseau entièrement connecté. Chaque connexion entre deux neurones possède un poids qui détermine l'importance du signal transmis. Chaque neurone applique une [fonction d'activation](https://fr.wikipedia.org/wiki/Fonction_d%27activation) non linéaire à la somme pondérée de ses entrées pour produire sa sortie.

L'apprentissage d'un perceptron multicouche se fait généralement par l'algorithme de [rétropropagation du gradient](https://fr.wikipedia.org/wiki/R%C3%A9tropropagation_du_gradient) (backpropagation). Ce processus comporte deux phases principales :
1. **Propagation avant** : Les données d'entrée sont transmises à travers le réseau pour générer une prédiction.
2. **Rétropropagation** : L'erreur entre la prédiction et la valeur cible est calculée via une fonction de coût, puis propagée en arrière à travers le réseau pour ajuster les poids des connexions.

Le perceptron multicouche est utilisé dans de nombreux domaines comme la classification d'images, la reconnaissance de formes, la prévision de séries temporelles, le traitement du langage naturel, l'approximation de fonctions complexes, les systèmes de recommandation, le diagnostic médical et la reconnaissance de la parole.

Malgré sa puissance, le perceptron multicouche présente certaines limitations comme le risque de surapprentissage, la difficulté à déterminer l'architecture optimale, les problèmes de disparition ou d'explosion du gradient, et le grand nombre de paramètres dans les architectures fully connected. Ces limitations ont conduit au développement d'architectures plus spécialisées comme les réseaux convolutifs ([CNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif)), les réseaux récurrents (RNN, LSTM), les [Transformers](https://fr.wikipedia.org/wiki/Transformer_(machine_learning)) et les architectures à connexions résiduelles (ResNet).