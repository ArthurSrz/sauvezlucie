---
title: Ingénierie des prompts pour l'optimisation du LLM
type: concept
tags:
- Prompt Engineering
- Large Language Models (LLM)
- Artificial Intelligence
- Natural Language Processing (NLP)
- Optimization Techniques
- Structured Queries
- Instruction Tuning
date_creation: '2025-04-02'
date_modification: '2025-04-02'
relatedTo: '[[Les LLM]]'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
---
## Généralité

L'[ingénierie des prompts](https://fr.wikipedia.org/wiki/Ing%C3%A9nierie_des_prompts) pour l'optimisation des [modèles de langage à large échelle](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) (LLM) désigne l'ensemble des techniques visant à formuler des requêtes ou des instructions de manière structurée et précise afin d'améliorer la qualité, la cohérence et la pertinence des réponses générées par ces modèles. Selon Wikipédia, cette pratique s'est particulièrement développée avec l'avènement de modèles comme [GPT-3](https://fr.wikipedia.org/wiki/GPT-3) en 2020.

## Points clés

- **Clarté et précision** : Les prompts doivent être formulés de manière à éviter les ambiguïtés et guider le modèle vers une réponse ciblée
- **Structures et formats spécifiques** : L'utilisation de formats structurés (listes, tableaux) ou de techniques comme le *few-shot prompting* améliore la cohérence
- **Tests itératifs** : L'optimisation repose sur des essais successifs et des ajustements basés sur des métriques précises
- **Techniques avancées** : Méthodes comme le chain-of-thought prompting ou la disambiguïsation permettent d'atteindre des résultats plus précis
- **Applications pratiques** : Support client, génération de contenu, analyse de données et éducation sont parmi les principaux domaines d'application

## Détails

**Clarté et précision des instructions**  
Une instruction claire spécifie explicitement le but, le format de sortie souhaité et les contraintes (ex. : "Générez une réponse de 100 mots en français, en évitant les termes techniques"). Selon [Wikipédia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal), des études montrent que les modèles comme [GPT-3](https://fr.wikipedia.org/wiki/GPT-3) répondent mieux aux instructions explicites utilisant des verbes d'action précis.

**Structures et formats spécifiques**  
L'utilisation de templates prédéfinis (ex. : "Question : [X] \n Réponse :") standardise les entrées. Le [few-shot prompting](https://fr.wikipedia.org/wiki/Apprentissage_par_l%27exemple), qui consiste à fournir des exemples d'entrée-sortie avant la requête cible, améliore significativement les résultats. L'emploi de formats structurés (listes, tableaux) ou de balises améliore la lisibilité. Le role-playing, où on assigne un rôle au modèle, oriente sa réponse vers un contexte spécifique. La technique du [chain-of-thought prompting](https://fr.wikipedia.org/wiki/Cha%C3%AEne_de_raisonnement) incite le modèle à détailler son raisonnement étape par étape.

**Tests itératifs et ajustements**  
L'optimisation nécessite une approche empirique reposant sur :  
- Le [A/B testing](https://fr.wikipedia.org/wiki/Test_A/B) pour comparer des versions de prompts  
- L'analyse des réponses via des feedback loops pour identifier les erreurs  
- L'utilisation de métriques comme la précision ou la cohérence  
- La personnalisation des prompts en fonction du domaine ou de l'utilisateur  

**Techniques avancées**  
Parmi les méthodes les plus efficaces :  
- Le chain-of-thought prompting pour obtenir un raisonnement détaillé  
- La disambiguïsation pour clarifier les termes ambigus en contexte  
- Le prompt stitching qui combine plusieurs techniques pour des résultats plus précis  

**Applications pratiques**  
Les principaux domaines d'application incluent :  
- Le support client pour des réponses automatisées cohérentes  
- La génération de contenu (articles, scripts ou emails personnalisés)  
- L'analyse de données pour extraire des insights à partir de textes  
- L'éducation via des exercices interactifs ou tutoriels guidés  

L'ingénierie des prompts est un processus itératif qui combine créativité technique et rigueur analytique. Selon [Wikipédia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal), cette discipline constitue aujourd'hui une compétence clé pour exploiter efficacement les LLM.

[1] Source Wikipédia: "Prompt engineering" (version anglaise, consultée le 20/06/2023)  
[2] Source Wikipédia: "BIG-bench" (benchmark collaboratif pour LLM)