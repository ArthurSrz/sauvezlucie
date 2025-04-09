---
title: 'Surapprentissage (Overfitting) '
type: concept
tags:
- Machine Learning
- Surapprentissage
- Overfitting
- Apprentissage automatique
- Modélisation
- Données
- Performance
- Généralisation
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo:
- '[[Méthodes de régularisation en machine learning]]'
- '[[Dilemme biais-variance]]'
- '[[Dropout]]'
- '[[Early stopping]]'
- '[[Sous-apprentissage (Underfitting)]]'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
causes: '[[Malédiction de la dimensionnalité ]]'
---
## Généralité

Le [surapprentissage](https://fr.wikipedia.org/wiki/Surapprentissage) (ou overfitting en anglais) est un phénomène courant en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) où un modèle apprend trop bien les données d'entraînement, y compris leur bruit et leurs fluctuations aléatoires, au point de perdre sa capacité à généraliser à de nouvelles données. Cela se traduit par des performances élevées sur les données d'entraînement mais médiocres sur les données de test ou en production.

## Points clés

- Le surapprentissage survient généralement lorsque le modèle est trop complexe par rapport à la quantité de données disponibles
- Un modèle surajusté capture le bruit et les détails spécifiques plutôt que les motifs généraux sous-jacents
- Plusieurs techniques permettent de prévenir le surapprentissage : régularisation, validation croisée, augmentation des données
- Le [compromis biais-variance](https://fr.wikipedia.org/wiki/Biais_(statistique)) explique théoriquement ce phénomène
- Les modèles complexes comme les [réseaux de neurones profonds](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_profond) sont particulièrement sujets au surapprentissage

## Détails

### Causes du surapprentissage
Le surapprentissage est particulièrement problématique dans les modèles ayant une grande capacité d'apprentissage. Plusieurs facteurs y contribuent :
- Ensemble d'entraînement trop petit ou non représentatif
- Modèle trop complexe (trop de paramètres)
- Entraînement trop long menant à une optimisation excessive

### Détection du surapprentissage
Pour détecter le surapprentissage, on observe généralement :
- Grande différence entre performances sur données d'entraînement et de test
- Performances d'entraînement exceptionnellement bonnes (précision >98%)
- Prédictions erratiques sur de nouvelles données

### Techniques de prévention
Plusieurs approches permettent de limiter le surapprentissage :

1. **Régularisation** : Ajout de termes de pénalité ([L1](https://fr.wikipedia.org/wiki/R%C3%A9gression_laplacienne), [L2](https://fr.wikipedia.org/wiki/R%C3%A9gression_ridge)) pour limiter la complexité

2. **Validation croisée** : Utilisation de sous-ensembles de validation via la méthode [k-fold](https://fr.wikipedia.org/wiki/Validation_crois%C3%A9e)

3. **Arrêt précoce** : Interruption de l'entraînement dès détection de surapprentissage

4. **Augmentation des données** : Génération de nouvelles données par transformation

5. **Dropout** : Désactivation aléatoire de neurones pendant l'entraînement (introduit par Geoffrey Hinton)

6. **Méthodes d'ensemblage** : Combinaison de plusieurs modèles comme les [forêts aléatoires](https://fr.wikipedia.org/wiki/For%C3%AAt_al%C3%A9atoire)

### Exemples concrets
Dans une tâche de classification d'images, un modèle surajusté pourrait :
- Mémoriser des artefacts spécifiques comme des marques de compression [JPEG](https://fr.wikipedia.org/wiki/JPEG)
- Être trop sensible à des variations mineures comme la luminosité
- Afficher une confiance excessive dans ses prédictions erronées
- Montrer des comportements erratiques face à des cas limites

Des exemples classiques incluent les modèles de régression polynomiale ou les [arbres de décision](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision) qui développent des branches trop spécifiques.