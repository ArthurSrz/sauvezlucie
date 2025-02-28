---
title: "Sécurité et robustesse en IA"
type: "enjeu"
tags: ["sécurité", "robustesse", "adversarial", "fiabilité", "résilience"]
relations:
  - type: "rdfs:subClassOf"
    target: "[[Les enjeux de l'intelligence artificielle]]"
  - type: "rdfs:seeAlso"
    target: ["[[Vie privée et protection des données]]", "[[Éthique et responsabilité]]", "[[Gouvernance et régulation]]"]
---

## Généralité

La sécurité et la robustesse en intelligence artificielle concernent la capacité des systèmes d'IA à fonctionner de manière fiable, prévisible et sécurisée face aux erreurs, aux attaques malveillantes et aux situations imprévues.

## Points clés

- Les systèmes d'IA présentent des vulnérabilités spécifiques comme la sensibilité aux exemples adversariaux
- La robustesse inclut la capacité à maintenir des performances cohérentes face à des données hors distribution
- Les applications critiques nécessitent des garanties formelles de sécurité et de fiabilité
- L'importance croissante de l'alignement des modèles d'IA avancés avec les intentions humaines

## Détails

À mesure que les systèmes d'intelligence artificielle s'intègrent dans des infrastructures critiques et des applications à haut risque, les questions de sécurité et de robustesse deviennent cruciales. Ces systèmes présentent des vulnérabilités uniques qui requièrent des approches spécifiques pour assurer leur fonctionnement sûr et fiable.

### Vulnérabilités spécifiques aux systèmes d'IA

Les modèles d'IA, particulièrement ceux basés sur l'apprentissage profond, sont sujets à plusieurs types de vulnérabilités:

1. **Exemples adversariaux**: Perturbations imperceptibles pour l'humain mais qui conduisent le modèle à des erreurs de classification significatives. Par exemple, l'ajout de pixels spécifiques peut amener un système de vision par ordinateur à confondre un panneau stop avec une limitation de vitesse.

2. **Empoisonnement des données**: Manipulation malveillante des données d'entraînement pour introduire des comportements indésirables ou des portes dérobées (backdoors) dans le modèle.

3. **Inversion de modèle**: Techniques permettant de reconstruire les données d'entraînement à partir du modèle, posant des risques pour la confidentialité.

4. **Transfert d'attaques**: Vulnérabilités découvertes sur un modèle qui peuvent être exploitées sur d'autres modèles similaires.

5. **Biais d'optimisation**: Tendance des systèmes à développer des stratégies imprévues pour optimiser leur fonction objective, parfois au détriment des intentions réelles.

### Dimensions de la robustesse

La robustesse d'un système d'IA comporte plusieurs facettes:

- **Robustesse distributionnelle**: Capacité à maintenir des performances acceptables lorsque les données d'entrée diffèrent des données d'entraînement.

- **Robustesse aux perturbations**: Résistance aux bruits et variations mineures dans les entrées.

- **Fiabilité de calibration**: Degré de confiance du modèle qui reflète correctement sa probabilité d'erreur.

- **Dégradation gracieuse**: En cas de défaillance, le système limite les conséquences négatives plutôt que d'échouer catastrophiquement.

- **Détection des anomalies**: Capacité à identifier les entrées inhabituelles ou potentiellement dangereuses.

### Méthodes et approches de sécurisation

Plusieurs stratégies sont développées pour renforcer la sécurité des systèmes d'IA:

1. **Entraînement robuste**: Inclusion d'exemples adversariaux dans les données d'entraînement pour immuniser le modèle.

2. **Distillation défensive**: Transfert des connaissances d'un modèle complexe vers un modèle plus simple et robuste.

3. **Vérification formelle**: Application de méthodes mathématiques pour prouver certaines propriétés de sécurité.

4. **Sandboxing et isolation**: Restriction des capacités d'action du système pour limiter les dommages potentiels.

5. **Mécanismes d'arrêt d'urgence**: Capacité à désactiver rapidement un système présentant un comportement anormal.

6. **Test de régression et red-teaming**: Évaluation systématique des vulnérabilités par des équipes spécialisées.

### Alignement et sécurité des systèmes avancés

Pour les systèmes d'IA avancés, le problème de l'alignement devient central:

- **Spécification des objectifs**: Comment définir précisément ce que nous voulons que le système accomplisse sans créer d'incitations perverses?

- **Robustesse des objectifs**: Comment s'assurer que le système maintient ses objectifs initiaux même s'il devient plus capable?

- **Interprétabilité**: Capacité à comprendre les raisons des décisions du système pour anticiper les comportements problématiques.

- **Surveillance humaine significative**: Concevoir des systèmes qui restent sous contrôle humain effectif malgré leur complexité.

Ces considérations deviennent particulièrement importantes à mesure que les systèmes d'IA gagnent en autonomie et sont déployés dans des contextes où leurs décisions peuvent avoir des impacts significatifs sur la sécurité et le bien-être humains.

## Liens complémentaires

### [[Attaques adversariales]]
### [[Vérification et validation des systèmes d'IA]]
### [[Alignement des systèmes d'IA]]
### [[Certification de sécurité]]
