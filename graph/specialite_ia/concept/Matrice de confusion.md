---
title: Matrice de confusion
type: concept
tags:
- Apprentissage automatique
- Intelligence artificielle
- Matrice de confusion
- Précision et rappel
- Évaluation des modèles
- Métriques d'évaluation
- Optimisation des algorithmes
- Classification
- Biais des données
date_creation: '2025-03-30'
date_modification: '2025-03-30'
isPartOf:
- '[[Apprentissage automatique (Machine Learning)]]'
- '[[Méthodes d''évaluation des modèles]]'
uses: '[[Validation croisée et évaluation de modèles]]'
depends: '[[Choix de la mesure d''erreur]]'
---
```markdown
## Généralité

Une **[matrice de confusion](https://fr.wikipedia.org/wiki/Matrice_de_confusion)** est un outil essentiel en **[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle)** (IA) pour évaluer et interpréter les performances d'un modèle de classification. Sous forme de tableau, elle compare les prédictions du modèle aux étiquettes réelles, permettant d'identifier les erreurs spécifiques (vrais/faux positifs/négatifs).

Originaire des statistiques, la matrice de confusion est aujourd'hui un standard dans l'évaluation des modèles supervisés, avec des variantes adaptées aux problèmes multiclasses. Sa simplicité visuelle en fait effectivement un outil pédagogique pour expliquer les performances d'un modèle à des non-experts.

## Points clés

- **Structure adaptée à l'IA** : Tableau [NxN](https://fr.wikipedia.org/wiki/Matrice_(math%C3%A9matiques)) pour des problèmes multiclasse courants en IA (ex. : classification d'objets dans des images)
- **Diagnostic des erreurs IA** : Identifie les erreurs de prédiction (ex. : confusion entre chiens et chats dans un modèle de [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur))
- **Optimisation des modèles** : Guide les ajustements des hyperparamètres ou l'équilibrage des données pour améliorer la robustesse des systèmes IA
- **Priorisation des métriques** : En IA, la précision et le rappel sont souvent prioritaires selon le contexte
- **Calcul de métriques clés** : Permet de déterminer l'exactitude, la précision, le rappel et le score F1

## Détails

Pour une **classification binaire** (ex. : spam/non-spam) :  

|               | **Prédit positif** | **Prédit négatif** |  
|---------------|--------------------|--------------------|  
| **Réel positif** | VP (vrais