---
title: Transformers et mécanismes d'attention
type: concept
tags:
- IA
- Deep Learning
- NLP
- Transformers
- Attention
- Réseaux neuronaux
- Vaswani
- Architecture
date_creation: '2025-04-08'
date_modification: '2025-04-08'
uses: '[[Modèles de langage génératifs pré-entraînés]]'
subClassOf: '[[Apprentissage profond (Deep Learning)]]'
sameAs: '[[Transformers et attention en NLP]]'
relatedTo: '[[Apprentissage auto-supervisé (Self-supervised Learning)]]'
isPartOf: '[[Sauvegarde différentielle des états contextuels LLM]]'
hasPart: '[[Mécanismes d''attention multi-tête]]'
seeAlso:
- '[[Attention différentielle pour les séries temporelles]]'
- '[[Architectures neuronales à couches d''attention emboîtées pour l''analyse multiniveau]]'
---
## Généralité

Les Transformers sont une architecture de réseau neuronal introduite en 2017 par Vaswani et al. dans l'article "Attention Is All You Need". Cette architecture révolutionnaire a supplanté les réseaux récurrents (RNN) et convolutifs (CNN) dans de nombreuses tâches de traitement du langage naturel (NLP) grâce à son mécanisme d'attention, qui permet de modéliser efficacement les dépendances à longue distance dans les séquences de données.

## Points clés

- Le mécanisme d'attention permet aux modèles de se concentrer sélectivement sur différentes parties d'une séquence d'entrée lors du traitement de chaque élément de sortie
- L'architecture Transformer repose sur l'auto-attention (self-attention) et n'utilise pas de récurrence, permettant une parallélisation efficace
- Les Transformers sont composés d'encodeurs et de décodeurs empilés, chacun utilisant des mécanismes d'attention multi-têtes
- Cette architecture est à la base des modèles de langage les plus performants comme BERT, GPT, T5 et autres modèles fondamentaux (foundation models)

## Détails

### Mécanisme d'attention

Le mécanisme d'attention permet à un modèle de pondérer l'importance de différentes parties d'une séquence d'entrée. Dans sa forme la plus simple, l'attention calcule des scores de similarité entre une requête (query) et un ensemble de clés (keys), puis utilise ces scores pour pondérer les valeurs (values) associées.

L'auto-attention, ou self-attention, est un cas particulier où les requêtes, clés et valeurs proviennent de la même séquence, permettant à chaque position de la séquence d'interagir avec toutes les autres positions.

La formule principale de l'attention est:
```
Attention(Q, K, V) = softmax(QK^T / √d_k)V
```
où Q, K, V sont respectivement les matrices de requêtes, clés et valeurs, et d_k est la dimension des clés.

### Architecture Transformer

Un Transformer complet comprend:

1. **Encodeur**: Composé de plusieurs couches identiques, chacune contenant:
   - Un sous-module d'auto-attention multi-têtes
   - Un réseau feed-forward
   - Des connexions résiduelles et normalisation de couche (layer normalization)

2. **Décodeur**: Également composé de couches empilées, chacune contenant:
   - Un sous-module d'auto-attention masquée (pour éviter de voir les positions futures)
   - Un sous-module d'attention qui utilise les sorties de l'encodeur
   - Un réseau feed-forward
   - Des connexions résiduelles et normalisation de couche

3. **Attention multi-têtes**: Permet au modèle d'assister simultanément à différentes représentations de différentes positions, capturant ainsi diverses relations sémantiques et syntaxiques.

### Avantages des Transformers

- **Parallélisation**: Contrairement aux RNN, les Transformers peuvent traiter tous les éléments d'une séquence en parallèle.
- **Modélisation des dépendances à longue distance**: Le mécanisme d'attention permet de capturer directement les relations entre des éléments éloignés dans une séquence.
- **Représentations contextuelles**: Chaque token est représenté en fonction de son contexte complet.
- **Scalabilité**: L'architecture peut être facilement étendue à des modèles de très grande taille avec des milliards de paramètres.

Les Transformers ont permis des avancées majeures dans le NLP et sont désormais appliqués avec succès à d'autres domaines comme la vision par ordinateur, l'audio, et même les problèmes de biologie moléculaire.