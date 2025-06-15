---
title: Apprentissage semi-supervisé
type: concept
tags:
- Apprentissage automatique
- Machine learning
- Données étiquetées
- Données non étiquetées
- Apprentissage supervisé
- Apprentissage non supervisé
- Performance des modèles
date_creation: '2025-03-30'
date_modification: '2025-03-30'
subClassOf: '[[Techniques de l''intelligence artificielle]]'
differentFrom:
- '[[Apprentissage supervisé]]'
- '[[Apprentissage non supervisé]]'
---
## Généralité

L'apprentissage semi-supervisé est une approche en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui combine des données étiquetées et non étiquetées pour améliorer la performance des modèles de machine learning. Cette méthode se situe entre l'[apprentissage supervisé](https://fr.wikipedia.org/wiki/Apprentissage_supervis%C3%A9), qui utilise uniquement des données étiquetées, et l'apprentissage non supervisé, qui ne nécessite aucune donnée étiquetée.

## Points clés

- **Combinaison de données** : Utilise à la fois des données étiquetées et non étiquetées pour entraîner le modèle
- **Réduction des coûts** : Diminue le besoin de données étiquetées, ce qui réduit les coûts et le temps d'annotation
- **Amélioration des performances** : Peut améliorer la précision du modèle en exploitant les informations contenues dans les données non étiquetées
- **Applications étendues** : Trouve des applications dans divers domaines comme la classification de documents, la détection de spams et la reconnaissance vocale

## Détails

L'apprentissage semi-supervisé est basé sur l'idée que les données non étiquetées peuvent fournir des informations supplémentaires sur la structure des données. Cette approche repose sur trois hypothèses fondamentales :
- L'hypothèse de continuité (points proches ont des étiquettes similaires)
- L'hypothèse de regroupement (les données tendent à former des clusters)
- L'hypothèse de variété (les classes sont séparables par des surfaces peu denses)

### Méthodes courantes

Les principales méthodes incluent :

- **Auto-étiquetage (Self-Training)** : Un modèle est d'abord entraîné sur un petit ensemble de données étiquetées, puis utilisé pour prédire les étiquettes des données non étiquetées. Popularisé par [Yarowsky](https://fr.wikipedia.org/wiki/David_Yarowsky) en [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel).

- **Co-entraînement (Co-Training)** : Utilise deux modèles différents qui se complètent mutuellement en étiquetant les données non étiquetées. Initialement développée par Blum et Mitchell (1998).

- **Méthodes basées sur les graphes** : Utilisent des [graphes](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_graphes) pour représenter les relations entre les données, comme l'algorithme Label Propagation.

- **Semi-Supervised Support Vector Machines (S3VM)** : Étend les [SVM](https://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support) classiques en incorporant un terme de régularisation.

- **Modèles génératifs** : Comme les [GMM](https://fr.wikipedia.org/wiki/M%C3%A9lange_gaussien) ou les GANs, qui apprennent la distribution sous-jacente des données.

### Applications pratiques

Cette approche trouve des applications dans divers domaines :

- **Reconnaissance de la parole** : Améliorations rapportées par diverses entreprises
- **Classification de textes** : Utilisé par les moteurs de recherche
- **Vision par ordinateur** : Gains observables dans la littérature scientifique
- **Médecine** : Analyse d'images médicales lorsque les annotations sont rares

### Avantages et limites

**Principaux avantages** :
- Réduit significativement le coût et le temps d'annotation
- Améliore potentiellement la performance des modèles
- Permet d'exploiter les vastes quantités de données non étiquetées disponibles

**Défis à considérer** :
- Sensibilité à la qualité des prédictions initiales
- Complexité computationnelle élevée pour certains algorithmes
- Performance variable selon la distribution des données

En conclusion, l'apprentissage semi-supervisé représente une approche puissante et économique en [machine learning](https://fr.wikipedia.org/wiki/Apprentissage_automatique), particulièrement utile lorsque les données étiquetées sont limitées ou coûteuses à obtenir.