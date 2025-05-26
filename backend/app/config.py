import os
from dotenv import load_dotenv
from functools import lru_cache

@lru_cache()
def get_settings():
    load_dotenv()  # Charge les variables depuis le fichier .env
    return {
        "API_KEY": os.getenv("API_KEY"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        # Ajoutez d'autres variables d'environnement ici
    }