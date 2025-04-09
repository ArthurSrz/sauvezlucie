---
title: Synthèse vocale (TTS)
type: concept
tags:
- synthèse vocale
- TTS
- text-to-speech
- technologie vocale
- accessibilité
- IA
- traitement du langage
- assistants vocaux
date_creation: '2025-04-04'
date_modification: '2025-04-04'
seeAlso: '[[Identification du locuteur]]'
relatedTo: '[[Reconnaissance automatique de la parole (ASR)]]'
isPartOf:
- '[[Traitement du langage naturel (NLP)]]'
- '[[Agents conversationnels et chatbots]]'
---
## Généralité

La [synthèse vocale](https://fr.wikipedia.org/wiki/Synth%C3%A8se_vocale) (TTS - Text-To-Speech) est une technologie qui convertit du texte écrit en parole artificielle. Elle permet aux machines de "lire" un texte à haute voix avec une voix synthétisée, offrant ainsi une interface vocale pour diverses applications. 

Cette technologie repose sur plusieurs techniques de [traitement du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel) et de synthèse sonore. Historiquement, les premiers systèmes remontent aux années 1930 avec le Voder de Bell Labs, mais les versions réellement utilisables sont apparues dans les années 1970-1980.

## Points clés

- **Conversion de texte en parole** : Utilisation de méthodes avancées comme la synthèse par concaténation et la synthèse paramétrique, avec des systèmes modernes basés sur des [réseaux de neurones profonds](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_profonds)
- **Applications variées** : Assistants vocaux (Siri, Alexa), systèmes de navigation GPS, logiciels pour [personnes malvoyantes](https://fr.wikipedia.org/wiki/Malvoyance), et applications médicales
- **Critères de qualité** : Naturalité (ressemblance humaine), intelligibilité (facilité de compréhension) et expressivité (transmission d'émotions)
- **Support multilingue** : Disponible pour de nombreuses langues, avec des performances variables selon les systèmes
- **Technologies émergentes** : Voix neuronales ultra-réalistes, contrôle des émotions, personnalisation vocale et synthèse en temps réel

## Détails

### Fonctionnement technique

La [synthèse vocale](https://fr.wikipedia.org/wiki/Synth%C3%A8se_vocale) fonctionne en plusieurs étapes :
1. Analyse du texte (normalisation des nombres et abréviations)
2. Traitement linguistique (étiquetage morphosyntaxique, analyse prosodique)
3. Génération de la parole (par modèles acoustiques ou concaténation)
4. Sortie audio

Les systèmes modernes comme [WaveNet](https://fr.wikipedia.org/wiki/WaveNet) utilisent des architectures avancées (RNN, Transformers) pour générer directement des formes d'onde, produisant des voix plus naturelles avec une latence réduite.

### Technologies émergentes

- **[Voix neuronales](https://fr.wikipedia.org/wiki/Synth%C3%A8se_vocale) ultra-réalistes** : Systèmes comme [WaveNet](https://fr.wikipedia.org/wiki/WaveNet) (DeepMind) réduisant l'effet de "vallée dérangeante"
- **Contrôle des émotions** : Modèles capables d'exprimer diverses émotions avec différents degrés d'intensité
- **Synthèse en temps réel** : Architectures comme FastSpeech permettant des latences inférieures à 300ms
- **Personnalisation vocale** : Transfert de style vocal à partir d'échantillons réduits
- **Nouvelles fonctionnalités** :
  - Modèles multilingues changeant de langue tout en conservant l'identité vocale
  - Synthèse de voix chantées
  - Génération adaptative au contexte
  - Intégration de pauses naturelles

### Défis persistants

- **Reproduction de l'intonation humaine** : Difficulté avec les nuances prosodiques subtiles ([prosodie](https://fr.wikipedia.org/wiki/Prosodie_(linguistique)))
- **Mots ambigus et langues complexes** : Problèmes avec les homographes et langues à tons
- **Besoins en puissance de calcul** : Voix haute qualité nécessitant des ressources importantes
- **Questions éthiques** :
  - Usages frauduleux ([deepfakes vocaux](https://fr.wikipedia.org/wiki/Deepfake))
  - Droits des donneurs de voix
  - Biais dans les modèles
  - Impact sur les professions vocales
  - Collecte de données personnelles