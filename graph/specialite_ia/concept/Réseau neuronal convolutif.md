---
title: Réseau neuronal convolutif
type: concept
tags:
- ConvNet
- intelligence artificielle
- CNN
- convolution
- vision par ordinateur
- deep learning
- réseaux de neurones
- apprentissage automatique
- traitement d'images
date_creation: '2025-03-29'
date_modification: '2025-04-04'
subClassOf:
- '[[Apprentissage automatique (Machine Learning)]]'
- '[[Réseaux neuronaux en IA]]'
relatedTo: '[[Techniques de l''intelligence artificielle]]'
seeAlso: '[[Architectures résiduelles (ResNets)]]'
---
## Généralité

Un [réseau neuronal convolutif](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif) (CNN ou ConvNet) est un type spécialisé de [réseau de neurones artificiels](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) conçu principalement pour traiter des données structurées en grille, comme les images. Inspiré par l'organisation du [cortex visuel](https://fr.wikipedia.org/wiki/Cortex_visuel) animal, il utilise des opérations mathématiques appelées convolutions pour extraire automatiquement des caractéristiques hiérarchiques à partir des données d'entrée.

Développés à partir des années 1980 avec le réseau Neocognitron de Kunihiko Fukushima, les CNN ont connu un essor majeur en 2012 grâce à [AlexNet](https://fr.wikipedia.org/wiki/AlexNet) qui a effectivement marqué une avancée significative dans la classification d'images. Depuis, ils sont devenus fondamentaux pour de nombreuses applications de [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur) et de traitement d'images.

## Points clés

- Les CNN utilisent des couches de convolution qui appliquent des filtres sur les données d'entrée pour détecter des motifs locaux, apprenant automatiquement des caractéristiques hiérarchiques (des bords simples aux formes complexes)
- L'architecture typique combine des couches de convolution (avec [ReLU](https://fr.wikipedia.org/wiki/Rectifier_(r%C3%A9seau_de_neurones))), de pooling et des couches entièrement connectées, popularisée par [LeNet-5](https://fr.wikipedia.org/wiki/LeNet) puis perfectionnée par AlexNet
- Les CNN réduisent considérablement le nombre de paramètres grâce au partage de poids et à la connectivité locale
- Particulièrement efficaces pour la reconnaissance d'images (avec [VGG](https://fr.wikipedia.org/wiki/VGG_(r%C3%A9seau_de_neurones)), ResNet), détection d'objets et segmentation sémantique ([U-Net](https://fr.wikipedia.org/wiki/U-Net))
- Applications modernes incluent le traitement du langage naturel, la génération d'images ([GANs](https://fr.wikipedia.org/wiki/R%C3%A9seaux_antagonistes_g%C3%A9n%C3%A9ratifs)) et l'analyse médicale

## Détails

### Architecture fondamentale

L'architecture d'un [CNN](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif) se compose généralement de :

1. **Couches de convolution**: Appliquent des filtres aux données d'entrée pour produire des cartes de caractéristiques, inspirées des récepteurs locaux du cortex visuel primaire.
2. **Fonction d'activation**: Généralement [ReLU](https://fr.wikipedia.org/wiki/Rectifier_(neural_networks)), qui introduit une non-linéarité dans le réseau.
3. **Couches de pooling**: Réduisent la dimension spatiale des cartes de caractéristiques (max-pooling courant).
4. **Couches entièrement connectées**: Utilisent les caractéristiques extraites pour la classification finale, parfois remplacées dans architectures récentes comme [ResNet](https://fr.wikipedia.org/wiki/Residual_neural_network).

### Avantages des CNN

- **Invariance à la translation**: Reconnaître des objets indépendamment de leur position dans l'image
- **Extraction hiérarchique de caractéristiques**: Des caractéristiques simples (bords) vers complexes (formes)
- **Réduction du nombre de paramètres**: Grâce au partage de poids et aux opérations de pooling

### Applications principales

- **Classification d'images**: Identification du contenu principal ([ImageNet](https://fr.wikipedia.org/wiki/ImageNet))
- **Détection d'objets**: Localisation et identification de multiples objets (YOLO, SSD)
- **Segmentation sémantique**: Attribution d'une classe à chaque pixel (U-Net en imagerie médicale)
- **Reconnaissance faciale**: Identification de visages et d'expressions (FaceNet)
- **Analyse médicale**: Détection d'anomalies dans des images médicale

### Architectures célèbres

- **LeNet-5** (1998): Yann LeCun pour la reconnaissance de chiffres manuscrits
- **AlexNet** (2012): Premier CNN profond à remporter ImageNet
- **VGG** (2014): Convolutions 3x3 empilées
- **GoogLeNet/Inception** (2014): Modules Inception
- **ResNet** (2015): Connexions résiduelles pour réseaux profonds