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
date_creation: '2025-04-04'
date_modification: '2025-04-04'
isPartOf: '[[Apprentissage automatique (Machine Learning)]]'
relatedTo: '[[Arbre de décision]]'
sameAs: '[[Ensemble learning]]'
seeAlso: '[[Algorithmes de boosting spécifiques]]'
---
## Généralité

Les méthodes d'ensemble en [machine learning](https://fr.wikipedia.org/wiki/Apprentissage_automatique) sont des techniques qui combinent plusieurs modèles d'apprentissage individuels (appelés "apprenants faibles") pour produire un modèle prédictif plus performant que chacun des modèles pris séparément. Selon Wikipédia [source: "Ensemble learning"], cette approche s'inspire effectivement du principe de [sagesse des foules](https://fr.wikipedia.org/wiki/Sagesse_des_foules) (wisdom of the crowd), où l'agrégation d'opinions multiples donne souvent de meilleurs résultats qu'une opinion individuelle, bien que ce principe ne s'applique pas systématiquement dans tous les contextes.

## Points clés

- **Diversité des modèles** : Obtenue par différentes méthodes d'entraînement ou jeux de données, elle permet de réduire les erreurs individuelles
- **Aggrégation judicieuse** : L'agrégation des prédictions améliore la robustesse globale du système prédictif
- **Trois principales méthodes** : 
  - [Bagging](https://fr.wikipedia.org/wiki/Bagging) (comme les forêts aléatoires)
  - [Boosting](https://fr.wikipedia.org/wiki/Boosting) (comme AdaBoost ou XGBoost)
  - Stacking (combinaison hiérarchique de modèles)
- **Large utilisation** : Employées dans les compétitions de science des données (comme [Kaggle](https://fr.wikipedia.org/wiki/Kaggle)) et applications industrielles
- **Avantages clés** : Réduction du biais (avec boosting) et de la variance (avec bagging) des prédictions

## Détails

### Principes fondamentaux

Ces approches reposent sur deux principes fondamentaux validés par la littérature scientifique :  
1. La diversité des modèles (obtenue par différentes méthodes d'entraînement ou jeux de données) permet effectivement de réduire les erreurs individuelles  
2. L'agrégation judicieuse des prédictions améliore la robustesse globale du système prédictif  

### Principales méthodes d'ensemble

1. **Bagging (Bootstrap Aggregating)**
   - Crée plusieurs modèles en utilisant différents sous-ensembles aléatoires des données d'entraînement (échantillonnage avec remplacement), une technique inspirée du [bootstrap](https://fr.wikipedia.org/wiki/Bootstrap_(statistiques)) statistique
   - Les prédictions finales sont obtenues par vote majoritaire (classification) ou moyenne (régression)
   - Réduit principalement la variance et aide à éviter le surapprentissage
   - Exemple populaire : [Random Forest](https://fr.wikipedia.org/wiki/For%C3%AAt_d%27arbres_d%C3%A9cisionnels) (introduit par Leo Breiman en 2001)

2. **Boosting**
   - Construit des modèles séquentiellement, chaque nouveau modèle se concentrant sur les erreurs des modèles précédents
   - Réduit principalement le biais et peut améliorer la précision des modèles faibles
   - Exemples : 
     - [AdaBoost](https://fr.wikipedia.org/wiki/AdaBoost) (Adaptive Boosting)
     - Gradient Boosting
     - Variantes modernes : XGBoost, LightGBM, CatBoost

3. **Stacking (Stacked Generalization)**
   - Combine les prédictions de plusieurs modèles hétérogènes à l'aide d'un méta-modèle
   - Permet d'exploiter les forces de différents types d'algorithmes
   - Souvent utilisé dans les solutions gagnantes des compétitions de machine learning

### Avantages et inconvénients

**Avantages**:
- Amélioration significative des performances par rapport aux modèles individuels
- Réduction du risque de surapprentissage grâce à l'agrégation de prédictions diversifiées
- Plus grande robustesse face aux données bruitées ou aberrantes
- Meilleure généralisation sur des données inconnues

**Inconvénients**:
- Complexité computationnelle accrue
- Interprétabilité réduite par rapport aux modèles simples
- Nécessité de plus de ressources mémoire
- Risque de surapprentissage si les hyperparamètres ne sont pas correctement ajustés

### Applications

Les méthodes d'ensemble sont particulièrement efficaces dans des domaines comme :
- Détection de fraude
- Prédiction de risques financiers
- Diagnostic médical
- Reconnaissance d'images ([ImageNet](https://fr.wikipedia.org/wiki/ImageNet))
- Systèmes de recommandation
- Traitement du langage naturel

Elles sont largement utilisées dans les applications industrielles où la précision est critique (mention générale confirmée par plusieurs articles Wikipédia sur les méthodes d'ensemble).