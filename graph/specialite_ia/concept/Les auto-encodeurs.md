---
title: Les auto-encodeurs
type: concept
tags:
- intelligence artificielle
- apprentissage non supervisé
- réseaux de neurones
- compression de données
- auto-encodeurs
- représentation de données
- encodage
- réduction de dimension
date_creation: '2025-03-18'
date_modification: '2025-03-18'
isPartOf: '[[Apprentissage non supervisé]]'
uses: '[[Réduction de dimensionnalité en machine learning]]'
seeAlso:
- '[[Auto-encodeurs convolutifs]]'
- '[[Auto-encodeurs pour la réduction de bruit]]'
- '[[Auto-encodeurs variationnels (VAE)]]'
- '[[Auto-encodeurs adversariaux]]'
- '[[Auto-encodeurs contractifs]]'
---
## Généralité

Un auto-encodeur est un type de réseau de neurones artificiels utilisé pour l'apprentissage non supervisé de représentations de données efficaces. Sa structure particulière lui permet d'apprendre à compresser puis à reconstruire ses données d'entrée avec une perte minimale d'information. L'objectif principal n'est pas la reconstruction elle-même, mais plutôt l'apprentissage d'une représentation utile (encodage) des données d'entrée, généralement dans un espace de dimension réduite.

## Points clés

- Un auto-encodeur se compose de deux parties principales : un encodeur qui compresse les données d'entrée en une représentation latente, et un décodeur qui tente de reconstruire les données originales à partir de cette représentation.
- L'espace latent (ou code) est généralement de dimension inférieure à l'espace d'entrée, forçant le réseau à apprendre les caractéristiques les plus importantes des données.
- Les auto-encodeurs sont entraînés en minimisant l'erreur de reconstruction entre les données d'entrée et leur version reconstruite.
- Ils peuvent être utilisés pour la réduction de dimensionnalité, la détection d'anomalies, le débruitage d'images et la génération de données.

## Détails

### Architecture

L'architecture d'un auto-encodeur est symétrique, avec un goulot d'étranglement au milieu. L'encodeur transforme progressivement l'entrée en une représentation compressée (le code ou l'espace latent), tandis que le décodeur fait l'opération inverse pour reconstruire l'entrée originale.

La fonction de coût typique est l'erreur quadratique moyenne entre l'entrée originale et sa reconstruction. Pour une entrée x et sa reconstruction x', on cherche à minimiser ||x - x'||².

### Variantes principales

1. **Auto-encodeurs sous-complets** : La dimension de l'espace latent est inférieure à celle de l'entrée, forçant le réseau à apprendre une représentation compressée.

2. **Auto-encodeurs débruitants** : Entraînés à reconstruire des entrées propres à partir de versions bruitées, ce qui les rend robustes aux perturbations.

3. **Auto-encodeurs variationnels (VAE)** : Introduisent une contrainte probabiliste sur l'espace latent, permettant la génération de nouvelles données.

4. **Auto-encodeurs convolutifs** : Utilisent des couches convolutives pour traiter efficacement les données d'image.

5. **Auto-encodeurs contractifs** : Ajoutent une pénalité qui force le modèle à être moins sensible aux variations dans les données d'entrée.

### Applications

Les auto-encodeurs trouvent des applications dans de nombreux domaines :

- **Réduction de dimensionnalité** : Alternative non-linéaire à des méthodes comme l'ACP.
- **Détection d'anomalies** : Les données anormales produisent généralement une erreur de reconstruction plus élevée.
- **Débruitage et restauration d'images** : Particulièrement avec les auto-encodeurs débruitants.
- **Compression de données** : Bien que rarement utilisés en production pour cette tâche.
- **Pré-entraînement de réseaux profonds** : Historiquement utilisés pour initialiser les poids des réseaux profonds.
- **Génération de données** : Particulièrement avec les VAE qui peuvent générer de nouvelles instances similaires aux données d'entraînement.

Les auto-encodeurs constituent une famille polyvalente de modèles qui continuent d'évoluer et de trouver de nouvelles applications dans le domaine de l'apprentissage automatique.