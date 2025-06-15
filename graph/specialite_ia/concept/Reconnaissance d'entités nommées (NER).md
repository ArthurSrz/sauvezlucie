---
title: Reconnaissance d'entités nommées (NER)
type: concept
tags:
- NLP
- TALN
- NER
- extraction d'information
- traitement du langage
- entités nommées
- analyse textuelle
- classification textuelle
date_creation: '2025-03-20'
date_modification: '2025-03-20'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
uses: '[[Transformers et attention en NLP]]'
---
## Généralité

La [Reconnaissance d'Entités Nommées](https://fr.wikipedia.org/wiki/Reconnaissance_d%27entités_nommées) (NER) est une sous-tâche fondamentale du [traitement automatique du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) (TALN) qui vise à localiser et classifier des éléments textuels en catégories prédéfinies. Cette technologie, apparue dans les années 1990 avec les travaux pionniers de la conférence [MUC](https://fr.wikipedia.org/wiki/Message_Understanding_Conference) (Message Understanding Conference), permet d'extraire des informations structurées à partir de textes non structurés.

## Points clés

- Identifie et catégorise des segments de texte en entités prédéfines (personnes, lieux, organisations, etc.)
- Catégories standardisées incluent : PER (personnes), ORG (organisations), LOC (lieux), TIME (expressions temporelles), MONEY (montants monétaires), PERCENT (pourcentages)
- Utilise des approches modernes comme BERT et les architectures Transformer, atteignant des F1-scores autour de 90-93% sur des corpus standard
- Applications concrètes : extraction d'informations, analyse de documents juridiques, amélioration des moteurs de recherche, traitement automatique de CV
- Défis principaux : ambiguïté des entités, reconnaissance dans des domaines spécialisés, traitement multilingue

## Détails

La NER fonctionne en analysant le contexte dans lequel apparaissent les mots pour déterminer leur catégorie d'entité. Par exemple, dans la phrase "Apple a lancé un nouveau produit à New York mardi dernier", un système NER identifierait :
- "Apple" comme une organisation (type ORG)
- "New York" comme un lieu (type LOC) 
- "mardi dernier" comme une expression temporelle (type TIME)

Les systèmes modernes utilisent des annotations BIO (Begin, Inside, Outside) pour délimiter précisément les entités dans le texte. Historiquement, les premières approches de NER reposaient sur des règles manuelles et des dictionnaires. L'évolution s'est faite vers des techniques statistiques comme les [Modèles de Markov Cachés](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_Markov_cach%C3%A9) (HMM) et Champs Aléatoires Conditionnels (CRF), puis vers des architectures modernes telles que BiLSTM-CRF combinant des réseaux de neurones récurrents bidirectionnels avec des CRF, et plus récemment des modèles de langage pré-entraînés comme [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage)) (atteignant ~92% de F1-score sur CoNLL-2003), RoBERTa, XLNet adaptés via fine-tuning, ou encore des architectures à base de transformers comme LUKE.

Les principaux défis incluent l'ambiguïté des entités (ex: "Washington" peut être une personne, un lieu ou une organisation), la reconnaissance dans des domaines spécialisés (biomédical, juridique), le traitement multilingue pour les langues peu dotées, et la détection d'entités imbriquées ou se chevauchant.

Les applications sont nombreuses : systèmes de recherche d'information, analyse de sentiments ciblée, extraction d'information structurée, anonymisation automatique (domaine médical), indexation de documents et systèmes de recommandation (réseaux sociaux). Les corpus annotés standards utilisés pour l'évaluation incluent CoNLL-2003, OntoNotes 5.0 et WNUT-17, avec des métriques comme la précision, le rappel et le F1-score, bien que leur couverture limitée pour certains domaines soit un problème reconnu.