---
title: Distillation de connaissances en IA
type: concept
tags:
- intelligence artificielle
- distillation de connaissances
- modèles IA
- optimisation
- Geoffrey Hinton
- teacher-student
- compression de modèles
- transfert de connaissances
- efficience IA
date_creation: '2025-03-29'
date_modification: '2025-03-29'
relatedTo: '[[Quantification et compression de modèles]]'
hasPart: '[[Algorithmes génétiques en IA]]'
---
## Généralité

La distillation de connaissances est une technique en intelligence artificielle qui permet de transférer les connaissances d'un modèle complexe (appelé "enseignant" ou "teacher") vers un modèle plus simple (appelé "élève" ou "student"). Introduite par [Geoffrey Hinton](https://fr.wikipedia.org/wiki/Geoffrey_Hinton) en 2015, cette approche vise à créer des modèles plus légers et plus rapides tout en préservant la majeure partie des performances des modèles plus grands et plus complexes.

## Points clés

- La distillation de connaissances permet de compresser l'information d'un grand modèle vers un modèle plus petit et plus efficace
- Le modèle élève apprend non seulement à partir des étiquettes réelles mais aussi des distributions de probabilité produites par le modèle enseignant
- Cette technique est particulièrement utile pour le déploiement de modèles d'IA sur des appareils à ressources limitées
- La température de distillation est un hyperparamètre crucial qui contrôle la "douceur" des probabilités du modèle enseignant

## Détails

Le processus de distillation de connaissances repose sur l'idée que les sorties d'un modèle complexe contiennent des informations plus riches que les simples étiquettes de classe. Par exemple, si un modèle enseignant attribue des probabilités de 0.7, 0.2 et 0.1 à trois classes différentes, ces valeurs révèlent des relations entre les classes que l'étiquette brute (qui serait simplement la première classe) ne capture pas.

La fonction de perte typique pour la distillation combine deux composantes :
1. Une perte standard entre les prédictions du modèle élève et les vraies étiquettes
2. Une perte de distillation qui mesure la divergence entre les distributions de probabilité du modèle élève et du modèle enseignant

Mathématiquement, on utilise souvent l'entropie croisée entre les distributions de probabilité "adoucies" des deux modèles. L'adoucissement est réalisé en divisant les logits (sorties avant la fonction softmax) par un paramètre de température T. Une température plus élevée produit une distribution plus uniforme, révélant davantage les nuances dans les prédictions du modèle enseignant.

La distillation de connaissances présente plusieurs avantages :
- Réduction significative de la taille du modèle (parfois jusqu'à 10-100 fois)
- Accélération de l'inférence pour les applications en temps réel
- [Diminution](https://fr.wikipedia.org/wiki/Diminution) des besoins en mémoire et en puissance de calcul
- Préservation d'une grande partie des performances du modèle original

Cette technique est largement utilisée dans l'industrie, notamment pour déployer des modèles d'IA sur des smartphones, des appareils IoT ou des systèmes embarqués. Des variantes comme la distillation en ligne (où l'enseignant et l'élève sont entraînés simultanément) ou la distillation mutuelle (où plusieurs modèles s'enseignent mutuellement) ont également été développées pour améliorer encore les performances.

## Applications pratiques

La distillation de connaissances est particulièrement utile dans les domaines comme la reconnaissance vocale sur appareil, la vision par ordinateur embarquée, et les assistants virtuels, où les contraintes de ressources sont importantes mais où la qualité des prédictions reste cruciale.