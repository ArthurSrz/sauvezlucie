---
title: Arbre de décision
type: concept
tags:
- arbre de décision
- algorithme
- machine learning
- data science
- aide à la décision
- classification
- modèle prédictif
date_creation: '2025-03-22'
date_modification: '2025-03-22'
isPartOf:
- '[[Apprentissage automatique (Machine Learning)]]'
- '[[Apprentissage supervisé]]'
seeAlso: '[[Forêt d''arbres décisionnels IA]]'
hasPart:
- '[[Impureté de Gini, entropie et erreur de classification]]'
- '[[Algorithme ID3]]'
- '[[Algorithme C4.5]]'
- '[[CHAID (CHi-squared Automatic Interaction Detector) ]]'
---
## Généralité

Un [arbre de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision) est un modèle prédictif utilisé en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) et en statistiques qui représente les décisions et leurs conséquences possibles sous forme d'arbre. Cette structure hiérarchique permet de décomposer un problème complexe en une série de décisions plus simples, facilitant ainsi l'analyse et la prise de décision.

Les arbres de décision sont particulièrement appréciés pour leur interprétabilité et leur capacité à modéliser des relations non linéaires entre variables. Ils trouvent leurs origines dans les travaux des années 1960 sur les systèmes d'apprentissage automatique et se sont popularisés avec des algorithmes comme [ID3](https://fr.wikipedia.org/wiki/ID3_(algorithme)) développé par Ross Quinlan en 1986, et ses améliorations ultérieures (C4.5, CART).

## Points clés

- Structure intuitive composée de [nœuds](https://fr.wikipedia.org/wiki/N%C5%93ud_(informatique)) (tests sur les attributs), de branches (résultats des tests) et de feuilles (décisions finales ou prédictions)
- Algorithmes populaires incluent [ID3](https://fr.wikipedia.org/wiki/ID3_(algorithme)), [C4.5](https://fr.wikipedia.org/wiki/C4.5), CART et [Random Forest](https://fr.wikipedia.org/wiki/For%C3%AAt_al%C3%A9atoire)
- Utilisable pour des tâches de classification (comme le diagnostic médical) et de régression (comme la prédiction de prix)
- Avantage majeur: facilité d'interprétation et de visualisation des règles de décision ("boîte blanche")
- Limite principale: tendance au [sur-apprentissage](https://fr.wikipedia.org/wiki/Surapprentissage) (overfitting)

## Détails

Un arbre de décision se compose de plusieurs éléments clés:
- **Nœud racine**: Point de départ de l'arbre, représentant l'attribut le plus discriminant
- **Nœuds internes**: Tests effectués sur des attributs spécifiques
- **Branches**: Résultats possibles des tests aux nœuds
- **Feuilles**: Nœuds terminaux représentant les décisions finales ou prédictions

La construction d'un arbre de décision repose sur la division récursive des données selon des critères d'homogénéité:
- **Entropie et gain d'information**: Utilisés par l'algorithme ID3
- **Indice de Gini**: Mesure d'impureté privilégiée par l'algorithme CART
- **Ratio de gain**: Amélioration du gain d'information utilisée par C4.5

Pour les arbres de régression, la variance est typiquement utilisée comme critère de division.

**Avantages:**
- Interprétabilité élevée (modèles "boîte blanche")
- Peu de prétraitement des données nécessaire
- Gestion naturelle des valeurs manquantes et des données catégorielles
- Capacité à capturer des relations non linéaires entre variables
- Robustesse relative aux valeurs aberrantes

**Limites:**
- Tendance au surapprentissage
- Instabilité face aux petites variations dans les données
- Performance parfois inférieure à d'autres algorithmes plus complexes

Pour surmonter certaines limitations, plusieurs techniques existent:
- **Élagage (pruning)**: Réduction de la complexité de l'arbre
- **Ensembles d'arbres**: 
  - [Random Forest](https://fr.wikipedia.org/wiki/For%C3%AAt_al%C3%A9atoire)
  - Gradient Boosting
- **Méthodes de régularisation**

Les arbres de décision sont largement utilisés dans divers domaines:
- Finance: évaluation des risques de crédit
- Médecine: aide au diagnostic
- Marketing: segmentation de clientèle
- Systèmes de recommandation
- Analyse de fiabilité et maintenance prédictive