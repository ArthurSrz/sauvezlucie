---
title: Programmation génétique
type: concept
tags:
- programmation génétique
- algorithmes génétiques
- intelligence artificielle
- évolution computationnelle
- sélection naturelle
- résolution de problèmes
- apprentissage automatique
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Algorithmes génétiques en IA]]'
depends: '[[Algorithmes génétiques pour l''optimisation combinatoire]]'
---
## Généralité

La [programmation génétique](https://fr.wikipedia.org/wiki/Programmation_g%C3%A9n%C3%A9tique) est une méthode d'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) inspirée de la théorie de l'évolution biologique, plus particulièrement des principes de sélection naturelle et d'hérédité génétique. Elle utilise des [algorithmes génétiques](https://fr.wikipedia.org/wiki/Algorithme_g%C3%A9n%C3%A9tique) pour faire évoluer automatiquement des programmes informatiques ou des modèles mathématiques afin de résoudre des problèmes complexes. Développée à partir des années 1990 par John Koza, cette technique appartient au champ plus large des algorithmes évolutionnaires.

## Points clés

- S'inspire des principes de [sélection naturelle](https://fr.wikipedia.org/wiki/S%C3%A9lection_naturelle) et de [génétique](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9tique), simplifiant les mécanismes biologiques décrits par [Charles Darwin](https://fr.wikipedia.org/wiki/Charles_Darwin)
- Génère des solutions via une optimisation heuristique basée sur une fonction de fitness, sans programmation explicite
- Particulièrement efficace pour certains problèmes d'optimisation complexes comme la conception de circuits ou l'optimisation de paramètres industriels
- Peut produire des solutions innovantes et parfois contre-intuitives
- Utilise une représentation arborescente des programmes (souvent en [LISP](https://fr.wikipedia.org/wiki/Lisp)) permettant des opérations génétiques

## Détails

La programmation génétique fonctionne en créant une population initiale de programmes aléatoires, puis en appliquant itérativement des opérations inspirées de la génétique pour améliorer ces programmes. Les principales étapes sont :

1. **Initialisation** : Création d'une population aléatoire de programmes (typiquement 500-10000 individus)
2. **Évaluation** : Calcul du score de fitness pour chaque programme
3. **Sélection** : Choix des meilleurs programmes via différents mécanismes (sélection par tournoi, proportionnelle à la fitness ou par élitisme)
4. **Reproduction** : Application d'opérateurs génétiques (croisement avec taux typique 60-90%, mutation avec taux 1-10%, reproduction clonale)
5. **Remplacement** : Formation d'une nouvelle génération
6. **Terminaison** : Arrêt après critère de fitness ou nombre d'itérations (typiquement 50-500 générations)

La programmation génétique trouve des applications dans divers domaines : conception de circuits électroniques, algorithmes de trading, reconnaissance de formes, robotique évolutive, découverte de lois scientifiques et optimisation de systèmes complexes en logistique ou aéronautique.

**Avantages** :
- Peut trouver des solutions innovantes et contre-intuitives
- Ne nécessite pas de connaissance approfondie du problème
- S'adapte bien aux problèmes mal définis
- Génère des solutions sans programmation explicite

**Limites** :
- Consommation importante de ressources computationnelles
- Difficulté à garantir la qualité des solutions
- Risque de convergence prématurée vers des solutions sous-optimales
- Nécessite une définition précise de la fonction de fitness
- Temps de calcul souvent longs
- Solutions parfois difficiles à interpréter