---
title: Apprentissage auto-supervisé (Self-supervised Learning)
type: concept
tags:
- intelligence artificielle
- machine learning
- apprentissage auto-supervisé
- self-supervised learning
- représentations
- données non étiquetées
- paradigme d'apprentissage
- IA
date_creation: '2025-03-29'
date_modification: '2025-03-29'
seeAlso:
- '[[Apprentissage par curriculum (Curriculum Learning)]]'
- '[[Apprentissage non supervisé par contrastif]]'
relatedTo: '[[Apprentissage non supervisé par contrastif]]'
subClassOf: '[[Apprentissage profond (Deep Learning)]]'
---
## Généralité

L'apprentissage auto-supervisé (Self-supervised Learning) est un paradigme d'apprentissage automatique où un modèle apprend à partir des données sans nécessiter d'étiquettes explicites créées par l'humain. Au lieu de cela, le système génère automatiquement des signaux de supervision à partir des données brutes elles-mêmes. Cette approche exploite la structure inhérente aux données pour créer des tâches "prétextes" qui permettent au modèle d'acquérir des représentations utiles, comblant ainsi le fossé entre l'apprentissage supervisé (qui nécessite des étiquettes) et l'apprentissage non supervisé (qui fonctionne sans étiquettes).

## Points clés

- L'apprentissage auto-supervisé génère automatiquement des signaux de supervision à partir des données brutes, sans nécessiter d'annotations manuelles coûteuses
- Il repose sur la création de tâches "prétextes" où une partie des données est utilisée pour prédire d'autres parties des mêmes données
- Cette approche permet d'apprendre des représentations riches et généralisables qui peuvent être transférées à diverses tâches en aval
- Il a révolutionné le traitement du langage naturel (avec des modèles comme BERT, GPT) et gagne en importance dans la vision par ordinateur et d'autres domaines

## Détails

L'apprentissage auto-supervisé fonctionne en transformant un problème non supervisé en un problème supervisé par la création de tâches prétextes. Ces tâches sont conçues pour forcer le modèle à comprendre la structure sous-jacente des données.

Dans le domaine du traitement du langage naturel (NLP), des exemples courants de tâches prétextes incluent:
- La prédiction de mots masqués (comme dans BERT)
- La prédiction du mot suivant dans une séquence (comme dans GPT)
- La reconstruction de phrases dont l'ordre des mots a été perturbé
- La détermination si deux phrases se suivent naturellement

Pour la vision par ordinateur, les tâches prétextes peuvent inclure:
- La prédiction de la partie manquante d'une image
- La colorisation d'images en noir et blanc
- La prédiction de la rotation appliquée à une image
- L'assemblage de parties d'images comme un puzzle

L'un des avantages majeurs de l'apprentissage auto-supervisé est sa capacité à exploiter d'énormes quantités de données non étiquetées, qui sont généralement beaucoup plus abondantes et moins coûteuses à obtenir que les données étiquetées. Cela permet d'entraîner des modèles plus grands et plus puissants.

Le processus typique d'utilisation de l'apprentissage auto-supervisé comprend deux phases:
1. **Pré-entraînement**: Le modèle apprend des représentations générales à partir de grandes quantités de données non étiquetées via des tâches prétextes
2. **Fine-tuning**: Le modèle pré-entraîné est ensuite affiné sur une tâche spécifique avec une quantité relativement petite de données étiquetées

Cette approche a conduit à des avancées significatives dans de nombreux domaines, notamment en permettant des performances état-de-l'art avec beaucoup moins de données étiquetées qu'auparavant. Elle est particulièrement utile dans les scénarios où les données étiquetées sont rares ou coûteuses à obtenir.

## Applications et tendances récentes

Les applications de l'apprentissage auto-supervisé s'étendent désormais au-delà du NLP et de la vision par ordinateur, touchant des domaines comme l'audio, la robotique, et les séries temporelles. Des approches multimodales combinant différents types de données (texte, image, son) émergent également comme une tendance prometteuse pour développer des systèmes d'IA plus robustes et plus généralisables.