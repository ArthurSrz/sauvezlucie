import os
import yaml
import re
from pathlib import Path
import base64
import pandas as pd
import tempfile

class StorageService:
    """Service pour la gestion des fichiers et du stockage."""
    
    def __init__(self, cache_dir=None):
        """
        Initialise le service de stockage.
        
        Args:
            cache_dir (str, optional): Répertoire de cache. Si None, utilise un emplacement temporaire.
        """
        if cache_dir is None:
            self.cache_dir = os.path.join(tempfile.gettempdir(), "streamlit_graph_cache")
        else:
            self.cache_dir = cache_dir
        
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def parse_directory(self, directory):
        """
        Parse tous les fichiers Markdown d'un répertoire.
        
        Args:
            directory (str): Chemin du répertoire à analyser.
            
        Returns:
            list: Liste des fichiers analysés.
        """
        markdown_files = self.find_markdown_files(directory)
        parsed_files = []
        
        for file_path in markdown_files:
            parsed_file = self.parse_markdown_file(file_path)
            if parsed_file:
                parsed_files.append(parsed_file)
        
        return parsed_files
    
    def find_markdown_files(self, directory):
        """
        Trouve tous les fichiers Markdown dans un répertoire et ses sous-répertoires.
        
        Args:
            directory (str): Chemin du répertoire.
            
        Returns:
            list: Liste des chemins de fichiers Markdown.
        """
        markdown_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    markdown_files.append(os.path.join(root, file))
        return markdown_files
    
    def parse_markdown_file(self, file_path):
        """
        Parse un fichier Markdown et extrait ses métadonnées et liens.
        
        Args:
            file_path (str): Chemin du fichier Markdown.
            
        Returns:
            dict: Données extraites du fichier, ou None en cas d'erreur.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            metadata = self.extract_yaml_metadata(content)
            internal_links = self.extract_internal_links(content)
            
            # Extrait les relations définies dans les métadonnées YAML
            relations = []
            if 'relations' in metadata:
                for relation in metadata.get('relations', []):
                    if 'target' in relation:
                        if isinstance(relation['target'], list):
                            for target in relation['target']:
                                self._add_relation(relations, relation, target)
                        else:
                            self._add_relation(relations, relation, relation['target'])
            
            return {
                'path': file_path,
                'filename': os.path.basename(file_path),
                'title': metadata.get('title', os.path.basename(file_path).replace('.md', '')),
                'type': metadata.get('type', ''),
                'tags': metadata.get('tags', []),
                'relations': relations,
                'internal_links': internal_links,
                'content': content
            }
        except Exception as e:
            print(f"Erreur lors de l'analyse du fichier {file_path}: {e}")
            return None
    
    def _add_relation(self, relations, relation, target):
        """Ajoute une relation à la liste des relations."""
        if isinstance(target, str) and target.startswith('[[') and target.endswith(']]'):
            relations.append((relation.get('type', 'link'), target[2:-2]))
    
    def extract_yaml_metadata(self, content):
        """
        Extrait les métadonnées YAML d'un fichier Markdown.
        
        Args:
            content (str): Contenu du fichier Markdown.
            
        Returns:
            dict: Métadonnées extraites.
        """
        yaml_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
        match = yaml_pattern.search(content)
        if match:
            yaml_content = match.group(1)
            try:
                return yaml.safe_load(yaml_content)
            except yaml.YAMLError:
                return {}
        return {}
    
    def extract_internal_links(self, content):
        """
        Extrait les liens internes ([[lien]]) d'un fichier Markdown.
        
        Args:
            content (str): Contenu du fichier Markdown.
            
        Returns:
            list: Liste des liens internes.
        """
        link_pattern = re.compile(r'\[\[(.*?)\]\]')
        return link_pattern.findall(content)
    
    def save_markdown_file(self, directory, title, content, metadata=None):
        """
        Sauvegarde un fichier Markdown dans le répertoire spécifié.
        
        Args:
            directory (str): Répertoire de destination.
            title (str): Titre du document (utilisé pour le nom de fichier).
            content (str): Contenu Markdown.
            metadata (dict, optional): Métadonnées YAML.
            
        Returns:
            str: Chemin du fichier créé.
        """
        # Créer un nom de fichier valide
        filename = re.sub(r'[^\w\s-]', '', title.lower())
        filename = re.sub(r'[-\s]+', '-', filename).strip('-_')
        filename = f"{filename}.md"
        
        # Chemin complet
        file_path = os.path.join(directory, filename)
        
        # Préparer le contenu avec les métadonnées YAML
        full_content = content
        if metadata:
            yaml_header = yaml.dump(metadata, default_flow_style=False)
            full_content = f"---\n{yaml_header}---\n\n{content}"
        
        # Écrire le fichier
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(full_content)
        
        return file_path
    
    def get_table_download_link(self, df, filename, text):
        """
        Génère un lien pour télécharger un DataFrame en CSV.
        
        Args:
            df (pandas.DataFrame): DataFrame à télécharger.
            filename (str): Nom du fichier.
            text (str): Texte du lien.
            
        Returns:
            str: Code HTML du lien de téléchargement.
        """
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">{text}</a>'
        return href
    
    def clean_content(self, content):
        """
        Nettoie le contenu Markdown en retirant les métadonnées YAML.
        
        Args:
            content (str): Contenu Markdown.
            
        Returns:
            str: Contenu nettoyé.
        """
        return re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)