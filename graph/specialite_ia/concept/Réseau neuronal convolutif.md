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
date_creation: '2025-03-19'
date_modification: '2025-03-19'
rdfs:subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
uses: '[[Auto-encodeurs convolutifs]]'
relatedTo: '[[Techniques de l''intelligence artificielle]]'
---

##Généralité

Un réseau neuronal convolutif (CNN ou ConvNet) est un type spécialisé de réseau de neurones artificiels conçu principalement pour traiter des données structurées en grille, comme les images. Inspiré par l'organisation du cortex visuel animal, il utilise des opérations mathématiques appelées convolutions pour extraire automatiquement des caractéristiques hiérarchiques à partir des données d'entrée. Les CNN sont devenus la pierre angulaire de nombreuses applications de vision par ordinateur et de traitement d'images.

## Points clés

- Les CNN utilisent des couches de convolution qui appliquent des filtres sur les données d'entrée pour détecter des motifs locaux
- L'architecture typique combine des couches de convolution, de pooling (sous-échantillonnage) et des couches entièrement connectées
- Les CNN réduisent considérablement le nombre de paramètres par rapport aux réseaux entièrement connectés grâce au partage de poids
- Ils sont particulièrement efficaces pour la reconnaissance d'images, la détection d'objets et la segmentation sémantique

## Détails

### Architecture fondamentale

L'architecture d'un CNN se compose généralement de plusieurs types de couches:

1. **Couches de convolution**: Ces couches appliquent des filtres (ou noyaux) aux données d'entrée pour produire des cartes de caractéristiques. Chaque filtre détecte un motif spécifique (comme des bords, des textures ou des formes) à différentes positions de l'entrée. Le partage des poids dans ces filtres permet de réduire considérablement le nombre de paramètres.

2. **Fonction d'activation**: Généralement ReLU (Rectified Linear Unit), qui introduit une non-linéarité dans le réseau en remplaçant toutes les valeurs négatives par zéro.

3. **Couches de pooling**: Ces couches réduisent la dimension spatiale des cartes de caractéristiques, diminuant ainsi la quantité de paramètres et de calculs dans le réseau. Le max-pooling, qui conserve la valeur maximale dans une fenêtre, est couramment utilisé.

4. **Couches entièrement connectées**: Situées généralement à la fin du réseau, elles utilisent les caractéristiques extraites pour effectuer la classification finale.

### Avantages des CNN

- **Invariance à la translation**: Les CNN peuvent reconnaître des objets indépendamment de leur position dans l'image.
- **Extraction hiérarchique de caractéristiques**: Les premières couches détectent des caractéristiques simples (bords, coins), tandis que les couches plus profondes combinent ces caractéristiques pour détecter des structures plus complexes.
- **Réduction du nombre de paramètres**: Grâce au partage de poids et aux opérations de pooling, les CNN nécessitent moins de paramètres que les réseaux entièrement connectés.

### Applications principales

Les CNN ont révolutionné de nombreux domaines:

- **Classification d'images**: Identification du contenu principal d'une image (ex: ImageNet)
- **Détection d'objets**: Localisation et identification de multiples objets dans une image (ex: YOLO, SSD, Faster R-CNN)
- **Segmentation sémantique**: Attribution d'une classe à chaque pixel d'une image
- **Reconnaissance faciale**: Identification de visages et d'expressions
- **Analyse médicale**: Détection d'anomalies dans des images médicales (radiographies, IRM)

### Architectures célèbres

Plusieurs architectures CNN ont marqué l'évolution de ce domaine:
- **LeNet-5** (1998): Pionnier des CNN modernes
- **AlexNet** (2012): Premier CNN profond à remporter la compétition ImageNet
- **VGG** (2014): Architecture simple mais profonde
- **GoogLeNet/Inception** (2014): Introduction des modules Inception
- **ResNet** (2015): Introduction des connexions résiduelles permettant l'entraînement de réseaux très profonds

Les réseaux neuronaux convolutifs continuent d'évoluer avec des innovations comme les connexions denses (DenseNet), les convolutions séparables en profondeur, et les architectures efficientes comme EfficientNet.