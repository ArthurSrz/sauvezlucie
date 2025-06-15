---
title: Apprentissage par renforcement
type: concept
tags:
- algorithmes
- environnement
- agent intelligent
- décision
- récompense
- intelligence artificielle
- apprentissage automatique
date_creation: '2025-04-08'
date_modification: '2025-04-09'
link:
- '[[Techniques de l''intelligence artificielle]]'
- '[[Exploration vs exploitation dans l''apprentissage par renforcement]]'
seeAlso:
- '[[Apprentissage par renforcement par démonstration]]'
- '[[Apprentissage par renforcement hiérarchique]]'
- '[[Apprentissage par renforcement inverse]]'
- '[[Apprentissage par renforcement profond]]'
---
## Généralité  

L'[apprentissage par renforcement](https://fr.wikipedia.org/wiki/Apprentissage_par_renforcement) (RL - Reinforcement Learning) est un paradigme d'[apprentissage automatique](https://fr.wikipedia.org/wiki/Apprentissage_automatique) où un agent apprend à prendre des décisions en interagissant avec un environnement. Contrairement à l'apprentissage supervisé, l'agent n'a pas accès à des exemples étiquetés, mais reçoit des récompenses ou des pénalités en fonction des actions qu'il entreprend. L'objectif de l'agent est de maximiser la somme des récompenses cumulées au fil du temps en développant une stratégie optimale (politique).  

Ce domaine trouve ses origines dans les travaux de [Richard Bellman](https://fr.wikipedia.org/wiki/Richard_Bellman) sur la programmation dynamique dans les années 1950, et a été popularisé par des succès récents comme AlphaGo de DeepMind. L'apprentissage par renforcement s'applique aujourd'hui à de nombreux domaines, notamment la robotique, les systèmes de recommandation et la finance algorithmique.

## Points clés  

- **Interaction agent-environnement** : Cadre [Markov Decision Process](https://fr.wikipedia.org/wiki/Processus_de_d%C3%A9cision_markovien) (MDP) où chaque état possède la propriété markovienne  
- **Objectif principal** : Maximiser les récompenses cumulées via une politique optimale, formalisé par la [Q-function](https://fr.wikipedia.org/wiki/Algorithme_Q-learning)  
- **Compromis fondamental** : Dilemme [exploration-exploitation](https://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)) illustré par le problème du bandit manchot  
- **Algorithmes majeurs** : Q-learning (méthode basée sur la valeur), SARSA (méthode sur politique), REINFORCE (méthode de politique par gradient)  
- **Applications principales** : Robotique (locomotion), jeux (AlphaGo), finance algorithmique, systèmes de recommandation  

## Détails  

L'apprentissage par renforcement repose sur plusieurs éléments essentiels : un [agent](https://fr.wikipedia.org/wiki/Agent_intelligent) prenant des décisions, un [environnement](https://fr.wikipedia.org/wiki/Environnement_(intelligence_artificielle)) d'interaction, des [états](https://fr.wikipedia.org/wiki/%C3%89tat_(informatique)) représentant la situation actuelle, des [actions](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_jeux) possibles, des signaux de [récompense](https://fr.wikipedia.org/wiki/Fonction_d%27utilit%C3%A9) guidant l'apprentissage et une [politique](https://fr.wikipedia.org/wiki/Politique_(apprentissage_automatique)) définissant la stratégie de décision.

Le cadre mathématique standard est le Processus de Décision Markovien (MDP) qui comprend un ensemble d'états, un ensemble d'actions, une fonction de transition, une fonction de récompense et un facteur d'actualisation.

Les algorithmes principaux se divisent en trois catégories :
1. **Méthodes basées sur la valeur** comme le [Q-learning](https://fr.wikipedia.org/wiki/Q-learning) (apprentissage hors politique) et SARSA (apprentissage sur politique)
2. **Méthodes basées sur la politique** comme REINFORCE (optimisation directe) et [Actor-Critic](https://fr.wikipedia.org/wiki/Actor-critic) (combinaison valeur-politique)
3. **Apprentissage par renforcement profond** avec [DQN](https://fr.wikipedia.org/wiki/Deep_Q-Network) (Q-learning avec réseaux profonds), [PPO](https://fr.wikipedia.org/wiki/Proximal_Policy_Optimization) (optimisation robuste) et [A3C](https://fr.wikipedia.org/wiki/Asynchronous_Advantage_Actor-Critic) (apprentissage asynchrone)

Les principaux défis incluent le [dilemme exploration-exploitation](https://fr.wikipedia.org/wiki/Dilemme_du_bandit_manchot), le problème d'attribution de crédit, la stabilité de l'apprentissage et l'efficacité des échantillons. Ce domaine continue d'évoluer avec des avancées majeures comme [AlphaGo](https://fr.wikipedia.org/wiki/AlphaGo) et [AlphaFold](https://fr.wikipedia.org/wiki/AlphaFold), démontrant son potentiel pour résoudre des problèmes complexes de prise de décision.