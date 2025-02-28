# Knowledge Graph Explorer & RAG Toolkit
Un outil interactif pour créer, explorer et exploiter des graphes de connaissances à partir de documents Markdown structurés, avec intégration d'un outil d'aide à la création de RAG (Retrieval-Augmented Generation) pour l'exploitation intelligente des connaissances.
Il a été conçu pour fonctionner avec le projet #sauvezlucie. 

## 📋 À propos

Ce projet a été conçu pour faciliter la gestion et l'exploitation de bases de connaissances interconnectées. Il permet de:

- Transformer une collection de documents Markdown en un graphe de connaissances interactif
- Explorer visuellement les relations entre les entités
- De tester différents algorithmes d'explorations et d'extraction de document

Au fil du temps, il évoluera pour devenir un outil complet de création, d'entretien et d'exploitation des graphes de connaissances.

## ✨ Fonctionnalités

### Disponibles actuellement

- **Analyse de documents Markdown** avec métadonnées YAML pour construire un graphe
- **Visualisation interactive** des nœuds et relations du graphe
- **Recherche par pertinence** combinant plusieurs techniques:
  - Embeddings vectoriels (similarité cosinus)
  - TF-IDF
  - BM25
  - Similarité de Jaccard sur les tags
- **Extraction contextuelle** de documents pour les requêtes LLM
- **Interface RAG** pour poser des questions sur le contenu du graphe

### À venir

- Fonctions avancées de création et d'édition du graphe
- Mécanismes d'inférence pour déduire de nouvelles relations
- Importation/exportation dans différents formats standards (RDF, JSON-LD, etc.)

## 🔧 Installation

### Prérequis

- Python 3.8 ou version ultérieure
- Un LLM accessible via API (local ou distant)

### Étapes d'installation

1. Clonez ce dépôt
   ```bash
   git clone https://github.com/votreutilisateur/knowledge-graph-explorer.git
   cd knowledge-graph-explorer
   ```

2. Installez les dépendances
   ```bash
   pip install -r requirements.txt
   ```

3. Créez un fichier `.env` à la racine du projet
   ```
   # Configuration LLM
   LLM_BASE_URL=http://localhost:8000/v1
   LLM_API_KEY=EMPTY
   LLM_MODEL=Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4

   # Configuration Embeddings
   EMBEDDING_MODEL=intfloat/multilingual-e5-large-instruct

   # Autres paramètres
   DEFAULT_MAX_TOKENS=16000
   DEFAULT_TEMPERATURE=0.3
   ```

## 🚀 Utilisation

### Démarrer l'application

```bash
streamlit run app.py
```

### Structure attendue des fichiers Markdown

Pour une intégration optimale, structurez vos fichiers Markdown comme suit:

```markdown
---
title: "Titre du document"
type: "concept/technique/application/acteur/etc."
tags: ["tag1", "tag2"]
relations:
  - type: "rdfs:subClassOf"
    target: "[[Document parent]]"
  - type: "rdfs:seeAlso"
    target: ["[[Document connexe 1]]", "[[Document connexe 2]]"]
date_creation: "YYYY-MM-DD"
date_modification: "YYYY-MM-DD"
---

Contenu du document...
```

### Fonctionnalités principales

1. **Analyse d'un répertoire**: Sélectionnez un répertoire contenant vos fichiers Markdown pour construire le graphe.
2. **Visualisation**: Explorez interactivement les relations entre vos documents.
3. **Recherche par pertinence**: Utilisez la recherche pour trouver les documents les plus pertinents par rapport à une requête.
4. **Extraction contextuelle**: Sélectionnez un sous-ensemble du graphe pour l'utiliser comme contexte dans des requêtes LLM.
5. **Questions & Réponses**: Posez des questions basées sur le contenu de votre graphe de connaissances.

## 📁 Structure du projet

```
knowledge-graph-explorer/
├── app.py                  # Application Streamlit principale
├── config.py               # Configuration et variables d'environnement
├── prompts.py              # Définitions des prompts pour les LLM
├── markdown_parser.py      # Analyse des fichiers Markdown
├── graph_builder.py        # Construction et manipulation du graphe
├── search_engine.py        # Moteur de recherche basique
├── relevance_scoring.py    # Algorithmes de scoring de pertinence
├── visualization.py        # Visualisation du graphe
├── .env                    # Configuration locale (non versionné)
└── requirements.txt        # Dépendances
```

## 🛣️ Roadmap

- [ ] Ajout de fonctionnalités d'édition du graphe directement dans l'interface
- [ ] Mécanismes d'inférence pour déduire de nouvelles relations
- [ ] Support pour l'importation/exportation dans des formats standards (RDF, JSON-LD)
- [ ] Amélioration des algorithmes de recherche avec apprentissage par retour d'utilisateur
- [ ] Extension des capacités RAG avec chunking intelligent et indexation avancée
- [ ] Support multi-utilisateurs et collaboration
