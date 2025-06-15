---
title: Problème du gradient évanescent dans les réseaux récurrents
type: concept
tags:
- deep learning
- réseaux de neurones récurrents
- RNN
- gradient évanescent
- rétropropagation
- BPTT
- apprentissage profond
- optimisation
- entraînement
date_creation: '2025-03-18'
date_modification: '2025-03-18'
isPartOf: '[[Réseaux de neurones récurrents (RNN)]]'
solvedBy: '[[LSTM (Long Short-Term Memory)]]'
hasPart: '[[Réseaux de neurones récurrents (RNN)]]'
---
## Généralité

Le [problème du gradient évanescent](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_gradient_%C3%A9vanescent) est un obstacle majeur dans l'entraînement des [réseaux de neurones récurrents](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents) (RNN). Identifié dès les années 1990 par Hochreiter et Schmidhuber, ce phénomène se produit lorsque les gradients calculés lors de la [rétropropagation du temps](https://fr.wikipedia.org/wiki/R%C3%A9tropropagation_du_gradient) (BPTT) deviennent exponentiellement petits à mesure qu'ils sont propagés en arrière à travers les couches temporelles, limitant considérablement la capacité à modéliser des dépendances à long terme.

## Points clés

- Les gradients diminuent exponentiellement avec le nombre d'étapes temporelles
- Ce phénomène rend l'apprentissage des dépendances à long terme particulièrement difficile
- Le problème affecte surtout les architectures RNN classiques comme les réseaux [Elman](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents#Réseau_d'Elman)
- Des solutions comme les LSTM et GRU ont été développées pour atténuer ce problème
- L'impact est plus marqué dans les tâches nécessitant de mémoriser des informations sur de longues séquences

## Détails

Le problème du gradient évanescent se manifeste particulièrement dans les réseaux de neurones récurrents profonds ou traitant de longues séquences temporelles. Lors de la rétropropagation, les gradients doivent traverser de nombreuses étapes temporelles, sub# 题目描述
## 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
## 请你找出符合题意的 最短 子数组，并输出它的长度。
### 我的题解：