---
title: L'algorithme du gradient
type: concept
tags:
- algorithme
- gradient
- optimisation
- mathématiques
- apprentissage automatique
- descente de gradient
- minimisation
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf:
- '[[Apprentissage automatique (Machine Learning)]]'
- '[[Algorithmes d''optimisation bayésienne]]'
depends: '[[Apprentissage automatique (Machine Learning)]]'
hasPart: '[[Métriques robustes aux valeurs aberrantes]]'
seeAlso:
- '[[Optimiseurs adaptatifs]]'
- '[[Descente de gradient stochastique (SGD)]]'
---
## Généralité

L'[algorithme du gradient](https://fr.wikipedia.org/wiki/Algorithme_du_gradient) (ou descente de gradient) est une méthode d'optimisation itérative utilisée pour minimiser une fonction de coût en [machine learning](https://fr.wikipedia.org/wiki/Apprentissage_automatique) et en optimisation mathématique. Cette méthode, apparue initialement dans les travaux de Cauchy en 1847 (selon la page Wikipédia "Gradient descent"), constitue aujourd'hui l'un des algorithmes fondamentaux en apprentissage automatique.

Le principe repose sur le calcul itératif du gradient (vecteur des dérivées partielles) de la fonction objectif, qui indique la direction de la plus forte pente ascendante (Wikipédia "Gradient"). En ajustant progressivement les paramètres du modèle dans la direction opposée au gradient (pour une minimisation), l'algorithme converge vers un minimum local - sans garantie d'atteindre un minimum global sauf pour certaines fonctions convexes.

## Points clés

- L'[algorithme du gradient](https://fr.wikipedia.org/wiki/Algorithme_du_gradient) modifie itérativement les paramètres dans la direction opposée au gradient pour minimiser une fonction de coût
- Existe en trois variantes principales : Batch (tout le dataset), Stochastique (un exemple à la fois), et Mini-batch (compromis entre les deux)
- La performance dépend crucialement du choix du taux d'apprentissage (learning rate)
- Fondamental pour l'entraînement des [réseaux neuronaux](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) et autres modèles de machine learning
- Rencontre des défis comme les minima locaux et les plateaux, surtout pour les fonctions non-convexes

## Détails

La [descente de gradient](https://fr.wikipedia.org/wiki/Algorithme_du_gradient) repose sur l'observation que si la fonction de coût $J(\theta)$ est définie et différentiable dans un voisinage d'un point $\theta$, alors $J(\theta)$ diminue le plus rapidement dans la direction opposée au gradient $\nabla J(\theta)$. Comme mentionné dans les travaux originaux d'[Augustin-Louis Cauchy](https://fr.wikipedia.org/wiki/Augustin-Louis_Cauchy) (1847), cette méthode est particulièrement efficace pour les fonctions convexes. L'algorithme met à jour les paramètres selon la formule:

$\theta_{t+1} = \theta_t - \alpha \nabla J(\theta_t)$

où $\alpha$ est le taux d'apprentissage qui détermine la taille du pas dans la direction du gradient négatif. Selon Wikipédia, ce taux doit être soigneusement choisi : une valeur trop élevée peut faire diverger l'algorithme, tandis qu'une valeur trop faible ralentit excessivement la convergence. [Source: Wikipedia "Gradient descent"]

**Variantes principales**:
1. **Gradient Batch (BGD)**: Calcule le gradient sur l'ensemble complet des données à chaque itération. Précis mais coûteux en calcul pour de grands ensembles de données. D'après les recherches en optimisation numérique, cette méthode garantit théoriquement la convergence vers le minimum global pour les fonctions convexes. [Source: Wikipedia "Gradient descent#Batch gradient descent"]
2. **Gradient Stochastique (SGD)**: Calcule le gradient sur un seul exemple à chaque itération. Plus rapide mais avec une convergence plus bruitée. La version moderne utilise souvent un "learning rate schedule" pour diminuer progressivement le pas d'apprentissage, améliorant ainsi la stabilité. [Source: Wikipedia "Stochastic gradient descent"]
3. **Mini-Batch Gradient**: Compromis entre les deux approches précédentes, calculant le gradient sur un petit sous-ensemble de données (typiquement entre 32 et 512 échantillons). Offre un bon équilibre entre vitesse et stabilité, et est particulièrement adapté aux architectures [GPU](https://fr.wikipedia.org/wiki/Unit%C3%A9_de_traitement_graphique) modernes grâce au parallélisme des opérations matricielles. [Source: Wikipedia "Stochastic gradient descent#Mini-batch gradient descent"]

**Défis et améliorations**:
L'algorithme du gradient présente plusieurs défis:
- Le choix du taux d'apprentissage: trop petit, la convergence est lente; trop grand, elle peut diverger
- Les plateaux et les ravins dans la fonction de coût peuvent ralentir la convergence, surtout pour les fonctions non-convexes comme celles rencontrées dans les [réseaux neuronaux profonds](https://fr.wikipedia.org/wiki/Apprentissage_profond)
- Le risque de rester piégé dans des minima locaux, un problème particulièrement important en haute dimension (millions de paramètres) [Source: Wikipedia "Gradient descent#Limitations"]