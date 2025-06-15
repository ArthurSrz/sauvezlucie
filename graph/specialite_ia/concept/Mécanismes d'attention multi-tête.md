---
title: Mécanismes d'attention multi-tête
type: concept
tags:
- réseaux neuronaux
- attention multi-tête
- transformers
- apprentissage automatique
- deep learning
- modèles d'attention
- IA
date_creation: '2025-04-04'
date_modification: '2025-04-04'
isPartOf: '[[Transformers et mécanismes d''attention]]'
relatedTo: '[[Transformers et attention en NLP]]'
---
## Généralité

Les mécanismes d'[attention multi-tête](https://fr.wikipedia.org/wiki/Attention_(apprentissage_automatique)) (ou "multi-head attention") sont une composante clé des architectures de [réseaux neuronaux](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) modernes, notamment des transformeurs introduits dans l'article fondateur "Attention Is All You Need" par Vaswani et al. en 2017. Ce mécanisme permet au modèle de traiter plusieurs représentations différentes d'une même entrée simultanément en divisant l'attention en plusieurs sous-espaces, ce qui est fondamental dans le domaine du [traitement automatique du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) (TALN).

## Points clés

- Permet de calculer plusieurs types d'[attention](https://fr.wikipedia.org/wiki/Mécanisme_d%27attention) en parallèle (typiquement 8 à 16 têtes selon l'architecture), chacune opérant dans un sous-espace différent de la représentation
- Chaque "tête" d'attention possède ses propres matrices de poids apprises (Q, K, V) indépendamment des autres têtes
- Les résultats des différentes têtes sont combinés par concaténation puis projection linéaire pour former la sortie finale, permettant une représentation plus riche
- Essentiel dans les architectures de [transformeurs](https://fr.wikipedia.org/wiki/Transformer_(machine_learning)) (BERT, GPT, etc.) où il permet de capturer simultanément diverses relations inter-tokens
- Introduit une capacité d'attention différentielle : certaines têtes peuvent se concentrer sur des motifs locaux tandis que d'autres captent des dépendances à longue distance

## Détails

Le mécanisme d'[attention multi-tête](https://fr.wikipedia.org/wiki/Attention_multi-t%C3%AAte) fonctionne en exécutant plusieurs opérations d'attention en parallèle (appelées "têtes"), chacune avec ses propres paramètres appris. Chaque tête projette les entrées dans différents sous-espaces à l'aide de matrices de poids distinctes (Q, K, V), calcule une fonction d'attention (généralement scaled dot-product attention) indépendamment, et produit une sortie de dimension réduite. Les sorties de toutes les têtes sont ensuite concaténées et projetées à nouveau via une dernière couche linéaire pour produire la sortie finale.

Les principaux avantages incluent la capacité à modéliser différents types de relations (locales/globales, syntaxiques/sémantiques) grâce à la spécialisation des têtes, la robustesse (si une tête donne des résultats médiocres, les autres peuvent compenser), la flexibilité (chaque tête peut se spécialiser dans un type particulier de pattern), l'efficacité du calcul parallèle sur [GPU](https://fr.wikipedia.org/wiki/Processeur_graphique)/[TPU](https://fr.wikipedia.org/wiki/Tensor_Processing_Unit), et l'adaptation aux dépendances multi-échelles (certaines têtes captent des relations locales tandis que d'autres se concentrent sur des dépendances à longue distance).

Ce mécanisme est fondamental dans le [traitement automatique des langues](https://fr.wikipedia.org/wiki/Traitement_automatique_des_langues) (traduction, compréhension) et des modèles comme [BERT](https://fr.wikipedia.org/wiki/BERT_(langage_de_mod%C3%A8les)) et [GPT](https://fr.wikipedia.org/wiki/Generative_Pre-trained_Transformer) qui utilisent l'attention multi-tête pour capturer simultanément des relations syntaxiques et sémantiques complexes.

Mathématiquement, pour h têtes d'attention:
- Chaque tête i calcule: head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
- Les sorties sont concaténées: MultiHead(Q,K,V) = Concat(head_1, ..., head_h)W^O

Où W_i^Q, W_i^K, W_i^V sont les matrices de poids pour la tête i, et W^O est la matrice de projection finale.