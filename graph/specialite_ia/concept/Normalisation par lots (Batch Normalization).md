---
title: Normalisation par lots (Batch Normalization)
type: concept
tags:
- Deep Learning
- Réseaux de neurones
- Normalisation
- Optimisation
- Apprentissage automatique
- Batch Normalization
- Entraînement des modèles
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo:
- '[[Initialisation des poids]]'
- '[[Dilemme biais-variance]]'
- '[[Les différentes métriques d''erreur]]'
isPartOf: '[[Méthodes de régularisation en machine learning]]'
---
## Généralité

La [normalisation par lots](https://fr.wikipedia.org/wiki/Normalisation_par_lots) (Batch Normalization) est une technique utilisée en [apprentissage profond](https://fr.wikipedia.org/wiki/Apprentissage_profond) pour stabiliser et accélérer l'entraînement des [réseaux de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels). Proposée en 2015 par Sergey Ioffe et Christian Szegedy (chercheurs chez Google), cette méthode s'est rapidement imposée comme un standard dans l'entraînement des réseaux neuronaux profonds.

## Points clés

- Réduit la dépendance aux initialisations des poids, permettant d'utiliser des taux d'apprentissage plus élevés
- Limite les problèmes de [disparition ou d'explosion des gradients](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_gradient)
- Agit comme un régularisateur léger, réduisant parfois le besoin d'autres techniques comme le [dropout](https://fr.wikipedia.org/wiki/Dropout)
- Améliore significativement la vitesse de convergence en réduisant les oscillations pendant l'optimisation
- Fonctionne particulièrement bien avec les [réseaux convolutifs](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif) et les réseaux résiduels (ResNets)

## Détails

### Fonctionnement technique

La normalisation par lots opère en deux étapes principales sur chaque lot de données pendant l'entraînement :

1. **Normalisation statistique** :
   - Calcul de la moyenne et variance pour chaque lot
   - Normalisation des activations : x̂ = (x - μ) / √(σ² + ε)
   - ε étant une petite constante pour la stabilité numérique

2. **Transformation apprenable** :
   - Application de paramètres γ (échelle) et β (décalage)
   - Sortie finale : y = γ * x̂ + β

Pendant l'inférence, on utilise généralement les moyennes et variances mobiles calculées pendant l'entraînement.

### Avantages principaux

- **Stabilité d'entraînement** : Réduit la sensibilité aux initialisations aléatoires
- **Performance** : Permet d'utiliser des taux d'apprentissage jusqu'à 14 fois plus élevés
- **Régularisation** : Effet régularisant similaire au dropout dans certains cas
- **Convergence accélérée** : Réduit le nombre d'itérations nécessaires
- **Compatibilité** : Fonctionne bien avec diverses architectures neuronales

### Limitations et considérations pratiques

- **Taille des lots** : Performance dégradée avec des lots de moins de 16 échantillons
- **Complexité** : Augmente légèrement le coût computationnel
- **Paramètres** : Introduit deux paramètres supplémentaires par couche (γ et β)
- **RNN** : Moins efficace avec les [réseaux récurrents](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents)
- **Optimisation** : Nécessite un réglage minutieux du momentum pour les statistiques d'inférence

La normalisation par lots reste cependant une des techniques les plus influentes en apprentissage profond, ayant permis des avancées significatives dans l'entraînement de réseaux très profonds.