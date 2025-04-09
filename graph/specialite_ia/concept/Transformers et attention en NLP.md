---
title: Transformers et attention en NLP
type: concept
tags:
- NLP
- Transformers
- Attention
- Deep Learning
- Architecture neuronale
- Vaswani
- Traitement du langage
- IA
- Réseaux de neurones
- Machine Learning
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf:
- '[[Traitement du langage naturel (NLP)]]'
- '[[Apprentissage profond (Deep Learning)]]'
- '[[Modèles de langage génératifs pré-entraînés]]'
hasPart:
- '[[Modèles de langage génératifs pré-entraînés]]'
- '[[Traduction automatique neuronale]]'
sameAs: '[[Transformers et mécanismes d''attention]]'
seeAlso: '[[Architectures neuronales à couches d''attention emboîtées pour l''analyse
  multiniveau]]'
---
## Généralité

Les [Transformers](https://fr.wikipedia.org/wiki/Transformers_(machine_learning)) sont une architecture révolutionnaire de réseau neuronal introduite en 2017 par Vaswani et al. dans l'article "Attention is All You Need". Cette architecture a radicalement transformé le [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) (NLP) en remplaçant les réseaux récurrents (RNN) et convolutifs (CNN) par un mécanisme d'auto-attention multi-têtes permettant un traitement parallèle des séquences.

## Points clés

- Mécanisme d'[attention multi-têtes](https://fr.wikipedia.org/wiki/Attention_(machine_learning)) permettant au modèle de se concentrer simultanément sur différentes parties d'une séquence
- Architecture composée d'encodeurs et de décodeurs empilés (6 couches dans l'implémentation originale) avec des connexions résiduelles et de la [normalisation par couches](https://fr.wikipedia.org/wiki/Normalisation_de_couche)
- Traitement parallèle des séquences contrairement aux [RNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9current), permettant un entraînement plus rapide sur GPU/TPU
- Encodage positionnel utilisant des fonctions sinus/cosinus pour injecter l'information de position
- Modèles dérivés influents comme [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage)) et [GPT](https://fr.wikipedia.org/wiki/Generative_pre-trained_transformer)

## Détails

Le cœur de l'architecture [Transformer](https://fr.wikipedia.org/wiki/Transformeur_(apprentissage_automatique)) est le mécanisme d'attention, qui permet de pondérer l'importance de différents mots dans une phrase. L'attention fonctionne en calculant des scores de compatibilité entre une requête (query) et un ensemble de clés (keys), puis en utilisant ces scores pour pondérer les valeurs (values) associées. L'attention multi-têtes divise l'espace de représentation en plusieurs sous-espaces (typiquement 8 têtes), permettant d'apprendre différents types de relations entre les mots. Chaque tête opère en parallèle sur des sous-espaces de dimension réduite.

Un Transformer standard comprend:
- Couche d'embedding convertissant les tokens en vecteurs
- Encodage positionnel utilisant des fonctions sinus/cosinus spécifiques
- Pile de N encodeurs (N=6 dans l'implémentation originale) contenant chacun:
  - Couche d'attention multi-têtes
  - Réseau feed-forward à deux couches
  - Connexions résiduelles et normalisation par couches
- Pile de N décodeurs avec:
  - Attention masquée
  - Couche d'attention croisée prenant en compte les sorties de l'encodeur
- Couche de sortie linéaire suivie d'un softmax

Comparé aux [RNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents) et [LSTM](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_m%C3%A9moire_court-long_terme), les Transformers offrent plusieurs avantages:
- Parallélisation complète: tous les mots sont traités simultanément
- Meilleure capture des dépendances à longue distance
- Réduction significative des problèmes de disparition du gradient
- Performance accrue sur des séquences longues
- Efficacité computationnelle supérieure pour les longues séquences

Les applications majeures incluent:
- [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage)): modèle utilisant uniquement l'encodeur
- GPT: série de modèles utilisant uniquement le décodeur
- T5: architecture unifiant toutes les tâches NLP en format texte-à-texte
- Variantes spécialisées comme Transformer-XL pour les séquences très longues ou Vision Transformer (ViT) pour le traitement d'images

Les Transformers ont établi des records de performance sur divers benchmarks:
- [GLUE](https://fr.wikipedia.org/wiki/General_Language_Understanding_Evaluation) (+7.7% pour BERT-base)
- SQuAD 2.0 (F1 score de 92.2)
- WMT14 (BLEU de 28.4)
- SuperGLUE (score de 90.8 pour T5-11B)