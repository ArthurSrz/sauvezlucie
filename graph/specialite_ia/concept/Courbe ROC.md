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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Apprentissage supervisé]]'
uses: '[[Entraînement d''un modèle d''IA]]'
---
## Généralité

La courbe [ROC](https://fr.wikipedia.org/wiki/Courbe_ROC) (Receiver Operating Characteristic) est un outil graphique fondamental pour évaluer les performances des modèles de [classification binaire](https://fr.wikipedia.org/wiki/Classification_binaire). Développée initialement pendant la [Seconde Guerre mondiale](https://fr.wikipedia.org/wiki/Seconde_Guerre_mondiale) pour l'analyse des signaux radar, elle représente la relation entre le taux de vrais positifs (sensibilité) et le taux de faux positifs (1-spécificité) pour différents seuils de décision.

## Points clés

- Permet de visualiser le compromis entre sensibilité et spécificité à différents seuils de classification
- L'[AUC-ROC](https://fr.wikipedia.org/wiki/Courbe_ROC#Aire_sous_la_courbe_(AUC)) (aire sous la courbe) quantifie la performance globale (1.0 = parfait, 0.5 = aléatoire)
- Particulièrement utile pour les problèmes avec classes déséquilibrées
- Outil standard pour comparer différents modèles en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique)
- Large application en médecine diagnostique, psychologie et imagerie médicale

## Détails

La courbe ROC est construite en faisant varier le seuil de décision d'un classifieur binaire et en calculant pour chaque seuil :
- TPR (Sensibilité) = VP / (VP + FN) : proportion d'exemples positifs correctement classifiés
- FPR (1-Spécificité) = FP / (FP + VN) : proportion d'exemples négatifs incorrectement classifiés

Où VP = vrais positifs, FN = faux négatifs, FP = faux positifs, VN = vrais négatifs.

Principes d'interprétation :
- Un classifieur parfait produit une courbe passant par le coin supérieur gauche (TPR=1, FPR=0)
- La diagonale (y=x) représente un classifieur aléatoire
- Plus la courbe s'éloigne vers le coin supérieur gauche, meilleur est le modèle

### Applications pratiques
- **Comparaison de modèles** : Évaluation objective indépendante du seuil
- **Sélection du seuil optimal** : Selon les coûts relatifs des erreurs (ex: [indice de Youden](https://fr.wikipedia.org/wiki/Indice_de_Youden) en médecine)
- **Données déséquilibrées** : Moins affectée par la distribution des classes que d'autres métriques

### Limites et considérations
- Peut être trompeuse pour des classes très déséquilibrées (ratios <1:100)
- Ne tient pas compte des probabilités prédites, seulement de leur ordre
- Ne reflète pas directement les coûts métier des différents types d'erreurs
- Pour les déséquilibres extrêmes, la courbe Precision-Recall peut être préférable

### Choix du point optimal
Le choix dépend du contexte d'application :
- **Médecine** : Priorité à la haute sensibilité (peu de faux négatifs)
- **Sécurité informatique** : Priorité à la haute spécificité (peu de faux positifs)
- **Applications générales** : Compromis selon les coûts relatifs des erreurs

### Échelle d'interprétation de la AUC
- 0.9-1.0 : Excellent
- 0.8-0.9 : Bon
- 0.7-0.8 : Acceptable
- <0.7 : Médiocre
(Note: Ces seuils peuvent varier selon les domaines)