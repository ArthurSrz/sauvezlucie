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

Les métriques robustes aux valeurs aberrantes sont des mesures statistiques conçues pour maintenir leur fiabilité même en présence de données extrêmes ou atypiques. Contrairement aux métriques classiques comme la [moyenne](https://fr.wikipedia.org/wiki/Moyenne) ou l'[écart-type](https://fr.wikipedia.org/wiki/%C3%89cart_type), ces métriques offrent une représentation plus fidèle de la tendance centrale et de la dispersion des données dans des contextes réels souvent imparfaits. Elles trouvent leurs origines dans le domaine de la [statistique robuste](https://fr.wikipedia.org/wiki/Statistique_robuste), un champ d'étude formalisé notamment par [Peter Huber](https://fr.wikipedia.org/wiki/Peter_Huber).

## Points clés

- **Minimisent l'influence des [valeurs aberrantes](https://fr.wikipedia.org/wiki/Valeur_aberrante)** sans nécessiter leur identification ou suppression préalable (approche formalisée par [Tukey](https://fr.wikipedia.org/wiki/John_Tukey))
- **Essentielles dans les domaines avec observations extrêmes** ([finance](https://fr.wikipedia.org/wiki/Finance), détection d'anomalies, traitement d'images)
- **Caractérisées par leur point de rupture** (proportion de données aberrantes tolérées), notion développée par Frank Hampel
- **Compromis entre robustesse et efficience statistique** (ex: médiane a 50% de point de rupture mais 64% d'efficience)
- **Applications émergentes** dans l'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) et l'analyse de données satellitaires

## Détails

### Mesures de tendance centrale robustes

La [médiane](https://fr.wikipedia.org/wiki/M%C3%A9diane_(statistiques)) est la métrique robuste la plus connue avec un point de rupture de 50%. D'autres estimateurs incluent :

- [Moyenne tronquée](https://fr.wikipedia.org/wiki/Moyenne_tronqu%C3%A9e) (popularisée par Tukey)
- Moyenne winsorisée (utile en finance)
- [M-estimateurs](https://fr.wikipedia.org/wiki/M-estimateur) comme celui de Huber (efficience de 95%)

### Mesures de dispersion robustes

- [Écart absolu médian](https://fr.wikipedia.org/wiki/%C3%89cart_absolu_m%C3%A9dian) (MAD) - point de rupture de 50%
- [Écart interquartile](https://fr.wikipedia.org/wiki/%C3%89cart_interquartile) (IQR) - utilisé dans les boxplots
- Écart-type tronqué/winsorisé
- Estimateurs basés sur les rangs

### Applications pratiques

En [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique), les métriques robustes servent à :

- Évaluer des modèles sur données bruitées (MAE vs MSE)
- Détection d'anomalies et fraudes
- Prétraitement des données (méthodes comme [RANSAC](https://fr.wikipedia.org/wiki/RANSAC))
- Traitement d'images (filtrage du bruit impulsionnel)

### Limites et considérations

- Efficacité statistique moindre pour données normalement distribuées (médiane: 64% vs moyenne: 100%)
- Choix dépend du contexte :
  - Sciences environnementales/météorologie : méthodes robustes préférées
  - Données propres/normalement distribuées : métriques classiques
  - Applications émergentes : hybrides comme estimateurs de Huber

Cette discipline continue d'évoluer avec des applications dans des domaines variés.