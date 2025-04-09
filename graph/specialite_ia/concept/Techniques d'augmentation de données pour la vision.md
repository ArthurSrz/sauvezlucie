---
title: Techniques d'augmentation de données pour la vision
type: concept
tags:
- vision par ordinateur
- apprentissage automatique
- augmentation de données
- traitement d'images
- deep learning
- données synthétiques
- transformation d'images
date_creation: '2025-04-04'
date_modification: '2025-04-04'
uses: '[[Réseau neuronal convolutif]]'
---
## Généralité

Les techniques d'[augmentation de données](https://fr.wikipedia.org/wiki/Augmentation_de_donn%C3%A9es) pour la vision sont des méthodes utilisées pour augmenter artificiellement la taille et la diversité d'ensemble de données d'images, généralement pour améliorer la performance des modèles d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique). Ces techniques, largement utilisées dans le domaine du [deep learning](https://fr.wikipedia.org/wiki/Apprentissage_profond) et de la vision par ordinateur, appliquent des transformations géométriques ou des modifications de couleur pour générer de nouvelles variantes des images originales.

## Points clés

- Améliore la généralisation des modèles en évitant le [surajustement](https://fr.wikipedia.org/wiki/Surajustement) (overfitting)
- Permet de travailler avec des ensembles de données limités
- Simule des variations réalistes que le modèle pourrait rencontrer en conditions réelles
- Peut être appliquée à la volée (online) pendant l'entraînement ou en prétraitement (offline)
- Existe en deux catégories principales: augmentations spatiales et augmentations de pixels

## Détails

Les techniques d'augmentation spatiale incluent la [rotation](https://fr.wikipedia.org/wiki/Rotation) (généralement de -30° à +30°), la translation (déplacement horizontal/vertical), la mise à l'échelle (zoom avant/arrière), le retournement horizontal, le recadrage aléatoire et la distorsion élastique. Ces transformations modifient la géométrie de l'image tout en préservant son contenu sémantique.

Les techniques d'augmentation de pixels comprennent la modification de luminosité/contraste, le changement de balance des couleurs, l'ajout de [bruit](https://fr.wikipedia.org/wiki/Bruit_num%C3%A9rique) (gaussien, sel et poivre), le flou gaussien, les filtres de couleur (sépia, niveaux de gris) et la correction gamma. Ces méthodes altèrent les propriétés photométriques de l'image.

Parmi les approches avancées, on trouve Mixup (combinaison linéaire de deux images), Cutout (masquage aléatoire de régions), CutMix (remplacement de régions par des parties d'autres images), [StyleGAN](https://fr.wikipedia.org/wiki/StyleGAN) (génération d'images synthétiques réalistes), AutoAugment (recherche automatique des meilleures stratégies d'augmentation) et les [réseaux antagonistes génératifs](https://fr.wikipedia.org/wiki/R%C3%A9seaux_antagonistes_g%C3%A9n%C3%A9ratifs) (GANs).

Les bonnes pratiques recommandent de conserver les transformations plausibles pour le domaine d'application, d'éviter les transformations qui pourraient modifier le label de l'image, de combiner plusieurs techniques pour une meilleure diversité, d'adapter l'intensité des transformations au cas d'usage, de valider l'impact des augmentations sur un ensemble de test et d'utiliser des méthodes adaptées au type de données.

Les applications principales incluent la [classification d'images](https://fr.wikipedia.org/wiki/Classification_d%27images), la [détection d'objets](https://fr.wikipedia.org/wiki/D%C3%A9tection_d%27objets), la [segmentation sémantique](https://fr.wikipedia.org/wiki/Segmentation_d%27images), la [reconnaissance faciale](https://fr.wikipedia.org/wiki/Reconnaissance_faciale), les systèmes [ADAS](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27aide_%C3%A0_la_conduite) et l'[imagerie médicale](https://fr.wikipedia.org/wiki/Imagerie_m%C3%A9dicale).