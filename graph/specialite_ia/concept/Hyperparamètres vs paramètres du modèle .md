---
title: 'Hyperparamètres vs paramètres du modèle '
type: concept
tags:
- Machine Learning
- Apprentissage automatique
- Hyperparamètres
- Paramètres du modèle
- Optimisation
- Data Science
- Algorithmes
date_creation: '2025-04-08'
date_modification: '2025-04-08'
isPartOf: '[[Taux d''apprentissage (Learning Rate)]]'
---
## Généralité

Les hyperparamètres et les paramètres du modèle sont deux concepts fondamentaux en apprentissage automatique. Les hyperparamètres sont des configurations externes au modèle, définies avant l'entraînement, tandis que les paramètres du modèle sont des variables internes apprises automatiquement pendant l'entraînement.

## Points clés

- **Hyperparamètres** : Configurations externes contrôlant le processus d'apprentissage (ex: taux d'apprentissage, nombre de couches dans un réseau de neurones).
- **Paramètres du modèle** : Variables internes apprises à partir des données (ex: poids dans un réseau de neurones).
- **Différence clé** : Les hyperparamètres sont fixés avant l'entraînement, tandis que les paramètres sont optimisés pendant l'entraînement.

## Détails

### Hyperparamètres
Les hyperparamètres sont des réglages qui influencent la performance et le comportement d'un modèle d'apprentissage automatique. Ils ne sont pas appris à partir des données mais sont plutôt définis par l'utilisateur ou optimisés via des techniques comme la recherche sur grille ou la recherche aléatoire. Exemples courants :
- **Taux d'apprentissage** : Contrôle la vitesse à laquelle le modèle s'adapte pendant l'entraînement.
- **Nombre de couches cachées** : Définit l'architecture d'un réseau de neurones.
- **Taille du lot (batch size)** : Nombre d'échantillons traités avant une mise à jour des paramètres.

### Paramètres du modèle
Les paramètres du modèle sont les variables que le modèle apprend à partir des données pendant l'entraînement. Ils sont ajustés pour minimiser la fonction de perte. Exemples :
- **Poids et biais** : Dans un réseau de neurones, ces valeurs sont mises à jour via la rétropropagation.
- **Coefficients** : Dans une régression linéaire, ce sont les valeurs qui définissent la relation entre les variables.

### Importance de la distinction
- **Hyperparamètres** : Requièrent une sélection minutieuse, souvent via validation croisée, car ils impactent directement la capacité du modèle à généraliser.
- **Paramètres** : Sont automatiquement optimisés par l'algorithme d'apprentissage, reflétant les motifs trouvés dans les données.

## Exemples concrets

- **Régression linéaire** :
  - Hyperparamètre : Degré du polynôme (si on utilise une régression polynomiale).
  - Paramètre : Coefficients de la droite de régression.

- **Réseau de neurones** :
  - Hyperparamètre : Nombre de neurones par couche.
  - Paramètre : Valeurs des poids entre les neurones.