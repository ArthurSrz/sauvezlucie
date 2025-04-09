---
title: Propagation d'affinités pour la détection automatisée de groupes
type: concept
tags:
- clustering
- analyse de données
- apprentissage automatique
- propagation d'affinités
- détection de groupes
- algorithmes
- similarité
date_creation: '2025-04-02'
date_modification: '2025-04-02'
subClassOf: '[[Méthodes de clustering]]'
relatedTo: '[[Techniques de regroupement par détection de noyaux denses]]'
---
## Généralité

La propagation d'affinités est une méthode de [clustering](https://fr.wikipedia.org/wiki/Partitionnement_de_donn%C3%A9es) automatique qui identifie des groupes naturels dans des données en se basant sur des mesures de similarité entre points. Contrairement aux méthodes traditionnelles comme les [k-moyennes](https://fr.wikipedia.org/wiki/K-moyennes), elle ne nécessite pas de spécifier à l'avance le nombre de clusters et détermine automatiquement des exemples représentatifs (appelés "exemplaires") pour chaque groupe. Cette méthode a été proposée par Brendan J. Frey et Delbert Dueck en 2007 dans la revue [Science](https://fr.wikipedia.org/wiki/Science_(revue)).

## Points clés

- Méthode basée sur l'échange de messages ("responsabilités" et "disponibilités") entre points de données
- Ne nécessite pas de fixer le nombre de clusters à l'avance
- Identifie automatiquement des points représentatifs (exemplaires) pour chaque groupe
- Particulièrement efficace pour des données où les clusters ont des formes complexes
- Utilise une matrice de similarité comme entrée principale (peut être asymétrique)

## Détails

La propagation d'affinités fonctionne en échangeant des messages entre les points de données jusqu'à convergence. Deux types de messages sont calculés itérativement : les **messages de responsabilité** qui indiquent dans quelle mesure un point est adapté pour servir d'exemplaire à un autre point, et les **messages de disponibilité** qui montrent dans quelle mesure un point est disponible pour être un exemplaire.

L'algorithme procède en trois phases principales : 
1. **Initialisation** avec le calcul de la matrice de [similarité](https://fr.wikipedia.org/wiki/Similarit%C3%A9_(math%C3%A9matiques)) s(i,k)
2. **Itérations** avec mise à jour alternée des messages et amortissement
3. **Sélection finale** des exemplaires et affectation des points

Cette méthode trouve des groups naturels dans divers domaines comme l'[analyse d'images](https://fr.wikipedia.org/wiki/Analyse_d%27images), la [bio-informatique](https://fr.wikipedia.org/wiki/Bio-informatique), le [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel), le [marketing](https://fr.wikipedia.org/wiki/Marketing) ou l'[astronomie](https://fr.wikipedia.org/wiki/Astronomie).

Parmi ses principaux **avantages**, on note que la méthode :
- Ne nécessite pas de spécifier le nombre de [clusters](https://fr.wikipedia.org/wiki/Partitionnement_de_donn%C3%A9es)
- Gère bien les clusters de formes complexes
- Produit des résultats reproductibles
- Est robuste au [bruit](https://fr.wikipedia.org/wiki/Bruit_(information))

Cependant, elle présente certaines **limites** :
- Une [complexité algorithmique](https://fr.wikipedia.org/wiki/Complexit%C3%A9_algorithmique) élevée (O(N²) en mémoire)
- Une sensibilité au choix des paramètres de similarité
- Des performances sur de grands jeux de données
- Une difficulté avec des clusters de tailles très déséquilibrées