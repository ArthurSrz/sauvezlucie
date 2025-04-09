---
title: Ensemble learning
type: concept
tags:
- ensemble learning
- apprentissage automatique
- modèles de machine learning
- base learners
- robustesse des modèles
date_creation: '2025-03-30'
date_modification: '2025-04-04'
sameAs: '[[Méthodes d''ensemble en machine learning]]'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
seeAlso: '[[Fusion contextuelle de modèles LLM hétérogènes]]'
---
## Généralité

L'[ensemble learning](https://fr.wikipedia.org/wiki/M%C3%A9thode_ensemble), ou apprentissage par ensemble, est une technique en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui consiste à combiner plusieurs modèles (appelés "base learners" ou "weak learners") pour améliorer les performances prédictives et la robustesse du modèle final. Cette approche repose sur le principe que la combinaison de plusieurs modèles peut produire des prédictions plus précises et plus robustes que n'importe quel modèle individuel, particulièrement pour des problèmes complexes.

## Points clés

- **Diversité des modèles** : L'efficacité dépend de la diversité des modèles de base ([source](https://fr.wikipedia.org/wiki/Apprentissage_ensemble))
- **Trois techniques principales** : 
  - [Bagging](https://fr.wikipedia.org/wiki/Bootstrap_aggregating) (ex: Random Forests)
  - [Boosting](https://fr.wikipedia.org/wiki/Boosting_(machine_learning)) (ex: AdaBoost, XGBoost)
  - [Stacking](https://fr.wikipedia.org/wiki/Stacking_(machine_learning))
- **Amélioration des performances** : Réduction du biais (boosting) et de la variance (bagging)
- **Applications étendues** : Vision par ordinateur, traitement du langage naturel, détection de fraudes

## Détails

Les techniques principales d'ensemble learning incluent le Bagging (Bootstrap Aggregating), le Boosting et le Stacking. 

Le **Bagging** crée plusieurs sous-ensembles de données par échantillonnage avec remise et combine les prédictions par moyenne (régression) ou vote majoritaire (classification), réduisant ainsi la variance et l'overfitting ([source](https://fr.wikipedia.org/wiki/Bootstrap_aggregating)). 

Le **Boosting** entraîne les modèles séquentiellement en corrigeant les erreurs précédentes, utilisant une combinaison pondérée des prédictions pour réduire le biais ([source](https://fr.wikipedia.org/wiki/Boosting_(machine_learning))). 

Le **Stacking** utilise un méta-modèle (souvent une régression linéaire) pour combiner les prédictions des modèles de base ([source](https://fr.wikipedia.org/wiki/Stacked_generalization)).

Ces méthodes offrent plusieurs avantages :
- Amélioration significative des performances (10-25% sur les benchmarks UCI)
- Robustesse accrue aux variations des données
- Applicabilité à divers types de problèmes
- Limitation de l'[overfitting](https://fr.wikipedia.org/wiki/Surapprentissage)

Les performances varient selon la technique :
- Boosting réduit le biais (jusqu'à 40% dans certains cas)
- Bagging réduit la variance (30-50% en conditions optimales)
- Records sur ImageNet (vision) et GLUE (NLP) avec méthodes d'ensemble

Les applications concrètes sont nombreuses :
- **Finance** : Prédiction des marchés et gestion des risques
- **Recommandation** : Amélioration de la précision
- **NLP** : Traduction automatique, analyse de sentiments
- **Vision** : Classification d'images, détection d'objets ([source](https://fr.wikipedia.org/wiki/Applications_of_ensemble_learning))

Plusieurs études confirment l'efficacité des méthodes d'ensemble :
- Efficacité maximale obtenue avec des modèles diversifiés (Wikipédia)
- Étude Dietterich (2002) sur la corrélation optimale entre modèles
- Benchmarks montrant des gains de 10-25% sur UCI datasets
- Performances exceptionnelles en vision (ImageNet) et NLP (GLUE)