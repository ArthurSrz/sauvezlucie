---
title: Quantification et compression de modèles
type: concept
tags:
- IA
- optimisation
- quantification
- compression
- déploiement
- inférence
- modèles
- ressources limitées
- edge computing
- efficience
date_creation: '2025-04-04'
date_modification: '2025-04-04'
subClassOf: '[[Déploiement d''un modèle d''IA]]'
seeAlso: '[[Compression différentielle des connaissances dans les LLM]]'
---
## Généralité

La [quantification](https://fr.wikipedia.org/wiki/Quantification_(informatique)) et la [compression de modèles](https://fr.wikipedia.org/wiki/Compression_de_données) sont des techniques d'optimisation visant à réduire la taille et les besoins en ressources des modèles d'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle), tout en préservant au maximum leurs performances. Ces approches sont essentielles pour le déploiement sur des appareils à ressources limitées (smartphones, IoT) ou pour réduire les coûts d'inférence dans les environnements cloud.

## Points clés

- La quantification réduit la précision numérique des poids du modèle (ex: float32 à int8), permettant typiquement une réduction de 75% de la taille du modèle avec 90-95% de précision conservée
- La compression inclut des techniques comme l'élagage (jusqu'à 90% des poids éliminés), la distillation de connaissances et la factorisation de matrices
- Ces techniques permettent d'accélérer l'inférence (jusqu'à 4x), réduire les coûts (jusqu'à 70% d'énergie) et déployer sur appareils mobiles/IoT
- Les frameworks comme [TensorFlow Lite](https://fr.wikipedia.org/wiki/TensorFlow) et ONNX Runtime proposent des outils intégrés pour ces techniques
- Le défi principal est de maintenir l'équilibre entre réduction de taille et préservation des performances

## Détails

La [quantification](https://fr.wikipedia.org/wiki/Quantification_(Machine_Learning)) transforme les valeurs float32 en représentations de plus faible précision (int8 ou int4), réduisant la taille jusqu'à 75% tout en accélérant les calculs. Elle préserve 85-95% de la précision originale selon l'architecture, étant particulièrement efficace pour les [réseaux de neurones convolutifs](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_convolutifs) et certains transformers.

On distingue plusieurs types de quantification :
- **Quantification post-entraînement (PTQ)** : appliquée après l'entraînement sans réentraînement (supportée par TensorFlow Lite et ONNX Runtime)
- **Quantification consciente de l'entraînement (QAT)** : intégrée pendant l'entraînement pour mieux préserver les performances
- **Quantification dynamique** : effectuée à l'exécution, avec implémentations matérielles spécialisées par des entreprises comme [NVIDIA](https://fr.wikipedia.org/wiki/Nvidia)

Parmi les techniques de compression, l'**élagage (pruning)** identifie et supprime les connexions ou neurones les moins importants. Cette technique peut éliminer jusqu'à 90% des paramètres. Le pruning structuré (suppression de couches entières) est particulièrement efficace pour l'accélération matérielle.

La **distillation de connaissances** transfère les connaissances d'un grand modèle (enseignant) vers un modèle plus petit (élève). Cette technique, validée par les travaux de Hinton et al., permet de créer des modèles compacts tout en conservant une grande partie des performances.

La **factorisation de matrices** réduit la dimensionnalité des couches denses, bien documentée dans la littérature scientifique. Des approches hybrides combinant plusieurs techniques (quantification + pruning) ont montré les meilleurs résultats selon les publications récentes (NeurIPS, ICML).

Ces techniques sont cruciales pour des architectures complexes comme les transformers (pouvant atteindre plusieurs centaines de Go), comme confirmé par les publications sur GPT-3. Des entreprises comme Google et NVIDIA ont développé des méthodes avancées permettant de maintenir une grande partie de la précision tout en réduisant considérablement l'empreinte mémoire et la consommation énergétique.