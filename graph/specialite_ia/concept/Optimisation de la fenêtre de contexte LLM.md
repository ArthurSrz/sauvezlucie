---
title: Optimisation de la fenêtre de contexte LLM
type: concept
tags:
- LLM
- Fenêtre de contexte
- Optimisation
- Gestion de la mémoire
- Tokens
- Performance des modèles
- IA
- Traitement du langage naturel
date_creation: '2025-04-02'
date_modification: '2025-04-04'
subClassOf: '[[Les LLM]]'
seeAlso: '[[Traitement du langage naturel (NLP)]]'
hasPart: '[[Sauvegarde différentielle des états contextuels LLM]]'
---
## Généralité

L'optimisation de la [fenêtre de contexte](https://fr.wikipedia.org/wiki/Fen%C3%AAtre_de_contexte) [LLM](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) (Large Language Model) désigne le processus de gestion des limites de la mémoire de travail d'un modèle linguistique, en particulier la quantité de données (texte, code, etc.) qu'il peut traiter simultanément. Cette optimisation est cruciale pour exploiter pleinement les capacités des LLM dans des scénarios réels, tout en tenant compte des contraintes techniques des architectures [Transformer](https://fr.wikipedia.org/wiki/Transformer_(machine_learning_model)).

## Points clés

- **Limitation des tokens** : Les LLM ont une capacité de contexte maximale fixe (ex. 2048 tokens pour GPT-3, jusqu'à 128 000 tokens pour GPT-4 Turbo)
- **Techniques d'optimisation** : Troncation, résumé automatique, segmentation dynamique ("chunking"), et mécanismes de mémoire externe
- **Impact sur les performances** : Le "syndrome d'amnésie des LLM" entraîne une perte de cohérence sur les longs textes, avec des chutes de performance allant jusqu'à 40%
- **Solutions hybrides** : Les combinaisons de techniques (ex: troncation + résumé) sont souvent les plus efficaces pour les cas d'usage complexes
- **Évolution technologique** : Les modèles récents comme GPT-4 introduisent des mécanismes dynamiques d'ajustement de la fenêtre contextuelle

## Détails

### Limitations techniques
Les modèles LLM stockent temporairement les données d'entrée dans une mémoire de contexte, dont la taille est fixée par l'architecture. Cette contrainte est intrinsèque à l'architecture Transformer qui utilise des mécanismes d'attention quadratiques - leur coût calculatoire augmente exponentiellement avec la taille du contexte.

### Techniques d'optimisation

#### Troncation
- **Troncation de début** : Suppression des tokens les plus anciens
- **Troncation de fin** : Suppression des derniers tokens
- **Troncation centrale** : Suppression d'une partie centrale pour conserver les débuts et fins

#### Résumé automatique
- **Extractif** : Extraction de phrases clés
- **Abstractif** : Synthèse en nouveaux termes

#### Segmentation dynamique ("Chunking")
- Fenêtres glissantes (overlap de 10-15% pour la cohérence)
- Découpage sémantique (par section/chapitre)

### Impact sur les performances
Des benchmarks montrent une chute de 38% de précision sur des textes dépassant 8k tokens. Les stratégies complexes augmentent également la latence :
- Résumé abstractif : +15-20% de temps vs. troncation simple
- Mémoire externe : jusqu'à 2x plus de RAM

### Cas d'utilisation avancés
- **Dialogue continu** : Optimisation par "attention différentielle"
- **Analyse de documents** : Pré-traitement par graphes de connaissances
- **Génération de code** : Priorisation via analyse syntaxique

### Outils et bibliothèques
- **[LangChain](https://fr.wikipedia.org/wiki/LangChain)** : Intègre le "Contextual Compression"
- **Hugging Face** : Pipelines de résumé avec modèles dédiés
- **Frameworks maison** : Google utilise T5-XL pour le pré-traitement

### Évaluation
Métriques clés :
- **ROUGE-L** : Mesure la qualité des résumés
- **BERTScore** : Évalue la similarité sémantique
- **Latence 95e percentile** : Critique pour les applications temps réel

Exemple de benchmark :
| Méthode         | ROUGE-L | BERTScore | Latence |
|-----------------|---------|-----------|---------|
| Troncation      | 0.45    | 0.68      | 120ms   |
| Résumé abstractif | 0.72    | 0.85      | 280ms   |
| Chunking        | 0.61    | 0.78      | 190ms   |