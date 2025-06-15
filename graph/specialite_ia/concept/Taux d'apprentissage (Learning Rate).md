---
title: Taux d'apprentissage (Learning Rate)
type: concept
tags:
- Machine Learning
- Deep Learning
- Réseaux de Neurones
- Hyperparamètres
- Optimisation
- Descente de Gradient
- Apprentissage Automatique
date_creation: '2025-04-08'
date_modification: '2025-04-08'
depends: '[[L''algorithme du gradient]]'
hasPart: '[[Hyperparamètres vs paramètres du modèle ]]'
subClassOf: '[[Entraînement d''un modèle d''IA]]'
---
## Généralité

Le [taux d'apprentissage](https://fr.wikipedia.org/wiki/Taux_d%27apprentissage) (learning rate) est un hyperparamètre crucial dans les algorithmes [d'apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique), en particulier pour l'entraînement des [réseaux de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels). Il détermine la taille des pas effectués lors de la mise à jour des poids du modèle pendant la descente de gradient, influençant ainsi la vitesse et la qualité de la convergence.

## Points clés

- Contrôle la vitesse à laquelle un modèle apprend à partir des données
- Compromis entre vitesse d'apprentissage et stabilité
- Valeurs typiques entre 0.1 et 10^-6 selon les modèles
- Méthodes adaptatives comme [Adam](https://fr.wikipedia.org/wiki/Adam_(optimisation)) ou RMSprop
- Impact différent selon l'architecture du modèle

## Détails

Le taux d'apprentissage influence directement la performance d'un modèle d'apprentissage automatique. Un **taux trop élevé** peut provoquer des oscillations ou une divergence, où le modèle ne converge pas vers un minimum de la fonction de perte. Selon Wikipédia, ce compromis entre vitesse et stabilité est bien documenté dans la littérature sur l'[optimisation mathématique](https://fr.wikipedia.org/wiki/Optimisation_(mathematiques)). À l'inverse, un **taux trop faible** ralentit considérablement l'entraînement et peut bloquer le modèle dans un minimum local non optimal.

Plusieurs méthodes permettent d'optimiser le taux d'apprentissage :
- **Taux constant** : Fixé manuellement avant l'entraînement, nécessite souvent des essais-erreurs
- **Planification du taux (Learning Rate Scheduling)** : Réduit progressivement le taux selon un calendrier prédéfini
- **Méthodes adaptatives** : Algorithmes comme [Adam](https://fr.wikipedia.org/wiki/Adam_(optimisation)), RMSprop ou Adagrad qui ajustent automatiquement le taux

Les valeurs optimales varient selon les applications :
- **Réseaux de neurones profonds** : Généralement compris entre 0.001 et 0.0001
- **Régression logistique** : Peut aller jusqu'à 0.1
- **Modèles simples** : Entre 0.001 et 0.1

Parmi les bonnes pratiques, on recommande :
- Utiliser une recherche sur grille pour trouver un taux initial optimal
- Surveiller la courbe de perte pour détecter des signes de sous/sur-apprentissage
- Combiner avec des techniques comme le momentum
- Adapter selon l'architecture du modèle et la nature des données

Historiquement, le concept est issu des travaux sur la méthode du gradient en optimisation mathématique datant du 19ème siècle. Son application en machine learning remonte aux années 1950-1960 avec le perceptron de Rosenblatt, mais son importance s'est considérablement accrue avec l'essor des réseaux neuronaux profonds dans les années 2010.

Notons que le taux d'apprentissage n'est pas à confondre avec le momentum, un autre hyperparamètre qui influence la direction de la mise à jour plutôt que son amplitude.