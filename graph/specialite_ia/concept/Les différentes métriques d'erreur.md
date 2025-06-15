---
title: Les différentes métriques d'erreur
type: concept
tags:
- deep learning
- apprentissage par transfert
- modèles pré-entraînés
- data science
- machine learning
date_creation: '2025-03-30'
date_modification: '2025-03-30'
subClassOf: '[[Choix de la mesure d''erreur]]'
---
## Généralité

L'[apprentissage par transfert](https://fr.wikipedia.org/wiki/Apprentissage_par_transfert) en [deep learning](https://fr.wikipedia.org/wiki/Apprentissage_profond) est une technique qui consiste à réutiliser un modèle pré-entraîné sur une tâche pour améliorer les performances sur une tâche similaire. Cette approche s'inspire de la capacité humaine à transférer des connaissances d'un domaine à un autre.

## Points clés

- **[Réutilisation des modèles pré-entraînés](https://fr.wikipedia.org/wiki/Apprentissage_par_transfert)** : Utilisation de modèles comme [VGG](https://fr.wikipedia.org/wiki/VGG16), [ResNet](https://fr.wikipedia.org/wiki/ResNet) ou BERT disponibles dans des frameworks comme TensorFlow Hub ou Hugging Face
- **[Adaptation fine (Fine-tuning)](https://fr.wikipedia.org/wiki/Fine-tuning)** : Ajustement des poids du modèle pré-entraîné sur de nouvelles données spécifiques
- **Économie de ressources** : Réduction du temps et des ressources nécessaires pour entraîner un modèle à partir de zéro
- **Utilité dans les domaines à données limitées** : Particulièrement précieux en médecine ou en [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur)
- **Plusieurs types de transfert** : Transfert inductif, transductif et non supervisé selon la nature des tâches

## Détails

Les modèles pré-entraînés sont généralement formés sur de grandes bases de données, telles que [ImageNet](https://fr.wikipedia.org/wiki/ImageNet) pour la vision par ordinateur (14 197 122 images annotées) ou des corpus de texte massifs comme Wikipedia. Ces modèles apprennent des représentations de haut niveau qui capturent des caractéristiques importantes des données.

Selon Wikipédia [Source: "Transfer learning" sur Wikipedia], il existe plusieurs types d'apprentissage par transfert :
- Transfert inductif (tâches source et cible différentes mais liées)
- Transfert transductif (même tâche mais distributions de données différentes)
- Transfert non supervisé (sans données labellisées dans le domaine cible)

Parmi les architectures populaires, on trouve :
- [VGG-16](https://fr.wikipedia.org/wiki/VGG16) (16 couches dont 13 convolutives)
- ResNet (utilisant des connexions résiduelles)
- EfficientNet (optimisé pour l'efficacité computationnelle)

L'adaptation fine (Fine-tuning) est particulièrement efficace lorsque le domaine source et le domaine cible partagent des caractéristiques sous-jacentes similaires. Les stratégies principales incluent :
1. **Geler certaines couches** : Geler les couches initiales et entraîner uniquement les couches finales
2. **Réentraîner toutes les couches** : Avec un learning rate typiquement 10 à 100 fois plus faible
3. **Approches hybrides** : Utilisation de learning rates différenciés selon les couches

Dans le diagnostic médical, des modèles pré-entraînés sur ImageNet ont été adaptés avec des résultats prometteurs pour certaines tâches d'analyse d'images radiologiques. Selon Wikipédia, les gains en ressources peuvent inclure :
- Réduction des données d'entraînement (10-100 fois moins)
- Réduction des itérations d'entraînement (50-90% moins)