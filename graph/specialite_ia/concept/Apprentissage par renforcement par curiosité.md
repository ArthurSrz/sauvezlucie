---
title: Apprentissage par renforcement par curiosité
type: concept
tags:
- IA
- Apprentissage par renforcement
- Curiosité intrinsèque
- Exploration
- Intelligence artificielle
date_creation: '2025-03-30'
date_modification: '2025-03-30'
subClassOf: '[[Apprentissage par renforcement]]'
relatedTo: '[[Exploration vs exploitation dans l''apprentissage par renforcement]]'
---
## Généralité

L'[apprentissage par renforcement](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement) par curiosité est une approche en [intelligence artificielle](https://fr.wikipedia.org/wiki/Intelligence_artificielle) qui vise à encourager les agents à explorer leur environnement de manière proactive en récompensant leur comportement exploratoire. Cette méthode s'inspire du concept de curiosité intrinsèque chez les êtres humains et les animaux, où l'exploration de l'inconnu est motivée par le désir de comprendre et de maîtriser l'environnement.

## Points clés

- **Curiosité intrinsèque** : Les agents sont motivés à explorer leur environnement par un intérêt intrinsèque, indépendamment des récompenses externes, inspiré des mécanismes d'[apprentissage](https://fr.wikipedia.org/wiki/Apprentissage) humains.
- **Exploration proactive** : L'exploration est encouragée de manière proactive, permettant aux agents de découvrir de nouvelles stratégies et de s'adapter plus rapidement.
- **Récompenses intrinsèques** : Les agents reçoivent des récompenses basées sur la nouveauté ou la complexité de leurs expériences, ce qui stimule leur curiosité.
- **Apprentissage autonome** : Cette approche permet aux agents d'apprendre de manière plus efficace et autonome, en atténuant les problèmes d'over-exploitation.
- **Applications variées** : Trouve des applications dans les jeux vidéo, la robotique et la recherche scientifique.

## Détails

### Fondements théoriques

Selon les recherches en [psychologie cognitive](https://fr.wikipedia.org/wiki/Psychologie_cognitive), la curiosité intrinsèque joue un rôle important dans l'apprentissage humain, étant associée à des mécanismes neurologiques impliquant notamment le [système dopaminergique](https://fr.wikipedia.org/wiki/Syst%C3%A8me_dopaminergic). En IA, cette approche se matérialise souvent par des "récompenses intrinsèques" calculées en fonction de la nouveauté perçue des états de l'environnement.

### Mécanismes d'implémentation

Des algorithmes comme ICM (Intrinsic Curiosity Module) ou RND (Random Network Distillation) permettent d'implémenter cette curiosité artificielle (source Wikipédia: "Reinforcement learning"). Ils créent des modèles internes de prédiction que l'agent cherche continuellement à améliorer, générant ainsi une motivation pour explorer.

1. **Prédiction d'Erreurs** : Récompense basée sur l'erreur de prédiction entre l'état actuel et l'état prédit.
2. **Nouveauté** : Récompense pour visiter des états jamais rencontrés auparavant.
3. **Complexité** : Récompense pour l'acquisition de connaissances complexes ou l'identification de patterns non triviaux.

### Avantages

- **Apprentissage plus rapide** : Démonstration dans des environnements complexes comme Montezuma's Revenge.
- **Adaptabilité** : Capacité accrue à s'adapter à des environnements dynamiques.
- **Créativité** : Production de solutions innovantes et inattendues.

### Défis

- **Équilibre exploration-exploitation** : Nécessité de trouver le bon équilibre.
- **Surapprentissage** : Risque de surapprentissage des comportements exploratoires.
- **Complexité algorithmique** : Augmentation des ressources computationnelles nécessaires.

### Applications

- **Jeux** : Amélioration des performances dans des jeux complexes (Go, Atari).
- **Robotique** : Développement de robots autonomes explorateurs.
- **Recherche scientifique** : Aide à la découverte de nouvelles connaissances.

### Conclusion

L'apprentissage par renforcement par curiosité est une approche prometteuse qui permet aux agents d'apprendre de manière plus autonome et efficace, en stimulant leur désir d'explorer et de comprendre leur environnement, un principe profondément enraciné dans l'apprentissage biologique.