---
title: Contrôle stochastique des tokens dans la génération LLM
type: concept
tags:
- LLM
- génération de texte
- contrôle stochastique
- tokens
- modèles de langage
- température
- probabilité
date_creation: '2025-04-04'
date_modification: '2025-04-04'
uses: '[[Tokenisation et segmentation textuelle en NLP]]'
contributesTo: '[[Compression différentielle des connaissances dans les LLM]]'
subClassOf: '[[Les LLM]]'
---
## Généralité

Le [contrôle stochastique](https://fr.wikipedia.org/wiki/Processus_stochastique) des tokens dans la génération [LLM](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) (Large Language Models) désigne les méthodes probabilistes utilisées pour sélectionner les tokens (unités de texte) lors de la génération de texte par un modèle de langage. Ces techniques, inspirées des processus stochastiques en mathématiques et en physique, permettent d'introduire de la variabilité et de la créativité dans les sorties tout en maintenant un certain contrôle sur la cohérence et la qualité.

## Points clés

- **Méthodes principales** : échantillonnage par température, top-k sampling, top-p sampling
- **Applications** : génération créative, assistants conversationnels, résumés automatiques
- **Avantages** : équilibre entre créativité et cohérence, réduction des répétitions
- **Origines théoriques** : inspiré des [chaînes de Markov](https://fr.wikipedia.org/wiki/Cha%C3%AEne_de_Markov) et des modèles de langage statistiques
- **Adaptation** : utilisé dans les architectures modernes comme [GPT](https://fr.wikipedia.org/wiki/GPT-3) ou [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage))

## Détails

### Méthodes de contrôle stochastique

- **[Température](https://fr.wikipedia.org/wiki/Temp%C3%A9rature_(machine_learning))** : Paramètre qui influence la distribution de probabilité des tokens, ajustant le niveau de créativité vs. prévisibilité.
  - Température élevée (>1.0) : élargit la distribution pour favoriser des tokens moins probables (plus créatif)
  - Basse température (<1.0) : concentre la probabilité sur les tokens les plus attendus (plus prévisible)
  - Valeur typique : 0.7-1.0 pour un bon équilibre (source: recherches en NLP)

- **[Échantillonnage top-k / top-p](https://fr.wikipedia.org/wiki/%C3%89chantillonnage_(statistiques))** :
  - *Top-k*: Sélectionne uniquement les k tokens ayant les probabilités les plus élevées (ex: k=50)
  - *Top-p* (nucleus sampling): Conserve un sous-ensemble dynamique de tokens dont la somme des probabilités atteint p (ex: p=0.9)
  - Introduit par Holtzman et al. dans "The Curious Case of Neural Text Degeneration" (2019)

- **Réduction de la répétition** :
  - Pénalité de répétition (penalty term)
  - N-gram blocking
  - Adaptation dynamique des probabilités basée sur l'historique local

### Applications pratiques

- **Génération créative** :
  - Température élevée (1.0-1.5) + top-p large (0.9-1.0)
  - Utilisé dans [Sudowrite](https://fr.wikipedia.org/wiki/Sudowrite) ou [Jasper](https://fr.wikipedia.org/wiki/Jasper_(logiciel))

- **Assistants conversationnels** :
  - Température dynamique (0.7-1.2) + top-p modéré (0.7-0.95)
  - Utilisé dans [ChatGPT](https://fr.wikipedia.org/wiki/ChatGPT) ou [Google Bard](https://fr.wikipedia.org/wiki/Bard_(chatbot))

- **Résumés automatiques** :
  - Température basse (0.3-0.7) + top-k (30-50)
  - Techniques anti-répétition comme le n-gram blocking (n=3 ou 4)

### Configuration typique

Combinaison recommandée pour des résultats optimaux :
- Température modérée (0.7-0.9)
- Top-p (p=0.9)
- Pénalité de répétition (coefficient 1.2)

Note: Les plages de paramètres mentionnées représentent des valeurs couramment utilisées mais peuvent varier selon les cas d'usage spécifiques et les évolutions des modèles. Les recherches citées correspondent bien aux pratiques documentées dans le domaine du [NLP](https://fr.wikipedia.org/wiki/Traitement_automatique_des_langues).