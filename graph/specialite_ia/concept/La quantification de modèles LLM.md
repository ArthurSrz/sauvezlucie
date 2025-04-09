---
title: La quantification de modèles LLM
type: concept
tags:
- optimisation
- déploiement
- LLM
- quantification
- modèles de langage
- ressources limitées
- performance
- réduction de la taille
- IA
date_creation: '2025-04-02'
date_modification: '2025-04-02'
subClassOf: '[[Quantification et compression de modèles]]'
isPartOf: '[[Optimisation de ressources en IA embarquée]]'
---
## Généralité

La **quantification de modèles [LLM](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage)** (Large Language Models) est une technique d'optimisation qui réduit la précision des paramètres (poids) et des activations d'un modèle de langage pour diminuer sa taille, son coût de calcul et sa consommation mémoire. Selon Wikipédia, cette approche s'inscrit dans le cadre plus large de l'optimisation des modèles d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) et est particulièrement cruciale pour les [réseaux neuronaux profonds](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_artificiels).

## Points clés

- **Réduction de taille** : Permet de réduire la taille mémoire des modèles de 4x (pour du 8 bits) jusqu'à 8x (pour du 4 bits)
- **Optimisation des performances** : Accélère les calculs (jusqu'à 2-3x sur certains matériels) et facilite le déploiement sur appareils edge
- **Techniques variées** : Inclut la quantification post-entraînement (PTQ), la quantification aware training (QAT) et des méthodes hybrides
- **Applications clés** : Déploiement d'[LLM](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) sur smartphones, IoT et optimisation pour serveurs à faible puissance
- **Compromis** : Perte d'exactitude généralement limitée à 1-2% sur les tâches courantes, mais pouvant varier selon les modèles

## Détails

La quantification transforme les valeurs flottantes ([float32](https://fr.wikipedia.org/wiki/Virgule_flottante)) des paramètres du modèle en valeurs entières à faible bit-depth (ex: int8, int4). Cela se fait en trois étapes principales : échantillonnage des distributions des poids, compression des valeurs dans une plage réduite, et conversion des valeurs flottantes vers le format cible.

On distingue plusieurs types de quantification :
- **Statique** : Appliquée une fois pendant le post-traitement avec un faible surcoût à l'inference mais une perte d'exactitude potentielle
- **Dynamique** : Adapte les plages en temps réel, utile pour les activations variables
- **Mixte** : Combine des bits différents pour poids et activations, optimisant le compromis performance/efficacité

Les techniques avancées incluent la quantification asymétrique avec des plages personnalisées pour chaque couche, la quantification en post-entraînement (PTQ) sans réentraînement, et la quantification avec réentraînement (QAT) qui peut améliorer la précision de 1-3%.

Parmi les outils et frameworks disponibles, on trouve [TensorFlow Lite](https://fr.wikipedia.org/wiki/TensorFlow), [PyTorch](https://fr.wikipedia.org/wiki/PyTorch), ONNX Runtime, Bitsandbytes (Hugging Face) et GPTQ spécialisé pour les modèles de langage.

Les défis principaux incluent une perte d'exactitude pouvant atteindre 5% dans les cas extrêmes, la sensibilité des mécanismes d'attention des LLM, et des limitations de compatibilité sur certaines architectures.

Les cas d'usage typiques comprennent :
- Déploiement Edge avec des modèles sur smartphones via quantification 4 bits
- Réduction des coûts d'instances sur serveur cloud
- Applications mobiles comme la reconnaissance vocale en temps réel

Le processus typique de quantification suit cinq étapes : analyse du modèle, choix du bit-depth, application de la quantification, évaluation des résultats, et ajustement si nécessaire.

---

[1] https://en.wikipedia.org/wiki/Quantization_(machine_learning)  
[2] https://en.wikipedia.org/wiki/Floating-point_arithmetic  
[3] https://en.wikipedia.org/wiki/Quantization_(signal_processing)#Quantization_in_machine_learning  
[4] https://en.wikipedia.org/wiki/Model_compression  
[5] https://en.wikipedia.org/wiki/TensorFlow#TensorFlow_Lite