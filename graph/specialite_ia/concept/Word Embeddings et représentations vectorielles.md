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
date_creation: '2025-03-20'
date_modification: '2025-03-20'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
uses: '[[Modèles de langage génératifs pré-entraînés]]'
isDefinedBy: '[[Similarité sémantique dans le traitement du langage naturel]]'
---
## Généralité

Les word embeddings (ou plongements lexicaux) sont des représentations vectorielles de mots dans un espace continu à N dimensions. Contrairement aux représentations one-hot qui traitent les mots comme des entités discrètes et indépendantes, les word embeddings capturent les relations sémantiques et syntaxiques entre les mots en les positionnant dans un espace vectoriel où la proximité reflète la similarité. Ces représentations denses permettent aux algorithmes d'apprentissage automatique de traiter efficacement le langage naturel en transformant les mots en vecteurs numériques manipulables mathématiquement.

## Points clés

- Les word embeddings transforment les mots en vecteurs denses de nombres réels dans un espace multidimensionnel où la distance et la direction entre vecteurs capturent des relations sémantiques
- Ils permettent de réaliser des opérations arithmétiques sur les mots (ex: "roi" - "homme" + "femme" ≈ "reine"), démontrant leur capacité à capturer des analogies linguistiques
- Les principales techniques incluent Word2Vec (CBOW et Skip-gram), GloVe, FastText et les embeddings contextuels comme ceux de BERT
- Les word embeddings constituent souvent la première couche des architectures de traitement du langage naturel modernes

## Détails

Les word embeddings sont générés par des algorithmes qui analysent de vastes corpus de textes pour apprendre les associations entre les mots basées sur leurs contextes d'apparition. Le principe fondamental est que "des mots qui apparaissent dans des contextes similaires tendent à avoir des significations similaires" (hypothèse distributionnelle).

Word2Vec, développé par Mikolov et al. chez [Google](https://fr.wikipedia.org/wiki/Google) en 2013, a popularisé deux architectures principales:
- CBOW (Continuous Bag of Words): prédit un mot à partir de son contexte
- Skip-gram: prédit le contexte à partir d'un mot donné

GloVe (Global Vectors), développé à Stanford, combine l'apprentissage de représentations locales (comme Word2Vec) avec des statistiques globales de co-occurrence de mots dans un corpus.

FastText, créé par Facebook Research, étend Word2Vec en représentant chaque mot comme un sac de n-grammes de caractères, permettant de gérer les mots hors vocabulaire et de capturer la morphologie.

Les dimensions typiques des word embeddings varient entre 50 et 300, chaque dimension capturant potentiellement différentes caractéristiques linguistiques. L'interprétabilité de ces dimensions reste cependant limitée.

Les embeddings contextuels, issus de modèles comme BERT, ELMo ou GPT, représentent une évolution majeure: contrairement aux embeddings statiques, ils génèrent des représentations dynamiques qui varient selon le contexte d'utilisation du mot, capturant ainsi la polysémie.

Les applications des word embeddings sont nombreuses:
- Analyse de sentiments
- Classification de textes
- Systèmes de recommandation
- Traduction automatique
- Recherche d'information
- Chatbots et assistants virtuels

Les limites incluent la difficulté à représenter les expressions idiomatiques, la sensibilité aux biais présents dans les données d'entraînement (genre, race, etc.), et l'incapacité des embeddings statiques à gérer la polysémie.

Les techniques d'évaluation comprennent des tests d'analogie (king:queen::man:woman), des benchmarks de similarité sémantique, et des évaluations extrinsèques sur des tâches spécifiques comme la classification de textes.