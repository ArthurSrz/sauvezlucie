---
title: Segmentation sémantique et d'instances
type: concept
tags:
- vision par ordinateur
- segmentation sémantique
- segmentation d'instances
- traitement d'images
- intelligence artificielle
- apprentissage automatique
- pixel classification
date_creation: '2025-04-04'
date_modification: '2025-04-04'
subClassOf: '[[Reconnaissance d''images et classification visuelle]]'
relatedTo: '[[Détection et localisation d''objets]]'
---
## Généralité

La [segmentation sémantique](https://fr.wikipedia.org/wiki/Segmentation_d%27image) et la [segmentation d'instances](https://fr.wikipedia.org/wiki/Instance_segmentation) sont deux techniques fondamentales en [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur) pour la compréhension d'images. Ces approches relèvent de l'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) et utilisent généralement des algorithmes d'[apprentissage profond](https://fr.wikipedia.org/wiki/Apprentissage_profond).

## Points clés

- **[Segmentation sémantique](https://fr.wikipedia.org/wiki/Segmentation_s%C3%A9mantique)** : Classifie chaque pixel sans distinguer les instances individuelles d'une même classe
- **[Segmentation d'instances](https://fr.wikipedia.org/wiki/Segmentation_d%27instances)** : Identifie et sépare chaque objet individuel même s'ils partagent la même classe
- **Applications variées** : Conduite autonome, médecine, robotique, surveillance
- **Bases de données clés** : Pascal VOC, COCO, Cityscapes
- **Technologies sous-jacentes** : Réseaux de neurones convolutifs (CNN), U-Net, Mask R-CNN

## Détails

### Segmentation sémantique
La segmentation sémantique consiste à attribuer une étiquette de classe à chaque pixel d'une image, créant ainsi une carte de classes où chaque région est identifiée par sa catégorie (par exemple : route, voiture, piéton). 

**Techniques courantes** :
- [Réseaux de neurones convolutifs](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_convolutifs) (CNN) comme U-Net
- Architectures basées sur des transformateurs (Vision Transformers) comme Segmenter

### Segmentation d'instances
La segmentation d'instances identifie et délimite chaque objet individuel même s'ils appartiennent à la même classe - par exemple, en distinguant chaque voiture individuelle dans un parking.

**Techniques courantes** :
- Architectures comme Mask R-CNN
- Méthodes basées sur des modèles à deux étapes
- Méthodes récentes utilisant des réseaux attentionnels

### Applications

1. **Conduite autonome** : Identification des [routes](https://fr.wikipedia.org/wiki/Route), [piétons](https://fr.wikipedia.org/wiki/Pi%C3%A9ton), et autres [véhicules](https://fr.wikipedia.org/wiki/V%C3%A9hicule)
2. **Médecine** : Segmentation des organes ou tumeurs dans les images médicales
3. **Robotique** : Navigation et interaction avec des objets spécifiques
4. **Surveillance** : Détection et suivi d'individus ou objets dans des vidéos

### Défis techniques

- **Complexité computationnelle** : Modèles comme [Mask R-CNN](https://fr.wikipedia.org/wiki/Mask_R-CNN) nécessitent jusqu'à 200 GFLOPs par image
- **Qualité des données** : Annotation manuelle coûteuse pour des datasets comme [COCO](https://fr.wikipedia.org/wiki/COCO_(base_de_donn%C3%A9es))
- **Variabilité des scènes** : Performances affectées par les conditions lumineuses et angles de vue

### Différences et complémentarité

- La segmentation sémantique pour l'analyse globale
- La segmentation d'instances pour l'identification précise
- Approches hybrides comme la [segmentation panoptique](https://fr.wikipedia.org/wiki/Segmentation_panoptique)