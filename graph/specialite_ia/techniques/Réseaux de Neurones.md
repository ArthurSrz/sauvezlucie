---
title: "Réseaux de Neurones"
type: "technique"
tags: ["deep learning", "apprentissage profond", "neurones artificiels", "connexionnisme", "backpropagation"]
relations:
  - type: "rdfs:subClassOf"
    target: "[[Techniques de l'intelligence artificielle]]"
  - type: "rdfs:seeAlso"
    target: ["[[L'invention du perceptron]]", "[[L'apprentissage automatique et le deep learning]]"]
---

## Généralité

Les réseaux de neurones artificiels sont des modèles informatiques inspirés du fonctionnement des neurones biologiques, capables d'apprendre à partir de données et d'effectuer des tâches complexes comme la reconnaissance d'images ou le traitement du langage.

## Points clés

- Inspirés du fonctionnement des neurones biologiques dans le cerveau
- Composés de couches de neurones interconnectés avec des poids ajustables
- Utilisent l'algorithme de rétropropagation pour ajuster leurs paramètres
- Peuvent prendre différentes architectures selon les problèmes à résoudre

## Détails

Les réseaux de neurones artificiels constituent une famille de modèles mathématiques s'inspirant de la structure et du fonctionnement du cerveau humain. Ils représentent l'épine dorsale du deep learning et ont révolutionné de nombreux domaines de l'intelligence artificielle.

**Structure fondamentale:**

Un réseau de neurones se compose d'unités de calcul simples (neurones) organisées en couches:
- **Couche d'entrée**: reçoit les données brutes
- **Couches cachées**: effectuent des transformations successives
- **Couche de sortie**: produit le résultat final

Chaque neurone artificiel:
1. Reçoit des entrées pondérées depuis d'autres neurones
2. Applique une fonction d'activation non-linéaire à la somme pondérée
3. Transmet le résultat aux neurones de la couche suivante

L'apprentissage s'effectue principalement par rétropropagation du gradient d'erreur, un algorithme qui ajuste progressivement les poids synaptiques pour minimiser l'écart entre les prédictions et les valeurs attendues.

**Principales architectures:**

1. **Perceptron multicouche (MLP)**: Réseau feed-forward simple avec des couches entièrement connectées, adapté pour la classification et la régression.

2. **Réseaux convolutifs (CNN)**: Spécialisés dans le traitement d'images et de données structurées en grille, utilisant des filtres convolutifs pour extraire des caractéristiques spatiales.

3. **Réseaux récurrents (RNN)**: Conçus pour traiter des séquences temporelles grâce à des connexions cycliques permettant une forme de mémoire.

4. **LSTM et GRU**: Variantes avancées de RNN avec des mécanismes de portes pour capturer des dépendances à long terme.

5. **Transformers**: Architecture basée sur l'attention qui a révolutionné le traitement du langage naturel depuis 2017.

6. **Autoencodeurs**: Réseaux apprenant des représentations compactes des données par compression puis reconstruction.

7. **Réseaux génératifs (GAN, VAE)**: Capables de générer de nouvelles données semblables à celles de l'entraînement.

Les réseaux de neurones profonds excellent particulièrement dans les tâches impliquant des données non structurées (images, texte, audio) et constituent la base des systèmes d'IA les plus avancés comme GPT, DALL-E ou AlphaFold.

## Liens complémentaires

### [[Architectures de réseaux neuronaux]]
### [[Fonctions d'activation et optimiseurs]]
### [[Deep Learning et applications]]
### [[Rétropropagation du gradient]]
