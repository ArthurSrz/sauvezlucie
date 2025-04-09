---
title: Fonction d'activation Softmax pour la classification multi-classes
type: concept
tags:
- machine learning
- réseaux de neurones
- classification
- softmax
- fonction d'activation
- probabilités
- multi-classes
- deep learning
- couche de sortie
- distribution de probabilités
date_creation: '2025-03-21'
date_modification: '2025-03-21'
subClassOf: '[[Impact du choix des fonctions d''activation sur l''apprentissage profond]]'
---
## Généralité

La [fonction d'activation](https://fr.wikipedia.org/wiki/Fonction_d%27activation) Softmax est une généralisation de la [fonction logistique](https://fr.wikipedia.org/wiki/R%C3%A9gression_logistique) pour les problèmes de classification multi-classes. Elle transforme un vecteur de valeurs réelles en une distribution de probabilités sur plusieurs classes, où la somme des probabilités est égale à 1. Selon Wikipédia, la fonction Softmax a été introduite dans le domaine des statistiques sous le nom de "fonction exponentielle normalisée" avant d'être largement adoptée en apprentissage automatique.

## Points clés

- Convertit un vecteur de scores (logits) en probabilités normalisées entre 0 et 1 dont la somme est égale à 1 ([source Wikipedia](https://fr.wikipedia.org/wiki/Fonction_softmax))
- Accentue les différences entre les valeurs d'entrée, rendant la classe la plus probable encore plus dominante
- Opère sur l'ensemble des sorties du réseau, garantissant une distribution de probabilité cohérente (contrairement à sigmoïde ou ReLU)
- Différentiable, ce qui la rend compatible avec la rétropropagation du gradient
- Standard pour les couches de sortie dans les problèmes de classification multi-classes

## Détails

### Définition mathématique

Pour un vecteur z = [z₁, z₂, ..., zₙ], la fonction Softmax calcule:

σ(z)ᵢ = e^(zᵢ) / Σⱼ e^(zⱼ)

Où σ(z)ᵢ représente la probabilité de la classe i, e est la base du [logarithme naturel](https://fr.wikipedia.org/wiki/Logarithme_naturel), et le dénominateur est la somme des exponentielles de toutes les composantes du vecteur z.

### Propriétés importantes

La fonction Softmax présente plusieurs propriétés remarquables :
- Sensibilité à l'échelle : multiplication par un facteur modifie la "pointe" de la distribution
- Invariance par translation : ajout d'une constante ne change pas le résultat
- Amplification exponentielle des différences entre classes
- Produit toujours une distribution de probabilité valide (somme à 1)

### Architecture typique dans les réseaux de neurones

Dans les implémentations pratiques :
1. La couche de sortie contient autant de neurones que de classes possibles
2. Application de Softmax sur les logits (sorties brutes avant normalisation)
3. Utilisation conjointe avec l'entropie croisée comme fonction de perte
4. Possibilité d'ajouter une température pour contrôler la "dureté" des prédictions

### Applications principales

Les domaines d'application classiques incluent :
- [Reconnaissance d'images](https://fr.wikipedia.org/wiki/Reconnaissance_d%27images) : classification d'objets dans des architectures comme ResNet ou EfficientNet
- [Traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) : classification de textes dans modèles comme BERT ou GPT
- Reconnaissance vocale : conversion de caractéristiques acoustiques en probabilités phonétiques
- Systèmes de recommandation : classement des préférences parmi de nombreux items possibles

### Applications émergentes

De nouveaux usages apparaissent dans :
- Recherche médicale (diagnostics différentiels automatisés)
- Robotique cognitive (sélection d'actions discrètes parmi un large éventail)
- Trading algorithmique (classification des signaux de marché complexes)
- Génération de contenu (sélection parmi plusieurs stratégies créatives)

*Note technique* : Ces applications avancées utilisent souvent des variantes adaptées de la fonction Softmax standard, comme le Softmax hiérarchique ou le Sampled Softmax pour gérer des espaces de sortie très larges.