---
title: Algorithmes génétiques en IA
type: concept
tags:
- intelligence artificielle
- algorithmes génétiques
- optimisation
- John Holland
- évolution
- sélection naturelle
- algorithmes évolutionnaires
- recherche
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo: '[[Apprentissage automatique (Machine Learning)]]'
subClassOf: '[[Techniques bio-inspirées en IA]]'
seeAlso:
- '[[Algorithmes génétiques pour l''optimisation combinatoire]]'
- '[[Optimisation stigmergique : modélisation des comportements collectifs dans les
  systèmes complexes]]'
- '[[Programmation génétique]]'
isPartOf: '[[Distillation de connaissances en IA]]'
---
## Généralité

Les [algorithmes génétiques](https://fr.wikipedia.org/wiki/Algorithme_g%C3%A9n%C3%A9tique) (AG) sont des méthodes d'optimisation et de recherche inspirées par le processus d'[évolution naturelle](https://fr.wikipedia.org/wiki/%C3%89volution_(biologie)) et la [sélection naturelle](https://fr.wikipedia.org/wiki/S%C3%A9lection_naturelle). Développés initialement par [John Holland](https://fr.wikipedia.org/wiki/John_Henry_Holland) et ses collègues à l'Université du Michigan dans les années 1960 et 1970, ces algorithmes appartiennent à la famille plus large des algorithmes évolutionnaires en intelligence artificielle.

## Points clés

- Inspirés des principes de la génétique mendélienne et de la théorie synthétique de l'évolution
- Utilisent trois opérateurs principaux : sélection, croisement et mutation
- Particulièrement efficaces pour les problèmes NP-difficiles et les vastes espaces de recherche
- Applications variées : optimisation de fonctions, machine learning, planification, conception automatique
- Avantages clés : robustesse, parallélisme implicite, capacité à traiter des problèmes mal définis

## Détails

Un algorithme génétique typique fonctionne selon ces étapes :

1. **Initialisation** : Création d'une population initiale de solutions candidates
2. **Évaluation** : Calcul de la valeur d'adaptation (fitness) de chaque individu
3. **Sélection** : Choix des individus pour la reproduction (méthodes courantes : roulette, tournoi ou élitisme)
4. **Croisement** : Combinaison de paires d'individus (taux typique : 60-95%)
5. **Mutation** : Modification aléatoire (taux généralement faible : 0.1-5%) 
6. **Remplacement** : Formation d'une nouvelle génération
7. **Itération** : Répétition jusqu'à atteindre un critère d'arrêt

Les solutions sont encodées sous forme de "chromosomes" :
- **Binaire** : Traditionnel, idéal pour les problèmes combinatoires
- **Réel** : Pour les problèmes d'optimisation continue
- **Permutation** : Pour les problèmes d'ordonnancement
- **Structure arborescente** : Utilisé en programmation génétique

Domaines d'application principaux :
- **Apprentissage automatique** :
  - Optimisation des hyperparamètres
  - Sélection de caractéristiques
- **Réseaux de neurones** :
  - Détermination des poids et architectures
- **Planification et ordonnancement** :
  - Problème du voyageur de commerce
  - Optimisation de trajectoires
- **Conception assistée par ordinateur**
- **Robotique**
- **Arts génératifs**

**Avantages** :
- Capacité à traiter des espaces de recherche complexes
- Robustesse face aux optima locaux
- Parallélisation naturelle
- Applicable à des problèmes mal définis
- Flexibilité dans la représentation

**Limitations** :
- Difficulté à définir une fonction de fitness appropriée
- Risque de convergence prématurée
- Coût computationnel potentiellement élevé
- Sensibilité au choix des paramètres
- Difficulté à garantir des solutions optimales

Variantes modernes :
- Stratégies d'évolution
- Programmation génétique
- Algorithmes à estimation de distribution
- Algorithmes génétiques hybrides