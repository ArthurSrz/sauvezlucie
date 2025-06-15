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

La distillation de connaissances est une technique en [intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) qui permet de transférer les connaissances d'un modèle complexe (appelé "enseignant" ou "teacher") vers un modèle plus simple (appelé "élève" ou "student"). Introduite par [Geoffrey Hinton](https://fr.wikipedia.org/wiki/Geoffrey_Hinton), Oriol Vinyals et Jeff Dean dans leur article "Distilling the Knowledge in a Neural Network" en 2015, cette approche vise à créer des modèles plus légers et plus rapides tout en préservant une grande partie des performances des modèles plus grands et plus complexes.

## Points clés

- Transfère les connaissances via des "soft targets" (sorties probabilistes du modèle enseignant)
- Particulièrement utile pour le déploiement sur [appareils mobiles](https://fr.wikipedia.org/wiki/Appareil_mobile) et systèmes embarqués
- Permet des réductions de taille de modèle allant jusqu'à 100x selon les cas d'usage
- Applications dans la [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur), le traitement du langage naturel et la [reconnaissance vocale](https://fr.wikipedia.org/wiki/Reconnaissance_vocale)
- Utilise un hyperparamètre crucial appelé "température de distillation" (noté T)

## Détails

### Principe fondamental

Le processus de [distillation de connaissances](https://fr.wikipedia.org/wiki/Distillation_de_connaissances) repose sur l'idée que les sorties d'un modèle complexe contiennent des informations plus riches que les simples étiquettes de classe. Le modèle élève apprend non seulement à partir des étiquettes réelles mais aussi des distributions de probabilité produites par le modèle enseignant (appelées "soft targets"). Ces soft targets capturent des relations subtiles entre les classes apprises par le modèle complexe.

### Fonctionnement technique

La fonction de perte typique pour la distillation combine deux composantes :
1. Une perte standard entre les prédictions du modèle élève et les vraies étiquettes
2. Une perte de distillation qui mesure la divergence entre les distributions de probabilité du modèle élève et du modèle enseignant

Mathématiquement, on utilise souvent l'[entropie croisée](https://fr.wikipedia.org/wiki/Entropie_crois%C3%A9e) entre les distributions de probabilité "adoucies" des deux modèles. L'adoucissement est réalisé en divisant les logits (sorties avant la fonction softmax) par un paramètre de température T.

### Applications concrètes

Selon Wikipédia et des publications scientifiques, cette technique a trouvé des applications dans plusieurs domaines clés :

- **Reconnaissance vocale mobile** : Utilisée par des assistants comme [Siri](https://fr.wikipedia.org/wiki/Siri) ou [Google Assistant](https://fr.wikipedia.org/wiki/Google_Assistant) pour permettre un traitement local
- **Vision par ordinateur embarquée** : Appliquée dans les systèmes ADAS (Advanced Driver Assistance Systems)
- **Assistants personnels intelligents** : L'utilisation de modèles comme DistilBERT (réduction de 40% de la taille avec 97% des performances)

### Avantages principaux

- Réduction significative de la taille du modèle (10-100 fois)
- Accélération de l'inférence pour les applications en temps réel
- Diminution des besoins en mémoire et en puissance de calcul
- Préservation d'une grande partie des performances du modèle original (80-95%)
- Adaptabilité à divers domaines ([NLP](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel), [IoT](https://fr.wikipedia.org/wiki/Internet_des_objets))

### Variantes avancées

- Distillation en ligne (enseignant et élève entraînés simultanément)
- Distillation mutuelle (plusieurs modèles s'enseignent mutuellement)
- Self-distillation (un modèle s'enseigne à lui-même)