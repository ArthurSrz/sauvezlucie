---
title: Dilemme biais-variance
type: concept
tags:
- machine learning
- biais-variance
- apprentissage automatique
- modélisation prédictive
- sous-ajustement
- sur-ajustement
- généralisation
date_creation: '2025-04-04'
date_modification: '2025-04-04'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
relatedTo:
- '[[Apprentissage supervisé]]'
- '[[Méthodes de régularisation en machine learning]]'
---
## Généralité

Le [dilemme biais-variance](https://fr.wikipedia.org/wiki/Biais-variance) est un concept fondamental en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui décrit le compromis entre la capacité d'un modèle à s'adapter aux données d'entraînement (faible biais) et sa capacité à généraliser à de nouvelles données (faible variance). Ce dilemme est au cœur de la performance des modèles prédictifs.

## Points clés

- **Biais élevé** : [Sous-ajustement](https://fr.wikipedia.org/wiki/Sous-ajustement) - Le modèle est trop simple et ne capture pas les tendances des données, avec une erreur systématiquement élevée dans les données d'entraînement et de test.
- **Variance élevée** : [Surajustement](https://fr.wikipedia.org/wiki/Surajustement) - Le modèle est trop complexe et mémorise le bruit des données d'entraînement, performant bien sur l'entraînement mais mal sur les nouvelles données.
- **Compromis optimal** : Trouver un équilibre entre biais et variance pour minimiser l'erreur de généralisation, comme établi par le [théorème de Gauss-Markov](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Gauss-Markov).
- **Méthodes de régulation** : Techniques comme la régularisation, le dropout et l'élagage pour contrôler le compromis biais-variance.
- **Décomposition de l'erreur** : La formule E[(y-ŷ)²] = Biais(ŷ)² + Variance(ŷ) + Irréductible, applicable à l'erreur quadratique moyenne.

## Détails

### Origine et définition

Selon Wikipédia, ce compromis trouve son origine dans la théorie de l'estimation statistique et a été initialement exploré par plusieurs statisticiens, notamment dans le contexte de la théorie de la décision, avant d'être formalisé plus récemment en apprentissage automatique. Le biais correspond à l'erreur due à des hypothèses simplificatrices dans le modèle, tandis que la variance reflète la sensibilité du modèle aux fluctuations des données d'entraînement.

### Impact sur les performances

- Un modèle avec un **biais élevé** aura des performances médiocres sur les données d'entraînement et de test (sous-apprentissage).
- Un modèle avec une **variance élevée** performera bien sur les données d'entraînement mais mal sur les données de test (surapprentissage).

### Stratégies pour équilibrer le dilemme

1. **[Régularisation](https://fr.wikipedia.org/wiki/R%C3%A9gularisation_(math%C3%A9matiques))** :
   - Techniques comme L1/L2 pour pénaliser la complexité du modèle
   - Méthodes avancées : early stopping, dropout (réseaux neuronaux), élagage (arbres)
2. **[Validation croisée](https://fr.wikipedia.org/wiki/Validation_crois%C3%A9e)** :
   - K-fold pour évaluer la capacité de généralisation
   - Détection robuste du surajustement
3. **Sélection de modèle** :
   - Choix d'algorithmes adaptés à la complexité des données
   - Compromis selon le théorème biais-variance
4. **[Ensemble Learning](https://fr.wikipedia.org/wiki/Apprentissage_ensembliste)** :
   - Bagging (ex: Random Forest) réduit la variance
   - Boosting (ex: XGBoost) réduit le biais

### Exemples pratiques

- **[Régression linéaire](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire)** : Souffre d'un biais élevé pour des données non linéaires, mais bénéficie d'une faible variance.
- **[Arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision) profonds** : Ont généralement une variance élevée car sensibles aux petites variations des données.

### Formulation mathématique

L'erreur totale d'un modèle peut être décomposée en :
\[ \text{Erreur} = \mathbb{E}[(y-\hat{y})^2] = \text{Biais}(\hat{y})^2 + \text{Variance}(\hat{y}) + \text{Erreur irréductible} \]
Où :
- Biais² : Erreur systématique des prédictions
- Variance : Variabilité des prédictions sur différents jeux d'entraînement
- Erreur irréductible : Bruit intrinsèque des données (ne peut être réduit)