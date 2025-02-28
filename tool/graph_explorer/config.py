import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Configuration pour le LLM
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:8000/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "EMPTY")
LLM_MODEL = os.getenv("LLM_MODEL", "Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4")

# Configuration pour les embeddings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-large-instruct")

# Autres configurations
DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", "16000"))
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.3"))