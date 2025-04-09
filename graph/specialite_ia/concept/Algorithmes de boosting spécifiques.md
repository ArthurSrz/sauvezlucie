---
title: Algorithmes de boosting spécifiques
type: concept
tags:
- boosting
- apprentissage automatique
- AdaBoost
- classification
- régression
- arbres de décision
- modèles faibles
- modèles forts
date_creation: '2025-04-04'
date_modification: '2025-04-04'
subClassOf: '[[Méthodes d''ensemble en machine learning]]'
uses: '[[Arbre de décision]]'
---
```
## Généralité

Les algorithmes de [boosting](https://fr.wikipedia.org/wiki/Boosting_(apprentissage_automatique)) sont des techniques d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui combinent plusieurs modèles faibles (généralement des [arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision)) pour former un modèle fort. Ces algorithmes améliorent progressivement les performances en corrigeant les erreurs des modèles précédents selon le principe de l'apprentissage adaptatif (adaptive boosting). Ils sont particulièrement efficaces pour les problèmes de classification et de régression.

## Points clés

- **[AdaBoost (Adaptive Boosting)](https://fr.wikipedia.org/wiki/AdaBoost)** : L'un des premiers algorithmes de boosting (introduit en 1995), il ajuste les poids des instances mal classées à chaque itération.
- **[Gradient Boosting](https://fr.wikipedia.org/wiki/Gradient_boosting)** : Utilise une [descente de gradient](https://fr.wikipedia.org/wiki/Algorithme_du_gradient) pour minimiser la fonction de perte, en ajoutant des modèles qui corrigent les erreurs résiduelles.
- **[XGBoost (Extreme Gradient Boosting)](https://fr.wikipedia.org/wiki/XGBoost)** : Une version optimisée de Gradient Boosting, connue pour sa rapidité et ses performances élevées.
- **LightGBM** : Conçu pour être plus efficace en termes de mémoire et de calcul, utilisant une technique appelée "Gradient-based One-Side Sampling".
- **CatBoost** : Spécialisé dans le traitement des données catégorielles, évitant le prétraitement fastidieux des variables catégorielles.

## Détails

Les algorithmes de boosting varient dans leur approche mais partagent le même principe fondamental d'apprentissage itératif. Voici les principales caractéristiques :

**AdaBoost (Adaptive Boosting)**  
Développé en 1995 par [Yoav Freund](https://fr.wikipedia.org/wiki/Yoav_Freund) et [Robert Schapire](https://fr.wikipedia.org/wiki/Robert_Schapire), AdaBoost attribue des poids plus élevés aux instances mal classées par les modèles précédents. Simple à implémenter, il est souvent utilisé comme référence pour les problèmes de [classification binaire](https://fr.wikipedia.org/wiki/Classification_binaire).

**Gradient Boosting**  
Popularisé par [Jerome H. Friedman](https://fr.wikipedia.org/wiki/Jerome_H._Friedman) en 1999, cette méthode construit des modèles pour prédire les résidus (erreurs) des modèles précédents en utilisant une approche par [descente de gradient](https://fr.wikipedia.org/wiki/Algorithme_du_gradient). Elle s'adapte à diverses fonctions de perte et offre une grande flexibilité.

**XGBoost (Extreme Gradient Boosting)**  
Développé par [Tianqi Chen](https://fr.wikipedia.org/wiki/Tianqi_Chen) en 2014, XGBoost introduit des techniques de régularisation pour éviter le [surajustement](https://fr.wikipedia.org/wiki/Surapprentissage) et prend en charge le parallélisme, ce qui en fait l'un des algorithmes les plus performants actuellement.

**LightGBM**  
Cré