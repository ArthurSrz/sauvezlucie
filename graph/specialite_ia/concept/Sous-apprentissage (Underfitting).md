---
title: Sous-apprentissage (Underfitting)
type: concept
tags:
- Machine Learning
- Underfitting
- Apprentissage automatique
- Modélisation
- Performance des modèles
- Data Science
- Erreurs de prédiction
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo:
- '[[Dilemme biais-variance]]'
- '[[Surapprentissage (Overfitting) ]]'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
---
## Généralité

Le sous-apprentissage ([underfitting](https://fr.wikipedia.org/wiki/Surapprentissage_et_sous-apprentissage) en anglais) est un phénomène en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) où un modèle est trop simple pour capturer les relations complexes dans les données d'entraînement. Cela se traduit par de mauvaises performances à la fois sur les données d'entraînement et sur les données de test. Un exemple typique est un modèle linéaire essayant d'apprendre une relation non-linéaire complexe.

## Points clés

- Le modèle est incapable d'apprendre correctement les motifs sous-jacents des données, souvent dû à une capacité insuffisante ou des [features](https://fr.wikipedia.org/wiki/Feature_(apprentissage_automatique)) non informatives ([source](https://fr.wikipedia.org/wiki/Sous-apprentissage))
- Performances médiocres à la fois sur les données d'entraînement et de validation, contrairement au surapprentissage ([source](https://fr.wikipedia.org/wiki/Surapprentissage))
- Correspond à un biais élevé dans le [compromis biais-variance](https://fr.wikipedia.org/wiki/Biais_et_variance_d%27un_estimateur), avec des hypothèses trop simplistes
- Peut être causé par une [régularisation](https://fr.wikipedia.org/wiki/Régularisation_(machine_learning)) excessive ou un mauvais prétraitement des données
- Solutions incluent l'augmentation de la complexité du modèle ou l'amélioration des caractéristiques

## Détails

### Causes principales

1. **Modèle trop simple** : Lorsque le modèle manque de capacité (peu de paramètres ou fonction trop basique), il ne peut pas représenter la complexité des données. Par exemple, utiliser une [régression linéaire](https://fr.wikipedia.org/wiki/Régression_linéaire) pour modéliser des données non linéaires.

2. **Entraînement insuffisant** : Si le modèle n'est pas entraîné assez longtemps (en particulier pour les réseaux de neurones), il n'a pas le temps d'apprendre les motifs importants.

3. **Mauvais prétraitement des données** : Des caractéristiques mal choisies ou une normalisation inadéquate peuvent empêcher le modèle d'apprendre efficacement. L'[ingénierie des caractéristiques](https://fr.wikipedia.org/wiki/Feature_engineering) est cruciale.

### Détection

- **Performances médiocres** : Le modèle a une faible précision/métrique sur les données d'entraînement.
- **Courbes d'apprentissage** : Une courbe montrant à la fois une erreur d'entraînement et de validation élevée est typique.

### Solutions

- **Augmenter la complexité du modèle** : Passer à un modèle plus sophistiqué comme un [réseau de neurones](https://fr.wikipedia.org/wiki/Réseau_de_neurones_artificiels).
- **Ajouter des caractéristiques** : Intégrer plus de variables explicatives ou créer de nouvelles caractéristiques.
- **Réduire la régularisation** : La régularisation pénalise la complexité ; la diminuer peut aider.
- **Entraîner plus longtemps** : Pour les modèles itératifs comme les réseaux de neurones.
- **Améliorer le prétraitement** : Techniques comme la normalisation ou l'[analyse en composantes principales](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales).

### Exemple classique

Un modèle de [régression linéaire](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire) essayant de prédire des données [sinusoïdales](https://fr.wikipedia.org/wiki/Sinuso%C3%AFde) illustre parfaitement les limites des modèles linéaires face à des relations non-linéaires complexes. Pour résoudre ce type de sous-apprentissage, on pourrait :
1. Utiliser un modèle plus complexe comme un réseau de neurones
2. Ajouter des caractéristiques polynomiales
3. Réduire la régularisation

[Plus d'informations sur le compromis biais-variance](https://fr.wikipedia.org/wiki/Biais_(statistique)#Compromis_biais-variance)