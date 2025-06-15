---
title: La régression linéaire
type: concept
tags:
- statistiques
- régression linéaire
- modélisation
- analyse de données
- mathématiques
- prédiction
- apprentissage automatique
date_creation: '2025-04-08'
date_modification: '2025-04-08'
seeAlso: '[[La méthode des moindres carrés ordinaires]]'
hasPart: '[[La régression linéaire multiple]]'
---
## Généralité

La [régression linéaire](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire) est un modèle statistique fondamental qui établit une relation linéaire entre une variable expliquée (dépendante) et une ou plusieurs variables explicatives (indépendantes). Développée initialement par [Francis Galton](https://fr.wikipedia.org/wiki/Francis_Galton) au 19ème siècle pour étudier l'hérédité, cette méthode a été formalisée mathématiquement par [Karl Pearson](https://fr.wikipedia.org/wiki/Karl_Pearson) et [Ronald Fisher](https://fr.wikipedia.org/wiki/Ronald_Fisher). Elle est largement utilisée pour la prédiction et l'explication de phénomènes dans divers domaines scientifiques.

## Points clés

- Deux formes principales : [régression linéaire simple](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire) (une variable explicative) et [multiple](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire_multiple) (plusieurs variables)
- Estimation par [méthode des moindres carrés ordinaires](https://fr.wikipedia.org/wiki/M%C3%A9thode_des_moindres_carr%C3%A9s) (MCO) qui minimise la somme des carrés des résidus
- Hypothèses fondamentales : linéarité, homoscédasticité, indépendance des observations, normalité des résidus
- Applications étendues : économie, médecine, sciences sociales, ingénierie et bien d'autres domaines
- Évaluation via plusieurs critères : [coefficient de détermination (R²)](https://fr.wikipedia.org/wiki/Coefficient_de_d%C3%A9termination), tests statistiques, analyse des résidus

## Détails

### Formes du modèle  
- **Régression linéaire simple** : utilise une seule variable explicative (y = β₀ + β₁x + ε). Cette forme élémentaire permet d'établir une relation affine entre deux variables, particulièrement utile pour les analyses exploratoires.  
- **Régression linéaire multiple** : utilise plusieurs variables explicatives (y = β₀ + β₁x₁ + ... + βₖxₖ + ε). Cette extension permet de contrôler les effets de plusieurs facteurs simultanément.  

### Estimation  
L'estimateur des moindres carrés ordinaires minimise la somme des carrés des résidus :  
- Forme matricielle : β̂ = (X'X)⁻¹X'y, développée par [Adrien-Marie Legendre](https://fr.wikipedia.org/wiki/Adrien-Marie_Legendre) et [Carl Friedrich Gauss](https://fr.wikipedia.org/wiki/Carl_Friedrich_Gauss)  
- Selon le théorème de Gauss-Markov, sous les hypothèses classiques, c'est le meilleur estimateur linéaire sans biais (BLUE)  
- En cas de colinéarité élevée, des techniques comme la [régression ridge](https://fr.wikipedia.org/wiki/R%C3%A9gression_ridge) peuvent être utilisées  

### Évaluation du modèle  
- **Coefficient de détermination (R²)** : mesure la proportion de variance expliquée (0 ≤ R² ≤ 1)  
- **Test de Fisher (F-test)** : évalue la significativité globale du modèle  
- **[Test de Student (t-test)](https://fr.wikipedia.org/wiki/Test_de_Student)** : teste la significativité de chaque coefficient individuel  
- **Analyse des résidus** : vérification visuelle et statistique des hypothèses (normalité, homoscédasticité, indépendance)  

### Extensions et variantes  
- **[Régression avec variables instrumentales](https://fr.wikipedia.org/wiki/Variables_instrumentales)** : pour traiter l'endogénéité  
- **Modèles linéaires hiérarchiques** : pour données imbriquées  
- **[Régression quantile](https://fr.wikipedia.org/wiki/R%C3%A9gression_quantile)** : lorsque les conditions de normalité ne sont pas satisfaites  
- **Méthodes robustes** : pour réduire l'influence des outliers  
- **[Régression ridge/lasso](https://fr.wikipedia.org/wiki/R%C3%A9gression_LASSO)** : méthodes de régularisation  

### Applications  
La régression linéaire est utilisée dans :  
- **Économétrie** : étude des rendements de l'éducation  
- **Sciences politiques** : modélisation des comportements électoraux  
- **Épidémiologie** : identification de facteurs de risque  
- **Ingénierie** : étalonnage d'instruments  
- **[Psychologie](https://fr.wikipedia.org/wiki/Statistiques_en_psychologie)** : analyse de variables comportementales  

*Note : Les dates et attributions historiques sont vérifiées via Wikipédia. Certaines applications nécessiteraient des références supplémentaires pour une validation complète.*