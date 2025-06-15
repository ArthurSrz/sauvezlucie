---
title: Recherche d'architecture neurale (NAS)
type: concept
tags:
- Apprentissage automatique
- Réseaux neuronaux
- AutoML
- Intelligence artificielle
- Optimisation
- Deep Learning
- Algorithmes
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

La [Recherche d'Architecture Neuronale](https://fr.wikipedia.org/wiki/Recherche_d%27architecture_neuronale) (Neural Architecture Search, NAS) est une méthode d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) visant à automatiser la conception des architectures de réseaux neuronaux.

## Points clés

- **Automatisation** : Conception automatique d'architectures performantes réduisant le besoin d'expertise manuelle
- **Optimisation** : Utilisation d'algorithmes sophistiqués comme l'[apprentissage par renforcement](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement) ou les méthodes évolutionnaires
- **Efficacité** : Architectures surpassant souvent celles conçues manuellement, notamment en [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur) et traitement du langage naturel

## Détails

La NAS permet d'identifier des modèles optimaux pour des tâches spécifiques sans intervention humaine intensive, en explorant un vaste espace de configurations possibles. Les composantes principales incluent :

1. **Espace de recherche** : Définit l'ensemble des architectures potentielles (couches [convolutionnelles](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_%C3%A0_convolutions), [récurrentes](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_r%C3%A9current), etc.) et peut intégrer des contraintes pratiques comme la latence ou la taille du modèle.

2. **Stratégie de recherche** : Plusieurs approches existent :
   - Apprentissage par renforcement (popularisé par Zoph et Le avec NASNet)
   - Algorithmes évolutionnaires (comme dans AmoebaNet)
   - Optimisation bayésienne
   - NAS différentiable (DARTS) permettant une optimisation par gradient

3. **Évaluation des performances** : Utilise diverses techniques pour réduire le coût computationnel, notamment l'évaluation partielle, le partage de poids (ENAS) ou les modèles prédictifs.

Les applications majeures incluent la [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur) (EfficientNet, NASNet), le [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) (Evolved Transformer), et l'intégration dans des pipelines AutoML comme Google's AutoML.

Parmi les frameworks disponibles, on trouve [AutoKeras](https://fr.wikipedia.org/wiki/AutoKeras), [Google's AutoML](https://fr.wikipedia.org/wiki/Google_Cloud_AutoML), [H2O.ai](https://fr.wikipedia.org/wiki/H2O.ai), ainsi que des modules dans [PyTorch](https://fr.wikipedia.org/wiki/PyTorch) et [TensorFlow](https://fr.wikipedia.org/wiki/TensorFlow).

Les défis actuels incluent le coût computationnel (résolu partiellement par des méthodes comme ENAS), le surapprentissage (atténué par des techniques de méta-apprentissage) et la reproductibilité des résultats.