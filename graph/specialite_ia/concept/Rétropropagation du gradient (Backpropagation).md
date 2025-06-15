---
title: Rétropropagation du gradient (Backpropagation)
type: concept
tags:
- réseaux de neurones
- apprentissage profond
- algorithme
- gradient
- optimisation
- machine learning
- backpropagation
date_creation: '2025-04-08'
date_modification: '2025-04-08'
uses:
- '[[Le perceptron multicouche]]'
- '[[Apprentissage profond (Deep Learning)]]'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
---
## Généralité

La [rétropropagation du gradient](https://fr.wikipedia.org/wiki/Rétropropagation_du_gradient) (Backpropagation) est un algorithme clé en apprentissage profond, utilisé pour entraîner les [réseaux de neurones artificiels](https://fr.wikipedia.org/wiki/Réseau_de_neurones_artificiels). Développée initialement par Paul Werbos en 1974 et popularisée par Rumelhart, Hinton et Williams en 1986, cette méthode permet un calcul efficace des gradients pour l'optimisation des paramètres du réseau.

## Points clés

- **Algorithme en deux phases** : Forward pass (calcul des sorties) et backward pass (propagation de l'erreur)
- **Calcul optimisé des gradients** : Utilisation de la règle de la chaîne du calcul différentiel
- **Large applicabilité** : Utilisé dans presque tous les modèles modernes (CNN, RNN, Transformers)
- **Problèmes connus** : Vanishing/exploding gradients et sensibilité à l'initialisation
- **Optimisation efficace** : Permet l'apprentissage de réseaux très profonds via des méthodes comme SGD, Adam

## Détails

### Fonctionnement

La rétropropagation fonctionne en deux phases principales :

1. **Phase avant (Forward Pass)** :
   - Propagation des données d'entrée à travers le réseau
   - Calcul des sommes pondérées et application des fonctions d'activation ([ReLU](https://fr.wikipedia.org/wiki/ReLU), sigmoïde, etc.)
   - Calcul de l'erreur entre sortie prédite et sortie attendue

2. **Phase arrière (Backward Pass)** :
   - Propagation de l'erreur à rebours selon la règle de la chaîne
   - Calcul des dérivées partielles de l'erreur par rapport à chaque poids
   - Mise à jour des poids via des méthodes d'optimisation

### Aspects mathématiques

Pour un neurone avec sortie \( a_j \) et fonction d'activation \( \sigma \), l'erreur \( \delta_j \) est calculée comme :
\[ \delta_j = \frac{\partial \mathcal{L}}{\partial a_j} \cdot \sigma'(z_j) \]

Les gradients des poids sont calculés par :
\[ \frac{\partial \mathcal{L}}{\partial w_{ij}} = \delta_j \cdot a_i \]

### Applications principales

- **Réseaux convolutifs ([CNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif))** : Vision par ordinateur
- **Réseaux récurrents ([RNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_r%C3%A9current))** : Traitement séquentiel
- **Transformers](https://fr.wikipedia.org/wiki/Transformeur_(apprentissage_automatique))** : Traitement du langage naturel
- **Réseaux profonds** : Applications diverses (médical, autonome, etc.)

### Limitations et solutions

- **Gradients disparaissants/explosifs** :
  - Problème : Gradients trop petits/grands dans réseaux profonds
  - Solutions : Connexions résiduelles ([ResNet](https://fr.wikipedia.org/wiki/R%C3%A9seau_r%C3%A9siduel)), fonctions ReLU

- **Surapprentissage** ([Surapprentissage](https://fr.wikipedia.org/wiki/Surapprentissage)) :
  - Solutions : Dropout, régularisation L1/L2, augmentation de données

- **Coût computationnel** :
  - Nécessité d'accélérateurs ([GPU](https://fr.wikipedia.org/wiki/Unit%C3%A9_de_traitement_graphique))
  - Complexité O(n×m) pour n exemples et m paramètres

- **Autres défis** :
  - Sensibilité à l'initialisation (solutions : Xavier/Glorot)
  - Besoin de données étiquetées en grande quantité