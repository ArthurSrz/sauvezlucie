---
title: Tokenisation et segmentation textuelle en NLP
type: concept
tags:
- NLP
- tokenisation
- segmentation
- traitement du langage
- text mining
- prétraitement
- analyse textuelle
- linguistique computationnelle
- tokens
- TAL
date_creation: '2025-03-20'
date_modification: '2025-03-20'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
uses:
- '[[Transformers et attention en NLP]]'
- '[[Modèles de langage génératifs pré-entraînés]]'
depends: '[[Similarité sémantique dans le traitement du langage naturel]]'
---
## Généralité

La tokenisation et la segmentation textuelle sont des processus fondamentaux en traitement du langage naturel (NLP) qui consistent à décomposer un texte en unités plus petites et manipulables. La tokenisation divise le texte en tokens (mots, caractères ou sous-mots), tandis que la segmentation découpe le texte en unités plus larges comme des phrases ou des paragraphes. Ces étapes préliminaires sont essentielles car elles transforment le texte brut en format structuré que les algorithmes de NLP peuvent traiter efficacement.

## Points clés

- La tokenisation est le processus de découpage d'un texte en unités élémentaires (tokens) qui peuvent être des mots, des caractères, des sous-mots ou des n-grammes
- La segmentation textuelle opère à un niveau plus élevé en divisant le texte en phrases, paragraphes ou sections thématiques
- Ces processus constituent généralement la première étape de tout pipeline de traitement du langage naturel
- Différentes langues et applications nécessitent des approches de tokenisation spécifiques (par exemple, les langues sans espaces comme le chinois)

## Détails

### Types de tokenisation

1. **Tokenisation par mots** : La méthode la plus intuitive qui divise le texte aux espaces et signes de ponctuation. Par exemple, "J'aime le NLP." devient ["J'", "aime", "le", "NLP", "."]. Cette approche présente des défis avec les contractions, les mots composés et les expressions idiomatiques.

2. **Tokenisation par caractères** : Décompose le texte en caractères individuels. Utile pour certaines tâches comme la correction orthographique ou pour les modèles qui travaillent au niveau des caractères.

3. **Tokenisation par sous-mots** : Méthodes comme BPE (Byte-Pair Encoding), WordPiece ou SentencePiece qui décomposent les mots en unités plus petites. Ces approches offrent un bon compromis entre la tokenisation par mots et par caractères, particulièrement efficaces pour gérer les mots rares et les langues morphologiquement riches.

### Défis de la tokenisation

- **Ambiguïtés linguistiques** : Par exemple, "l'homme" peut être tokenisé comme ["l'", "homme"] ou ["l", "'", "homme"]
- **Ponctuation** : Décider si la ponctuation constitue des tokens séparés ou s'attache aux mots
- **Entités nommées** : Reconnaître que "New York" devrait être considéré comme une seule entité
- **Langues sans séparateurs** : Le chinois, le japonais ou le thaï n'utilisent pas d'espaces entre les mots

### Segmentation en phrases

La segmentation en phrases identifie les limites des phrases dans un texte. Bien que les points (.) soient souvent des indicateurs de fin de phrase, de nombreuses exceptions existent :
- Abréviations (Dr., M., etc.)
- Nombres décimaux (3.14)
- Acronymes (U.S.A.)

Des algorithmes plus sophistiqués utilisent des règles linguistiques ou des modèles d'apprentissage automatique pour résoudre ces ambiguïtés.

### Outils et bibliothèques

Plusieurs bibliothèques offrent des fonctionnalités de tokenisation et segmentation :
- NLTK (Natural Language Toolkit)
- spaCy
- Stanford CoreNLP
- Transformers (HuggingFace) avec des tokeniseurs comme BERT, GPT, etc.

La qualité de la tokenisation et de la segmentation influence directement les performances des tâches NLP en aval comme la classification de texte, l'analyse de sentiment, la traduction automatique ou la génération de texte.