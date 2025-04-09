---
title: 'Architecture d''un réseau neuronal '
type: concept
tags:
- réseaux neuronaux
- machine learning
- architecture IA
- couches neuronales
- apprentissage automatique
- deep learning
- modélisation IA
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf:
- '[[Réseaux neuronaux en IA]]'
- '[[Le perceptron multicouche]]'
relatedTo: '[[Apprentissage profond (Deep Learning)]]'
---
## Généralité

Un [réseau neuronal artificiel](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) est un système informatique inspiré du fonctionnement des neurones biologiques. Son architecture désigne la structure et l'organisation des couches et des neurones qui le composent, définissant comment les données circulent depuis l'entrée jusqu'à la sortie à travers différentes transformations mathématiques.

## Points clés

- Composé de trois types de couches : entrée, cachée(s) et sortie ([source Wikipédia](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels))
- Utilise des fonctions d'activation non-linéaires comme ReLU, sigmoïde ou tanh ([source Wikipédia](https://fr.wikipedia.org/wiki/Fonction_d%27activation))
- Apprentissage par rétropropagation du gradient ([source Wikipédia](https://fr.wikipedia.org/wiki/R%C3%A9tropropagation_du_gradient))
- Existe en plusieurs architectures spécialisées (CNN, RNN, Transformers)
- Performance influencée par le choix architectural et les hyperparamètres

## Détails

### Structure fondamentale

1. **Couches** :
   - **Couche d'entrée** : Reçoit les données brutes (pixels, mots, etc.)
   - **Couches cachées** : Effectuent des transformations intermédiaires (de quelques couches à des centaines pour le [deep learning](https://fr.wikipedia.org/wiki/Apprentissage_profond))
   - **Couche de sortie** : Produit le résultat final (classification, prédiction)

2. **Poids et biais** :
   Chaque connexion entre neurones a un poids ajusté pendant l'entraînement pour minimiser l'erreur.

### Fonctions d'activation

Introduisent de la non-linéarité essentielle pour modéliser des relations complexes :
- **ReLU** : max(0, x) - très utilisé dans les couches cachées
- **Sigmoïde** : transforme entre 0 et 1 - pour des probabilités
- **Softmax** : normalise les sorties en probabilités pour classification multiclasse
- **Tanh** : sorties entre -1 et 1 ([source Wikipédia](https://fr.wikipedia.org/wiki/Fonction_d%27activation))

### Principales architectures

- **Perceptron multicouche ([MLP](https://fr.wikipedia.org/wiki/Perceptron_multicouche))** : Plusieurs couches fully-connected
- **Réseaux convolutifs ([CNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif))** : Pour le traitement d'images avec couches de convolution
- **Réseaux récurrents ([LSTM](https://fr.wikipedia.org/wiki/Long_short-term_memory), [GRU](https://fr.wikipedia.org/wiki/Gated_recurrent_unit))** : Pour les séquences temporelles
- **Transformers ([BERT](https://fr.wikipedia.org/wiki/BERT_(language_model)), [GPT](https://fr.wikipedia.org/wiki/Generative_pre-trained_transformer))** : Basés sur des mécanismes d'attention ([source Wikipédia](https://fr.wikipedia.org/wiki/Transformer_(machine_learning_model)))

### Facteurs influençant l'architecture

- Nature des données (images, texte, séries temporelles...)
- Tâche spécifique (classification, régression, génération...)
- Contraintes matérielles et temporelles
- Compromis performance/complexité

Les techniques modernes incluent le dropout (prévention du surapprentissage) et les connexions résiduelles (facilitation de l'entraînement des réseaux profonds), comme le confirment les articles Wikipédia sur le [ResNet](https://fr.wikipedia.org/wiki/Residual_neural_network) et le dropout.