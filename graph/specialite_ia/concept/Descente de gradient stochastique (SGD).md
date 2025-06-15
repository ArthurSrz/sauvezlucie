---
title: Descente de gradient stochastique (SGD)
type: concept
tags:
- machine learning
- optimisation
- descente de gradient
- SGD
- algorithmes
- apprentissage automatique
- fonction de coût
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[L''algorithme du gradient]]'
depends: '[[Choix de la fonction de minimisation]]'
---
## Généralité

La [descente de gradient stochastique](https://fr.wikipedia.org/wiki/Descente_de_gradient_stochastique) (SGD) est une méthode d'optimisation itérative utilisée pour minimiser une fonction de coût en ajustant progressivement les paramètres d'un modèle. Contrairement à la descente de gradient classique, qui utilise l'ensemble du jeu de données à chaque itération, la SGD met à jour les paramètres en se basant sur un seul échantillon ou un petit lot (mini-batch) à la fois, ce qui la rend plus efficace pour les grands ensembles de données.

## Points clés

- **Efficacité sur les grands jeux de données** : Particulièrement adaptée aux problèmes où le volume de données est trop important pour être traité en une seule passe. Couramment utilisée dans l'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) à grande échelle.
- **Convergence plus rapide mais plus bruyante** : Les mises à jour basées sur des échantillons individuels introduisent du bruit, mais permettent souvent une convergence plus rapide vers un minimum local.
- **Flexibilité** : Peut être utilisée avec diverses fonctions de coût et est compatible avec des techniques comme la régularisation ou le momentum pour améliorer les performances.
- **Économie de mémoire** : Ne nécessite pas de charger l'ensemble des données en mémoire.
- **Capacité à échapper aux minima locaux** : Le bruit introduit par les mises à jour stochastiques peut aider à éviter de rester bloqué dans des minima locaux non optimaux.

## Détails

### Fonctionnement

La descente de gradient stochastique fonctionne en suivant ces étapes principales :

1. **Initialisation** : Les paramètres du modèle (par exemple, les poids dans un [réseau de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels)) sont initialisés aléatoirement ou selon une heuristique.
2. **Sélection d'un échantillon** : À chaque itération, un échantillon (ou un mini-batch) est sélectionné aléatoirement dans le jeu de données.
3. **Calcul du gradient** : Le gradient de la [fonction de coût](https://fr.wikipedia.org/wiki/Fonction_de_co%C3%BBt) est calculé uniquement pour cet échantillon.
4. **Mise à jour des paramètres** : Les paramètres sont ajustés dans la direction opposée au gradient, proportionnellement à un [taux d'apprentissage](https://fr.wikipedia.org/wiki/Taux_d%27apprentissage).
5. **Répétition** : Les étapes 2 à 4 sont répétées jusqu'à ce qu'un critère de convergence soit atteint.

### Avantages et inconvénients

**Avantages** :
- **Efficacité en pratique** : Bien que théoriquement plus lente, la SGD converge souvent plus rapidement en pratique que le gradient batch pour les grands datasets.
- **Économie de mémoire** : Permet d'entraîner des modèles sur des datasets massifs (comme [ImageNet](https://fr.wikipedia.org/wiki/ImageNet) avec 14 millions d'images) avec des ressources limitées.
- **Capacité à échapper aux minima locaux** : Le bruit introduit par les mises à jour stochastiques peut aider à éviter de rester bloqué dans des minima locaux non optimaux.

**Inconvénients** :
- **Sensibilité au taux d'apprentissage** : Un mauvais choix de taux d'apprentissage peut entraîner une divergence ou une convergence trop lente.
- **Variabilité des résultats** : En raison de la nature aléatoire des échantillons, les performances peuvent varier d'une exécution à l'autre.
- **Difficulté de parallélisation** : La nature séquentielle de la SGD rend sa parallélisation plus complexe.

### Variantes

Plusieurs variantes de la SGD ont été développées pour améliorer ses performances :

- **SGD avec momentum** : Ajoute une composante de "vitesse" pour accélérer la convergence dans les directions pertinentes.
- **AdaGrad, RMSprop, Adam** : Des méthodes adaptatives qui ajustent automatiquement le taux d'apprentissage pour chaque paramètre.
- **SGD asynchrone** : Permet une certaine forme de parallélisation malgré la nature séquentielle de l'algorithme de base.

### Historique

La méthode a été initialement proposée par [Herbert Robbins](https://fr.wikipedia.org/wiki/Herbert_Robbins) et Sutton Monro en 1951 dans le contexte des méthodes de [stochastic approximation](https://fr.wikipedia.org/wiki/Stochastic_approximation). Elle est particulièrement adaptée aux problèmes d'apprentissage automatique où les données sont nombreuses.