---
title: Identification du locuteur
type: concept
tags:
- traitement vocal
- reconnaissance vocale
- sécurité
- authentification
- biométrie
- IA
- traitement automatique
date_creation: '2025-04-08'
date_modification: '2025-04-08'
uses: '[[Algorithme de classification]]'
relatedTo:
- '[[Reconnaissance automatique de la parole (ASR)]]'
- '[[Détection d''émotions dans la voix]]'
subClassOf: '[[Synthèse vocale (TTS)]]'
---
## Généralité

L'[identification du locuteur](https://fr.wikipedia.org/wiki/Reconnaissance_du_locuteur) (aussi appelée reconnaissance du locuteur ou vérification du locuteur) est une technique de [traitement automatique de la parole](https://fr.wikipedia.org/wiki/Traitement_automatique_de_la_parole) visant à reconnaître ou vérifier l'identité d'une personne à partir de ses caractéristiques vocales uniques, telles que la fréquence fondamentale, le timbre, les formants et les caractéristiques comportementales comme le débit de parole. 

Cette technologie s'appuie sur des modèles [biométriques](https://fr.wikipedia.org/wiki/Biom%C3%A9trie) vocaux qui analysent de nombreux paramètres acoustiques pour créer une empreinte vocale unique.

## Points clés

- Utilise des caractéristiques vocales uniques comme les [fréquences fondamentales](https://fr.wikipedia.org/wiki/Fr%C3%A9quence_fondamentale) (typiquement 85-180 Hz pour les hommes, 165-255 Hz pour les femmes), le [timbre](https://fr.wikipedia.org/wiki/Timbre_(musique)), les formants et les modèles de parole
- Deux approches principales : reconnaissance (qui parle ?) et vérification (est-ce bien cette personne ?)
- Applications majeures : sécurité (contrôle d'accès), authentification (services bancaires), assistants vocaux et analyses judiciaires
- Technologies sous-jacentes : Modèles GMM-UBM traditionnels et réseaux de neurones profonds pour les systèmes modernes

## Détails

Les principales applications de l'identification du locuteur incluent :

- **Sécurité** : Déverrouillage vocal (avec des taux de succès dépassant 95% en environnement contrôlé), contrôle d'accès [biométrique](https://fr.wikipedia.org/wiki/Biom%C3%A9trie) dans les systèmes bancaires comme le [Voice ID d'HSBC](https://fr.wikipedia.org/wiki/HSBC)
- **Service client** : Authentification dans les centres d'appels avec des technologies comme VoiceGrid ou Batvox
- **Domotique** : Personnalisation des assistants vocaux ([Alexa](https://fr.wikipedia.org/wiki/Amazon_Alexa), [Google Assistant](https://fr.wikipedia.org/wiki/Google_Assistant)) avec reconnaissance multi-utilisateurs
- **Forensique** : Analyse d'enregistrements pour enquêtes judiciaires utilisant des techniques avancées comme les x-vectors

Les défis techniques rencontrés dans ce domaine comprennent :
- Variabilité due au [bruit ambiant](https://fr.wikipedia.org/wiki/Bruit_ambiant) ou aux changements émotionnels
- Tentatives de fraude (enregistrements vocaux, synthèse de voix via [deepfakes](https://fr.wikipedia.org/wiki/Deepfake))
- Problèmes éthiques liés à la vie privée et au consentement (cadre du [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es))

Les performances des systèmes sont évaluées selon plusieurs métriques :
- Taux de fausse acceptation (FAR) : Typiquement <1% pour les systèmes commerciaux
- Taux de faux rejet (FRR) : Souvent entre 5-10%
- Courbe DET (Detection Error Tradeoff) : Méthode standardisée ISO/IEC 19795-1

Les autres défis incluent les biais algorithmiques (performances dégradées pour certaines voix), la latence (temps de traitement) et la compatibilité multi-langues.