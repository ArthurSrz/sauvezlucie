---
title: Modèles de diffusion
type: concept
tags:
- modèles de diffusion
- apprentissage automatique
- génération d'images
- IA générative
- Stable Diffusion
- DALL-E
- deep learning
date_creation: '2025-04-08'
date_modification: '2025-04-08'
subClassOf: '[[Apprentissage profond (Deep Learning)]]'
relatedTo: '[[Réseaux génératifs pour la synthèse et manipulation d''images (au-delà
  des GANs)]]'
---
## Généralité

Les [modèles de diffusion](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_diffusion) sont une classe de modèles génératifs en [apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) qui permettent de générer des données complexes (images, sons, textes) en apprenant progressivement à supprimer du bruit ajouté à des données d'entrée. Inspirés des processus thermodynamiques, ces modèles s'appuient sur des fondements théoriques en [physique statistique](https://fr.wikipedia.org/wiki/Physique_statistique) et en [équations différentielles stochastiques](https://fr.wikipedia.org/wiki/%C3%89quation_diff%C3%A9rentielle_stochastique).

## Points clés

- **Processus itératif** : Fonctionnent en deux phases - bruitage progressif (forward process) et débruitage appris (reverse process)
- **Flexibilité** : Peuvent générer des données conditionnées (par texte, image) ou non conditionnées
- **Qualité élevée** : Capables de produire des résultats très réalistes avec des résolutions atteignant 2048x2048 pixels
- **Applications variées** : De la création artistique à la recherche médicale en passant par le design industriel
- **Efficacité améliorée** : Les versions récentes utilisent des espaces latents pour réduire la complexité computationnelle

## Détails

Les modèles de diffusion fonctionnent selon un processus en deux étapes. Le **Forward Process (Bruitage)** consiste à altérer progressivement une image par l'ajout de bruit gaussien sur plusieurs étapes (généralement 1000 pas), suivant une [chaîne de Markov](https://fr.wikipedia.org/wiki/Cha%C3%AEne_de_Markov). Le **Reverse Process (Débruitage)** utilise un réseau de neurones (souvent une architecture U-Net améliorée) entraîné à prédire et retirer le bruit à chaque étape.

Ces modèles présentent plusieurs avantages notables. Ils offrent une grande **stabilité** en évitant les problèmes de mode collapse grâce à leur processus d'entraînement déterministe. Ils permettent un **contrôle fin** de la génération via des prompts textuels (comme dans [Stable Diffusion](https://fr.wikipedia.org/wiki/Stable_Diffusion)) et sont **évolutifs**, avec des performances qui s'améliorent avec l'augmentation des données et de la puissance de calcul. La qualité des résultats est souvent supérieure, avec des scores FID (Frechet Inception Distance) plus bas que les GANs dans certains domaines.

Cependant, certaines limitations existent. Le **coût computationnel** est élevé, avec un processus itératif qui peut être lent (plusieurs minutes par image en haute résolution). La **complexité** des modèles nécessite un réglage minutieux des hyperparamètres et une grande quantité de données. On note également une **latence** dans le temps de génération plus longue que pour d'autres approches, ainsi qu'une importante **consommation énergétique** lors de l'entraînement à grande échelle.

Les applications des modèles de diffusion couvrent de nombreux domaines. Dans l'**art et design**, ils permettent la création d'illustrations et logos via [Stable Diffusion](https://fr.wikipedia.org/wiki/Stable_Diffusion) et [MidJourney](https://fr.wikipedia.org/wiki/Midjourney). En **photographie**, ils améliorent ou restaurent des images avec des outils comme [DALL-E 2](https://fr.wikipedia.org/wiki/DALL-E). La **recherche médicale** les utilise pour générer des images synthétiques destinées à l'entraînement de modèles diagnostiques. L'industrie du **jeu vidéo** y recourt pour concevoir textures ou environnements virtuels avec des outils comme [NVIDIA's Canvas](https://fr.wikipedia.org/wiki/Nvidia), tandis que la **mode et le design industriel** les exploitent pour générer motifs textiles et prototypes produits.

Parmi les variantes notables, on trouve [Stable Diffusion](https://fr.wikipedia.org/wiki/Stable_Diffusion), un modèle open-source optimisé pour matériel grand public ; [DALL-E](https://fr.wikipedia.org/wiki/DALL-E), système développé par [OpenAI](https://fr.wikipedia.org/wiki/OpenAI) avec résolution 1024x1024 pixels ; Imagen, modèle de Google Research utilisant une cascade de diffusion ; MidJourney, modèle propriétaire accessible via Discord ; et les Latent Diffusion Models (LDM), architecture développée par CompVis réduisant les besoins computationnels.