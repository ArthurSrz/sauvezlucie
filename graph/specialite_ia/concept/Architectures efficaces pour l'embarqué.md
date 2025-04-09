---
title: Architectures efficaces pour l'embarqué
type: concept
tags:
- systèmes embarqués
- architecture matérielle
- optimisation
- temps réel
- faible consommation
- CPU
- mémoire
- IoT
date_creation: '2025-04-08'
date_modification: '2025-04-08'
relatedTo:
- '[[Optimisation de ressources en IA embarquée]]'
- '[[Architectures matérielles dédiées à l''IA (TPU, NPU)]]'
depends: '[[Fondamentaux de la robotique intelligente]]'
isPartOf: '[[Optimisation de ressources en IA embarquée]]'
---
## Généralité

Les architectures efficaces pour l'embarqué désignent les modèles de conception et d'organisation matérielle/logicielle optimisés pour les [systèmes embarqués](https://fr.wikipedia.org/wiki/Syst%C3%A8me_embarqu%C3%A9). Ces systèmes représentent environ 98% des processeurs fabriqués dans le monde et se trouvent dans des applications diverses comme les dispositifs médicaux, les systèmes automobiles ou les appareils domestiques intelligents. Ces architectures visent à concilier performance, faible consommation énergétique, fiabilité et contraintes de coût.

## Points clés

- **Optimisation des ressources** : Utilisation efficace du [CPU](https://fr.wikipedia.org/wiki/Processeur), [mémoire](https://fr.wikipedia.org/wiki/M%C3%A9moire_informatique) et périphériques pour minimiser la consommation et les coûts
- **Modularité** : Conception modulaire pour faciliter la maintenance et l'évolutivité, notamment avec des standards comme [AUTOSAR](https://fr.wikipedia.org/wiki/AUTOSAR)
- **Temps réel** : Prise en compte des contraintes temporelles strictes pour les applications critiques
- **Sécurité et fiabilité** : Intégration de mécanismes avancés comme le lockstep processing ou les architectures Triple Modular Redundant
- **Gestion de l'énergie** : Techniques avancées comme le [Dynamic Voltage and Frequency Scaling](https://fr.wikipedia.org/wiki/Dynamic_voltage_scaling) et les modes veille profonde

## Détails

### Choix du matériel

- **Microcontrôleurs vs Microprocesseurs** : Les microcontrôleurs [ARM Cortex-M](https://fr.wikipedia.org/wiki/ARM_Cortex-M) dominent le marché avec d'excellentes efficacités énergétiques
- **SoC (System on Chip)** : Intégration de multiples composants sur une seule puce (ex: SoC Qualcomm Snapdragon)
- **FPGA et ASIC** : Utilisés pour des applications nécessitant une personnalisation matérielle poussée ([FPGA](https://fr.wikipedia.org/wiki/Circuit_logique_programmable) Xilinx et Intel)

### Systèmes d'exploitation embarqués

- **RTOS (Real-Time Operating System)** : FreeRTOS, [Zephyr](https://fr.wikipedia.org/wiki/Zephyr_(syst%C3%A8me_d%27exploitation))
- **Linux embarqué** : Adapté pour des systèmes complexes (Yocto, Buildroot)
- **Bare-metal** : Approche sans OS pour des applications ultra-légères

### Optimisation logicielle

- **Code minimaliste** : Normes [MISRA-C](https://fr.wikipedia.org/wiki/MISRA_C) et CERT-C
- **Gestion de la mémoire** : SLAB allocators, régions mémoire protégées (MPU)
- **Parallelisme** : [DSP](https://fr.wikipedia.org/wiki/Traitement_num%C3%A9rique_du_signal) pour le traitement du signal

### Architectures courantes

- **Monolithique** : Tout le code s'exécute dans un processus unique, idéal pour systèmes simples ([architecture monolithique](https://fr.wikipedia.org/wiki/Architecture_monolithique))
- **Hétérogène** : Combinaison de cœurs généralistes et spécialisés ([ARM](https://fr.wikipedia.org/wiki/Architecture_ARM) + DSP)
- **En clusters** : Plusieurs nœuds embarqués communiquant via un bus (CAN, Ethernet)
- **Edge Computing** : Traitement local des données pour réduire la latence ([Edge computing](https://fr.wikipedia.org/wiki/Edge_computing))

### Méthodologies de développement

- **[Prototypage rapide](https://fr.wikipedia.org/wiki/Prototypage_rapide)** : Utilisation de cartes comme [Raspberry Pi](https://fr.wikipedia.org/wiki/Raspberry_Pi) pour valider les concepts
- **[Profiling](https://fr.wikipedia.org/wiki/Profiling_(informatique))** : Mesure des performances pour identifier les goulots d'étranglement
- **Documentation** : Maintien d'une documentation précise avec outils comme [Doxygen](https://fr.wikipedia.org/wiki/Doxygen)