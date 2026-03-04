# Utiliser une image de base légère pour Python 3.11
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer uv explicitement
RUN pip install --no-cache-dir uv

# Copier uniquement les fichiers de configuration et de verrouillage des dépendances
COPY pyproject.toml uv.lock ./

# Installer les dépendances en utilisant uv sync
# --frozen : respecte exactement uv.lock sans le modifier
# --no-dev : exclut les dépendances de développement
RUN uv sync --frozen --no-dev

# Copier le reste du code source de l'application
COPY . .

# Spécifier la commande pour lancer l'application
CMD ["python", "main.py"]
