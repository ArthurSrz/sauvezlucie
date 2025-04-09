---
title: Théorie PAC (Probably Approximately Correct)
type: concept
tags:
- Apprentissage automatique
- Théorie PAC
- Leslie Valiant
- Modélisation mathématique
- Généralisation
- Algorithmes d'apprentissage
- Garanties théoriques
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
---
## Généralité

La théorie [PAC](https://fr.wikipedia.org/wiki/Apprentissage_probablement_approximativement_correct) (Probably Approximately Correct) est un cadre théorique fondamental en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui fournit des garanties mathématiques sur la performance des algorithmes d'apprentissage. Introduite par [Leslie Valiant](https://fr.wikipedia.org/wiki/Leslie_Valiant) en 1984, cette théorie permet d'évaluer la capacité d'un modèle à généraliser à partir d'un ensemble de données d'entraînement fini.

## Points clés

- **Définition formelle** : Un algorithme est [PAC-apprenant](https://fr.wikipedia.org/wiki/Apprentissage_PAC) s'il peut produire une hypothèse avec une erreur faible et une probabilité élevée sur des données non vues.
- **Complexité d'échantillonnage** : La théorie établit des bornes sur le nombre d'exemples nécessaires pour apprendre un concept, dépendant souvent de la [dimension VC](https://fr.wikipedia.org/wiki/Dimension_de_Vapnik-Chervonenkis).
- **Applications pratiques** : Sous-tend de nombreux algorithmes modernes comme les [machines à vecteurs de support](https://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support) et les [boosting algorithms](https://fr.wikipedia.org/wiki/Boosting).
- **Paramètres clés** : Précision (ε), confiance (δ) et taille d'échantillon (m) sont les trois paramètres principaux de la théorie.

## Détails

Le cadre PAC établit des bornes sur le nombre d'exemples nécessaires pour qu'un algorithme apprenne un concept avec une haute probabilité (1-δ) et une erreur faible (inférieure à ε). Un problème est dit PAC-apprenable s'il existe un algorithme qui, pour toute distribution de probabilité sur les données, peut produire un classifieur satisfaisant ces conditions en temps polynomial.

Les paramètres principaux incluent :
- **Précision (ε)** : L'erreur maximale tolérée entre l'hypothèse apprise et le concept cible (typiquement entre 0 et 0.1)
- **Confiance (δ)** : La probabilité que l'algorithme produise une hypothèse satisfaisant la précision ε (souvent fixé à 0.01 ou 0.05)
- **Taille de l'échantillon (m)** : Le nombre d'exemples nécessaires, avec des bornes théoriques dépendant de la complexité de la classe de concepts

Parmi les concepts avancés, on trouve :
- **Dimension VC** : Mesure de la capacité d'une classe de fonctions à classifier des points de manière diverse
- **Apprentissage PAC bayésien** : Extension intégrant des connaissances a priori via des distributions de probabilité
- **Classes de concepts** : Distinction entre concepts PAC-apprenables, faiblement apprenables et non-apprenables

La théorie PAC a influencé de nombreux domaines :
- Les méthodes de régularisation dans les réseaux de neurones
- Le développement des algorithmes de boosting comme [AdaBoost](https://fr.wikipedia.org/wiki/AdaBoost)
- Les extensions vers l'apprentissage actif et semi-supervisé
- La compréhension des limites fondamentales de l'apprentissage

Elle reste un pilier théorique pour comprendre les capacités et limites des algorithmes d'apprentissage automatique, bien que son application directe aux architectures modernes comme les réseaux profonds reste un sujet de recherche actif.