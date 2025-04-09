---
title: Distance d'édition et algorithme de Wagner-Fischer
type: concept
tags:
- algorithme
- programmation dynamique
- distance de Levenshtein
- Wagner-Fischer
- comparaison de chaînes
- informatique théorique
- traitement de texte
- bioinformatique
- similarité textuelle
- édition de texte
date_creation: '2025-03-20'
date_modification: '2025-03-20'
isPartOf: '[[Traitement du langage naturel (NLP)]]'
---
## Généralité

La [distance d'édition](https://fr.wikipedia.org/wiki/Distance_de_Levenshtein), également connue sous le nom de distance de Levenshtein, est une mesure qui quantifie la différence entre deux chaînes de caractères. Elle représente le nombre minimal d'opérations élémentaires (insertion, suppression, substitution) nécessaires pour transformer une chaîne en une autre. Cette notion a été introduite par le [mathématicien](https://fr.wikipedia.org/wiki/Math%C3%A9maticien) russe [Vladimir Levenshtein](https://fr.wikipedia.org/wiki/Vladimir_Levenshtein) en 1965, alors qu'il travaillait sur les théories des codes correcteurs d'erreurs.

## Points clés

- Mesure la similarité entre chaînes par le nombre minimal d'opérations (insertion, suppression, substitution)
- Introduite en 1965 par Vladimir Levenshtein pour les codes correcteurs d'erreurs
- Calculée efficacement par l'[algorithme de Wagner-Fischer](https://fr.wikipedia.org/wiki/Distance_de_Levenshtein#Algorithme_de_Wagner-Fischer) (complexité O(mn))
- Applications variées : correction orthographique, bioinformatique, reconnaissance vocale
- Exemple classique : transformation de "kitten" en "sitting" requiert 3 opérations

## Détails

L'[algorithme de Wagner-Fischer](https://fr.wikipedia.org/wiki/Algorithme_de_Wagner-Fischer) construit une matrice où chaque cellule d[i,j] représente la distance d'édition entre les i premiers caractères de la première chaîne et les j premiers caractères de la seconde. La matrice est remplie en utilisant la relation de récurrence suivante :