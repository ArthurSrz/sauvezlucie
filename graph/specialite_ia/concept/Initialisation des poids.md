---
title: Initialisation des poids
type: '[[Techniques de l''intelligence artificielle]]'
tags:
- réseaux de neurones
- apprentissage automatique
- initialisation des poids
- Xavier
- Glorot
- He
- convergence
- deep learning
date_creation: '2025-04-04'
date_modification: '2025-04-04'
relatedTo:
- '[[Fonction d''activation ReLU et ses variantes]]'
- '[[Fonctions d''activation sigmoïde et tangente hyperbolique]]'
- '[[Impact du choix des fonctions d''activation sur l''apprentissage profond]]'
subClassOf: '[[Optimiseurs adaptatifs]]'
---
## Généralité

L'[initialisation des poids](https://fr.wikipedia.org/wiki/Initialisation_des_poids_d%27un_réseau_de_neurones) est une étape cruciale dans l'entraînement des [réseaux de neurones](https://fr.wikipedia.org/wiki/Réseau_de_neurones_artificiels). Elle consiste à attribuer des valeurs initiales aux paramètres du modèle avant le début de l'apprentissage. Une bonne initialisation peut accélérer la convergence et améliorer les performances finales du modèle.

Historiquement, l'importance de l'initialisation a été mise en lumière par les travaux de [LeCun](https://fr.wikipedia.org/wiki/Yann_LeCun), Bengio et Glorot entre les années 1990 et 2010, qui ont contribué à formaliser mathématiquement les relations entre l'initialisation des poids et la stabilité de l'apprentissage.

## Points clés

- L'initialisation influence directement la vitesse de convergence et les performances finales du modèle
- Les méthodes principales incluent :
  - Initialisation aléatoire (normale ou uniforme)
  - Initialisation [Xavier/Glorot](https://fr.wikipedia.org/wiki/Initialisation_d%27un_r%C3%A9seau_de_neurones) (optimale pour sigmoïde/tanh)
  - Initialisation He (optimale pour [ReLU](https://fr.wikipedia.org/wiki/Rectifier_(neural_networks)))
- Une mauvaise initialisation peut causer :
  - [Vanishing gradient](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_gradient_qui_dispara%C3%AEt)
  - Exploding gradient
  - Problème de symétrie (si tous poids à zéro)

## Détails

### Méthodes d'initialisation

**Initialisation aléatoire**  
Distribution uniforme ou normale autour de zéro. Des études montrent qu'une initialisation aléatoire simple peut conduire à une variance des sorties qui varie avec la profondeur du réseau.

**Initialisation Xavier/Glorot**  
Proposée en 2010 par Glorot et Bengio, elle utilise une distribution normale avec une variance de 1/n (où n est le nombre de neurones d'entrée). Optimale pour les fonctions d'activation sigmoïde et tanh, elle aide à maintenir une variance constante des gradients durant l'apprentissage.

**Initialisation He**  
Développée par Kaiming He en 2015, elle utilise une variance de 2/n. Spécialement conçue pour les réseaux utilisant des fonctions d'activation ReLU, elle compense l'effet "dying ReLU".

**Initialisation orthogonale**  
Maintient la norme des gradients et est potentiellement bénéfique pour les réseaux très profonds (>50 couches). La méthode LSUV (Layer-sequential Unit-variance) ajuste les poids couche par couche.

### Considérations pratiques

Pour le choix de la méthode :
- Initialisation He recommandée pour ReLU
- Initialisation Xavier préférable pour sigmoïde/tanh
- Initialisation orthogonale ou LSUV pour réseaux très profonds

Problèmes à éviter :
- Initialisation à zéro (problème de symétrie)
- Valeurs trop grandes (gradients explosifs)
- Valeurs trop petites (vanishing gradient)

### Recherche récente

Le domaine de l'initialisation reste actif avec :
- Méthodes adaptatives (Self-gating) pour les architectures [Transformer](https://fr.wikipedia.org/wiki/Transformer_(machine_learning_model))
- Initialisations différentiables apprenables
- Techniques spécifiques pour réseaux ultra-profonds

Des benchmarks montrent que :
- L'initialisation He améliore la convergence de 30% pour les CNN avec ReLU
- L'initialisation Xavier reste compétitive pour les RNN avec tanh
- Les méthodes adaptatives réduisent significativement le temps d'entraînement sur les réseaux très profonds