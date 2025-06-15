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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
uses:
- '[[Transformers et attention en NLP]]'
- '[[Modèles de langage génératifs pré-entraînés]]'
depends: '[[Similarité sémantique dans le traitement du langage naturel]]'
---
## Généralité

La [tokenisation](https://fr.wikipedia.org/wiki/Tokenisation_(informatique)) et la segmentation textuelle sont des processus fondamentaux en [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) (NLP) qui consistent à décomposer un texte en unités plus petites et manipulables. Ces étapes préliminaires transforment le texte brut en format structuré que les algorithmes de NLP peuvent traiter efficacement.

## Points clés

- La tokenisation divise le texte en tokens (mots, caractères ou sous-mots) selon différentes approches (word, character ou subword tokenization)
- La segmentation découpe le texte en unités plus larges comme des phrases ou des paragraphes
- Ces processus constituent la première étape de tout pipeline NLP et influencent directement les performances des systèmes
- Différentes langues nécessitent des approches spécifiques (ex: [Maximum Matching](https://fr.wikipedia.org/wiki/Algorithme_de_maximum_matching) pour le chinois)
- Des techniques avancées comme [Byte Pair Encoding](https://fr.wikipedia.org/wiki/Byte_pair_encoding) (BPE) sont devenues standard dans les modèles modernes

## Détails

La tokenisation peut s'effectuer selon différents types :

1. **Tokenisation par mots** : Divise le texte aux espaces et signes de ponctuation. Adaptée à l'anglais et aux langues romanes, mais moins efficace pour des langues comme l'allemand où les mots composés sont fréquents [source : Wikipédia "Word segmentation"].

2. **Tokenisation par caractères** : Décompose le texte en caractères individuels. Utile pour les langues à écriture non séparée comme le [chinois](https://fr.wikipedia.org/wiki/Chinois) ou le [japonais](https://fr.wikipedia.org/wiki/Japonais) [source : Wikipédia "Text segmentation"].

3. **Tokenisation par sous-mots** : Méthodes comme BPE, WordPiece ou SentencePiece qui offrent un bon compromis. Initialement développé pour la compression de données avant d'être adapté au NLP [sources : Wikipédia "Byte pair encoding" et "WordPiece"].

Les défis principaux incluent les ambiguïtés linguistiques (comme en allemand où la segmentation peut changer le sens), la gestion de la ponctuation (qui varie selon les langues comme le point-virgule inversé en arabe), la reconnaissance d'entités nommées (comme "New York") et le traitement des langues sans séparateurs (requérant des algorithmes spécifiques comme [Jieba](https://fr.wikipedia.org/wiki/Jieba) pour le chinois) [sources : Wikipédia "German orthography", "Arabic punctuation", "Chinese word segmentation"].

La segmentation en phrases doit gérer plusieurs complexités comme les abréviations (variant selon les langues), les nombres décimaux (avec des conventions différentes) et les acronymes. Les modèles modernes atteignent une précision élevée sur l'anglais (~98%) [source : Wikipédia "Sentence boundary disambiguation"].

Parmi les outils et bibliothèques populaires, on trouve :
- [NLTK (Natural Language Toolkit)](https://fr.wikipedia.org/wiki/Natural_Language_Toolkit) pour l'enseignement et la recherche
- spaCy, optimisé pour la production
- Stanford CoreNLP, efficace pour l'anglais
- Transformers (HuggingFace) avec des tokeniseurs spécifiques aux modèles comme [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage))

La qualité de ces opérations impacte directement la performance des systèmes de NLP ultérieurs [source : Wikipédia "Tokenization (lexical analysis)"].