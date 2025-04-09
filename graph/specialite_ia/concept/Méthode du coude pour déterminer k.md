---
title: Méthode du coude pour déterminer k
type: concept
tags:
- clustering
- k-means
- analyse de données
- machine learning
- méthode du coude
- inertie intra-cluster
- optimisation
date_creation: '2025-04-02'
date_modification: '2025-04-04'
relatedTo: '[[K-means et algorithmes de clustering]]'
subClassOf: '[[Méthodes de clustering]]'
isPartOf: '[[Compression différentielle des connaissances dans les LLM]]'
---
## Généralité

La méthode du coude est une technique visuelle utilisée en [analyse de clusters](https://fr.wikipedia.org/wiki/Classification_automatique) pour déterminer le nombre optimal de clusters (k) dans des algorithmes comme [k-means](https://fr.wikipedia.org/wiki/K-moyennes). Elle analyse l'évolution de l'inertie intra-cluster (WCSS - Within-Cluster Sum of Squares) en fonction du nombre de clusters pour identifier le point optimal où l'ajout de clusters supplémentaires n'apporte plus d'amélioration significative.

## Points clés

- La méthode repose sur l'identification d'un "coude" dans la courbe d'inertie intra-cluster (somme des distances au carré entre points et centroïdes)
- Elle est particulièrement adaptée aux algorithmes de partitionnement comme [k-means](https://fr.wikipedia.org/wiki/K-moyennes)
- Son application nécessite une interprétation visuelle qui peut parfois être subjective
- Elle présente des limites avec des données complexes ou des clusters non sphériques
- Des alternatives existent comme le [score de silhouette](https://fr.wikipedia.org/wiki/Coefficient_de_silhouette) ou le critère d'information bayésien (BIC)

## Détails

La méthode du coude s'appuie sur le calcul de l'[inertie intra-cluster](https://fr.wikipedia.org/wiki/Inertie_intra-classe) (WCSS). Lorsqu'on trace cette inertie pour différentes valeurs de k, on observe généralement une décroissance rapide suivie d'un ralentissement. Le point où cette décroissance ralentit (le "coude") suggère une valeur raisonnable pour k.

### Étapes d'application

1. **Calculer l'inertie** pour différentes valeurs de k (par exemple, de 1 à 10 clusters)
2. **Tracer la courbe** de l'inertie en fonction de k
3. **Identifier le coude**, c'est-à-dire le point où la courbe commence à s'aplatir
4. **Choisir k** correspondant à ce coude

### Avantages et limites

**Avantages :**
- Simple à mettre en œuvre et à interpréter visuellement
- Ne nécessite pas de connaissances a priori sur la structure des données
- Particulièrement efficace pour les données avec des clusters sphériques et de taille similaire

**Limites :**
- Subjectivité dans l'identification du coude
- Peut ne pas fonctionner pour des données sans structure claire
- Moins adaptée aux algorithmes de clustering non basés sur les centroïdes

### Alternatives et compléments

D'autres méthodes peuvent compléter ou remplacer la méthode du coude :
- Le [score de silhouette](https://fr.wikipedia.org/wiki/Coefficient_de_silhouette)
- Le critère de Calinski-Harabasz
- Le critère d'information bayésien (BIC)
- Des méthodes plus récentes comme le Gap statistic

### Exemple pratique