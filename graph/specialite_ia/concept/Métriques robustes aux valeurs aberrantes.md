---
title: Métriques robustes aux valeurs aberrantes
type: concept
tags:
- statistiques
- valeurs aberrantes
- métriques robustes
- analyse de données
- tendance centrale
- dispersion
- outliers
- statistique descriptive
- robustesse
date_creation: '2025-03-22'
date_modification: '2025-03-22'
differentFrom: '[[La méthode des moindres carrés ordinaires]]'
isPartOf: '[[L''algorithme du gradient]]'
subClassOf: '[[Choix de la mesure d''erreur]]'
hasPart: '[[Validation croisée et évaluation de modèles]]'
---
## Généralité

Les métriques robustes aux valeurs aberrantes sont des mesures statistiques conçues pour maintenir leur fiabilité même en présence de données extrêmes ou atypiques. Contrairement aux métriques classiques comme la moyenne ou l'écart-type, qui peuvent être fortement influencées par des valeurs aberrantes, les métriques robustes offrent une représentation plus fidèle de la tendance centrale et de la dispersion des données dans des contextes réels souvent imparfaits.

## Points clés

- Les métriques robustes minimisent l'influence des valeurs aberrantes sans nécessiter leur identification ou suppression préalable
- Elles sont essentielles dans les domaines où les données contiennent naturellement des observations extrêmes (finance, détection d'anomalies, traitement d'images)
- Le compromis entre robustesse et efficience statistique doit être considéré lors du choix d'une métrique
- Les métriques robustes sont souvent caractérisées par leur point de rupture, qui quantifie la proportion de données aberrantes qu'elles peuvent tolérer

## Détails

### [Mesures](https://fr.wikipedia.org/wiki/Mesures) de tendance centrale robustes

La médiane est la métrique robuste la plus connue pour estimer la tendance centrale. Contrairement à la moyenne arithmétique, la médiane n'est pas affectée par l'amplitude des valeurs extrêmes, mais uniquement par leur nombre. Son point de rupture est de 50%, ce qui signifie qu'elle reste fiable même si près de la moitié des données sont aberrantes.

D'autres estimateurs robustes de tendance centrale incluent :
- La moyenne tronquée : calcule la moyenne après avoir éliminé un pourcentage fixe des valeurs les plus extrêmes
- La moyenne winsorisée : remplace les valeurs extrêmes par les valeurs les plus proches non considérées comme aberrantes
- Les M-estimateurs : généralisent la notion de maximum de vraisemblance avec des fonctions de perte moins sensibles aux valeurs extrêmes

### [Mesures](https://fr.wikipedia.org/wiki/Mesures) de dispersion robustes

L'écart absolu médian (MAD) est l'équivalent robuste de l'écart-type. Il est défini comme la médiane des écarts absolus par rapport à la médiane des données. D'autres mesures robustes de dispersion incluent :
- L'écart interquartile (IQR) : différence entre le 3ème et le 1er quartile
- L'écart-type tronqué ou winsorisé
- Les estimateurs de dispersion basés sur les rangs

### Applications pratiques

En apprentissage automatique, les métriques robustes sont particulièrement utiles pour :
- L'évaluation de modèles sur des données bruitées (MAE vs MSE)
- La détection d'anomalies et de fraudes
- Le prétraitement des données sans élimination manuelle des valeurs aberrantes
- Les algorithmes d'apprentissage robustes comme RANSAC (Random Sample Consensus)

### Limites et considérations

Bien que les métriques robustes offrent une protection contre les valeurs aberrantes, elles présentent généralement une efficacité statistique moindre lorsque les données suivent parfaitement une distribution normale. Le choix entre métriques classiques et robustes dépend donc du contexte d'application, de la qualité des données et de l'importance relative accordée à la robustesse par rapport à l'efficacité statistique.