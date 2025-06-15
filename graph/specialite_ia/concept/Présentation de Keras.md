---
title: Présentation de Keras
type: concept
tags:
- Keras
- Deep Learning
- Python
- TensorFlow
- Machine Learning
date_creation: '2025-03-29'
date_modification: '2025-03-29'
subClassOf: '[[Frameworks Python pour le Deep Learning]]'
isPartOf: '[[Système de développement d''IA, principaux langages de programmation
  et frameworks]]'
---
## Généralité

Keras est une bibliothèque de [deep learning](https://fr.wikipedia.org/wiki/Apprentissage_profond) de haut niveau, écrite en [Python](https://fr.wikipedia.org/wiki/Python_(langage)), qui fonctionne comme une interface utilisateur pour [TensorFlow](https://fr.wikipedia.org/wiki/TensorFlow). Créée par François Chollet, ingénieur chez Google, Keras a été conçue pour permettre un prototypage rapide et une facilité d'utilisation, tout en offrant une grande flexibilité pour la construction de modèles de deep learning complexes. Initialement développée comme un projet indépendant, Keras a été intégrée à TensorFlow en 2017 comme son API haut niveau officielle (tf.keras).

## Points clés

- **Facilité d'utilisation** : API simple et cohérente, inspirée de Scikit-learn et Torch, avec des concepts modulaires comme les couches et optimiseurs prédéfinis
- **Flexibilité** : Supporte à la fois des modèles séquentiels simples et des architectures complexes via l'API fonctionnelle
- **Intégration avec TensorFlow** : Intégrée par défaut dans TensorFlow depuis 2019 (tf.keras), permettant d'utiliser toutes ses fonctionnalités avancées
- **Architecture modulaire** : Modèles construits en empilant des couches, offrant une grande flexibilité dans la conception
- **Large communauté** : Une des bibliothèques de deep learning les plus populaires, avec de nombreuses ressources disponibles

## Détails

Keras est basée sur une architecture modulaire, où les modèles sont construits en empilant des couches. Chaque couche est un objet qui reçoit des données en entrée, effectue une transformation, et transmet les résultats à la couche suivante. Cette modularité permet une grande flexibilité dans la conception des modèles, facilitant l'expérimentation et l'optimisation.

La bibliothèque offre une variété de couches, y compris les couches denses (fully connected), de [convolution](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_%C3%A0_convolutions), de pooling, de normalisation, de régularisation et d'embedding pour le traitement du langage naturel.

Le processus typique d'entraînement dans Keras comprend trois étapes principales : la compilation (spécification d'une fonction de perte, d'un optimiseur et de métriques d'évaluation), l'entraînement proprement dit (utilisation de la méthode `fit` avec données d'entraînement et étiquettes) et l'utilisation de callbacks pour des fonctionnalités comme l'early stopping et la sauvegarde automatique pendant l'entraînement.

Après l'entraînement, le modèle peut être évalué sur des données de test, utilisé pour faire des prédictions sur de nouvelles données ou intégré dans des pipelines plus complexes avec d'autres bibliothèques comme scikit-learn.

Historiquement, Keras supportait plusieurs backends comme Theano et Microsoft Cognitive Toolkit (CNTK), mais depuis la version 2.4.0 (2020), Keras ne supporte officiellement plus que TensorFlow comme backend.

Keras est largement adopté dans la recherche académique, le prototypage industriel et les projets open source. Sa philosophie de "rendre le deep learning accessible à tous" en fait un choix populaire pour les débutants comme pour les experts.