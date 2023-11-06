# Imports spécifiques à l'API
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Imports pour notre modèle de prédiction
import pickle
#import tensorflow_hub as hub

import numpy as np

# Instanciation de notre API
app = FastAPI()

# Chargement du modèle choisi précédemment enregistré
with open('KNeighborsClassifier_and_bin.pkl', 'rb') as fichier:
    model_and_bin = pickle.load(fichier)

# Chargement du modèle USE pré-entraîné (s'il n'avait pas été chargé précédemment)
# embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Fonction de prédiction
def tags_predict(document):

    ddd = document.replace('[', '').replace(']', '')
    ddd = ddd.split()
    ddd = np.array([float(item) for item in ddd])


    # Encodage du document avec USE
    #document_USE = embed([document])
    #document_USE = ddd
    # Prédiction avec le modèle entraîné
    #prediction = model_and_bin[0].predict(ddd)
    # Décodage de la prédiction pour avoir les tags sous forme textuelle
    #tags = ', '.join(model_and_bin[1].inverse_transform(prediction)[0])


    prediction = model_and_bin[0].predict([ddd])
    tags = ', '.join(model_and_bin[1].inverse_transform(prediction)[0])

    return tags

##################
# Page d'accueil #
##################
# Page d'accueil avec un formulaire pour entrer un document
@app.get("/", response_class=HTMLResponse)
def prediction_form():
    """
    - Page d'accueil de l'interface web.
    - Entrez le texte de votre document dans le champs textuel,
      puis cliquez sur le bouton "Prédiction".
    """
    return """
                <html>
                <body style="background-color: #000D4B;">
                    &nbsp;
                    &nbsp;
                    <h1 style="text-align: center;">
                        <span style="font-size:72px; color:#FFFFFF; font-family:arial,helvetica,sans-serif;">
                        <strong>PR&Eacute;DICTION DE TAGS</strong>
                        </span>
                    </h1>
                    <p style="text-align: center;">
                        <span style="font-size:22px; color:#FFFFFF; font-family:arial,helvetica,sans-serif;">
                        <em>Entrez le texte de votre document dans le formulaire et cliquez sur le bouton &quot;Pr&eacute;diction&quot; :</em>
                        </span>
                    </p>
                    <form action="/predict_web" method="get">
                        <p align="center">
                            <textarea id="document" name="document" rows="20" cols="120"></textarea>
                            <br><br>
                            <input type="submit" value="Prédiction" style="width: 120px; height: 60px; font-size: 20px; background-color: #000D4B; color: #FFFFFF;">
                        </p>
                    </form>
                    <p style="text-align: center;">
                        <span style="font-size:22px; color:#FFFFFF; font-family:arial,helvetica,sans-serif;">
                            <a href="/docs" style="color:#FFFFFF">Consultez la documentation</a>
                        </span>
                    </p>
                </body>
                </html>
"""

#########################
# Page de résultats web #
#########################
@app.get("/predict_web", response_class=HTMLResponse)
def prediction_result_web(document: str):
    """
    - Page de résultat de la prédiction sur l'interface web.
    - Indique les tags prédits par le modèle en fonction
      du texte que vous avez entré.
    - Cliquez sur le bouton "Faire une autre prédiction"
      pour faire une nouvelle prédiction.
    """
    predicted_tags = tags_predict(document)
    return f"""
                <html>
                    <body style="background-color: #000D4B;">
                        &nbsp;
                        &nbsp;
                        <h1 style="text-align: center;">
                            <span style="font-size:72px; color:#FFFFFF; font-family:arial,helvetica,sans-serif;">
                            <strong>R&Eacute;SULTAT DE LA PR&Eacute;DICTION</strong>
                            </span>
                        </h1>
                        <p style="text-align: center;">
                            <span style="font-size:32px; color:#FFFFFF; font-family:arial,helvetica,sans-serif;">Pour le texte suivant :<br><br></span>
                            <span style="font-size:22px; color:#FFFFFF; font-family:arial,helvetica,sans-serif;"><em>{document}</em></span>
                        </p>
                        <h2 style="text-align: center;">
                            <span style="font-size:48px; color:#FFFFFF; font-family:arial,helvetica,sans-serif;">Tags pr&eacute;dits : {predicted_tags}</span>
                        </h2>
                        <form action="/" method="get">
                            <p align="center">
                                <button type="submit" style="width: 200px; height: 60px; font-size: 20px; background-color: #000D4B; color: #FFFFFF;">Faire une autre pr&eacute;diction</button>
                            </p>
                        </form>
                    </body>
                </html>
"""

###############################
# Renvoi des résultats en STR #
###############################
@app.get("/predict")
def prediction_result(document):
#async def prediction_result(document: str):
    """
    - Fonction de prédiction qui retourne uniquement
      les tags prédits sous forme de string.
    - À utiliser comme API depuis un autre programme.
    """
    predicted_tags = tags_predict(document)
    return predicted_tags

# Si le fichier est exécuté en tant que
# programme principal et non importé
if __name__ == '__main__':
    uvicorn.run('main:app')

