# Choix de la version de Python à utiliser.
FROM python:3.11

# Création du dossier de travail.
WORKDIR /code

# Copier uniquement les dépendances dans le répertoire de travail
# pour qu'elles soient mises en cache séparément.
COPY ./requirements.txt /code/requirements.txt

# Copier le modèle entraîné dans le répertoire de travail.
# Attention, si le fichier est hébergé sur Git LFS, dans le workflow Github Actions,
# il faudra au préalable activer LFS lors du Checkout repository et faire un pull,
# sinon seul le pointeur sera copié et non le fichier réel.
COPY ./KNeighborsClassifier_and_bin.pkl /code/KNeighborsClassifier_and_bin.pkl

# Installation des dépendances indiquées dans le fichier des prérequis.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copie des fichiers de code dans le dossier de travail,
# à l'exception éventuelle de fichiers à exclure qui seraient
# précisés dans un fichier .dockerignore
COPY ./app /code/app

# Indiquer la commande uvicorn qui s'exécutera à l'intérieur du conteneur
# pour lancer notre API.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]