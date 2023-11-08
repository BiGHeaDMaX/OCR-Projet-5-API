# **Introduction**
Cette API, basée sur FastAPI, permet de proposer des tags pour un texte donné en entrée. L'API est basée sur un modèle supervisé, entraîné sur 50 000 messages et leurs tags associés provenant de Stack Overflow. Les tags proposés ont donc une forte dimension technique. Les messages ont été récupérés sur le [*StackExchange Data Explorer*](https://data.stackexchange.com/stackoverflow/query/new).
> **Note**<br>
Pour cette version dans le cloud, pour des raisons de limitations techniques, le document devra être encodé avec [USE](https://tfhub.dev/google/universal-sentence-encoder/4) en local avant d'être transmis à l'API. En effet le modèle de sentence embedding préentraîné USE nécessite plus de RAM que celle disponible dans la solution de cloud utilisée. Sans cette limitation technique, il est bien sûr tout à fait possible d'inclure cet encodage dans l'API, que nous pourrions alors directement requêter avec les documents bruts.
<br><br>
Le sentence embedding avec USE est si performant qu'il permet de capter le sens des documents dans plusieurs langues, sans prétraitements préalables. Ce qui fait que même si notre modèle de prédiction a été entraîné sur des documents en Anglais (préalablement encodés avec USE), il fonctionne également avec des documents dans d'autres langues.

# **Contenu de ce repository**
- **Dockerfile** : utilisé pour la création d'une image docker
- **KNeighborsClassifier_and_bin.pkl** : modèle préentraîné (stocké via Git LFS)
- **requirements.txt** : dépendances pour faire fonctionner l'API
- **app/main.py** : code de l'API
- **app/requirements_test.txt** : dépendances pour les tests unitaires
- **app/test_main.py** : code des tests unitaires avec pytest
- **.github/workflows/azure-docker-python.yml** : workflow déclenché lors d'un push sur la branche master

# **Workflow**
Lors d'un push sur la branche master, un workflow GitHub Actions est déclenché et réalise les actions suivantes : 
- Test unitaires avec pytest. Si un des tests retourne une erreur, le workflow est stoppé.
- Si tous les tests sont passés avec succès, une image docker est crée.
- L'image docker est poussée sur un registre de conteneur Azure.
- L'instance de conteneur Azure qui utilise l'image docker est redémarrée afin de prendre en compte les changements.

# **Repository associé**
Tout le travail de prétraitement des données et de recherche des meilleurs modèles se trouve dans [ce repository](https://github.com/BiGHeaDMaX/OCR-Projet-5).
