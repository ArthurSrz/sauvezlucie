---
title: Méthodes d'ensemble en machine learning
type: concept
tags:
- machine learning
- méthodes d'ensemble
- modèles prédictifs
- apprentissage automatique
- combinaison de modèles
- data science
- algorithmes
- intelligence artificielle
- modélisation
- performance prédictive
date_creation: '2025-03-20'
date_modification: '2025-03-20'
isPartOf: '[[Apprentissage automatique (Machine Learning)]]'
relatedTo: '[[Arbre de décision]]'
---
## Généralité

Les méthodes d'ensemble en machine learning sont des techniques qui combinent plusieurs modèles d'apprentissage individuels pour produire un modèle prédictif plus performant que chacun des modèles pris séparément. Ces approches reposent sur le principe que la diversité des modèles permet de réduire les erreurs individuelles et d'améliorer la robustesse globale du système prédictif. Les méthodes d'ensemble sont largement utilisées dans les compétitions de science des données et les applications industrielles en raison de leur capacité à améliorer significativement les performances prédictives.

## Points clés

- Les méthodes d'ensemble combinent plusieurs modèles pour réduire la variance (bagging), le biais (boosting) ou améliorer la précision globale (stacking)
- Les trois principales approches d'ensemble sont le bagging, le boosting et le stacking
- Ces méthodes permettent généralement d'obtenir de meilleures performances que les modèles individuels, au prix d'une complexité accrue
- La diversité entre les modèles de base est essentielle pour l'efficacité des méthodes d'ensemble

## Détails

### Principales méthodes d'ensemble

1. **Bagging (Bootstrap Aggregating)**
   - Crée plusieurs modèles en utilisant différents sous-ensembles aléatoires des données d'entraînement (échantillonnage avec remplacement)
   - Les prédictions finales sont obtenues par vote majoritaire (classification) ou moyenne (régression)
   - Réduit principalement la variance et aide à éviter le surapprentissage
   - Exemple populaire : Random Forest, qui combine plusieurs arbres de décision entraînés sur différents sous-ensembles de données et de caractéristiques

2. **Boosting**
   - Construit des modèles séquentiellement, chaque nouveau modèle se concentrant sur les erreurs des modèles précédents
   - Attribue des poids plus élevés aux exemples mal classifiés pour les modèles suivants
   - Réduit principalement le biais et peut améliorer la précision des modèles faibles
   - Exemples : AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost

3. **Stacking (Stacked Generalization)**
   - [Combine](https://fr.wikipedia.org/wiki/Combine) les prédictions de plusieurs modèles hétérogènes à l'aide d'un méta-modèle
   - Utilise les prédictions des modèles de base comme entrées pour le méta-modèle
   - Permet d'exploiter les forces de différents types d'algorithmes
   - Souvent utilisé dans les solutions gagnantes des compétitions de machine learning

### Avantages des méthodes d'ensemble

- Amélioration significative des performances par rapport aux modèles individuels
- Réduction du risque de surapprentissage
- Plus grande robustesse face aux données bruitées ou aberrantes
- Meilleure généralisation sur des données inconnues

### Inconvénients

- Complexité computationnelle accrue (temps d'entraînement et de prédiction plus longs)
- Interprétabilité réduite par rapport aux modèles simples
- [Nécessité](https://fr.wikipedia.org/wiki/Nécessité) de plus de ressources mémoire
- Risque de surapprentissage si les hyperparamètres ne sont pas correctement ajustés

### Applications

Les méthodes d'ensemble sont particulièrement efficaces dans des domaines comme la détection de fraude, la prédiction de risques financiers, le diagnostic médical, la reconnaissance d'images et les systèmes de recommandation, où la précision des prédictions est cruciale et où les données peuvent être complexes et bruitées.