---
title: Réseaux à capsules (Capsule Networks)
type: concept
tags:
- Réseaux de neurones
- Capsule Networks
- Intelligence artificielle
- Apprentissage automatique
- Geoffrey Hinton
- CNN
- Vision par ordinateur
date_creation: '2025-04-04'
date_modification: '2025-04-04'
relatedTo: '[[Réseau neuronal convolutif]]'
subClassOf:
- '[[Réseaux neuronaux en IA]]'
- '[[Apprentissage profond (Deep Learning)]]'
---
## Généralité

Les [réseaux à capsules](https://fr.wikipedia.org/wiki/R%C3%A9seau_%C3%A0_capsules) (Capsule Networks ou CapsNets) sont une architecture innovante de [réseaux de neurones](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels) introduite par [Geoffrey Hinton](https://fr.wikipedia.org/wiki/Geoffrey_Hinton) et ses collaborateurs en 2017. Ils visent à surmonter certaines limitations des réseaux de neurones convolutifs (CNN) traditionnels, notamment en préservant les informations spatiales et en modélisant mieux les relations hiérarchiques entre les caractéristiques.

## Points clés

- **Représentation vectorielle** : Utilisation de capsules (vecteurs) pour encoder à la fois la présence et les propriétés spatiales des entités
- **Routage dynamique** : Mécanisme itératif permettant d'établir des relations hiérarchiques entre capsules
- **Avantages sur les CNN** : Meilleure robustesse aux transformations spatiales et préservation des informations de position/orientation
- **Applications prometteuses** : Reconnaissance d'objets sous angles variés, imagerie médicale, robotique
- **Limitations actuelles** : Coût computationnel élevé et performances encore à démontrer sur des datasets complexes

## Détails

Les réseaux à capsules reposent sur deux concepts principaux : les capsules et le routage dynamique. Une [capsule](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_capsules) est un groupe de neurones dont le vecteur d'activation représente les propriétés d'une entité spécifique dans l'image (position, orientation, échelle). La longueur du vecteur indique la probabilité de présence, tandis que sa direction encode ses attributs. Le mécanisme de routage dynamique permet aux capsules de niveau inférieur de prédire les sorties des capsules de niveau supérieur via un processus itératif d'accord par consensus, s'apparentant à l'algorithme [Expectation-Maximization](https://fr.wikipedia.org/wiki/Algorithme_esp%C3%A9rance-maximisation).

Comparés aux CNN traditionnels, les CapsNets présentent plusieurs différences notables. Ils préservent mieux les relations spatiales (équivariance plutôt qu'invariance), montrent une meilleure robustesse aux rotations et déformations (ex: 97.5% vs 92.3% sur smallNORB), et pourraient potentiellement nécessiter moins de données pour généraliser sur certains benchmarks.

Les applications des CapsNets sont particulièrement prometteuses dans des domaines où la compréhension des relations spatiales est cruciale : reconnaissance d'objets sous angles inhabituels, analyse d'images médicales ([IRM](https://fr.wikipedia.org/wiki/Imagerie_par_r%C3%A9sonance_magn%C3%A9tique), radiographies), robotique et réalité augmentée, ainsi que dans la sécurité biométrique (reconnaissance faciale).

Depuis l'article fondateur ["Dynamic Routing Between Capsules" (Sabour et al., 2017)](https://arxiv.org/abs/1710.09829), plusieurs extensions ont été développées. Parmi elles, on trouve les Matrix Capsules (2018) qui utilisent des matrices pour mieux modéliser les transformations 3D, les Capsules EM (2019) qui réduisent le coût computationnel, et des adaptations comme Capsule-Forensics pour la détection de deepfakes.

En termes de performances, les CapsNets atteignent 99.75% sur MNIST (avec augmentation de données), 97.5% sur smallNORB et 89.4% sur CIFAR10. Il est à noter que les CNN modernes dépassent désormais certains de ces scores sur ces benchmarks, ce qui souligne l'importance des recherches en cours pour améliorer les architectures à capsules.