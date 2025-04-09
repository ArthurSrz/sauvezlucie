---
title: Traduction automatique neuronale
type: concept
tags:
- intelligence artificielle
- traduction automatique
- NMT
- réseaux de neurones
- traitement du langage naturel
- linguistique computationnelle
- IA
- technologies de traduction
- apprentissage profond
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Traitement du langage naturel (NLP)]]'
uses: '[[Apprentissage profond (Deep Learning)]]'
isPartOf: '[[Transformers et attention en NLP]]'
---
## Généralité

La [traduction automatique neuronale](https://fr.wikipedia.org/wiki/Traduction_automatique_neuronale) (NMT - Neural Machine Translation) est une approche de [traduction automatique](https://fr.wikipedia.org/wiki/Traduction_automatique) qui utilise des [réseaux de neurones artificiels](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) profonds pour prédire la probabilité d'une séquence de mots. Apparue dans les années 2010 (avec les premiers modèles pratiques vers 2014 selon Wikipedia), cette méthode a rapidement supplanté les approches statistiques traditionnelles (SMT) grâce à ses performances supérieures en termes de fluidité.

## Points clés

- Utilise des architectures de [réseaux de neurones profonds](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels), principalement des modèles [séquence à séquence](https://fr.wikipedia.org/wiki/Mod%C3%A8le_s%C3%A9quence_%C3%A0_s%C3%A9quence) (seq2seq) avec mécanismes d'attention
- Traite les phrases comme des unités complètes plutôt que des segments isolés, améliorant ainsi la cohérence et préservant mieux le contexte
- Forme la base des systèmes de traduction modernes comme Google Translate, [DeepL](https://fr.wikipedia.org/wiki/DeepL) et Microsoft Translator
- A considérablement amélioré la qualité des traductions automatiques depuis son introduction en 2014-2016
- Nécessite d'importantes quantités de données parallèles pour l'entraînement

## Détails

La traduction automatique neuronale repose sur des architectures de [réseaux de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) complexes. Les premiers systèmes NMT utilisaient principalement des architectures encodeur-décodeur avec des [réseaux de neurones récurrents](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents) (RNN), notamment des cellules [LSTM](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_%C3%A0_m%C3%A9moire_%C3%A0_court_terme) (Long Short-Term Memory) ou GRU (Gated Recurrent Unit). Plus récemment, les architectures basées sur les Transformers ont supplanté les RNN dans les systèmes NMT.

Les systèmes NMT présentent plusieurs avantages par rapport aux approches statistiques traditionnelles (SMT): meilleure gestion des dépendances à longue distance, capacité à capturer des nuances sémantiques plus subtiles, production de traductions généralement plus fluides et naturelles, meilleure gestion des langues morphologiquement riches, et adaptation plus aisée à de nouveaux domaines.

Cependant, ils comportent aussi certaines limitations: forte dépendance à la qualité et à la quantité des données d'entraînement, tendance à produire des traductions "hallucinées", difficulté persistante à traduire des termes rares, consommation importante de ressources computationnelles, et sensibilité aux biais présents dans les données d'entraînement.

La [traduction automatique neuronale](https://fr.wikipedia.org/wiki/Traduction_automatique_neuronale) est aujourd'hui utilisée dans de nombreux domaines comme la localisation de contenu numérique (Google Translate, [DeepL](https://fr.wikipedia.org/wiki/DeepL)), la communication internationale (Skype Translator), la traduction de documents techniques, l'accessibilité (sous-titres YouTube) et l'aide à la rédaction (Grammarly).

Les avancées récentes incluent les modèles multilingues, les systèmes de traduction sans parallèle, l'intégration de mémoires de traduction, les architectures massives comme GPT-3, et les approches hybrides combinant NMT et règles linguistiques pour des langues peu dotées.