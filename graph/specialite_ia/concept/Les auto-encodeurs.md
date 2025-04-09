---
title: Les auto-encodeurs
type: concept
tags:
- intelligence artificielle
- apprentissage non supervisé
- réseaux de neurones
- compression de données
- auto-encodeurs
- représentation de données
- encodage
- réduction de dimension
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Apprentissage non supervisé]]'
uses: '[[Réduction de dimensionnalité en machine learning]]'
seeAlso:
- '[[Auto-encodeurs pour la réduction de bruit]]'
- '[[Auto-encodeurs variationnels (VAE)]]'
- '[[Auto-encodeurs adversariaux]]'
- '[[Auto-encodeurs contractifs]]'
- '[[Auto-encodeurs convolutifs]]'
---
## Généralité

Un [auto-encodeur](https://fr.wikipedia.org/wiki/Auto-encodeur) est un type de [réseau de neurones artificiels](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) utilisé pour l'apprentissage non supervisé de représentations de données efficaces. Initialement proposé dans les années 1980 par [Geoffrey Hinton](https://fr.wikipedia.org/wiki/Geoffrey_Hinton), il permet d'apprendre à compresser puis reconstruire des données avec une perte minimale d'information.

## Points clés

- Structure symétrique composée d'un encodeur (compression) et d'un décodeur (reconstruction)
- Apprentissage d'une représentation utile dans un espace latent de dimension réduite
- Applications variées en vision par ordinateur, traitement du langage et recommandation
- Entraînement par minimisation de l'erreur de reconstruction (erreur quadratique moyenne ou entropie croisée)
- Principales variantes : débruiteurs, variationnels, contractifs et épars

## Détails

L'architecture des auto-encodeurs est symétrique avec un goulot d'étranglement central. L'encodeur transforme l'entrée en représentation compressée (espace latent), tandis que le décodeur reconstruit l'entrée originale. La fonction de coût typique est l'erreur quadratique moyenne ||x - x'||² entre entrée x et reconstruction x'. D'autres fonctions comme l'entropie croisée peuvent être utilisées pour des données binaires.

Les applications principales incluent :
- [Réduction de dimensionnalité](https://fr.wikipedia.org/wiki/R%C3%A9duction_de_dimensionnalit%C3%A9) (alternative non linéaire à l'ACP)
- Détection d'anomalies via l'identification d'échantillons avec fortes erreurs de reconstruction
- Débruitage d'images grâce aux auto-encodeurs débruiteurs
- Génération de données particulièrement avec les auto-encodeurs variationnels
- Étape de pré-traitement avant classification ou initialisation des poids dans réseaux profonds

Les variantes notables comprennent :
1. **Auto-encodeurs sous-complets** : Espace latent de dimension inférieure à l'entrée, forme classique de compression.
2. **Auto-encodeurs débruitants** : Reconstruisent des entrées propres à partir de versions bruitées.
3. **[Auto-encodeurs variationnels (VAE)](https://fr.wikipedia.org/wiki/Auto-encodeur_variationnel)** : Apprennent une distribution de probabilité dans l'espace latent.
4. **Auto-encodeurs contractifs** : Ajoutent une régularisation pour des caractéristiques plus robustes.
5. **Auto-encodeurs épars** : Imposent une contrainte de parcimonie sur les activations.

Ces différentes approches offrent des solutions adaptées à divers problèmes d'apprentissage automatique, tout en conservant le principe fondamental d'apprentissage de représentations efficaces.