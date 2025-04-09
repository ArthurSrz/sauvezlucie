---
title: Word Embeddings et représentations vectorielles
type: concept
tags:
- NLP
- word embeddings
- traitement du langage
- vectorisation
- sémantique
- représentation continue
- plongements lexicaux
- apprentissage automatique
- linguistique computationnelle
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

Les [word embeddings](https://fr.wikipedia.org/wiki/Word_embedding) (ou plongements lexicaux) sont des représentations vectorielles de mots dans un espace continu à N dimensions. Développés initialement dans le domaine du [traitement automatique du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) (TALN), ces représentations sont devenues fondamentales pour de nombreuses applications comme la traduction automatique, l'analyse de sentiment ou la reconnaissance vocale.

## Points clés

- Les word embeddings transforment les mots en vecteurs denses (50-300 dimensions) capturant des relations sémantiques et syntaxiques
- Ils permettent des opérations arithmétiques sur les mots (ex: "roi" - "homme" + "femme" ≈ "reine")
- Les principales techniques incluent [Word2Vec](https://fr.wikipedia.org/wiki/Word2vec), GloVe, FastText et les embeddings contextuels comme [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage))
- Ils réduisent considérablement la dimensionnalité par rapport aux encodages one-hot traditionnels
- Ils capturent à la fois des similarités lexicales et certaines connaissances encyclopédiques

## Détails

### Principes et méthodologies
Les word embeddings sont générés par des algorithmes qui analysent de vastes corpus de textes pour apprendre les associations entre les mots basées sur leurs contextes d'apparition. Le principe fondamental repose sur l'hypothèse distributionnelle de [Zellig Harris](https://fr.wikipedia.org/wiki/Zellig_Harris) (1954) selon laquelle des mots apparaissant dans des contextes similaires ont des significations similaires.

Parmi les méthodes principales :
1. **[Word2Vec](https://fr.wikipedia.org/wiki/Word2vec)** (Mikolov et al., 2013) propose deux architectures :
   - CBOW (Continuous Bag of Words) prédit un mot à partir de son contexte
   - Skip-gram prédit le contexte à partir d'un mot donné
2. **[GloVe](https://fr.wikipedia.org/wiki/GloVe)** (Pennington et al., 2014) combine apprentissage de représentations locales et statistiques globales de matrice de co-occurrence
3. **[FastText](https://fr.wikipedia.org/wiki/FastText)** (Bojanowski et al., 2017) représente chaque mot comme un sac de n-grammes de caractères (3-6 caractères), permettant de gérer efficacement les mots hors vocabulaire

### Applications et performances
Les word embeddings trouvent des applications dans :
- Analyse de sentiments et classification de textes
- Systèmes de recommandation et recherche d'information
- Traduction automatique et assistants virtuels
- Chatbots et interfaces conversationnelles

Leurs performances sont évaluées à travers :
- Tests d'analogie et benchmarks de similarité sémantique
- Évaluations extrinsèques dans des tâches concrètes
- Mesures de réduction de biais et alignement avec [WordNet](https://fr.wikipedia.org/wiki/WordNet)

### Limites et défis
Malgré leur efficacité, les word embeddings présentent plusieurs limitations :
- Gestion difficile des expressions idiomatiques et de la polysémie
- Sensibilité aux biais présents dans les données d'entraînement
- Problèmes avec les mots rares et capture involontaire de stéréotypes
- Interprétabilité limitée des dimensions vectorielles
- Transition nécessaire vers des embeddings contextuels plus avancés ([BERT](https://fr.wikipedia.org/wiki/BERT_(langage)), ELMo, GPT) pour certains cas d'usage

Les caractéristiques techniques principales incluent des dimensions typiques entre 50 et 300, avec une évolution marquée vers des modèles contextuels capables de mieux représenter la polysémie et les nuances linguistiques.