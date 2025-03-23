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
date_creation: '2025-03-20'
date_modification: '2025-03-20'

- type: isPartOf
  target: '[[Traitement du langage naturel (NLP)]]'
---

## Généralité

Les modèles N-gram sont des techniques probabilistes fondamentales en traitement du langage naturel (NLP) qui permettent de prédire l'occurrence d'un mot en fonction des N-1 mots qui le précèdent. Un N-gram est simplement une séquence contiguë de N éléments (généralement des mots ou des caractères) extraite d'un texte. Ces modèles reposent sur l'hypothèse markovienne selon laquelle la probabilité d'apparition d'un mot dépend uniquement d'un nombre limité de mots précédents, plutôt que de tout le contexte antérieur.

## Points clés

- Les N-grams sont classés selon leur taille: unigrams (N=1), bigrams (N=2), trigrams (N=3), etc., chacun capturant différents niveaux de dépendance contextuelle
- Ces modèles estiment les probabilités conditionnelles à partir des fréquences observées dans un corpus d'entraînement
- Les techniques de lissage (smoothing) comme Laplace, Good-Turing ou Kneser-Ney sont essentielles pour gérer les N-grams non observés dans les données d'entraînement
- Malgré leur simplicité, les N-grams restent pertinents pour de nombreuses applications de NLP comme la correction orthographique, la complétion automatique et la traduction automatique

## Détails

### Fonctionnement mathématique

Un modèle N-gram calcule la probabilité d'une séquence de mots en décomposant cette probabilité selon la règle de la chaîne:

P(w₁, w₂, ..., wₘ) = P(w₁) × P(w₂|w₁) × P(w₃|w₁,w₂) × ... × P(wₘ|w₁,...,wₘ₋₁)

L'approximation N-gram simplifie ce calcul en supposant que la probabilité d'un mot dépend uniquement des N-1 mots précédents:

P(wₙ|w₁,...,wₙ₋₁) ≈ P(wₙ|wₙ₋ₙ₊₁,...,wₙ₋₁)

Par exemple, dans un modèle trigram (N=3), on approxime:

P(wₙ|w₁,...,wₙ₋₁) ≈ P(wₙ|wₙ₋₂,wₙ₋₁)

### Estimation des probabilités

Les probabilités sont généralement estimées par maximum de vraisemblance à partir des fréquences relatives dans le corpus d'entraînement:

P(wₙ|wₙ₋ₙ₊₁,...,wₙ₋₁) ≈ count(wₙ₋ₙ₊₁,...,wₙ₋₁,wₙ) / count(wₙ₋ₙ₊₁,...,wₙ₋₁)

### Problème de rareté des données

Un défi majeur des modèles N-gram est le problème de rareté des données (data sparsity): de nombreuses séquences valides n'apparaissent jamais dans le corpus d'entraînement, ce qui conduit à des probabilités nulles. Pour résoudre ce problème, diverses techniques de lissage sont employées:

1. **Lissage de Laplace (Add-one)**: Ajoute 1 à tous les comptages
2. **Lissage de Good-Turing**: Réestime les probabilités en fonction de la fréquence des fréquences
3. **Lissage de Kneser-Ney**: Considère la diversité des contextes dans lesquels un mot apparaît
4. **Backoff et interpolation**: Combinent les estimations de modèles d'ordres inférieurs

### Limites et évolutions

Bien que les N-grams aient été largement supplantés par les modèles neuronaux pour de nombreuses tâches avancées de NLP, ils présentent plusieurs avantages:
- Simplicité conceptuelle et computationnelle
- Interprétabilité des résultats
- Efficacité pour certaines applications spécifiques

Les modèles de langue neuronaux modernes comme BERT, GPT et autres transformers peuvent être vus comme des extensions sophistiquées qui surmontent les limitations des N-grams traditionnels, notamment leur incapacité à capturer les dépendances à long terme et les relations sémantiques complexes.