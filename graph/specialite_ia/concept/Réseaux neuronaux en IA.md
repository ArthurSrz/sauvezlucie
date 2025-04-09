---
title: Réseaux neuronaux en IA
type: concept
tags:
- intelligence artificielle
- réseaux neuronaux
- machine learning
- IA
- deep learning
- algorithmes
- informatique
- data science
date_creation: '2025-04-08'
date_modification: '2025-04-08'
seeAlso:
- '[[Le perceptron multicouche]]'
- '[[Réseaux de neurones récurrents (RNN)]]'
- '[[Les GNN]]'
- '[[Réseau neuronal convolutif]]'
- '[[Réseaux de neurones auto-organisés (SOM)]]'
- '[[Réseaux à capsules (Capsule Networks)]]'
- '[[Architecture d''un réseau neuronal ]]'
subClassOf: '[[Techniques de l''intelligence artificielle]]'
createdBy:
- '[[Walter Pitts]]'
- '[[Warren McCulloch]]'
---
## Généralité

Les [réseaux neuronaux](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) sont des modèles informatiques inspirés du fonctionnement du [cerveau humain](https://fr.wikipedia.org/wiki/Cerveau_humain), constituant une technologie fondamentale de l'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) moderne. Ces systèmes sont composés de neurones artificiels interconnectés organisés en couches qui traitent l'information de manière distribuée et parallèle.

## Points clés

- Architecture en couches: entrée, cachée(s) et sortie
- Capacité d'apprentissage via la [rétropropagation du gradient](https://fr.wikipedia.org/wiki/R%C3%A9tropropagation_du_gradient)
- Utilisation de [fonctions d'activation](https://fr.wikipedia.org/wiki/Fonction_d%27activation) non-linéaires (ReLU, sigmoïde...)
- Variété d'architectures spécialisées (CNN, RNN, Transformers...)
- Applications étendues: vision par ordinateur, traitement du langage, diagnostic médical...

## Détails

Un [réseau neuronal artificiel](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) est typiquement organisé en couches: une couche d'entrée qui reçoit les données, une ou plusieurs couches cachées qui effectuent des transformations, et une couche de sortie qui produit le résultat. Chaque [neurone artificiel](https://fr.wikipedia.org/wiki/Neurone_artificiel) reçoit des signaux pondérés des neurones de la couche précédente, les combine (parfois avec un terme de biais ajouté), puis applique une fonction d'activation non-linéaire.

L'apprentissage d'un réseau neuronal se déroule généralement en trois phases: propagation avant où les données traversent le réseau de l'entrée vers la sortie, calcul de l'erreur par comparaison entre la sortie prédite et la sortie attendue, et rétropropagation qui ajuste les poids synaptiques pour minimiser l'erreur.

Parmi les principales architectures, on trouve le [Perceptron multicouche](https://fr.wikipedia.org/wiki/Perceptron_multicouche) (MLP) comme architecture de base, les réseaux convolutifs (CNN) spécialisés dans le traitement d'images, les réseaux récurrents (RNN) adaptés aux données séquentielles, les Transformers basés sur l'attention, et les réseaux antagonistes génératifs (GAN) pour générer des données synthétiques.

Les applications des réseaux neuronaux sont nombreuses et incluent la reconnaissance d'images et vision par ordinateur, le traitement du langage naturel, les systèmes de recommandation, le diagnostic médical, la conduite autonome et la génération de contenu. Cependant, ils présentent également des défis comme le besoin de grandes quantités de données, un coût computationnel élevé, un manque d'interprétabilité, une vulnérabilité aux attaques adverses et une sensibilité aux biais dans les données.