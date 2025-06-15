---
title: Attention locale vs globale dans les modèles séquentiels
type: concept
tags:
- Machine Learning
- Modèles séquentiels
- Attention mécanisme
- RNN
- Transformers
- Téchniques NLP
- Intelligence artificielle
date_creation: '2025-04-02'
date_modification: '2025-04-02'
subClassOf: '[[Transformers et attention en NLP]]'
---
## Généralité

L'attention locale et globale sont deux mécanismes distincts utilisés dans les modèles séquentiels, comme les [réseaux de neurones récurrents](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents) (RNN) ou les [Transformers](https://fr.wikipedia.org/wiki/Transformer_(machine_learning_model)), pour déterminer comment les éléments d'une séquence sont pondérés lors du traitement. Ces mécanismes, s'inspirant partiellement des travaux en neurosciences sur l'[attention humaine](https://fr.wikipedia.org/wiki/Attention_(cognition)), sont devenus des composants clés dans les architectures de [deep learning](https://fr.wikipedia.org/wiki/Apprentissage_profond) modernes.

## Points clés

- **Attention locale** : Se concentre sur une partie restreinte de la séquence, offrant une meilleure efficacité computationnelle
- **Attention globale** : Considère l'ensemble de la séquence, permettant de capturer des relations à longue distance
- **Applications distinctes** : Locale pour les tâches à pertinence locale (reconnaissance vocale), globale pour celles nécessitant un contexte large (traduction)
- **Approches hybrides** : Architectures comme [Longformer](https://fr.wikipedia.org/wiki/Longformer) ou [BigBird](https://fr.wikipedia.org/wiki/BigBird_(transformer)) combinent les deux mécanismes
- **Impact historique** : L'article "Attention Is All You Need" (2017) a marqué un tournant en [traitement automatique du langage](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage)

## Détails

L'attention locale restreint le champ d'attention à une sous-partie de la séquence, ce qui permet de réduire significativement le nombre de calculs nécessaires. Inspirée des mécanismes d'attention humaine, elle est particulièrement utile pour les séquences longues (comme l'[ADN](https://fr.wikipedia.org/wiki/Acide_d%C3%A9soxyribonucl%C3%A9ique) ou des documents étendus).

**Avantages de l'attention locale** :
- Efficacité computationnelle (complexité linéaire ou quasi-linéaire)
- Réduction du bruit en ignorant les éléments distants non pertinents
- Adaptée aux tâches où les dépendances sont principalement locales

**Inconvénients de l'attention locale** :
- Risque de manquer des dépendances à long terme
- Nécessité de définir empiriquement une taille de fenêtre appropriée

L'attention globale prend en compte tous les éléments de la séquence. Introduite dans l'article "Attention Is All You Need", cette méthode repose sur le calcul matriciel des scores d'attention.

**Avantages de l'attention globale** :
- Capacité à modéliser des dépendances à long terme
- Flexibilité pour capturer des motifs globaux
- Idéale pour des tâches nécessitant une compréhension contextuelle large

**Inconvénients de l'attention globale** :
- Coût computationnel quadratique (O(n²))
- Limitation pratique pour des séquences très longues

Le choix entre attention locale et globale dépend des exigences de la tâche et des contraintes computationnelles. Les approches hybrides comme Sparse Transformers ou Longformer combinent des avantages des deux méthodes.

**Exemples d'utilisation** :

**Attention locale** :
- Modèles [LAS](https://fr.wikipedia.org/wiki/Listen,_Attend_and_Spell) pour la [reconnaissance vocale](https://fr.wikipedia.org/wiki/Reconnaissance_automatique_de_la_parole)
- [WaveNet](https://fr.wikipedia.org/wiki/WaveNet) pour la synthèse vocale
- Traitement de séquences biologiques ([ADN](https://fr.wikipedia.org/wiki/Acide_d%C3%A9soxyribonucl%C3%A9ique), protéines)

**Attention globale** :
- [Transformers](https://fr.wikipedia.org/wiki/Transformeur_(apprentissage_automatique)) comme [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage)) et [GPT](https://fr.wikipedia.org/wiki/Generative_Pre-trained_Transformer)
- ViT (Vision Transformer) pour la classification visuelle
- T5 pour des tâches de transfert learning en [NLP](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel)