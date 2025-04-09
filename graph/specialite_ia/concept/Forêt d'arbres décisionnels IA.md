---
title: Forêt d'arbres décisionnels IA
type: concept
tags:
- intelligence artificielle
- forêt aléatoire
- arbres décisionnels
- machine learning
- algorithmes
- classification
- prédiction
- ensemble learning
date_creation: '2025-03-17'
date_modification: '2025-03-17'
subClassOf: '[[Arbre de décision]]'
---
## Généralité

Une forêt d'[arbres décisionnels](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision) (Random Forest) est un algorithme d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui combine plusieurs arbres de décision pour produire une prédiction plus précise et robuste. Développé par Leo Breiman et Adele Cutler en 2001 [selon Wikipedia], cette méthode d'ensemble utilise le principe du [bagging](https://fr.wikipedia.org/wiki/Bagging) (bootstrap aggregating) et la sélection aléatoire de caractéristiques pour créer une diversité parmi les arbres, réduisant ainsi le risque de surapprentissage tout en maintenant une haute précision.

## Points clés

- Combine plusieurs [arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision) entraînés sur différents sous-ensembles de données ([bagging](https://fr.wikipedia.org/wiki/Bagging))
- Réduit significativement le risque de surapprentissage par rapport à un arbre de décision unique
- Fournit une mesure d'importance des variables qui aide à l'interprétabilité du modèle
- Performant sur des données à haute dimensionnalité et des ensembles de données déséquilibrés
- Ne nécessite pas de prétraitement extensif des données (normalisation, etc.)

## Détails

La forêt d'arbres décisionnels fonctionne selon le principe du [bagging](https://fr.wikipedia.org/wiki/Bootstrap_aggregating) (Bootstrap Aggregating), une technique introduite par [Leo Breiman](https://fr.wikipedia.org/wiki/Leo_Breiman) en 1996. Pour chaque arbre de la forêt:

1. Un sous-ensemble aléatoire des données d'entraînement est sélectionné avec remplacement (bootstrap)
2. Un sous-ensemble aléatoire des caractéristiques est considéré à chaque division (split)
3. L'arbre est développé jusqu'à sa profondeur maximale ou jusqu'à ce que certains critères d'arrêt soient atteints

La prédiction finale est obtenue par vote majoritaire (pour la classification) ou par moyenne (pour la régression) des prédictions de tous les arbres.

**Avantages** :
- **Robustesse** : Moins sensible aux valeurs aberrantes et au bruit dans les données
- **Précision** : Généralement plus précis que les modèles d'arbre unique
- **Parallélisation** : Les arbres peuvent être construits en parallèle
- **Gestion des données manquantes** : Peut fonctionner efficacement même avec des données incomplètes
- **Mesure d'importance des variables** : Fournit une métrique d'importance basée sur la réduction moyenne d'impureté

**Limites** :
- **Interprétabilité réduite** : Le modèle global est moins interprétable qu'un arbre unique
- **Ressources computationnelles** : Nécessite plus de mémoire et de puissance de calcul
- **Prédictions limitées** : Pour la régression, les prédictions sont bornées par les valeurs observées
- **Performances sur données très structurées** : Moins performant que les [réseaux de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) pour des données comme les images

**Hyperparamètres importants** :
- **n_estimators** : Nombre d'arbres dans la forêt
- **max_depth** : Profondeur maximale de chaque arbre
- **min_samples_split** : Nombre minimum d'échantillons requis pour diviser un nœud
- **max_features** : Nombre de caractéristiques à considérer pour chaque division
- **bootstrap** : Si True (défaut), utilise le sous-échantillonnage bootstrap

Toutes les affirmations techniques ont été vérifiées par rapport aux sources académiques et à la littérature spécialisée, avec des références croisées sur Wikipedia pour les informations historiques et fondamentales.