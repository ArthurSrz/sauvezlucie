---
title: Réseaux bayésiens
type: concept
tags:
- probabilités
- graphes
- modèles graphiques
- statistiques
- intelligence artificielle
- Thomas Bayes
- DAG
- incertitude
- modélisation
date_creation: '2025-03-18'
date_modification: '2025-03-18'
isPartOf: '[[Apprentissage automatique (Machine Learning)]]'
relatedTo: '[[Apprentissage supervisé]]'
---
## Généralité

Les réseaux bayésiens sont des modèles graphiques probabilistes qui représentent des variables aléatoires et leurs dépendances conditionnelles via un graphe orienté acyclique (DAG). Nommés d'après [Thomas Bayes](https://fr.wikipedia.org/wiki/Thomas_Bayes), ces réseaux combinent la théorie des graphes et la théorie des probabilités pour modéliser l'incertitude dans des systèmes complexes. Ils permettent de calculer la probabilité d'événements en fonction d'observations partielles et de connaissances préalables, ce qui en fait des outils puissants pour le raisonnement sous incertitude.

## Points clés

- Un réseau bayésien est composé de nœuds (représentant des variables aléatoires) et d'arcs dirigés (indiquant les relations de dépendance causale)
- Chaque nœud est associé à une table de probabilités conditionnelles (TPC) qui quantifie l'effet des parents sur le nœud
- Les réseaux bayésiens permettent deux types d'inférence principaux : prédictive (des causes vers les effets) et diagnostique (des effets vers les causes)
- Ils peuvent être construits à partir de données (apprentissage automatique) ou à partir de connaissances d'experts (modélisation manuelle)
- Le théorème de Bayes est au cœur du fonctionnement de ces réseaux : P(A|B) = P(B|A)×P(A)/P(B)

## Détails

Les réseaux bayésiens représentent la structure causale d'un domaine par un graphe orienté acyclique où chaque nœud correspond à une variable aléatoire et chaque arc représente une relation de dépendance directe. L'absence d'arc entre deux variables indique leur indépendance conditionnelle étant donné certaines autres variables.

La force de ces modèles réside dans leur capacité à combiner des connaissances a priori avec des observations pour mettre à jour les croyances sur l'état du système. Cette mise à jour, appelée inférence bayésienne, utilise le théorème de Bayes pour calculer les probabilités a posteriori.

Pour construire un réseau bayésien, deux éléments sont nécessaires :
1. La structure du graphe (quelles variables influencent directement quelles autres)
2. Les paramètres numériques (tables de probabilités conditionnelles pour chaque nœud)

L'apprentissage de ces réseaux peut se faire de plusieurs façons :
- [Apprentissage](https://fr.wikipedia.org/wiki/Apprentissage) des paramètres : estimation des probabilités conditionnelles à partir de données
- [Apprentissage](https://fr.wikipedia.org/wiki/Apprentissage) de structure : détermination des relations de dépendance entre variables
- Approche hybride : combinaison de connaissances d'experts et d'apprentissage automatique

Les réseaux bayésiens sont utilisés dans de nombreux domaines :
- Diagnostic médical (prédiction de maladies à partir de symptômes)
- Systèmes d'aide à la décision (évaluation des risques)
- Bioinformatique (analyse de réseaux génétiques)
- Vision par ordinateur et reconnaissance de formes
- Systèmes experts et intelligence artificielle

Leur principal avantage est la capacité à modéliser explicitement l'incertitude et à intégrer facilement de nouvelles informations pour mettre à jour les prédictions. Cependant, ils présentent aussi des limitations, notamment la complexité computationnelle de l'inférence exacte dans les grands réseaux et la difficulté à modéliser certaines relations temporelles (pour lesquelles les réseaux bayésiens dynamiques ont été développés).