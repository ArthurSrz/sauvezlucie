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
date_creation: '2025-03-22'
date_modification: '2025-03-22'
isPartOf:
- '[[Traitement du langage naturel (NLP)]]'
- '[[Apprentissage profond (Deep Learning)]]'
- '[[Modèles de langage génératifs pré-entraînés]]'
hasPart:
- '[[Modèles de langage génératifs pré-entraînés]]'
- '[[Traduction automatique neuronale]]'
---
## Généralité

Les Transformers sont une architecture de réseau neuronal introduite en 2017 par Vaswani et al. dans l'article "Attention is All You Need". Cette architecture a révolutionné le traitement du langage naturel (NLP) en remplaçant les réseaux récurrents (RNN) par un mécanisme d'attention qui permet de traiter les séquences en parallèle plutôt que séquentiellement. Le mécanisme d'attention permet au modèle de se concentrer sur différentes parties d'une séquence d'entrée lors de la génération de chaque élément de sortie, ce qui améliore considérablement les performances sur diverses tâches linguistiques.

## Points clés

- Les Transformers utilisent un mécanisme d'attention multi-têtes qui permet au modèle de se concentrer simultanément sur différentes parties d'une séquence d'entrée
- L'architecture Transformer est composée d'encodeurs et de décodeurs empilés, chacun contenant des couches d'attention et des réseaux feed-forward
- Contrairement aux RNN, les Transformers traitent les séquences en parallèle, ce qui permet un entraînement plus rapide et une meilleure capture des dépendances à long terme
- Les modèles basés sur les Transformers comme BERT, GPT, T5 et autres ont établi de nouveaux standards de performance dans presque toutes les tâches de NLP

## Détails

### Mécanisme d'attention

Le cœur de l'architecture Transformer est le mécanisme d'attention, qui permet au modèle de pondérer l'importance de différents mots dans une phrase lors du traitement d'un mot spécifique. L'attention fonctionne en calculant des scores de compatibilité entre une requête (query) et un ensemble de clés (keys), puis en utilisant ces scores pour pondérer les valeurs (values) associées.

L'attention multi-têtes divise l'espace de représentation en plusieurs sous-espaces, permettant au modèle d'apprendre différents types de relations entre les mots (syntaxiques, sémantiques, etc.) dans chaque tête d'attention.

### Architecture complète

Un Transformer standard comprend:
1. Une couche d'embedding qui convertit les tokens en vecteurs
2. Un encodage positionnel qui ajoute l'information sur la position des mots
3. Une pile d'encodeurs (pour comprendre l'entrée)
4. Une pile de décodeurs (pour générer la sortie)
5. Une couche de sortie linéaire

Chaque encodeur contient une couche d'attention multi-têtes suivie d'un réseau feed-forward. Les décodeurs ont une structure similaire mais incluent une couche d'attention supplémentaire qui prend en compte les sorties de l'encodeur.

### Avantages par rapport aux architectures précédentes

Les Transformers présentent plusieurs avantages par rapport aux RNN et LSTM:
- Parallélisation: tous les mots sont traités simultanément
- Capture efficace des dépendances à longue distance
- Pas de problème de disparition du gradient
- Meilleure performance sur des séquences longues

### Applications majeures

Les Transformers ont donné naissance à de nombreux modèles influents:
- BERT (Bidirectional Encoder Representations from Transformers): préentraîné pour comprendre le contexte bidirectionnel
- GPT (Generative Pre-trained Transformer): spécialisé dans la génération de texte
- T5 (Text-to-Text Transfer Transformer): qui reformule toutes les tâches NLP en problèmes de texte à texte
- XLNet, RoBERTa, ALBERT: variantes améliorées de BERT

Ces modèles ont transformé le domaine du NLP en permettant des performances sans précédent sur des tâches comme la traduction, la classification de texte, la réponse aux questions et la génération de texte.