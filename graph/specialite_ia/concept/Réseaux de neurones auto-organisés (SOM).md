---
title: Réseaux de neurones auto-organisés (SOM)
type: concept
tags:
- SOM
- Réseaux de neurones
- Non supervisé
- Réduction de dimensionnalité
- Visualisation de données
- Teuvo Kohonen
- Topologie
- Apprentissage machine
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Réseaux neuronaux en IA]]'
relatedTo:
- '[[Apprentissage non supervisé]]'
- '[[Traitement automatique des données multimodales]]'
---
## Généralité

Les [Réseaux de Neurones Auto-Organisés](https://fr.wikipedia.org/wiki/Carte_auto_adaptative) (Self-Organizing Maps, SOM), également appelés cartes de Kohonen, sont un type de [réseau neuronal artificiel](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) non supervisé utilisé principalement pour la réduction de dimensionnalité et la visualisation de données multidimensionnelles. Développés par [Teuvo Kohonen](https://fr.wikipedia.org/wiki/Teuvo_Kohonen) dans les années 1980, les SOM permettent de cartographier des données de haute dimension sur une grille bidimensionnelle tout en préservant les relations topologiques entre les points de données.

## Points clés

- **[Non supervisé](https://fr.wikipedia.org/wiki/Apprentissage_non_supervis%C3%A9)** : Les SOM apprennent sans nécessiter de labels de classe, adaptés à l'exploration de données non étiquetées.
- **[Réduction de dimensionnalité](https://fr.wikipedia.org/wiki/R%C3%A9duction_de_dimension)** : Transformation de données de haute dimension en représentation bidimensionnelle, facilitant la visualisation.
- **Topologie préservée** : Maintien de la proximité spatiale entre les points de données, inspiré de l'organisation du [cortex cérébral](https://fr.wikipedia.org/wiki/Cortex_c%C3%A9r%C3%A9bral).
- **Apprentissage compétitif** : Mécanisme "winner-takes-most" où seul le neurone le plus similaire et ses voisins sont mis à jour.
- **Interprétabilité** : Résultats plus facilement interprétables que de nombreux modèles de [deep learning](https://fr.wikipedia.org/wiki/Apprentissage_profond).

## Détails

### Principe de fonctionnement

1. **Initialisation** : Les poids des [neurones](https://fr.wikipedia.org/wiki/Neurone_formel) sont initialisés de manière aléatoire ou selon une distribution spécifique.

2. **Présentation des données** : Chaque vecteur de données est présenté à la carte, avec souvent une recommandation de [normalisation des données](https://fr.wikipedia.org/wiki/Normalisation_(statistiques)).

3. **Recherche du neurone gagnant** : Identification du neurone dont les poids sont les plus proches du vecteur de données (mesuré par une [distance euclidienne](https://fr.wikipedia.org/wiki/Distance_euclidienne)).

4. **Mise à jour des poids** : Ajustement des poids du BMU et de ses voisins pour se rapprocher du vecteur de données, avec diminution progressive de la taille du voisinage.

5. **Répétition** : Répétition du processus pour chaque vecteur de données jusqu'à convergence.

### Avantages

- **Visualisation** : Représentation visuelle intuitive des données, facilitant la détection de clusters.
- **Interprétation** : Topologie préservée permettant une meilleure compréhension des relations entre données.
- **Flexibilité** : Utilisable pour classification, régression et détection d'anomalies.
- **Apprentissage non supervisé** : Ne nécessite pas de données étiquetées, utile pour l'exploration de données.

### Limites

- **Paramètres** : Choix du taux d'apprentissage, taille du voisinage et nombre d'itérations influençant significativement les résultats.
- **Complexité** : Mise à jour des poids et recherche du BMU coûteuses en calcul pour grandes cartes ou ensembles de données.
- **Interprétation** : Interprétation parfois subjective nécessitant l'intervention d'un expert.

### Applications

Les SOM trouvent des applications variées en exploration de données (clustering), reconnaissance de formes, analyse d'images satellitaires et bio-informatique. Leur capacité à créer des représentations intuitives de données complexes les rend utiles comme outil exploratoire dans des domaines comme le marketing ou la finance.