---
title: Fuite de données (Data leakage)
type: concept
tags:
- sécurité informatique
- protection des données
- cybersécurité
- confidentialité
- fuite d'information
- RGPD
- menaces informatiques
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo: '[[Sécurité des systèmes IA en temps réel]]'
uses: '[[Préparation des données]]'
---
## Généralité

La [fuite de données](https://fr.wikipedia.org/wiki/Fuite_de_donn%C3%A9es) (data leakage) désigne la divulgation non intentionnelle ou non autorisée d'informations sensibles ou confidentielles en dehors d'un environnement sécurisé. Cela peut survenir à travers des erreurs humaines, des failles de sécurité ou des attaques malveillantes comme le [phishing](https://fr.wikipedia.org/wiki/Hame%C3%A7onnage) ou les [ransomware](https://fr.wikipedia.org/wiki/Ran%C3%A7ongiciel). Ces incidents représentent une menace majeure pour la confidentialité et la sécurité des données, avec des conséquences potentielles incluant des pertes financières, des atteintes à la réputation et des sanctions réglementaires.

## Points clés

- **Types de données exposées** : Données personnelles, informations financières, secrets industriels et [données médicales](https://fr.wikipedia.org/wiki/Donnée_de_santé)
- **Causes principales** : Erreurs humaines (20% des incidents), cyberattaques ([phishing](https://fr.wikipedia.org/wiki/Phishing), [ransomware](https://fr.wikipedia.org/wiki/Ransomware)), problèmes techniques (bases de données mal configurées)
- **Secteurs vulnérables** : Santé, finance et technologie sont les plus touchés
- **Réglementations clés** : [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es) en Europe (amendes jusqu'à 4% du CA), [CCPA](https://fr.wikipedia.org/wiki/California_Consumer_Privacy_Act) aux États-Unis
- **Mesures de prévention** : Chiffrement ([AES-256](https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard)), formation des employés, audits réguliers ([ISO 27001](https://fr.wikipedia.org/wiki/ISO/CEI_27001))

## Détails

Les fuites peuvent concerner divers types d'informations sensibles, notamment des données personnelles (noms, adresses, numéros de sécurité sociale), des informations financières (numéros de carte de crédit), des secrets industriels, des [données médicales](https://fr.wikipedia.org/wiki/Donnée_de_santé) (dossiers patients) et des identifiants de connexion (mots de passe).

Les principales causes incluent des erreurs humaines (envoi d'e-mails à de mauvais destinataires, partage accidentel de fichiers sensibles), des cyberattaques (piratage de systèmes, exploitation de vulnérabilités logicielles) et des problèmes techniques (configuration incorrecte des [bases de données](https://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es), serveurs non sécurisés).

Certains secteurs sont particulièrement vulnérables :
- **Santé** : Dossiers médicaux très recherchés (ex: hôpital de Dax 2021)
- **Finance** : Données sensibles sur les clients (ex: First American Financial 2019)
- **Technologie** : Vastes quantités de données utilisateurs (ex: [LinkedIn](https://fr.wikipedia.org/wiki/LinkedIn) 2021)

Pour prévenir ces incidents, plusieurs mesures sont essentielles :
- Chiffrement des données avec des algorithmes comme [AES-256](https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard)
- Formation des employés à la sensibilisation aux bonnes pratiques
- Audits réguliers selon le standard [ISO 27001](https://fr.wikipedia.org/wiki/ISO/CEI_27001)
- Mise en place de systèmes [SIEM](https://fr.wikipedia.org/wiki/Security_information_and_event_management)
- Élaboration d'un plan de réponse conforme au [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es)

L'impact réglementaire est significatif, avec des législations strictes comme le RGPD (notification sous 72 heures, amendes jusqu'à 20M€ ou 4% du CA) et le CCPA (amendes jusqu'à 7 500$ par violation intentionnelle). Des exemples marquants incluent les sanctions contre Google (50M€ par la [CNIL](https://fr.wikipedia.org/wiki/Commission_nationale_de_l%27informatique_et_des_libert%C3%A9s) en 2019), Equifax (575M$ en 2019) et Amazon (746M€ en 2021).

Parmi les fuites de données les plus notoires :
- **[Facebook-Cambridge Analytica](https://fr.wikipedia.org/wiki/Scandale_Facebook-Cambridge_Analytica)** (2018) : 87M utilisateurs
- **[Equifax](https://fr.wikipedia.org/wiki/Equifax)** (2017) : 147M consommateurs
- **[Marriott International](https://fr.wikipedia.org/wiki/Marriott_International)** (2018) : 500M clients