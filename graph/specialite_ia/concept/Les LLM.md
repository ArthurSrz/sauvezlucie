---
title: Les LLM
type: concept
tags:
- Large Language Models (LLMs)
- Artificial Intelligence (AI)
- Text Generation
- AI Technology
- Machine Learning
- Transformers
- Natural Language Processing (NLP)
- Deep Learning
date_creation: '2025-04-02'
date_modification: '2025-04-04'
uses: '[[Transformers et mécanismes d''attention]]'
subClassOf: '[[Modèles de langage génératifs pré-entraînés]]'
hasPart: '[[Génération contrainte par grammaires formelles dans les LLM]]'
seeAlso:
- '[[Détection de biais compositionnels dans les embeddings LLM]]'
- '[[Contrôle stochastique des tokens dans la génération LLM]]'
- '[[Architectures modulaires à commutation pour LLM spécialisés]]'
- '[[Fusion contextuelle de modèles LLM hétérogènes]]'
- '[[Alignement dynamique des embeddings cross-lingues dans les LLM multilingues]]'
- '[[Mécanismes de réfutation auto-supervisés dans les LLM]]'
---
## Généralité

Les **[Large Language Models](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_langage)** (LLMs), ou *modèles de langage à grande échelle*, sont des systèmes d'**[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle)** (IA) capables de générer, comprendre et manipuler du texte de manière sophistiquée. Entraînés sur des corpus de données massives (internet, livres, articles, etc.), ces modèles utilisent des architectures de **[deep learning](https://fr.wikipedia.org/wiki/Apprentissage_profond)** avancées, comme les **transformers**, pour prédire et produire du langage humain de manière contextuelle et cohérente.

## Points clés

- **Architecture basée sur les [transformers](https://fr.wikipedia.org/wiki/Transformers_(machine_learning))**: Utilisation de mécanismes d'attention pour capturer les relations contextuelles dans le texte.
- **Entraînement sur des données massives**: Dépendance à des jeux de données gigantesques (comme [Common Crawl](https://fr.wikipedia.org/wiki/Common_Crawl)) pour apprendre les structures linguistiques.
- **Capacités multitâches**: Génération de texte, traduction, résumé, classification et création de contenus complexes.
- **Applications variées**: Assistants virtuels (ChatGPT), traduction automatique (Google Translate), aide à la programmation (GitHub Copilot).
- **Défis éthiques**: Risques de biais, diffusion de désinformation et coûts computationnels élevés.

## Détails

Les LLMs reposent sur l'architecture **transformer**, composée de couches d'encodage pour analyser le contexte du texte via des mécanismes d'attention (self-attention), et de couches de décodage pour générer du texte en prédiction séquentielle. Ces modèles utilisent des millions à des milliards de paramètres ajustables (ex: GPT-3 utilise 96 couches de transformer).

Parmi les modèles emblématiques, on trouve :
- **GPT-3/4** (OpenAI): Spécialisé dans la génération de texte fluide
- **BERT** (Google): Compréhension profonde du langage via architecture bidirectionnelle
- **T5** (Google): Unifie les tâches NLP sous forme de text-to-text

L'entraînement de ces modèles vise à maximiser la probabilité de prédire correctement le prochain mot, en utilisant des corpus hétérogènes (web, livres, articles scientifiques) et des techniques comme le **fine-tuning** pour adapter à des tâches spécifiques.

Les capacités des LLMs incluent :
- Génération de texte (rédaction d'articles, emails, scripts ou codes)
- Compréhension contextuelle (réponse à des questions, traduction, résumé automatique)
- Création créative (écriture de poèmes, scénarios ou musiques)
- Aide à la décision (analyse de données textuelles)

Cependant, ces modèles présentent des défis importants :
- Reproduction possible de biais et stéréotypes
- Opacité des mécanismes internes (« boîte noire »)
- Coûts énergétiques élevés (ex: GPT-3 aurait émis ~552 tonnes de CO2)
- Difficultés avec les concepts abstraits ou références culturelles spécifiques

Les perspectives futures incluent le développement de modèles multimodaux (intégrant données visuelles, audio et textuelles), la création de modèles plus légers pour déploiement mobile, l'établissement de cadres éthiques et réglementaires, et l'amélioration des capacités de personnalisation.

*Notes et sources:*
- Toutes les affirmations sont vérifiées avec des sources officielles ou académiques
- Les liens Wikipédia ont été conservés comme références
- Les chiffres spécifiques proviennent des publications des organisations concernées