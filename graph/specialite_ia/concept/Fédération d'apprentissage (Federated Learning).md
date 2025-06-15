---
title: Fédération d'apprentissage (Federated Learning)
type: concept
tags:
- IA
- apprentissage automatique
- données décentralisées
- confidentialité
- machine learning
- federated learning
- modèles distribués
- protection des données
- edge computing
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
createdBy: '[[Google]]'
seeAlso: '[[Sécurité des systèmes IA en temps réel]]'
---
## Généralité

La [fédération d'apprentissage](https://fr.wikipedia.org/wiki/Apprentissage_f%C3%A9d%C3%A9r%C3%A9) (Federated Learning) est une technique d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) distribuée qui permet d'entraîner des modèles d'[IA](https://fr.wikipedia.org/wiki/Intelligence_artificielle) sur des données décentralisées. Développée initialement par Google en 2016, cette approche répond aux enjeux croissants de confidentialité des données et de réduction de la bande passante en entraînant les algorithmes directement sur les appareils des utilisateurs (smartphones, ordinateurs, objets connectés).

## Points clés

- **Confidentialité renforcée** : Les données restent localement sur les appareils, améliorant la conformité aux réglementations comme le [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es) et le [CCPA](https://fr.wikipedia.org/wiki/California_Consumer_Privacy_Act). [Source: Wikipédia - Protection des données personnelles]

- **Optimisation des coûts** : Réduit les coûts de bande passante (jusqu'à 100x moins selon Google Research) en ne transférant que les paramètres du modèle. [Source: Wikipédia - Calcul distribué]

- **Accès à des données diversifiées** : Permet d'utiliser des ensembles de données géographiquement distribués et autrement inaccessibles. [Source: Wikipédia - Apprentissage automatique]

## Détails

Le processus fonctionne selon un cycle itératif en quatre étapes principales : initialisation d'un modèle global sur le serveur central (utilisant souvent du [transfert learning](https://fr.wikipedia.org/wiki/Apprentissage_par_transfert)), entraînement local sur chaque appareil (consommant 1-10% de batterie par cycle selon Google Research), agrégation des mises à jour via des algorithmes comme [FedAvg](https://fr.wikipedia.org/wiki/Apprentissage_f%C3%A9d%C3%A9r%C3%A9), puis redistribution du modèle global mis à jour.

Il existe plusieurs variantes techniques de fédération d'apprentissage : la fédération horizontale pour des données partageant les mêmes caractéristiques sur différents appareils, la fédération verticale pour des données avec caractéristiques différentes sur les mêmes entités, et la fédération transfert quand les données ne partagent ni caractéristiques ni espace d'échantillonnage.

Parmi les principaux défis rencontrés figurent l'hétérogénéité des appareils (nécessitant des stratégies d'équilibrage de charge), la nécessité d'une communication efficace (via des techniques de compression comme la quantification), et les enjeux de sécurité (résolus par l'utilisation de [chiffrement homomorphe](https://fr.wikipedia.org/wiki/Chiffrement_homomorphe) et [Secure Aggregation](https://fr.wikipedia.org/wiki/Cryptographie)).

Cette technologie trouve des applications concrètes dans plusieurs domaines : les assistants virtuels (implémenté dans [Gboard](https://fr.wikipedia.org/wiki/Gboard) depuis 2017), la recherche médicale (utilisé par [NVIDIA Clara](https://fr.wikipedia.org/wiki/NVIDIA) pour l'analyse d'imagerie), la détection de fraudes dans les applications bancaires, et les voitures autonomes où des expérimentations sont en cours.