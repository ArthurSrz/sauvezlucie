---
title: Quantification et compression de modèles
type: concept
tags:
- IA
- optimisation
- quantification
- compression
- déploiement
- inférence
- modèles
- ressources limitées
- edge computing
- efficience
date_creation: '2025-03-22'
date_modification: '2025-03-22'
subClassOf: '[[Déploiement d''un modèle d''IA]]'
---
## Généralité

La quantification et la compression de modèles sont des techniques d'optimisation visant à réduire la taille et les besoins en ressources des modèles d'intelligence artificielle, tout en préservant au maximum leurs performances. Ces approches sont devenues essentielles face à l'augmentation constante de la taille des modèles d'IA, particulièrement pour leur déploiement sur des appareils à ressources limitées ou pour réduire les coûts d'inférence dans les environnements cloud.

## Points clés

- La quantification réduit la précision numérique des poids du modèle (par exemple, de float32 à int8), diminuant significativement l'empreinte mémoire
- La compression de modèles englobe diverses techniques comme l'élagage (pruning), la distillation de connaissances et la factorisation de matrices
- Ces techniques permettent d'accélérer l'inférence, réduire les coûts de déploiement et rendre possible l'utilisation de modèles complexes sur des appareils à ressources limitées
- Le défi principal est de maintenir un équilibre entre la réduction de taille et la préservation des performances

## Détails

### Techniques de quantification

La quantification transforme les valeurs à virgule flottante de haute précision (généralement float32) en représentations de plus faible précision comme int8 ou même int4. Cette conversion peut réduire la taille du modèle jusqu'à 75% tout en accélérant les calculs, car les opérations sur des entiers sont généralement plus rapides que celles sur des nombres à virgule flottante.

On distingue plusieurs types de quantification :
- **Quantification post-entraînement (PTQ)** : appliquée après l'entraînement du modèle sans réentraînement
- **Quantification consciente de l'entraînement (QAT)** : intègre la quantification pendant l'entraînement pour mieux préserver les performances
- **Quantification dynamique** : effectuée à l'exécution, offrant plus de flexibilité

### Techniques de compression

L'**élagage (pruning)** identifie et supprime les connexions ou neurones les moins importants du réseau. Cette technique peut éliminer jusqu'à 90% des paramètres avec un impact minimal sur la précision dans certains cas.

La **distillation de connaissances** transfère les "connaissances" d'un grand modèle (enseignant) vers un modèle plus petit (élève). Le modèle élève apprend à imiter les sorties du modèle enseignant plutôt que directement des données d'entraînement.

La **factorisation de matrices** décompose les grandes matrices de poids en produits de matrices plus petites, réduisant ainsi le nombre total de paramètres.

### Compromis et considérations

L'application de ces techniques implique généralement un compromis entre :
- Taille du modèle et consommation mémoire
- Vitesse d'inférence
- Précision et qualité des prédictions
- Consommation énergétique

Pour les modèles de langage de grande taille (LLM), des techniques spécifiques comme la quantification à bits mixtes sont développées, où différentes parties du modèle sont quantifiées à différentes précisions selon leur sensibilité.

### Applications pratiques

Ces techniques sont particulièrement importantes pour :
- Le déploiement de modèles sur smartphones et appareils IoT
- La réduction des coûts d'inférence dans les services cloud
- L'accélération des modèles pour les applications en temps réel
- L'optimisation des modèles pour des accélérateurs matériels spécifiques comme les TPU ou les puces neuromorphiques