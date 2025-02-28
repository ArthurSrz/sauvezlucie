---
title: "Biais et discrimination en IA"
type: "enjeu"
tags: ["biais algorithmiques", "équité", "discrimination", "diversité", "inclusion"]
relations:
  - type: "rdfs:subClassOf"
    target: "[[Les enjeux de l'intelligence artificielle]]"
  - type: "rdfs:seeAlso"
    target: ["[[Éthique et responsabilité]]", "[[Gouvernance et régulation]]", "[[Transparence et explicabilité]]"]
---

## Généralité

Les biais et discriminations en intelligence artificielle désignent les inégalités de traitement et les préjudices systématiques que peuvent reproduire, amplifier ou générer les systèmes algorithmiques à l'encontre de certains groupes sociaux ou individus.

## Points clés

- Les systèmes d'IA peuvent perpétuer voire amplifier les biais sociaux présents dans leurs données d'entraînement
- Les biais peuvent apparaître à toutes les étapes du développement: collecte des données, conception, déploiement, interprétation
- L'équité algorithmique est un problème technique ET socio-politique nécessitant des approches interdisciplinaires
- Des méthodes de détection et d'atténuation des biais se développent mais soulèvent des questions de compromis avec d'autres objectifs

## Détails

Les biais et discriminations représentent l'un des défis majeurs pour le développement d'une intelligence artificielle éthique et responsable. Ces problèmes surviennent lorsque les systèmes d'IA produisent des résultats inéquitables, défavorisant systématiquement certains groupes ou individus sur la base de caractéristiques comme le genre, l'ethnicité, l'âge, le handicap ou le statut socio-économique.

### Sources et types de biais

Les biais peuvent s'introduire dans les systèmes d'IA de multiples façons:

1. **Biais dans les données d'entraînement**:
   - Représentation déséquilibrée de certains groupes
   - Données reflétant des discriminations historiques ou sociétales
   - Étiquetage incorrect ou biaisé par les annotateurs humains

2. **Biais de conception**:
   - Choix de variables ou caractéristiques utilisées par le modèle
   - Sélection des métriques d'optimisation
   - Mauvaise définition du problème à résoudre

3. **Biais d'interaction et d'interprétation**:
   - Interprétation différente des résultats selon le contexte culturel
   - Utilisation inappropriée du système dans certains contextes

### Exemples concrets de biais algorithmiques

De nombreux cas documentés illustrent la réalité de ce phénomène:

- Systèmes de recrutement favorisant inconsciemment les candidats masculins
- Algorithmes de crédit désavantageant certaines communautés
- Outils de reconnaissance faciale moins performants pour les personnes à la peau foncée
- Modèles de langage reproduisant des stéréotypes de genre ou raciaux
- Systèmes de santé allouant moins de ressources à certains groupes démographiques

### Approches d'équité algorithmique

Diverses définitions mathématiques de l'équité ont été proposées, chacune reflétant différentes conceptions de la justice:

- **Parité démographique**: Taux de sélection similaires entre groupes protégés
- **Égalité des chances**: Taux d'erreur similaires entre groupes
- **Équité causale**: Élimination des relations causales avec les attributs sensibles
- **Équité procédurale**: Respect d'un processus équitable plutôt que focus sur les résultats

Ces définitions peuvent être mutuellement incompatibles, nécessitant des choix explicites selon le contexte.

### Stratégies d'atténuation

Plusieurs méthodes sont développées pour lutter contre les biais:

1. **Interventions sur les données**:
   - Rééquilibrage des ensembles de données
   - Augmentation des données sous-représentées
   - Suppression de variables sensibles ou corrélées

2. **Interventions sur les algorithmes**:
   - Techniques d'apprentissage équitable (fairness constraints)
   - Optimisation multi-objectif incluant des métriques d'équité
   - Post-traitement des résultats pour corriger les disparités

3. **Approches organisationnelles**:
   - Diversité des équipes de développement
   - Audits systématiques des systèmes d'IA
   - Inclusion des parties prenantes potentiellement affectées

Le défi reste entier: construire des systèmes équitables nécessite une réflexion approfondie sur les valeurs sociales, les compromis inévitables entre différentes conceptions de l'équité, et une vigilance constante face à l'émergence de nouveaux biais.

## Liens complémentaires

### [[Équité algorithmique]]
### [[Méthodes de détection des biais]]
### [[Impact social des biais d'IA]]
### [[Diversité et inclusion dans le développement de l'IA]]
