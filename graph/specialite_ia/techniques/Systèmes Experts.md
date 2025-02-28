---
title: "Systèmes Experts"
type: "technique"
tags: ["IA symbolique", "base de connaissances", "règles", "inférence", "raisonnement"]
relations:
  - type: "rdfs:subClassOf"
    target: "[[Techniques de l'intelligence artificielle]]"
  - type: "rdfs:seeAlso"
    target: ["[[Les premières avancées]]", "[[Approches Hybrides en IA]]"]
---

## Généralité

Les systèmes experts sont des programmes informatiques qui reproduisent le processus de décision d'un expert humain dans un domaine spécifique, en s'appuyant sur une base de connaissances et un moteur d'inférence.

## Points clés

- Représentent l'une des premières applications réussies de l'intelligence artificielle
- S'appuient sur une base de connaissances formalisée et un moteur d'inférence
- Particulièrement efficaces dans des domaines spécialisés et bien définis
- Permettent l'explicabilité des résultats grâce à leur raisonnement basé sur des règles

## Détails

Les systèmes experts, apparus dans les années 1970, représentent une approche de l'intelligence artificielle fondée sur la capture et la formalisation de l'expertise humaine. Contrairement aux méthodes d'apprentissage automatique qui apprennent par l'exemple, les systèmes experts s'appuient sur des connaissances explicites encodées sous forme de règles et de faits.

**Structure et composants principaux:**

1. **Base de connaissances**: Elle stocke l'ensemble des connaissances du domaine sous forme de règles (généralement "SI...ALORS...") et de faits. Ces connaissances sont fournies par des experts humains et traduites par des ingénieurs de la connaissance.

2. **Moteur d'inférence**: C'est le "cerveau" du système qui applique les règles aux faits pour en déduire de nouvelles conclusions. Il peut fonctionner selon deux modes principaux:
   - Chaînage avant: part des faits pour atteindre des conclusions
   - Chaînage arrière: part des hypothèses et cherche à les confirmer

3. **Interface utilisateur**: Permet l'interaction avec le système, la saisie de données et la présentation des résultats et explications.

Parmi les systèmes experts historiques marquants:
- **MYCIN** (1970s): diagnostic d'infections sanguines et prescription d'antibiotiques
- **DENDRAL** (1965): identification de structures moléculaires en chimie
- **PROSPECTOR**: évaluation de sites pour l'exploration minière
- **XCON/R1**: configuration d'ordinateurs VAX pour Digital Equipment Corporation

Bien que supplantés par les approches d'apprentissage automatique dans de nombreux domaines, les systèmes experts conservent leur pertinence dans certains secteurs où l'explicabilité et le respect strict de règles sont essentiels, comme la médecine réglementée, la finance ou le droit. Leur intégration dans des systèmes hybrides permet également de combiner leur capacité de raisonnement transparent avec la puissance prédictive des techniques d'apprentissage.

## Liens complémentaires

### [[Représentation des connaissances]]
### [[Moteurs d'inférence]]
### [[Les premières avancées]]
### [[Approches Hybrides en IA]]
