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
date_creation: '2025-03-20'
date_modification: '2025-03-20'
follows: '[[Choix de la fonction de minimisation]]'
subClassOf: '[[Les étapes clés pour concevoir un système d''Intelligence Artificielle]]'
precedes: '[[Entraînement d''un modèle d''IA]]'
seeAlso:
- '[[Métriques d''évaluation pour les modèles de régression]]'
- '[[Métriques robustes aux valeurs aberrantes]]'
- '[[Compromis biais-variance dans la sélection de métriques]]'
hasPart: '[[Critères d''erreur pour séries temporelles]]'
---
## Généralité

Le choix de la mesure d'erreur détermine comment évaluer et quantifier les performances d'un modèle d'intelligence artificielle, en définissant mathématiquement l'écart entre les prédictions et les valeurs réelles.

## Points clés

- Doit être alignée avec l'objectif métier du projet d'IA
- Varie selon le type de problème (classification, régression, ranking, etc.)
- Influence directement le comportement du modèle pendant l'apprentissage
- Peut nécessiter des ajustements pour les cas déséquilibrés ou les coûts d'erreur asymétriques

## Détails

La mesure d'erreur (ou métrique d'évaluation) joue un rôle critique dans le développement d'un système d'intelligence artificielle. Elle permet non seulement d'évaluer les performances d'un modèle, mais influence également son comportement pendant l'apprentissage et guide les choix d'optimisation.

### Métriques pour les problèmes de régression

Pour les problèmes prédisant des valeurs continues:

- **Erreur Quadratique Moyenne (MSE)**: Moyenne des carrés des différences entre prédictions et valeurs réelles. Particulièrement sensible aux valeurs aberrantes en raison de l'élévation au carré.
  
- **Erreur Absolue Moyenne (MAE)**: Moyenne des valeurs absolues des erreurs. Plus robuste aux outliers que la MSE.
  
- **Erreur Relative Moyenne (MAPE)**: Exprime l'erreur en pourcentage relatif à la valeur réelle, utile quand l'échelle des valeurs est importante.
  
- **R²**: Coefficient de détermination indiquant la proportion de variance expliquée par le modèle. Varie entre 0 et 1 (ou négatif si le modèle est pire qu'une simple moyenne).

### Métriques pour les problèmes de classification

Pour les problèmes d'attribution d'étiquettes:

- **Précision (Accuracy)**: Proportion de prédictions correctes. Problématique pour les jeux de données déséquilibrés.
  
- **Précision et Rappel**: 
  - Précision: Proportion des instances identifiées comme positives qui sont correctes
  - Rappel: Proportion des instances positives réelles qui ont été correctement identifiées
  
- **F1-Score**: Moyenne harmonique de la précision et du rappel, équilibrant ces deux aspects.
  
- **AUC-ROC**: Mesure la capacité du modèle à distinguer les classes à différents seuils de décision.
  
- **Log Loss (Cross-Entropy)**: Pénalise fortement les probabilités confiantes mais incorrectes, encourageant la calibration du modèle.

### Considérations pour le choix de la métrique

La sélection d'une métrique appropriée dépend de plusieurs facteurs:

1. **Contexte métier**: Les conséquences des différents types d'erreurs (faux positifs vs faux négatifs) peuvent avoir des impacts très différents selon le domaine (médical, financier, etc.).

2. **Distribution des données**: Pour les jeux déséquilibrés, des métriques comme l'accuracy peuvent être trompeuses.

3. **Interprétabilité**: Certaines métriques sont plus facilement compréhensibles par les parties prenantes non techniques.

4. **Objectif d'optimisation**: La métrique choisie guidera l'algorithme d'apprentissage et influencera le comportement du modèle.

Il est souvent judicieux d'utiliser plusieurs métriques complémentaires pour obtenir une vision plus complète des performances du modèle et éviter les optimisations trop ciblées qui pourraient masquer certaines faiblesses.