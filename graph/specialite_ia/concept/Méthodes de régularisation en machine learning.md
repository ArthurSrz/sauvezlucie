---
title: Méthodes de régularisation en machine learning
type: concept
tags:
- régularisation
- machine learning
- overfitting
- fonction de coût
- modèles robustes
date_creation: '2025-03-30'
date_modification: '2025-04-04'
relatedTo:
- '[[Apprentissage supervisé]]'
- '[[Validation croisée en apprentissage automatique]]'
subClassOf: '[[Entraînement d''un modèle d''IA]]'
hasPart: '[[Normalisation par lots (Batch Normalization)]]'
---
## Généralité

La [régularisation](https://fr.wikipedia.org/wiki/Régularisation_(mathématiques)) est une technique fondamentale en [machine learning](https://fr.wikipedia.org/wiki/Apprentissage_automatique) utilisée pour prévenir le surapprentissage (overfitting) et améliorer la généralisation des modèles. Elle repose sur l'ajout d'une pénalité à la fonction de coût, inspirée des travaux de [Tikhonov](https://fr.wikipedia.org/wiki/Andreï_Tikhonov) sur les problèmes mal posés dans les années 1940.

## Points clés

- **Prévention du surapprentissage** : Réduit la complexité des modèles pour éviter l'adaptation excessive aux données d'entraînement
- **Amélioration de la généralisation** : Aide les modèles à mieux performer sur des données inconnues via le compromis biais-variance
- **Types principaux** :
  - L1 (Lasso) pour la sélection de caractéristiques
  - L2 (Ridge) contre la multicolinéarité
  - Elastic Net combinant L1 et L2
- **Applications étendues** : Essentielle des modèles linéaires aux [réseaux neuronaux](https://fr.wikipedia.org/wiki/Réseau_de_neurones_artificiels) profonds

## Détails

### Régularisation L1 (Lasso)

La [régularisation L1](https://fr.wikipedia.org/wiki/Régularisation_(mathématiques)) ou [Lasso](https://fr.wikipedia.org/wiki/Lasso_(statistiques)) ajoute une pénalité égale à la somme absolue des paramètres. Introduite par Tibshirani (1996), elle produit des modèles parcimonieux avec sélection automatique de caractéristiques.

**Formule** :
\[ \text{Fonction de coût régularisée} = \text{Fonction de coût} + \lambda \sum_{i=1}^{n} |w_i| \]

### Régularisation L2 (Ridge)

La [régularisation L2](https://fr.wikipedia.org/wiki/Régularisation_(mathématiques)) ou [Ridge](https://fr.wikipedia.org/wiki/Régression_ridge) pénalise la somme des carrés des paramètres. Développée par Hoerl et Kennard (1970), elle gère efficacement la multicolinéarité.

**Formule** :
\[ \text{Fonction de coût régularisée} = \text{Fonction de coût} + \lambda \sum_{i=1}^{n} w_i^2 \]

### Elastic Net

L'[Elastic Net](https://fr.wikipedia.org/wiki/Elastic_net) combine L1 et L2. Proposé par Zou et Hastie (2005), il est recommandé quand le nombre de caractéristiques excède les observations (p >> n).

**Formule** :
\[ \text{Fonction de coût régularisée} = \text{Fonction de coût} + \lambda \left( \alpha \sum |w_i| + (1-\alpha) \sum w_i^2 \right) \]

### Autres méthodes

- **Dropout** : Désactivation aléatoire de neurones (Hinton, 2012)
- **Arrêt précoce** : Interruption de l'entraînement avant surapprentissage

L'efficacité dépend du choix optimal du hyperparamètre λ, généralement déterminé par validation croisée. Ces techniques sont devenues incontournables dans l'apprentissage statistique moderne.