import json
import re
import os
from openai import OpenAI

class LLMService:
    """Service pour l'interaction avec le modèle de langage."""
    
    def __init__(self, api_key=None, base_url=None, model=None, temperature=0.3):
        """
        Initialise le service LLM.
        
        Args:
            api_key (str, optional): Clé API pour le service LLM.
            base_url (str, optional): URL de base pour le service LLM.
            model (str, optional): Nom du modèle à utiliser.
            temperature (float): Paramètre de température pour la génération.
        """
        self.api_key = api_key or os.getenv("LLM_API_KEY", "EMPTY")
        self.base_url = base_url or os.getenv("LLM_BASE_URL", "http://localhost:8000/v1")
        self.model = model or os.getenv("LLM_MODEL", "Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4")
        self.temperature = temperature
        self.client = None
        
        # Prompts pour différents cas d'utilisation
        self.tag_generation_prompt = """Tu es un expert en catégorisation. 
Parmi la liste de tags existants suivante, sélectionne 3 à 10 tags qui sont les plus pertinents pour la requête de l'utilisateur.
Ces tags doivent représenter les concepts clés, entités et sujets de la requête.
Sélectionne uniquement des tags de la liste fournie, ne crée pas de nouveaux tags.

Tags disponibles: {tags}

Réponds UNIQUEMENT avec un tableau JSON de chaînes: ["tag1", "tag2", "tag3"]"""
        
        self.qa_system_prompt = """Tu es un assistant de recherche qui aide à répondre aux questions en te basant sur les documents fournis.
Tu peux citer des extraits pertinents des documents pour justifier tes réponses.
Si l'information demandée ne figure pas dans les documents, indique-le clairement. Tu es pédagogique et tu arrives facilement a vulgariser quand il le faut."""
        
        self.qa_user_prompt_template = """Voici ma question: {query}

Utilise les documents suivants pour y répondre:

{context}"""
    
    def get_client(self):
        """
        Initialise et retourne un client LLM.
        
        Returns:
            OpenAI: Client LLM initialisé.
        """
        if self.client is None:
            try:
                self.client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.base_url,
                )
            except Exception as e:
                print(f"Erreur lors de l'initialisation du client LLM: {e}")
                return None
        
        return self.client
    
    def generate_tags_for_query(self, query, existing_tags, max_tags=200):
        """
        Génère des tags pour une requête en utilisant un LLM.
        
        Args:
            query (str): Requête utilisateur.
            existing_tags (list): Liste des tags existants.
            max_tags (int): Nombre maximum de tags à considérer.
            
        Returns:
            list: Tags générés pour la requête.
        """
        client = self.get_client()
        if client is None:
            return []
        
        # Limiter le nombre de tags si la liste est très longue
        tags_to_show = existing_tags[:max_tags] if len(existing_tags) > max_tags else existing_tags
        
        system_prompt = self.tag_generation_prompt.format(tags=', '.join(tags_to_show))
        
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query},
                ],
                temperature=self.temperature,
                max_tokens=150
            )
            
            content = response.choices[0].message.content.strip()
            content = re.sub(r'^```json\s*', '', content)
            content = re.sub(r'\s*```$', '', content)
            
            # Vérifier que le contenu a bien la structure d'un tableau JSON
            if not (content.startswith('[') and content.endswith(']')):
                content = f"[{content}]"
            
            try:
                tags = json.loads(content)
                # Vérifier que tous les tags sélectionnés font partie des tags existants
                valid_tags = [tag for tag in tags if tag in existing_tags]
                return valid_tags
            except:
                # En cas d'erreur de parsing, faire un parsing simple
                tags = content.replace('[', '').replace(']', '').replace('"', '').split(',')
                tags = [tag.strip() for tag in tags if tag.strip() in existing_tags]
                return tags
                
        except Exception as e:
            print(f"Erreur lors de la génération des tags: {e}")
            return []
    
    def generate_answer(self, query, context_docs, max_tokens=1600):
        """
        Génère une réponse à une question basée sur des documents contextuels.
        
        Args:
            query (str): Question de l'utilisateur.
            context_docs (list): Liste de documents contextuels.
            max_tokens (int): Nombre maximum de tokens pour la réponse.
            
        Returns:
            str: Réponse générée.
        """
        client = self.get_client()
        if client is None:
            return "Impossible de se connecter au service LLM."
        
        try:
            # Préparer le contexte
            context_text = "\n\n".join([
                f"# {doc['title']}\n{doc['content']}" 
                for doc in context_docs
            ])
            
            # Créer le prompt
            user_prompt = self.qa_user_prompt_template.format(
                query=query,
                context=context_text
            )
            
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.qa_system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=self.temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Erreur lors de la génération de la réponse: {e}"
    
    def suggest_metadata(self, content, existing_types=None, existing_tags=None):
        """
        Suggère des métadonnées (titre, type, tags) pour un contenu donné.
        
        Args:
            content (str): Contenu Markdown à analyser.
            existing_types (list, optional): Types existants.
            existing_tags (list, optional): Tags existants.
            
        Returns:
            dict: Métadonnées suggérées.
        """
        client = self.get_client()
        if client is None:
            return {"title": "", "type": "", "tags": []}
        
        system_prompt = """Tu es un expert en organisation de connaissances.
Analyse le contenu fourni et suggère des métadonnées pertinentes.
Réponds au format JSON uniquement avec la structure suivante :
{
  "title": "Un titre court et descriptif",
  "type": "Le type de document",
  "tags": ["tag1", "tag2", "tag3", "..."]
}"""
        
        if existing_types or existing_tags:
            system_prompt += "\n\nUtilise de préférence les types et tags existants suivants :\n"
            if existing_types:
                system_prompt += f"Types existants : {', '.join(existing_types)}\n"
            if existing_tags:
                system_prompt += f"Tags existants (utilise-en 3 à 7) : {', '.join(existing_tags[:100])}"
        
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": content},
                ],
                temperature=0.3,
                max_tokens=300
            )
            
            content = response.choices[0].message.content.strip()
            content = re.sub(r'^```json\s*', '', content)
            content = re.sub(r'\s*```$', '', content)
            
            try:
                metadata = json.loads(content)
                return {
                    "title": metadata.get("title", ""),
                    "type": metadata.get("type", ""),
                    "tags": metadata.get("tags", [])
                }
            except:
                return {"title": "", "type": "", "tags": []}
                
        except Exception as e:
            print(f"Erreur lors de la suggestion de métadonnées: {e}")
            return {"title": "", "type": "", "tags": []}