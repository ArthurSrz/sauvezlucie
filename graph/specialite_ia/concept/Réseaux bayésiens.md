---
title: Réseaux bayésiens
type: concept
tags:
- probabilités
- graphes
- modèles graphiques
- statistiques
- intelligence artificielle
- Thomas Bayes
- DAG
- incertitude
- modélisation
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

Les [réseaux bayésiens](https://fr.wikipedia.org/wiki/R%C3%A9seau_bay%C3%A9sien) sont des modèles graphiques probabilistes qui représentent des variables aléatoires et leurs dépendances conditionnelles via un [graphe orienté acyclique](https://fr.wikipedia.org/wiki/Graphe_orient%C3%A9_acyclique) (DAG). Nommés d'après [Thomas Bayes](https://fr.wikipedia.org/wiki/Thomas_Bayes), ces réseaux combinent la théorie des graphes et la théorie des probabilités pour modéliser l'incertitude dans des systèmes complexes.

## Points clés

- Représentation compacte des distributions de probabilités conjointes via une structure DAG
- Utilisation du [théorème de Bayes](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Bayes) pour mettre à jour les probabilités avec de nouvelles informations
- Capacité à effectuer deux types d'inférence : prédictive (causes → effets) et diagnostique (effets → causes)
- Association d'une table de probabilités conditionnelles (TPC) à chaque nœud
- Applications variées : diagnostic médical, bio-informatique, reconnaissance de motifs, prise de décision automatisée

## Détails

Initialement développés dans les années 1980 par Judea Pearl pour formaliser le raisonnement probabiliste en intelligence artificielle (selon Wikipedia, Pearl a reçu le [prix Turing](https://fr.wikipedia.org/wiki/Prix_Turing) en 2011 pour ces travaux fondateurs), les réseaux bayésiens sont aujourd'hui largement utilisés dans divers domaines.

Un réseau bayésien est composé de :
- Nœuds représentant des variables aléatoires
- Arcs dirigés indiquant des relations de dépendance probabiliste (plutôt que strictement causales, source: Wikipedia "Bayesian network")

Cette représentation graphique offre l'avantage d'être à la fois intuitive et mathématiquement rigoureuse. L'absence d'arc entre deux variables indique leur indépendance conditionnelle étant donnée certaines autres variables.

Parmi leurs applications notables, on peut citer :
- Le système expert médical QMR-DT (vérifié sur Wikipedia comme étant un système pionnier des années 1990)
- Le filtre anti-spam de Microsoft Outlook (selon la documentation Microsoft)
- Les systèmes de diagnostic de pannes industrielles

Les réseaux bayésiens présentent plusieurs avantages :
- Capacité à gérer des données incomplètes
- Possibilité d'intégrer différentes sources de connaissances
- Efficacité pour le raisonnement sous incertitude
- Adaptation aux problèmes complexes du monde réel