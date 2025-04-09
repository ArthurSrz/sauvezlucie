---
title: Principes de la théorie de l'information
type: concept
tags:
- théorie de l'information
- Claude Shannon
- entropie
- communication
- mathématiques appliquées
- informatique théorique
- quantification de l'information
date_creation: '2025-04-04'
date_modification: '2025-04-04'
subClassOf: '[[Apprentissage automatique (Machine Learning)]]'
---
## Généralité

La théorie de l'information est une branche des mathématiques appliquées et de l'informatique qui étudie la quantification, le stockage et la communication de l'information. Fondée par Claude Shannon en 1948, elle fournit des outils pour mesurer l'information et analyser les systèmes de communication.

## Points clés

- **Entropie** : Mesure de l'incertitude ou de la quantité d'information contenue dans une source de données.
- **Capacité du canal** : Débit maximal d'information qu'un canal de communication peut transmettre sans erreur.
- **Codage** : Techniques pour représenter l'information de manière efficace et résistante aux erreurs.

## Détails

### Entropie
L'entropie, notée H(X), est une mesure fondamentale en théorie de l'information. Elle quantifie l'incertitude associée à une variable aléatoire X. Plus l'entropie est élevée, plus l'incertitude est grande. Par exemple, une pièce de monnaie équilibrée a une entropie maximale (1 bit), car le résultat est totalement imprévisible.

### Capacité du canal
La capacité d'un canal de communication est le débit maximal auquel l'information peut être transmise avec une probabilité d'erreur arbitrairement faible. Elle dépend des caractéristiques physiques du canal, comme la bande passante et le rapport signal/bruit. Le théorème de Shannon-Hartley donne la capacité C d'un canal gaussien :  
\[ C = B \log_2(1 + \frac{S}{N}) \]  
où B est la bande passante, S la puissance du signal et N la puissance du bruit.

### Codage
Le codage vise à optimiser la transmission et le stockage de l'information. Il existe deux types principaux :
1. **Codage source** : Réduit la redondance pour compresser les données (ex. Huffman, Lempel-Ziv).
2. **Codage canal** : Ajoute de la redondance pour détecter et corriger les erreurs (ex. codes de Hamming, codes convolutifs).

## Applications

La théorie de l'information a des applications dans de nombreux domaines :
- **Télécommunications** : Optimisation des réseaux et des protocoles.
- **Cryptographie** : Sécurisation des données.
- **Neuroscience** : Analyse des signaux neuronaux.
- **Apprentissage automatique** : Mesure de l'information mutuelle entre variables.