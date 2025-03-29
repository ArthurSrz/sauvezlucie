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
date_creation: '2025-03-29'
date_modification: '2025-03-29'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
createdBy: '[[Google]]'
---
## Généralité

La fédération d'apprentissage (Federated Learning) est une technique d'apprentissage automatique distribuée qui permet d'entraîner des modèles d'IA sur des données décentralisées. Contrairement aux approches traditionnelles qui nécessitent de centraliser toutes les données sur un serveur, cette méthode entraîne l'algorithme sur les appareils des utilisateurs (smartphones, ordinateurs, objets connectés) où résident les données. Seules les mises à jour des modèles sont partagées avec le serveur central, jamais les données brutes elles-mêmes.

## Points clés

- Les données restent localement sur les appareils des utilisateurs, améliorant significativement la confidentialité et la conformité aux réglementations sur la protection des données
- Réduit les coûts de bande passante et de stockage puisque les données brutes ne sont pas transférées vers un serveur central
- Permet d'accéder à des ensembles de données plus vastes et diversifiés qui seraient autrement inaccessibles pour des raisons de confidentialité
- Offre des avantages en termes de latence car les modèles peuvent être mis à jour et utilisés localement

## Détails

Le processus de fédération d'apprentissage se déroule généralement en plusieurs étapes cycliques :

1. **Initialisation** : Un modèle global initial est développé sur le serveur central et distribué aux appareils participants.

2. **Entraînement local** : Chaque appareil entraîne le modèle sur ses données locales, générant ainsi un modèle mis à jour spécifique à ses données.

3. **Agrégation** : Les mises à jour des modèles (généralement sous forme de gradients ou de poids) sont envoyées au serveur central qui les agrège pour créer une nouvelle version améliorée du modèle global.

4. **Distribution** : Le modèle global mis à jour est redistribué aux appareils, et le cycle recommence.

Cette approche présente plusieurs défis techniques, notamment la gestion de l'hétérogénéité des appareils (puissance de calcul variable), la communication efficace (minimiser les transferts de données), et la sécurité (protection contre les attaques adverses).

Plusieurs variantes de fédération d'apprentissage existent :

- **Fédération horizontale** : Les participants partagent les mêmes caractéristiques mais ont des échantillons différents.
- **Fédération verticale** : Les participants ont les mêmes échantillons mais des caractéristiques différentes.
- **Fédération par transfert** : [Combine](https://fr.wikipedia.org/wiki/Combine) l'apprentissage fédéré avec l'apprentissage par transfert.

[Google](https://fr.wikipedia.org/wiki/Google) a été pionnier dans ce domaine en implémentant la fédération d'apprentissage dans [Gboard](https://fr.wikipedia.org/wiki/Gboard), son clavier virtuel, pour améliorer les suggestions de texte sans collecter les données de frappe des utilisateurs. D'autres applications incluent la détection de fraudes bancaires, les diagnostics médicaux collaboratifs entre hôpitaux, et l'optimisation des réseaux de télécommunications.

## Applications pratiques

- Amélioration des assistants virtuels et des claviers prédictifs sur smartphones
- Recherche médicale collaborative entre institutions sans partage de dossiers patients
- Détection de fraudes dans le secteur financier
- [Maintenance](https://fr.wikipedia.org/wiki/Maintenance) prédictive dans l'industrie 4.0
- Optimisation des véhicules autonomes