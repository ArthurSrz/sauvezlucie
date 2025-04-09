---
title: 'Malédiction de la dimensionnalité '
type: concept
tags:
- machine learning
- dimensionnalité
- statistiques
- algorithmes
- données haute dimension
- performance
- complexité
- analyse de données
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Réduction de dimensionnalité en machine learning]]'
causedBy: '[[Surapprentissage (Overfitting) ]]'
---
## Généralité

La [malédiction de la dimensionnalité](https://fr.wikipedia.org/wiki/Mal%C3%A9diction_de_la_dimensionnalit%C3%A9) désigne les problèmes et défis qui surviennent lorsque l'on travaille avec des données en haute dimension (nombre élevé de variables ou caractéristiques). Ce terme a été introduit par [Richard E. Bellman](https://fr.wikipedia.org/wiki/Richard_Bellman) en 1961 dans le contexte des problèmes d'optimisation. Ce phénomène affecte particulièrement les algorithmes d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) et les méthodes statistiques, entraînant une dégradation des performances et une complexité accrue.

## Points clés

- **Rareté des données** : Dans les espaces de grande dimension, les points de données deviennent exponentiellement plus éloignés les uns des autres
- **Complexité computationnelle** : Le temps de calcul et les besoins en mémoire augmentent rapidement avec la dimension
- **Surapprentissage (overfitting)** : Les modèles tendent à s'adapter trop précisément aux données d'entraînement
- **Distance entre points moins significative** : En haute dimension, les distances entre points tendent à devenir similaires
- **Augmentation exponentielle de l'espace requis** : Le volume de l'espace croît rapidement avec le nombre de dimensions

## Détails

### Effets principaux

Le volume de l'espace croît rapidement avec le nombre de dimensions, rendant les données rares et dispersées. Ce phénomène est quantifié par la "[loi des cubes](https://fr.wikipedia.org/wiki/Fl%C3%A9au_de_la_dimension)" qui montre que pour couvrir 1% d'un espace à N dimensions, il faut environ 0.01^(1/N) de l'intervalle dans chaque dimension.

Les modèles deviennent trop complexes et s'adaptent mal aux nouvelles données en raison du bruit ou des corrélations fortuites. Le [théorème de Hughes](https://fr.wikipedia.org/wiki/Ph%C3%A9nom%C3%A8ne_de_Hughes) prédit que la performance d'un classifieur peut d'abord s'améliorer puis se dégrader lorsque le nombre de caractéristiques augmente.

En haute dimension, la plupart des paires de points ont une distance euclidienne relative qui converge vers une valeur constante ([concentration de la mesure](https://fr.wikipedia.org/wiki/Concentration_de_la_mesure)), réduisant l'efficacité des méthodes basées sur les voisinages.

### Domaines concernés

1. **Apprentissage automatique** :
   - Algorithmes comme les [forêts aléatoires](https://fr.wikipedia.org/wiki/For%C3%AAt_d%27arbres_d%C3%A9cisionnels) ou les [SVM](https://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support) peuvent souffrir de performances dégradées
   - La réduction de dimension ([PCA](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales), t-SNE) ou la sélection de caractéristiques deviennent essentielles

2. **Visualisation des données** :
   - Représenter des données en plus de 3 dimensions nécessite des techniques comme [t-SNE](https://fr.wikipedia.org/wiki/T-SNE) ou UMAP

3. **Calcul des distances** :
   - Méthodes comme [k-plus proches voisins](https://fr.wikipedia.org/wiki/K-plus_proches_voisins) deviennent moins discriminantes

### Solutions

- **Réduction de dimension** :  
  Techniques comme l'[Analyse en Composantes Principales](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales) (PCA) ou les autoencodeurs pour compresser l'information

- **Sélection de caractéristiques** :  
  Méthodes comme [Lasso](https://fr.wikipedia.org/wiki/R%C3%A9gression_Lasso) (régression L1) pour ne conserver que les variables pertinentes

- **Régularisation** :  
  Appliquer des pénalités (L1, L2) pour éviter la complexité excessive des modèles

- **Méthodes spécifiques** :  
  Techniques comme les Random Projections basées sur le lemme de Johnson-Lindenstrauss

- **Augmentation des données** :  
  Particulièrement utile pour compenser la rareté des données en haute dimension