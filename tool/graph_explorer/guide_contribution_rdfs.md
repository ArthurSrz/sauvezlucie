---
title: "Titre du document"
type: "concept/technique/application/acteur/etc."
tags: ["tag1", "tag2"]
relations:
  # La relation "partie-de" est exprimée par rdfs:subClassOf
  - type: "rdfs:subClassOf"
    target: "[[Document parent]]"
  # La relation "voir-aussi" est exprimée par rdfs:seeAlso
  - type: "rdfs:seeAlso"
    target: ["[[Document connexe 1]]", "[[Document connexe 2]]"]
date_creation: "YYYY-MM-DD"
date_modification: "YYYY-MM-DD"
---

![Thumbnail Image](url_de_l_image)

## Généralité

Brève description ou définition du sujet.

## Points clés

- Point important 1
- Point important 2
- Point important 3

## Détails

Contenu détaillé sur le sujet...

## Liens complémentaires

### [[Lien interne 1]]
### [[Lien interne 2]]
### [Lien externe](url)

---

### Note explicative sur le marquage RDFS et les liens externes

Pour uniformiser l'organisation des connaissances dans ce projet, nous utilisons exclusivement le marquage RDFS. Voici comment interpréter et contribuer aux documents :

- **Relations internes :**  
  - **rdfs:subClassOf** (utilisée dans le champ *relations* avec le type "partie-de") indique une relation hiérarchique.  
    *Exemple :* Un document sur les réseaux de neurones peut être considéré comme une sous-catégorie d'un document plus général sur l'intelligence artificielle.
  
  - **rdfs:seeAlso** (utilisée dans le champ *relations* avec le type "voir-aussi") est employée pour référencer des documents connexes ou complémentaires qui apportent des informations supplémentaires.

- **Liaison vers des sources externes :**  
  Pour enrichir vos documents et créer des liens vers des référentiels de qualité (comme Wikipedia ou Wikidata), utilisez également **rdfs:seeAlso**.  
  *Exemple en Turtle :*
  ```turtle
  @prefix ex: <http://example.com/> .
  @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

  ex:DocumentExemple a ex:Document ;
      rdfs:label "Exemple de Document" ;
      rdfs:seeAlso <https://fr.wikipedia.org/wiki/Exemple> ;
      rdfs:seeAlso <https://www.wikidata.org/entity/QXXXXXX> .
