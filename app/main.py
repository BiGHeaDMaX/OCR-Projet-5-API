# Imports spécifiques à l'API
from fastapi import FastAPI
import uvicorn

# Instanciation de notre API 
app = FastAPI()

##################
# Page d'accueil #
##################
@app.get("/")
def prediction_form():
    return "Bonjour new 2"

if __name__ == '__main__':
    uvicorn.run('main:app')

