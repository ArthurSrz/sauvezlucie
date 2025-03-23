---
title: La méthode des moindres carrés ordinaires
type: concept
tags:
- statistiques
- régression
- analyse de données
- moindres carrés
- modélisation
- mathématiques
- estimation
date_creation: '2025-03-20'
date_modification: '2025-03-20'

- type: owl:differentFrom
  target: '[[Métriques robustes aux valeurs aberrantes]]'
---

##Généralité

La méthode des moindres carrés ordinaires (MCO) est une technique statistique fondamentale utilisée en régression linéaire pour estimer les paramètres d'un modèle en minimisant la somme des carrés des écarts entre les valeurs observées et les valeurs prédites par le modèle. Cette approche, développée indépendamment par Carl Friedrich Gauss et Adrien-Marie Legendre au début du 19ème siècle, constitue la pierre angulaire de nombreuses analyses statistiques et économétriques modernes.

## Points clés

- La méthode MCO minimise la somme des carrés des résidus (différences entre valeurs observées et prédites)
- Sous certaines hypothèses (Gauss-Markov), les estimateurs MCO sont BLUE (Best Linear Unbiased Estimators)
- La méthode fournit des estimations des coefficients de régression ainsi que leurs erreurs standards
- L'approche est particulièrement adaptée aux relations linéaires entre variables explicatives et variable dépendante

## Détails

### Principe mathématique

Pour un modèle de régression linéaire simple de la forme $y = \beta_0 + \beta_1 x + \varepsilon$, où $y$ est la variable dépendante, $x$ la variable explicative, $\beta_0$ et $\beta_1$ les paramètres à estimer, et $\varepsilon$ le terme d'erreur, la méthode MCO cherche à minimiser:

$$S = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2$$

Les estimateurs MCO des paramètres sont donnés par:

$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

### Hypothèses de Gauss-Markov

Pour que les estimateurs MCO soient BLUE (meilleurs estimateurs linéaires sans biais), plusieurs hypothèses doivent être satisfaites:

1. **Linéarité**: La relation entre variables est linéaire dans les paramètres
2. **Exogénéité**: L'espérance conditionnelle des erreurs est nulle
3. **Homoscédasticité**: La variance des erreurs est constante
4. **Non-autocorrélation**: Les erreurs sont indépendantes entre observations
5. **Absence de multicolinéarité parfaite**: Les variables explicatives ne sont pas parfaitement corrélées

### Extensions et limites

La méthode MCO peut être étendue à la régression multiple avec plusieurs variables explicatives:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_k x_k + \varepsilon$$

Cependant, la méthode présente certaines limites:
- Sensibilité aux valeurs aberrantes (outliers)
- Inefficacité en présence d'hétéroscédasticité ou d'autocorrélation
- Inadaptation aux relations non linéaires sans transformation préalable

### Applications pratiques

La méthode MCO est largement utilisée dans divers domaines:
- Économétrie pour l'estimation de modèles économiques
- Sciences sociales pour l'analyse de données d'enquêtes
- Sciences naturelles pour modéliser des relations entre variables
- Finance pour l'analyse de séries temporelles et la prévision

Des logiciels comme R, Python (avec statsmodels ou scikit-learn), STATA ou SAS offrent des implémentations robustes de cette méthode, facilitant son application à des ensembles de données complexes.