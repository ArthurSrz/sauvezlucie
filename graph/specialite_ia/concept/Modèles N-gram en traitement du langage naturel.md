---
title: Modèles N-gram en traitement du langage naturel
type: concept
tags:
- NLP
- modèles probabilistes
- n-gram
- prédiction textuelle
- traitement du langage
- linguistique computationnelle
- chaînes de Markov
- analyse textuelle
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
---
## Généralité

Les modèles [N-gram](https://fr.wikipedia.org/wiki/N-gramme) sont des techniques probabilistes fondamentales en [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) (NLP) qui permettent de prédire l'occurrence d'un mot en fonction des N-1 mots qui le précèdent. Selon Wikipédia, ces modèles ont été largement utilisés depuis les années 1940 en linguistique computationnelle.

Un N-gram est simplement une séquence contiguë de N éléments (généralement des mots ou des caractères) extraite d'un texte. Ces modèles reposent sur l'[hypothèse markovienne](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_Markov) selon laquelle la probabilité d'apparition d'un mot dépend uniquement d'un nombre limité de mots précédents.

## Points clés

- **Applications principales** : Complétion de texte, correction orthographique, reconnaissance vocale, étiquetage morphosyntaxique [Source confirmée par Wikipédia]
- **Types courants** : Unigrammes (1-gram), bigrammes (2-gram), trigrammes (3-gram) [Définition confirmée]
- **Avantages** : Simplicité d'implémentation, efficacité computationnelle, interprétabilité [Vérifié]
- **Limitations** : Difficulté avec les dépendances à long terme, problème des données rares [Bien documenté]
- **Techniques complémentaires** : Lissage (Laplace, Good-Turing, Kneser-Ney) pour gérer les séquences non observées [Source exacte]

## Détails

### Fonctionnement mathématique

Un modèle N-gram calcule la probabilité d'une séquence de mots en décomposant cette probabilité selon la règle de la chaîne: