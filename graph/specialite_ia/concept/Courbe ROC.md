---
title: Courbe ROC
type: concept
tags:
- machine learning
- classification
- évaluation de modèle
- courbe ROC
- sensibilité
- spécificité
- seuil de décision
- visualisation
- performance
- classification binaire
date_creation: '2025-03-21'
date_modification: '2025-03-21'
isPartOf: '[[Apprentissage supervisé]]'
uses: '[[Entraînement d''un modèle d''IA]]'
---

## Généralité

La courbe ROC (Receiver Operating Characteristic) est un outil graphique d'évaluation et de visualisation des performances d'un modèle de classification binaire. Elle représente la relation entre le taux de vrais positifs (sensibilité) et le taux de faux positifs (1-spécificité) pour différents seuils de décision. Développée initialement pendant la Seconde Guerre mondiale pour l'analyse des signaux radar, la courbe ROC est aujourd'hui largement utilisée en apprentissage automatique, en médecine diagnostique et dans de nombreux domaines nécessitant l'évaluation de classifieurs.

## Points clés

- La courbe ROC trace le taux de vrais positifs (TPR) en fonction du taux de faux positifs (FPR) à différents seuils de classification
- L'aire sous la courbe ROC (AUC-ROC) est une métrique synthétique qui quantifie la performance globale du modèle (1.0 = parfait, 0.5 = aléatoire)
- Elle permet de comparer objectivement différents modèles de classification indépendamment du seuil choisi
- La courbe ROC est particulièrement utile pour les problèmes avec des classes déséquilibrées

## Détails

La courbe ROC est construite en faisant varier le seuil de décision d'un classifieur binaire et en calculant pour chaque seuil le taux de vrais positifs (TPR) et le taux de faux positifs (FPR). Ces taux sont définis comme suit :

- TPR (Sensibilité) = VP / (VP + FN) : proportion d'exemples positifs correctement classifiés
- FPR (1-Spécificité) = FP / (FP + VN) : proportion d'exemples négatifs incorrectement classifiés

Où VP = vrais positifs, FN = faux négatifs, FP = faux positifs, VN = vrais négatifs.

L'interprétation de la courbe ROC repose sur plusieurs principes :

1. Un classifieur parfait produirait une courbe passant par le coin supérieur gauche (TPR=1, FPR=0)
2. La diagonale du graphique (y=x) représente un classifieur aléatoire
3. Plus la courbe s'éloigne vers le coin supérieur gauche, meilleur est le modèle

L'aire sous la courbe ROC (AUC-ROC) est une métrique agrégée qui résume la performance du modèle en une seule valeur. Elle peut être interprétée comme la probabilité qu'un exemple positif aléatoire soit classé avec un score plus élevé qu'un exemple négatif aléatoire. Une AUC de 0.5 indique un modèle sans pouvoir discriminant (équivalent à un tirage aléatoire), tandis qu'une AUC de 1.0 représente un modèle parfait.

## Applications et limites

La courbe ROC est particulièrement utile dans les contextes suivants :
- Comparaison de plusieurs modèles de classification
- Sélection du seuil optimal selon les coûts relatifs des erreurs
- Évaluation des modèles sur des données déséquilibrées

Cependant, elle présente certaines limites :
- Elle peut être trompeuse lorsque les classes sont très déséquilibrées (dans ce cas, la courbe Precision-Recall peut être préférable)
- Elle ne tient pas compte des probabilités prédites, seulement de leur ordre
- Elle ne reflète pas directement les coûts métier des différents types d'erreurs

Pour choisir un point optimal sur la courbe ROC, il faut souvent considérer le compromis entre sensibilité et spécificité en fonction du contexte d'application spécifique et des coûts associés aux différents types d'erreurs.