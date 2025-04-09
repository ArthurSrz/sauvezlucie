---
title: Calibration et incertitude des modèles
type: concept
tags:
- modélisation
- calibration
- incertitude
- analyse scientifique
- fiabilité des modèles
- méthodologie
- validation
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo: '[[Optimiseurs adaptatifs]]'
uses:
- '[[Inférence bayésienne]]'
- '[[Méthodes de clustering]]'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
link:
- '[[Méthodes d''évaluation des modèles]]'
- '[[Explicabilité et interprétabilité des modèles d''IA]]'
---
## Généralité

La [calibration](https://fr.wikipedia.org/wiki/Étalonnage) et l'[incertitude](https://fr.wikipedia.org/wiki/Incertitude) des modèles sont des aspects essentiels de la modélisation scientifique et technique. Ces concepts jouent un rôle crucial dans divers domaines comme l'[ingénierie](https://fr.wikipedia.org/wiki/Ingénierie), la météorologie, l'économie et les sciences environnementales.

## Points clés

- **Calibration** : Processus d'ajustement des paramètres d'un modèle pour minimiser l'écart entre les prédictions et les observations ([méthode des moindres carrés](https://fr.wikipedia.org/wiki/Méthode_des_moindres_carrés), analyse bayésienne)
- **Incertitude** : Mesure des erreurs potentielles ou de la variabilité des résultats d'un modèle (intervalles de confiance, distributions de probabilité)
- **Validation** : Vérification que le modèle fonctionne correctement sur des données indépendantes ([Validation informatique](https://fr.wikipedia.org/wiki/Validation_(informatique)))
- **Sources d'incertitude** : Erreurs de mesure, paramètres mal connus, approximations mathématiques, variabilité naturelle
- **Domaines d'application** : Hydrologie, finance, médecine, météorologie, ingénierie

## Détails

La calibration est une étape critique pour s'assurer qu'un modèle reproduit fidèlement les phénomènes étudiés. Elle implique souvent des méthodes d'optimisation comme les [moindres carrés](https://fr.wikipedia.org/wiki/Méthode_des_moindres_carrés), l'[analyse bayésienne](https://fr.wikipedia.org/wiki/Inférence_bayésienne) ou des algorithmes plus avancés. Dans les [modèles climatiques](https://fr.wikipedia.org/wiki/Modèle_climatique), cela peut concerner l'ajustement des coefficients de transfert de chaleur, tandis qu'en météorologie, cela implique le recalibrage constant des modèles numériques de prévision.

L'incertitude est inhérente à tout processus de modélisation et se manifeste sous plusieurs formes : paramétrique (valeurs imprécises des paramètres), structurelle (simplifications ou hypothèses du modèle) et des données (erreurs de mesure ou manque de données). Elle peut être quantifiée à travers des méthodes comme les [Méthodes de Monte Carlo](https://fr.wikipedia.org/wiki/Méthode_de_Monte-Carlo), les analyses de sensibilité ou selon la norme ISO/IEC Guide 98-3:2008 pour l'incertitude de mesure.

Les applications varient selon les domaines :
- **Hydrologie** : Calibration des modèles de prévision des crues avec [algorithmes d'optimisation](https://fr.wikipedia.org/wiki/Optimisation_(mathématiques)) et incertitudes liées à la variabilité spatiale des précipitations
- **Finance** : Calibration des modèles comme [Black-Scholes](https://fr.wikipedia.org/wiki/Modèle_Black-Scholes) et incertitudes sur la volatilité implicite
- **Médecine** : Calibration des modèles [pharmacocinétiques](https://fr.wikipedia.org/wiki/Pharmacocinétique) avec incertitudes liées aux variations interindividuelles
- **Météorologie** : Calibration constante via assimilation de données avec incertitudes quantifiées par ensembles de prévisions
- **Ingénierie** : Calibration cruciale des modèles [éléments finis](https://fr.wikipedia.org/wiki/Méthode_des_éléments_finis) en crash-tests avec incertitudes sur les propriétés des matériaux

Pour réduire l'incertitude, plusieurs approches existent : collecte de données supplémentaires, amélioration de la structure du modèle, utilisation de méthodes bayésiennes ([Inférence bayésienne](https://fr.wikipedia.org/wiki/Inférence_bayésienne)), analyse multi-modèles (approche du [GIEC](https://fr.wikipedia.org/wiki/Groupe_d'experts_intergouvernemental_sur_l'évolution_du_climat)) et assimilation de données.