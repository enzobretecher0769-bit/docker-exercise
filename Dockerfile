# Image de base légère avec Python 3.13 (comme ta VM)
FROM python:3.13-slim

# Répertoire de travail dans le container
WORKDIR /app

# Copie d'abord les dépendances (optimise le cache Docker)
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le code de ton projet
COPY . .

# Expose le port 5000 (celui de Flask)
EXPOSE 5000

# Commande pour lancer l'API quand le container démarre
CMD ["python", "app.py"]

