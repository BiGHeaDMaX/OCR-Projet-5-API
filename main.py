# Imports spécifiques à l'API
from fastapi import FastAPI
import uvicorn

# Instanciation de notre API
app = FastAPI()

##################
# Page d'accueil #
##################
@app.get("/")
async def prediction_form():
    return "Bonjour"


#if __name__ == "__main__":
    #import uvicorn
    # Lancement de l'app sur un serveur uvicorn
#    uvicorn.run(app, host="127.0.0.1", port=8000)

#uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == '__main__':
    uvicorn.run('main:app')