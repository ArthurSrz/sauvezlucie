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

La distance d'édition, également connue sous le nom de distance de Levenshtein, est une mesure qui quantifie la différence entre deux chaînes de caractères. Elle représente le nombre minimal d'opérations élémentaires (insertion, suppression, substitution) nécessaires pour transformer une chaîne en une autre. L'algorithme de Wagner-Fischer est une méthode de programmation dynamique efficace pour calculer cette distance, développée par Robert A. Wagner et Michael J. Fischer en 1974.

## Points clés

- La distance d'édition mesure la similarité entre deux chaînes en comptant le nombre minimal d'opérations élémentaires nécessaires pour transformer l'une en l'autre
- Les opérations élémentaires sont généralement l'insertion, la suppression et la substitution de caractères, chacune ayant un coût de 1
- L'algorithme de Wagner-Fischer utilise la programmation dynamique pour calculer cette distance avec une complexité temporelle de O(mn) et spatiale de O(mn), où m et n sont les longueurs des chaînes
- Cette métrique est largement utilisée en traitement automatique du langage naturel, en bio-informatique et pour la correction orthographique

## Détails

L'algorithme de Wagner-Fischer construit une matrice où chaque cellule d[i,j] représente la distance d'édition entre les i premiers caractères de la première chaîne et les j premiers caractères de la seconde chaîne. La matrice est remplie progressivement en utilisant la relation de récurrence suivante:

```
d[i,0] = i  // Coût pour transformer les i premiers caractères en chaîne vide
d[0,j] = j  // Coût pour transformer la chaîne vide en j premiers caractères

Pour i de 1 à m et j de 1 à n:
    Si s1[i-1] = s2[j-1]:
        d[i,j] = d[i-1,j-1]  // Aucun coût si les caractères sont identiques
    Sinon:
        d[i,j] = 1 + min(
            d[i-1,j],    // Suppression
            d[i,j-1],    // Insertion
            d[i-1,j-1]   // Substitution
        )
```

La valeur finale d[m,n] donne la distance d'édition entre les deux chaînes complètes.

Une optimisation courante de l'algorithme consiste à ne stocker que deux lignes de la matrice à la fois, réduisant ainsi la complexité spatiale à O(min(m,n)).

### Applications pratiques

La distance d'édition trouve de nombreuses applications:

1. **Correction orthographique**: suggérer des corrections pour les mots mal orthographiés
2. **Bio-informatique**: comparer des séquences d'ADN ou de protéines
3. **Reconnaissance de la parole**: évaluer la précision des systèmes de reconnaissance vocale
4. **Détection de plagiat**: mesurer la similarité entre des textes
5. **Fuzzy string matching**: recherche approximative dans les bases de données

### Variantes

Plusieurs variantes de la distance d'édition existent:
- **Distance de Damerau-Levenshtein**: ajoute l'opération de transposition (échange de deux caractères adjacents)
- **Distance de Hamming**: compte uniquement les substitutions (applicable aux chaînes de même longueur)
- **Plus longue sous-séquence commune**: variante qui considère uniquement les insertions et suppressions

L'algorithme de Wagner-Fischer reste une référence fondamentale dans le domaine de la comparaison de chaînes de caractères et continue d'être utilisé dans de nombreuses applications modernes.