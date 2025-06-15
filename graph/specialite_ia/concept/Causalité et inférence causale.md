---
title: Causalité et inférence causale
type: concept
tags:
- causalité
- inférence causale
- statistiques
- recherche scientifique
- méthodologie
- analyse de données
- sciences sociales
date_creation: '2025-04-04'
date_modification: '2025-04-04'
isPartOf: '[[Algorithme C4.5]]'
---
## Généralité

La [causalité](https://fr.wikipedia.org/wiki/Causalité) et l'[inférence causale](https://fr.wikipedia.org/wiki/Inférence_causale) sont des concepts fondamentaux en statistique, en sciences sociales et en recherche scientifique. La causalité désigne la relation de cause à effet entre deux variables, tandis que l'inférence causale consiste à déterminer si une variable en influence une autre, en dépassant la simple corrélation. Selon Wikipédia, l'étude de la causalité remonte aux travaux de philosophes comme [Aristote](https://fr.wikipedia.org/wiki/Aristote), et a été révolutionnée par les travaux modernes de [Judea Pearl](https://fr.wikipedia.org/wiki/Judea_Pearl).

## Points clés

- La causalité implique une relation de cause à effet, contrairement à la corrélation qui ne mesure qu'une association
- L'inférence causale nécessite des méthodes spécifiques comme les expériences randomisées (gold standard), les variables instrumentales ou les approches contrefactuelles
- Le cadre des "résultats potentiels" (potential outcomes framework) développé par Donald Rubin permet de formaliser mathématiquement des questions causales
- Les graphiques causaux (DAGs) popularisés par Judea Pearl permettent de visualiser les relations complexes entre variables
- L'inférence causale s'applique dans de nombreux domaines : médecine, économie, sciences sociales, épidémiologie, marketing et sciences politiques

## Détails

### Méthodes d'inférence causale

Il existe plusieurs méthodes pour établir une relation causale :

- **Expériences randomisées** : Considérées comme le "gold standard" lorsque réalisables
- **Méthodes d'appariement (matching)** : Pour contrôler les variables confondantes
- **Variables instrumentales** : Lorsque la randomisation est impossible
- **Différences de différences (DiD)** : Compare l'évolution avant/après intervention
- **Approches contrefactuelles** : Modélise ce qui se serait passé sans l'intervention

Un exemple bien documenté est l'étude de l'impact du tabagisme sur le cancer du poumon, où les chercheurs ont dû distinguer la corrélation observée d'une véritable relation causale.

### Applications par domaine

L'inférence causale est utilisée dans divers domaines :

- **Économie** : Évaluer l'impact des [politiques publiques](https://fr.wikipedia.org/wiki/Politique_publique) avec des méthodes comme les [différences de différences](https://fr.wikipedia.org/wiki/Méthode_des_differences_de_differences)
- **Médecine** : Déterminer l'efficacité des traitements via des [essais cliniques randomisés](https://fr.wikipedia.org/wiki/Essai_clinique_randomisé)
- **Sciences sociales** : Comprendre les effets des comportements sociaux
- **Épidémiologie** : Analyser les facteurs de risque des maladies
- **Marketing** : Mesurer l'impact des campagnes publicitaires
- **Sciences politiques** : Évaluer l'effet des institutions politiques

### Défis et limites

Malgré ses avancées, l'inférence causale reste confrontée à des défis :

- Qualité des données (biais de mesure, données manquantes)
- Hypothèses fondamentales souvent non testables empiriquement
- Complexité des systèmes étudiés (sciences sociales, épidémiologie)
- Limitations méthodologiques pour les relations dynamiques ou effets indirects

Les progrès récents en modélisation graphique causale (source: [Causal graph](https://fr.wikipedia.org/wiki/Causal_graph) sur Wikipédia) offrent cependant des perspectives prometteuses.