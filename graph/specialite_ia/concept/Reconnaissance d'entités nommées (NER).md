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

La Reconnaissance d'Entités Nommées (NER) est une sous-tâche du traitement automatique du langage naturel (TALN) qui vise à localiser et classifier des éléments textuels en catégories prédéfinies telles que les noms de personnes, d'organisations, de lieux, d'expressions temporelles, de quantités, de valeurs monétaires, de pourcentages, etc. Cette technologie permet d'extraire des informations structurées à partir de textes non structurés, facilitant ainsi l'analyse et la compréhension automatique du contenu textuel.

## Points clés

- La NER identifie et catégorise des segments de texte en entités prédéfinies (personnes, lieux, organisations, dates, etc.)
- Elle constitue une étape fondamentale pour de nombreuses applications de TALN comme l'extraction d'information, les systèmes de question-réponse et la recherche d'information
- Les approches modernes de NER utilisent principalement l'apprentissage automatique, notamment les réseaux de neurones profonds comme BERT, RoBERTa ou les architectures BiLSTM-CRF
- L'évaluation des systèmes NER se fait généralement via les métriques de précision, rappel et F1-score

## Détails

La NER fonctionne en analysant le contexte dans lequel apparaissent les mots pour déterminer leur catégorie d'entité. Par exemple, dans la phrase "Apple a lancé un nouveau produit à New York mardi dernier", un système NER identifierait "Apple" comme une organisation, "New York" comme un lieu et "mardi dernier" comme une expression temporelle.

Historiquement, les premières approches de NER reposaient sur des règles manuelles et des dictionnaires. Ces méthodes ont progressivement évolué vers des techniques statistiques comme les Modèles de Markov Cachés (HMM) et les Champs Aléatoires Conditionnels (CRF). Aujourd'hui, les approches dominantes utilisent l'apprentissage profond.

Les architectures courantes pour la NER incluent:
- BiLSTM-CRF: combinant des réseaux de neurones récurrents bidirectionnels avec des CRF
- Modèles de langage pré-entraînés: BERT, RoBERTa, XLNet adaptés à la tâche de NER
- Architectures à base de transformers spécifiquement conçues pour la NER

La NER fait face à plusieurs défis:
1. L'ambiguïté des entités (ex: "Washington" peut être une personne, un lieu ou une organisation)
2. La reconnaissance d'entités dans des domaines spécialisés (médical, juridique, etc.)
3. Le traitement multilingue et la portabilité entre les langues
4. La détection d'entités imbriquées ou se chevauchant

Les applications de la NER sont nombreuses:
- Systèmes de recherche d'information améliorés
- Analyse de sentiments ciblée sur des entités spécifiques
- Extraction d'information structurée à partir de documents
- Anonymisation automatique de données sensibles
- Indexation et classification de documents
- Systèmes de recommandation basés sur les entités

Les corpus annotés comme CoNLL-2003, OntoNotes 5.0 ou WNUT-17 sont couramment utilisés pour l'entraînement et l'évaluation des systèmes NER, fournissant des références standardisées pour comparer les performances des différentes approches.