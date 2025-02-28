import os
import re
import yaml
from pathlib import Path

def find_markdown_files(directory):
    """Trouve tous les fichiers Markdown dans un répertoire et ses sous-répertoires."""
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def extract_yaml_metadata(content):
    """Extrait les métadonnées YAML d'un fichier Markdown."""
    yaml_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    match = yaml_pattern.search(content)
    if match:
        yaml_content = match.group(1)
        try:
            return yaml.safe_load(yaml_content)
        except yaml.YAMLError:
            return {}
    return {}

def extract_internal_links(content):
    """Extrait les liens internes ([[lien]]) d'un fichier Markdown."""
    link_pattern = re.compile(r'\[\[(.*?)\]\]')
    return link_pattern.findall(content)

def parse_markdown_file(file_path):
    """Parse un fichier Markdown et extrait ses métadonnées et liens."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        metadata = extract_yaml_metadata(content)
        internal_links = extract_internal_links(content)
        
        # Extrait les relations définies dans les métadonnées YAML
        relations = []
        if 'relations' in metadata:
            for relation in metadata.get('relations', []):
                if 'target' in relation:
                    if isinstance(relation['target'], list):
                        for target in relation['target']:
                            if isinstance(target, str) and target.startswith('[[') and target.endswith(']]'):
                                relations.append((relation.get('type', 'link'), target[2:-2]))
                    elif isinstance(relation['target'], str) and relation['target'].startswith('[[') and relation['target'].endswith(']]'):
                        relations.append((relation.get('type', 'link'), relation['target'][2:-2]))
        
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

def parse_markdown_directory(directory):
    """Parse tous les fichiers Markdown dans un répertoire et ses sous-répertoires."""
    markdown_files = find_markdown_files(directory)
    parsed_files = []
    
    for file_path in markdown_files:
        parsed_file = parse_markdown_file(file_path)
        if parsed_file:
            parsed_files.append(parsed_file)
    
    return parsed_files
