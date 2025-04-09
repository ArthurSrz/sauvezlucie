---
title: LoRA (Low-Rank Adaptation) pour le fine-tuning LLM
type: concept
tags:
- LoRA
- fine-tuning
- LLM
- machine learning
- low-rank adaptation
- parameter efficiency
- computational costs
- model adaptation
- NLP
- optimization
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo: '[[La quantification de modèles LLM]]'
isPartOf: '[[Apprentissage automatique (Machine Learning)]]'
---
## Généralité

LoRA ([Low-Rank Adaptation](https://fr.wikipedia.org/wiki/Adaptation_de_rang_faible)) est une méthode de fine-tuning pour les [modèles de langage géants](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) (LLM) qui permet d'adapter efficacement un modèle pré-entraîné à une tâche spécifique tout en réduisant les coûts de calcul et la consommation de mémoire. Développée par [Microsoft Research](https://fr.wikipedia.org/wiki/Microsoft_Research) en 2021, cette technique repose sur une décomposition matricielle de rang faible pour optimiser le processus d'adaptation.  

## Points clés

- Réduction drastique du nombre de paramètres à entraîner (jusqu'à 10 000 fois moins selon les expérimentations)
- Conservation des performances du modèle original dans la plupart des cas (avec une perte de précision généralement inférieure à 1-2%)
- Possibilité de réutiliser le modèle de base pour plusieurs tâches via des adaptateurs légers
- Compatibilité avec d'autres techniques d'optimisation comme la Quantization
- Économie significative de mémoire (généralement 60-90% de réduction selon les configurations)

## Détails

LoRA repose sur la décomposition de matrices en rang faible. Les poids de la couche cible sont exprimés comme la somme de la matrice de base (pré-entraînée) et d'une matrice de faible rang, construite à partir de deux petites matrices \( A \) et \( B \), où \( rank = r \) (généralement entre 1 et 8). La formule mathématique est :

\[
W_{adapté} = W_{base} + A \times B
\]

Lors de l'entraînement, seuls \( A \) et \( B \) sont ajustés, tandis que \( W_{base} \) reste fixe. Cette approche réduit drastiquement le nombre de paramètres à optimiser (de \( O(n^2) \) à \( O(r \times n) \)), où \( n \) est la dimension de la matrice originale.

Parmi les applications courantes, on trouve :
- La spécialisation de modèles : Adapter un LLM générique (Llama, BERT, GPT) à des tâches spécifiques
- La création de multiples adaptateurs pour un même modèle de base
- L'optimisation des performances pour des architectures de taille réduite
- Le déploiement efficace sur des appareils à ressources limitées