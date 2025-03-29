---
title: Apprentissage par curriculum (Curriculum Learning)
type: concept
tags:
- intelligence artificielle
- apprentissage automatique
- curriculum learning
- stratégie d'entraînement
- Bengio
- apprentissage progressif
- machine learning
- deep learning
- pédagogie IA
- optimisation
date_creation: '2025-03-29'
date_modification: '2025-03-29'
relatedTo: '[[Apprentissage profond (Deep Learning)]]'
isPartOf: '[[Entraînement d''un modèle d''IA]]'
subClassOf: '[[Apprentissage auto-supervisé (Self-supervised Learning)]]'
---
## Généralité

L'apprentissage par curriculum (Curriculum Learning) est une stratégie d'entraînement en apprentissage automatique qui s'inspire de la façon dont les humains apprennent, en commençant par des concepts simples avant de progresser vers des notions plus complexes. Introduite formellement par Bengio et al. en 2009, cette approche consiste à organiser les données d'entraînement selon un ordre de difficulté croissante, permettant au modèle d'établir progressivement une compréhension solide du domaine étudié.

## Points clés

- L'apprentissage par curriculum présente les exemples d'entraînement dans un ordre de complexité croissante, plutôt que de manière aléatoire
- Cette approche améliore généralement la vitesse de convergence et peut conduire à de meilleures performances finales du modèle
- Le curriculum peut être défini manuellement par des experts du domaine ou déterminé automatiquement par des métriques de difficulté
- Cette méthode est particulièrement efficace pour les problèmes complexes et les architectures profondes

## Détails

L'apprentissage par curriculum s'inspire directement de la pédagogie humaine, où l'enseignement est structuré pour introduire progressivement des concepts plus difficiles. Dans le contexte de l'apprentissage automatique, cette approche permet de guider l'optimisation du modèle vers de meilleures solutions en évitant les minima locaux que l'on pourrait rencontrer avec un apprentissage aléatoire standard.

La mise en œuvre d'un curriculum d'apprentissage nécessite de définir une mesure de difficulté pour les exemples d'entraînement. Cette mesure peut être :
- Définie par des experts humains (curriculum manuel)
- Calculée à partir de caractéristiques des données (comme la complexité visuelle pour les images)
- Déterminée par la confiance du modèle lui-même (auto-curriculum)
- Basée sur la perte d'entraînement des exemples (les exemples avec une perte élevée étant considérés comme plus difficiles)

L'apprentissage par curriculum peut prendre différentes formes :
1. **Curriculum statique** : l'ordre des exemples est prédéfini avant l'entraînement et reste fixe
2. **Curriculum dynamique** : l'ordre est ajusté pendant l'entraînement en fonction des performances du modèle
3. **Auto-curriculum** : le modèle génère lui-même des tâches de difficulté croissante (courant en apprentissage par renforcement)

Cette approche présente plusieurs avantages :
- Accélération de la convergence de l'entraînement
- Amélioration des performances finales, particulièrement sur des tâches complexes
- Réduction potentielle du surapprentissage
- Meilleure généralisation à de nouveaux exemples

L'apprentissage par curriculum est particulièrement utile dans des domaines comme la vision par ordinateur, le traitement du langage naturel, et l'apprentissage par renforcement. Par exemple, pour entraîner un modèle à reconnaître des objets, on pourrait commencer par des images avec un seul objet bien visible sur un fond simple, avant de passer progressivement à des scènes plus complexes avec plusieurs objets et des occlusions.

Des variantes comme l'apprentissage par anti-curriculum (commencer par les exemples difficiles) ou l'apprentissage par curriculum mixte (alterner entre exemples faciles et difficiles) ont également été explorées, montrant que la stratégie optimale peut dépendre du problème spécifique abordé.