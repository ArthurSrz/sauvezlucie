---
title: Méthodes de réduction de variance
type: concept
tags:
- réduction de variance
- statistique
- simulation
- estimateurs
- finance
- ingénierie
- recherche opérationnelle
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo: '[[Algorithmes d''optimisation bayésienne]]'
subClassOf: '[[Techniques de l''intelligence artificielle]]'
---
## Généralité

Les méthodes de [réduction de variance](https://fr.wikipedia.org/wiki/Méthode_de_réduction_de_la_variance) sont des techniques utilisées en [statistique](https://fr.wikipedia.org/wiki/Statistique) et en simulation pour diminuer la variance des estimateurs, ce qui améliore la précision des résultats obtenus à partir de simulations stochastiques. Ces techniques, développées initialement dans le cadre de la [méthode de Monte-Carlo](https://fr.wikipedia.org/wiki/Méthode_de_Monte-Carlo), trouvent des applications dans divers domaines scientifiques et industriels.

## Points clés

- **Amélioration de la précision** : Réduction significative du nombre de simulations nécessaires pour atteindre une précision donnée
- **Diversité des techniques** : Inclut l'échantillonnage préférentiel, les variables de contrôle, et la stratification
- **Applications variées** : Utilisées en finance, ingénierie, physique des particules et graphisme 3D
- **Origines historiques** : Développées par John von Neumann et Nicholas Metropolis dans les années 1940
- **Évolution moderne** : Adaptations pour les architectures de calcul parallèle contemporaines

## Détails

### Techniques principales

Les méthodes de réduction de variance reposent sur plusieurs principes mathématiques fondamentaux :

- **[Échantillonnage préférentiel](https://fr.wikipedia.org/wiki/Échantillonnage_préférentiel)** (importance sampling) : Technique qui consiste à échantillonnage à partir d'une distribution différente de celle de la variable aléatoire d'intérêt
- **Variables de contrôle** (control variates) : Utilisation de variables corrélées dont les propriétés sont connues
- **Stratification** (stratified sampling) : Division de la population en sous-groupes homogènes

### Applications pratiques

Ces méthodes sont particulièrement utiles dans :

1. **Finance** : Pour la valorisation d'options complexes
2. **Ingénierie** : Dans les études de fiabilité des systèmes
3. **Recherche opérationnelle** : Pour l'optimisation de processus stochastiques
4. **Physique des particules** : Simulation de phénomènes complexes
5. **Graphisme 3D** : Principalement pour le rendu par [lancer de rayons](https://fr.wikipedia.org/wiki/Lancer_de_rayons)

### Échantillonnage Importance

L'[échantillonnage importance](https://fr.wikipedia.org/wiki/Échantillonnage_importance) est particulièrement utile lorsque la distribution d'origine a une queue lourde ou des événements rares. Par exemple, dans l'évaluation d'[options financières](https://fr.wikipedia.org/wiki/Option_financière), cette méthode permet de concentrer les simulations sur les scénarios où l'option est la plus sensible.

### Références

[1] https://fr.wikipedia.org/wiki/Méthode_de_réduction_de_la_variance  
[2] https://fr.wikipedia.org/wiki/Simulation_en_physique_des_particules  
[3] https://fr.wikipedia.org/wiki/Lancer_de_rayons  
[4] https://fr.wikipedia.org/wiki/Méthode_de_Monte-Carlo