---
title: Apprentissage par curriculum (Curriculum Learning)
type: concept
tags:
- intelligence artificielle
- apprentissage automatique
- curriculum learning
- stratégie d'entraînement
- Bengio
- apprentissage progressif
- machine learning
- deep learning
- pédagogie IA
- optimisation
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo: '[[Apprentissage profond (Deep Learning)]]'
isPartOf: '[[Entraînement d''un modèle d''IA]]'
subClassOf: '[[Apprentissage auto-supervisé (Self-supervised Learning)]]'
---
## Généralité

L'[apprentissage par curriculum](https://fr.wikipedia.org/wiki/Apprentissage_par_curriculum) est une stratégie d'entraînement en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui s'inspire de la façon dont les humains apprennent, en commençant par des concepts simples avant de progresser vers des notions plus complexes. Introduite formellement par [Yoshua Bengio](https://fr.wikipedia.org/wiki/Yoshua_Bengio) et ses collaborateurs en 2009, cette approche repose sur des fondements pédagogiques établis depuis longtemps en éducation humaine (comme la progression graduelle proposée par [Comenius](https://fr.wikipedia.org/wiki/Jan_Amos_Comenius) au XVIIe siècle).

## Points clés

- Présente les exemples d'entraînement dans un ordre de complexité croissante, inspiré des méthodes pédagogiques humaines
- Améliore généralement la vitesse de convergence (jusqu'à 2 fois plus rapide) et peut conduire à de meilleures performances finales
- Particulièrement efficace pour les problèmes complexes comme la [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur) et le [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel)
- Peut être implémenté sous forme de curriculum statique, dynamique ou auto-curriculum
- S'inscrit dans la famille des méthodes de "self-paced learning" où le modèle participe à la sélection des exemples

## Détails

Le curriculum learning s'appuie sur trois principes fondamentaux : la séquence des exemples doit suivre une progression logique, la difficulté doit augmenter progressivement, et la transition entre niveaux doit être fluide.

Pour la mise en œuvre, la mesure de difficulté peut être définie par des experts humains (curriculum manuel), calculée à partir de caractéristiques des données, déterminée par la confiance du modèle lui-même (auto-curriculum), ou basée sur la perte d'entraînement des exemples.

Il existe trois types principaux de curriculum :
1. **Curriculum statique** : l'ordre des exemples est prédéfini avant l'entraînement et reste fixe
2. **Curriculum dynamique** : l'ordre est ajusté pendant l'entraînement en fonction des performances du modèle
3. **Auto-curriculum** : le modèle génère lui-même des tâches de difficulté croissante (courant en [apprentissage par renforcement](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement))

Les avantages documentés incluent l'accélération de la convergence de l'entraînement, l'amélioration des performances finales (confirmée sur des benchmarks comme [ImageNet](https://fr.wikipedia.org/wiki/ImageNet)), la réduction potentielle du surapprentissage, et une meilleure généralisation à de nouveaux exemples, notamment pour des données bruitées ou déséquilibrées.

Parmi les applications principales, on trouve la vision par ordinateur (reconnaissance d'objets dans des images désordonnées), le traitement du langage naturel (traduction automatique), et l'apprentissage par renforcement.

Il existe également des variantes intéressantes comme l'apprentissage par anti-curriculum (commencer par les exemples difficiles), l'apprentissage par curriculum mixte (alterner entre exemples faciles et difficiles), ou le Self-Paced Curriculum Learning (combinaison des deux approches).