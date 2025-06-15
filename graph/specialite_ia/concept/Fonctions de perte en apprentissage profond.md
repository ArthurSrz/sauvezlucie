---
title: Fonctions de perte en apprentissage profond
type: concept
tags:
- apprentissage profond
- deep learning
- fonctions de perte
- loss functions
- optimisation
- entraînement
- modèles
- algorithmes
- machine learning
- IA
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo: '[[Apprentissage profond (Deep Learning)]]'
subClassOf: '[[Choix de la mesure d''erreur]]'
isPartOf: '[[Apprentissage non supervisé par contrastif]]'
---
## Généralité

Les [fonctions de perte](https://fr.wikipedia.org/wiki/Fonction_de_perte) (loss functions) sont des composants essentiels en [apprentissage profond](https://fr.wikipedia.org/wiki/Apprentissage_profond) qui quantifient l'écart entre les prédictions d'un modèle et les valeurs réelles attendues. Elles définissent l'objectif que l'algorithme d'optimisation cherche à minimiser pendant l'entraînement.

## Points clés

- Le choix de la fonction de perte est crucial car il influence directement la convergence du modèle et ses performances
- Les fonctions principales diffèrent selon le type de problème : régression, classification ou ranking
- Elles doivent généralement être continues et différentiables pour permettre l'optimisation par [descente de gradient](https://fr.wikipedia.org/wiki/Algorithme_du_gradient)
- Les fonctions de perte sont souvent combinées avec des termes de [régularisation](https://fr.wikipedia.org/wiki/R%C3%A9gularisation_(math%C3%A9matiques))
- Le développement de nouvelles fonctions constitue un domaine de recherche actif en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique)

## Détails

### Types de fonctions selon les problèmes

Les fonctions de perte peuvent être classées en plusieurs catégories selon le type de problème :

**Pour les problèmes de régression** :
- L'erreur quadratique moyenne (MSE)
- L'erreur absolue moyenne (MAE)
- La fonction de perte Huber (robuste aux valeurs aberrantes)

**Pour les problèmes de classification** :
- L'[entropie croisée](https://fr.wikipedia.org/wiki/Entropie_crois%C3%A9e) (cross-entropy)
  - Binaire (Binary Cross-Entropy)
  - Catégorielle (Categorical Cross-Entropy)
  - Sparse Categorical Cross-Entropy
- Hinge Loss (utilisée notamment dans les [SVM](https://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support))

**Pour les tâches de ranking** :
- Triplet loss (notamment en reconnaissance faciale)

### Propriétés importantes

Les principales propriétés des fonctions de perte incluent :
- **Continuité et différentiabilité** : Généralement nécessaires pour les méthodes de descente de gradient
- **Sensibilité appropriée aux erreurs** : Pour éviter à la fois le surapprentissage et le sous-apprentissage
- **Robustesse aux valeurs aberrantes** : Certaines fonctions comme Huber loss sont conçues spécifiquement pour cela

### Applications avancées

Les développements récents incluent :
- Fonctions de perte adverses (adversarial loss) utilisées dans les GANs ([Generative adversarial network](https://fr.wikipedia.org/wiki/Generative_adversarial_network))
- Fonctions de perte contrastives (contrastive loss) appliquées en apprentissage par similarité ([Contrastive learning](https://fr.wikipedia.org/wiki/Contrastive_learning))
- Combinaison de l'entropie croisée avec la fonction d'activation [softmax](https://fr.wikipedia.org/wiki/Fonction_softmax) pour les problèmes de classification multi-classes

### Fonctions spécifiques détaillées

**Pour la classification** :
- **Entropie croisée binaire** : Pour les problèmes de [classification binaire](https://fr.wikipedia.org/wiki/Classification_binaire), strictement convexe facilitant l'optimisation
- **Entropie croisée catégorielle** : Pour les problèmes multi-classes, utilisée avec la fonction softmax en couche de sortie
- **Sparse Categorical Cross-Entropy** : Optimisée pour les étiquettes entières, efficace en mémoire pour les problèmes avec nombreuses classes
- **Hinge Loss** : Utilisée dans les SVM pour maximiser la marge entre classes

**Pour la régression** :
- **MSE (Mean Squared Error)** : Différentiable partout mais sensible aux outliers
- **MAE (Mean Absolute Error)** : Plus robuste aux valeurs aberrantes que la MSE mais moins sensible aux erreurs