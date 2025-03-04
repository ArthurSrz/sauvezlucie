# Knowledge Graph Explorer & RAG Toolkit

Un outil interactif pour créer, explorer et exploiter des graphes de connaissances à partir de documents Markdown structurés, avec intégration d'un outil d'aide à la création de RAG (Retrieval-Augmented Generation) pour l'exploitation intelligente des connaissances.

Conçu spécifiquement pour fonctionner avec le projet #sauvezlucie, cet outil transforme vos documents en un réseau de connaissances navigable et exploitable par les modèles de langage.

## 📋 À propos

Ce projet a été conçu pour faciliter la gestion et l'exploitation de bases de connaissances interconnectées. Il permet de:

- Transformer une collection de documents Markdown en un graphe de connaissances interactif
- Explorer visuellement les relations entre les entités
- Tester différents algorithmes d'exploration et d'extraction de documents
- Améliorer les capacités d'un LLM grâce au RAG en connectant vos connaissances structurées

L'outil évoluera progressivement vers une solution complète de création, maintenance et exploitation des graphes de connaissances avec des capacités d'IA augmentée.

## ✨ Fonctionnalités

### Disponibles actuellement

- **Analyse de documents Markdown** avec métadonnées YAML pour construire un graphe de connaissances
- **Visualisation interactive** des nœuds et relations du graphe avec navigation intuitive
- **Recherche multi-méthodes** combinant:
  - Embeddings vectoriels (similarité cosinus)
  - TF-IDF pour l'importance des termes
  - BM25 pour la recherche avancée basée sur la fréquence
  - Similarité de Jaccard sur les tags pour les associations thématiques
- **Extraction contextuelle intelligente** des documents les plus pertinents pour les requêtes LLM
- **Interface RAG complète** pour interroger le contenu du graphe avec des réponses enrichies
- **Assistant de création de nœuds** avec suggestions automatisées de tags et de liaisons (bêta)

### À venir

- Fonctions avancées d'édition du graphe avec UI simplifiée
- Mécanismes d'inférence pour déduire automatiquement de nouvelles relations
- Importation/exportation dans différents formats standards (RDF, JSON-LD, etc.)
- Moteur de règles pour la validation et l'enrichissement du graphe
- API pour intégrer le graphe de connaissances dans d'autres applications

## 🔧 Installation

### Prérequis

- Python 3.8 ou version ultérieure
- Un LLM accessible via API (local ou distant)
- 8 Go de RAM minimum recommandés

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

L'interface web s'ouvrira automatiquement dans votre navigateur par défaut.

### Guide de structuration des documents

Pour tirer le meilleur parti du graphe de connaissances, vos documents Markdown doivent suivre une structure cohérente. Vous pouvez regarder le fichier template.md Voici un guide détaillé:

#### Structure de base attendue

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
  - type: "dcterms:requires"
    target: ["[[Document prérequis 1]]", "[[Document prérequis 2]]"]
date_creation: "YYYY-MM-DD"
date_modification: "YYYY-MM-DD"
---

Contenu du document...
```

#### Explications des champs

- **title**: Titre unique du document, utilisé comme identifiant principal
- **type**: Catégorie du document. Valeurs recommandées:
  - `concept`: Idée ou notion théorique
  - `technique`: Méthode ou procédé
  - `application`: Outil ou logiciel
  - `acteur`: Personne ou organisation
  - `document`: Document de référence
  - `événement`: Événement historique ou planifié
- **tags**: Liste de mots-clés pour la catégorisation et la recherche
- **relations**: Connexions avec d'autres documents
  - `type`: Type de relation (voir vocabulaires recommandés ci-dessous)
  - `target`: Document(s) cible(s), entouré(s) de doubles crochets `[[...]]`
- **date_creation/date_modification**: Dates au format YYYY-MM-DD

#### Vocabulaires recommandés pour les relations

Pour une meilleure interopérabilité, utilisez ces vocabulaires standards:

- **RDFS/OWL**:
  - `rdfs:subClassOf`: Relation hiérarchique de type "est un sous-type de"
  - `rdfs:seeAlso`: Document connexe ou complémentaire
  - `owl:sameAs`: Document équivalent ou identique
  
- **Dublin Core (dcterms)**:
  - `dcterms:requires`: Prérequis ou dépendance
  
#### Bonnes pratiques

1. **Nommage cohérent**: Utilisez des titres clairs et consistants
2. **Granularité**: Préférez plusieurs documents spécifiques à un document générique trop long
3. **Liens bidirectionnels**: Établissez des relations dans les deux sens quand c'est pertinent
4. **Richesse des métadonnées**: Plus vous ajoutez d'informations structurées, meilleur sera le graphe
5. **Mise à jour régulière**: Actualisez les `date_modification` lors des changements significatifs

## 📁 Structure du projet

```
knowledge-graph-explorer/
├── app.py                  # Application Streamlit principale
├── config.py               # Configuration et variables d'environnement
├── domain/                 # Fonctions métier et modèles
├── services/               # Services externes (LLM, embeddings, etc.)
├── ui/                     # Composants d'interface utilisateur
├── utils/                  # Fonctions utilitaires
├── .env                    # Configuration locale (non versionné)
└── requirements.txt        # Dépendances
```

## 🛣️ Roadmap

- [ ] Amélioration de l'interface d'édition des nœuds et relations
- [ ] Système de versionnement du graphe de connaissances
- [ ] Moteur d'inférence pour déduire automatiquement de nouvelles relations
- [ ] Support pour l'importation/exportation dans des formats standards (RDF, JSON-LD)
- [ ] Algorithmes de recherche adaptatifs avec apprentissage par retour d'utilisateur
- [ ] Chunking intelligent avec conservation du contexte pour le RAG
- [ ] Amélioration des visualisations avec filtres et regroupements
- [ ] Intégration d'outils d'analyse de graphe pour identifier les patterns et incohérences
- [ ] Support multi-utilisateurs avec fonctionnalités collaboratives
- [ ] API REST pour intégration dans d'autres applications

## 🤝 Contribuer

Les contributions sont les bienvenues! N'hésitez pas à ouvrir une issue pour signaler des bugs ou proposer des améliorations, ou à soumettre une pull request.

## 📄 Licence

?