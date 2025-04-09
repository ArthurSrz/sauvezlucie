---
title: Systèmes de recommandation et filtrage collaboratif
type: concept
tags:
- intelligence artificielle
- recommandation
- filtrage collaboratif
- personnalisation
- machine learning
- data science
- algorithmes
- préférences utilisateurs
- similarité
date_creation: '2025-03-29'
date_modification: '2025-03-29'
subClassOf: '[[Systèmes de recommandation en IA]]'
uses: '[[Entreprises technologiques et géants du numérique dans le domaine de l''intelligence
  artificielle]]'
---
## Généralité

Les [systèmes de recommandation](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_recommandation) sont des outils d'[intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) qui suggèrent des produits, services ou contenus pertinents aux utilisateurs en fonction de leurs préférences et comportements. Ces systèmes visent à résoudre le problème de surcharge d'information en proposant des contenus personnalisés et permettent de traiter le "paradoxe du choix" où trop d'options peuvent paralyser la décision.

## Points clés

- Le [filtrage collaboratif](https://fr.wikipedia.org/wiki/Filtrage_collaboratif) est la technique la plus populaire, avec deux approches principales : basée sur les utilisateurs et basée sur les items
- Ces systèmes sont omniprésents dans le [commerce électronique](https://fr.wikipedia.org/wiki/Commerce_%C3%A9lectronique), les plateformes de streaming et les réseaux sociaux
- Les défis principaux incluent le "cold start", les problèmes de vie privée et la nécessité d'approches hybrides combinant [apprentissage profond](https://fr.wikipedia.org/wiki/Apprentissage_profond) et signaux contextuels

## Détails

Le filtrage collaboratif utilise les comportements et préférences collectives des utilisateurs. Selon [Wikipédia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_recommandation), cette technique a été popularisée par le système Tapestry développé au [Xerox PARC](https://fr.wikipedia.org/wiki/PARC_(entreprise)) en 1992. Il existe deux approches principales :

- **Basé sur les utilisateurs** : Recommande des items appréciés par des utilisateurs similaires. Utilise souvent des algorithmes de voisinage comme [k-NN](https://fr.wikipedia.org/wiki/Plus_proches_voisins).
- **Basé sur les items** : Recommande des items similaires à ceux que l'utilisateur a appréciés.

Le filtrage collaboratif repose sur une matrice utilisateur-item où chaque cellule représente l'interaction (notation, achat, visionnage). Pour le filtrage collaboratif basé sur les utilisateurs, l'algorithme identifie d'abord les utilisateurs similaires (voisins) à l'aide de mesures de similarité comme le cosinus ou la [corrélation de Pearson](https://fr.wikipedia.org/wiki/Corr%C3%A9lation_(statistiques)), puis agrège leurs préférences pour prédire les notes manquantes. Pour l'approche basée sur les items, l'algorithme calcule d'abord la similarité entre les items avant d'utiliser les items déjà notés pour prédire l'intérêt pour d'autres items similaires.

Les systèmes hybrides combinent plusieurs approches pour améliorer la précision des recommandations. Ils permettent notamment de surmonter certains défis majeurs comme :

- **Démarrage à froid** : Difficulté avec nouveaux items/utilisateurs sans historique
- **Problème de sparsité** : Matrice utilisateur-item souvent <1% remplie
- **Scalabilité** : Ressources importantes nécessaires pour traiter des millions d'entrées
- **Diversité** : Éviter l'effet de "bulle de filtre"
- **Vie privée** : Questions de confidentialité avec la collecte de données, particulièrement depuis le [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es)

Ces systèmes sont largement utilisés par des plateformes majeures comme [Amazon](https://fr.wikipedia.org/wiki/Amazon) (environ 35% des ventes), [Netflix](https://fr.wikipedia.org/wiki/Netflix) (réduction de l'attrition), [Spotify](https://fr.wikipedia.org/wiki/Spotify) (playlists personnalisées) et [YouTube](https://fr.wikipedia.org/wiki/YouTube) (recommandation de vidéos), démontrant ainsi leur importance dans l'écosystème numérique actuel.