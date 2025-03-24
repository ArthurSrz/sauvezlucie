---
title: Systèmes Experts
type: concept
tags:
- intelligence artificielle
- systèmes experts
- IA
- informatique
- connaissances
- expertise
- systèmes d'aide à la décision
date_creation: '2025-03-15'
date_modification: '2025-03-15'
subClassOf: '[[Techniques de l''intelligence artificielle]]'
---
##Généralité

Un système expert est un programme informatique conçu pour simuler la capacité de raisonnement et les connaissances d'un expert humain dans un domaine spécifique. Développés dans les années 1970 comme une branche de l'intelligence artificielle, ces systèmes utilisent des règles prédéfinies, des heuristiques et des méthodes d'inférence pour résoudre des problèmes complexes qui nécessiteraient normalement l'expertise humaine. Contrairement aux programmes informatiques conventionnels, les systèmes experts peuvent expliquer leur raisonnement et traiter des informations incertaines ou incomplètes.

## Points clés

- Les systèmes experts sont composés de deux éléments principaux : une base de connaissances (règles et faits) et un moteur d'inférence (mécanisme de raisonnement).
- Ils sont particulièrement efficaces dans des domaines spécialisés comme le diagnostic médical, l'analyse financière, la configuration de systèmes complexes et la maintenance industrielle.
- Contrairement aux modèles d'IA modernes basés sur l'apprentissage automatique, les systèmes experts reposent sur des connaissances explicitement codées par des experts humains.
- Ils peuvent expliquer leur raisonnement, ce qui les rend particulièrement utiles dans les domaines où la transparence des décisions est cruciale.

## Détails

### Structure d'un système expert

Un système expert typique comprend plusieurs composants essentiels :

1. **Base de connaissances** : Contient les faits (données) et les règles (heuristiques) du domaine d'expertise. Ces règles sont généralement exprimées sous forme de conditions "SI-ALORS".

2. **Moteur d'inférence** : C'est le "cerveau" du système qui applique les règles aux faits pour déduire de nouvelles informations. Il peut fonctionner en chaînage avant (des faits vers les conclusions) ou en chaînage arrière (des hypothèses vers les faits qui les soutiennent).

3. **Interface utilisateur** : Permet aux utilisateurs d'interagir avec le système, de poser des questions et de recevoir des réponses.

4. **Module d'explication** : Capable de justifier son raisonnement et d'expliquer comment il est arrivé à une conclusion particulière.

5. **Module d'acquisition de connaissances** : Facilite l'ajout, la modification et la mise à jour des connaissances dans le système.

### Exemples historiques notables

- **MYCIN** (1970s) : Développé à Stanford pour diagnostiquer des infections bactériennes du sang et recommander des antibiotiques.
- **DENDRAL** : Conçu pour identifier les structures moléculaires en chimie organique.
- **XCON/R1** : Utilisé par Digital Equipment Corporation pour configurer des systèmes informatiques.
- **PROSPECTOR** : Employé pour l'exploration géologique et la découverte de gisements minéraux.

### Avantages et limites

**Avantages :**
- Conservation et diffusion de l'expertise rare ou coûteuse
- Cohérence dans la prise de décision
- Capacité à traiter des problèmes complexes
- Transparence du raisonnement

**Limites :**
- Difficulté à acquérir et formaliser les connaissances des experts (goulot d'étranglement de l'acquisition)
- Manque de flexibilité face à des situations imprévues
- Difficulté à maintenir et mettre à jour des bases de connaissances volumineuses
- Incapacité à apprendre automatiquement de nouvelles connaissances

### Position dans l'écosystème IA moderne

Bien que les systèmes experts aient été partiellement éclipsés par les approches d'apprentissage automatique et d'apprentissage profond, ils conservent leur pertinence dans des domaines où l'explicabilité et la fiabilité sont primordiales. Ils sont souvent intégrés dans des systèmes hybrides qui combinent règles explicites et apprentissage automatique pour bénéficier des avantages des deux approches.

Dans le contexte actuel de l'IA explicable (XAI), les principes des systèmes experts connaissent un regain d'intérêt pour rendre les décisions des systèmes d'IA plus transparentes et compréhensibles.