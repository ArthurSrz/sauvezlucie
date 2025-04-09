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
date_creation: '2025-04-09'
date_modification: '2025-04-09'
---
## Généralité

L'[apprentissage auto-supervisé](https://fr.wikipedia.org/wiki/Apprentissage_automatique#Apprentissage_auto-supervis%C3%A9) (Self-supervised Learning) est un paradigme d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) où un modèle apprend à partir des données sans nécessiter d'étiquettes explicites créées par l'humain. Au lieu de cela, le système génère automatiquement des signaux de supervision à partir des données brutes elles-mêmes. Cette approche exploite la structure inhérente aux données pour créer des tâches "prétextes" qui permettent au modèle d'acquérir des représentations utiles, comblant ainsi le fossé entre l'apprentissage supervisé (qui nécessite des étiquettes) et l'apprentissage non supervisé (qui fonctionne sans étiquettes).

## Points clés

- L'[apprentissage auto-supervisé](https://fr.wikipedia.org/wiki/Apprentissage_auto-supervisé) génère automatiquement des signaux de supervision à partir des données brutes, sans nécessiter d'annotations manuelles coûteuses.
- Il repose sur la création de tâches "prétextes" où une [partie des données](https://fr.wikipedia.org/wiki/Donn%C3%A9es) est utilisée pour prédire d'autres parties des mêmes données.
- Cette approche permet d'apprendre des représentations riches et généralisables qui peuvent être transférées à diverses tâches en aval.
- Il a révolutionné le traitement du langage naturel et gagne en importance dans la vision par ordinateur et d'autres domaines.
- Les modèles auto-supervisés atteignent souvent 70-90% des performances des modèles supervisés tout en utilisant une fraction des données annotées.

## Détails

L'[apprentissage auto-supervisé](https://fr.wikipedia.org/wiki/Apprentissage_autosupervis%C3%A9) fonctionne en transformant un problème non supervisé en un problème supervisé par la création de tâches prétextes. Ces tâches sont conçues pour forcer le modèle à comprendre la structure sous-jacente des données.

### Tâches prétextes courantes

#### En traitement du langage naturel ([NLP](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel)):
- Prédiction de mots masqués (comme dans [BERT](https://fr.wikipedia.org/wiki/BERT_(mod%C3%A8le_de_langage)))
- Prédiction du mot suivant dans une séquence (comme dans GPT)
- Reconstruction de phrases dont l'ordre des mots a été perturbé
- Détermination si deux phrases se suivent naturellement (NSP - Next Sentence Prediction)
- Prédiction de contexte (comme dans [Word2Vec](https://fr.wikipedia.org/wiki/Word2vec))

#### En vision par ordinateur ([Computer Vision](https://fr.wikipedia.org/wiki/Vision_par_ordinateur)):
- Prédiction de la partie manquante d'une image (approche MAE - Masked Autoencoder)
- Colorisation d'images en noir et blanc
- Prédiction de la rotation appliquée à une image
- Assemblage de parties d'images comme un puzzle (Jigsaw Puzzles)
- Prédiction de profondeur à partir d'images monoculaires

### Processus en deux phases

1. **Pré-entraînement**: Le modèle apprend des représentations générales à partir de grandes quantités de données non étiquetées via des tâches prétextes.
2. **Fine-tuning**: Le modèle pré-entraîné est ensuite affiné sur une tâche spécifique avec une quantité relativement petite de données étiquetées.

### Applications avancées

Les applications s'étendent désormais au-delà du NLP et de la [vision par ordinateur](https://fr.wikipedia.org/wiki/Vision_par_ordinateur), touchant des domaines comme:
- **Audio**: avec des modèles comme Wav2Vec pour la [reconnaissance vocale](https://fr.wikipedia.org/wiki/Reconnaissance_automatique_de_la_parole)
- **Robotique**: pour l'apprentissage par imitation et la manipulation d'objets
- **Séries temporelles**: prédiction et classification
- **Approches multimodales**: combinant différents types de données (texte, image, son)

### Références

[1] https://fr.wikipedia.org/wiki/Apprentissage_automatique#Apprentissage_auto-supervis%C3%A9  
[2] Source additionnelle citant les limites du transfert learning en auto-supervisé