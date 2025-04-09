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
date_creation: '2025-04-08'
date_modification: '2025-04-08'
differentFrom: '[[Métriques robustes aux valeurs aberrantes]]'
subClassOf: '[[La régression linéaire]]'
---
## Généralité

La méthode des [moindres carrés ordinaires](https://fr.wikipedia.org/wiki/Moindres_carr%C3%A9s_ordinaires) (MCO) est une technique statistique fondamentale utilisée en [régression linéaire](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire) pour estimer les paramètres d'un modèle en minimisant la somme des carrés des écarts entre les valeurs observées et les valeurs prédites par le modèle. Développée indépendamment par [Carl Friedrich Gauss](https://fr.wikipedia.org/wiki/Carl_Friedrich_Gauss) (1809) et [Adrien-Marie Legendre](https://fr.wikipedia.org/wiki/Adrien-Marie_Legendre) (1805), elle constitue la pierre angulaire de nombreuses analyses statistiques et économétriques modernes.

## Points clés

- La méthode MCO minimise la somme des carrés des résidus (différences entre valeurs observées et prédites), une approche initialement développée pour l'ajustement de trajectoires astronomiques
- Sous les hypothèses de Gauss-Markov, les estimateurs MCO sont BLUE (Best Linear Unbiased Estimators) - cette propriété est bien documentée dans les [théorèmes de Gauss-Markov](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_de_Gauss-Markov)
- L'estimateur des MCO est défini par la formule β̂ = (XᵀX)⁻¹Xᵀy, où X est la matrice des variables explicatives et y le vecteur des observations
- La méthode s'étend à de nombreux domaines comme l'économie, la biostatistique, l'ingénierie et les sciences sociales
- Elle présente certaines limites importantes comme la sensibilité aux valeurs aberrantes et la dépendance aux hypothèses de Gauss-Markov

## Détails

Pour un modèle de [régression linéaire](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire) simple de la forme $y = \beta_0 + \beta_1 x + \varepsilon$, la méthode MCO cherche à minimiser:

$$S = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2$$

Les estimateurs MCO des paramètres sont donnés par:

$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

Dans le cas multivarié, la solution s'exprime sous forme matricielle compacte: $\hat{\beta} = (X^\top X)^{-1} X^\top y$, où $X$ est la matrice des variables explicatives.

Pour que les estimateurs MCO soient BLUE, plusieurs hypothèses doivent être satisfaites, comme énoncé par le [théorème de Gauss-Markov](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Gauss-Markov):

1. **Linéarité**: La relation entre variables est linéaire dans les paramètres ($y = X\beta + \varepsilon$)
2. **Exogénéité stricte**: $E[\varepsilon|X] = 0$, l'espérance conditionnelle des erreurs est nulle
3. **Homoscédasticité**: $Var(\varepsilon|X) = \sigma^2 I_n$, la variance des erreurs est constante
4. **Non-autocorrélation**: $Cov(\varepsilon_i, \varepsilon_j|X) = 0$ pour $i \neq j$, les erreurs sont non corrélées
5. **Absence de multicolinéarité parfaite**: $rang(X) = k$ (nombre de variables explicatives), garantissant l'inversibilité de $X^\top X$

La méthode MCO peut être étendue à divers contextes:
- **Régression multiple**: $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_k x_k + \varepsilon$
- **Modèles linéaires généralisés** pour des distributions non normales
- **Moindres carrés non linéaires** pour des relations paramétriques non linéaires

Cependant, la méthode présente certaines limites importantes:
- **Sensibilité aux valeurs aberrantes**: Une seule observation extrême peut considérablement influencer les estimations
- **Problèmes de spécification**: Les biais d'omission ou d'inclusion de variables non pertinentes
- **Problèmes numériques**: L'inversion de $X^\top X$ peut devenir instable avec de nombreuses variables corrélées
- **Hypothèse de Gauss-Markov**: En pratique, ces hypothèses sont souvent violées

Des alternatives robustes comme les moindres carrés reweightés ou la [régression robuste](https://fr.wikipedia.org/wiki/R%C3%A9gression_robuste) peuvent atténuer certains de ces problèmes.

La méthode MCO est un outil fondamental dans de nombreux domaines:
1. **Économétrie**: Estimation de fonctions de production, de courbes de revenu-dépense
2. **Finance**: Modélisation CAPM, prévision des rendements boursiers
3. **Sciences sociales**: Analyse d'impact de la scolarité sur les revenus ([équation de Mincer](https://fr.wikipedia.org/wiki/%C3%89quation_de_Mincer))
4. **Épidémiologie**: Étude des facteurs de risque pour les maladies
5. **Ingénierie**: Modélisation des relations entrées-sorties dans les processus industriels