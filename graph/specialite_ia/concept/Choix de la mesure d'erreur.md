---
title: Choix de la mesure d'erreur
type: concept
tags:
- mesure d'erreur
- évaluation
- métriques
- performance
- analyse
- statistiques
- modélisation
- erreur
date_creation: '2025-04-08'
date_modification: '2025-04-08'
follows: '[[Choix de la fonction de minimisation]]'
subClassOf: '[[Les étapes clés pour concevoir un système d''Intelligence Artificielle]]'
precedes: '[[Entraînement d''un modèle d''IA]]'
seeAlso:
- '[[Métriques d''évaluation pour les modèles de régression]]'
- '[[Métriques robustes aux valeurs aberrantes]]'
- '[[Compromis biais-variance dans la sélection de métriques]]'
- '[[Les différentes métriques d''erreur]]'
- '[[Fonctions de perte en apprentissage profond]]'
hasPart: '[[Critères d''erreur pour séries temporelles]]'
---
## Généralité

La mesure d'erreur est une étape fondamentale en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) et en [statistiques](https://fr.wikipedia.org/wiki/Statistique). Elle permet d'évaluer et quantifier les performances d'un modèle d'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) en définissant mathématiquement l'écart entre les prédictions du modèle et les valeurs réelles (ground truth). Son choix influence directement le comportement du modèle pendant l'apprentissage via la [descente de gradient](https://fr.wikipedia.org/wiki/Algorithme_du_gradient).

## Points clés

- **Dépend du type de problème** :
  - Classification : perte logistique, [entropie croisée](https://fr.wikipedia.org/wiki/Entropie_crois%C3%A9e)
  - Régression : [MSE](https://fr.wikipedia.org/wiki/Erreur_quadratique_moyenne), MAE, Huber
  - Ranking : NDCG, précision moyenne

- **Doit être alignée avec l'objectif métier** (ex: minimiser les faux négatifs en détection de fraude)

- **Caractéristiques importantes** :
  - Différentiabilité (comme le MSE) pour permettre l'optimisation
  - Robustesse aux valeurs aberrantes (comme MAE)
  - Adaptation aux cas déséquilibrés (F1-score, MCC)

## Détails

### Mesures d'erreur courantes

Selon Wikipédia, plusieurs types de mesures sont couramment utilisées :
- [Erreur quadratique moyenne](https://fr.wikipedia.org/wiki/Erreur_quadratique_moyenne) (MSE) : pénalise fortement les grandes erreurs
- [Erreur absolue moyenne](https://fr.wikipedia.org/wiki/Erreur_absolue_moyenne) (MAE) : moins sensible aux outliers
- Perte logistique : principalement pour les problèmes de classification binaire
- [Divergence de Kullback-Leibler](https://fr.wikipedia.org/wiki/Divergence_de_Kullback-Leibler) : dissimilarité entre distributions

### Métriques pour les problèmes de régression

Pour les problèmes prédisant des valeurs continues :

- **MSE** : Moyenne des carrés des différences. Sensible aux valeurs aberrantes.
- **MAE** : Moyenne des valeurs absolues des erreurs. Plus robuste mais non différentiable en zéro.
- **MAPE** : Erreur en pourcentage relatif. Indéfinie quand la valeur réelle est nulle.
- **R²** : Coefficient de détermination (varie entre -∞ et 1).
- **Perte de Huber** : Combinaison du MSE et MAE, robuste et différentiable.

### Métriques pour les problèmes de classification

Pour les problèmes d'attribution d'étiquettes :

- **Précision (Accuracy)** : Proportion de prédictions correctes. Problématique pour données déséquilibrées.
- **Précision et Rappel** :
  - Précision : Pertinente quand les faux positifs sont coûteux
  - Rappel : Crucial pour applications comme le [diagnostic médical](https://fr.wikipedia.org/wiki/Diagnostic_m%C3%A9dical)
- **F1-Score** : Moyenne harmonique de précision et rappel. Utile pour données déséquilibrées.
- **AUC-ROC** : Capacité à distinguer les classes à différents seuils.
- **Log Loss** : Pénalise les probabilités confiantes mais incorrectes.
- **Matrice de confusion** : Outil visuel complet montrant vrais/faux positifs/négatifs.

### Considérations pour le choix de la métrique

1. **Contexte métier** : Impacts différents selon le domaine (ex: faux négatifs en détection de fraude)
2. **Distribution des données** : Métriques adaptées aux jeux déséquilibrés (MCC)
3. **Interprétabilité** : Certaines métriques plus compréhensibles (MAPE en pourcentage)
4. **Objectif d'optimisation** : Influence le comportement du modèle
5. **Propriétés mathématiques** : Convexité, différentiabilité

Il est souvent judicieux d'utiliser plusieurs métriques complémentaires pour une évaluation complète des performances du modèle.