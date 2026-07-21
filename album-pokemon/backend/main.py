import os
import glob
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista de figurinhas com as 30 figurinhas.
# O imagem_url aponta para "/figurinhas/{id}/imagem".
# Deixamos ativas apenas as figurinhas cujas imagens existem na pasta 'figurinhas/'.
# Como todas as 30 imagens existem na pasta, todas permanecem ativas.
# Caso alguma não existisse (ex: se ids 3, 4 ou 5 fossem deletados do disco), a respectiva linha seria comentada.
figurinhas = [
    {"id": 1, "nome": "Pikachu ex", "categoria": "ELÉTRICO", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Raichu", "categoria": "ELÉTRICO", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Jolteon", "categoria": "ELÉTRICO", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Electabuzz", "categoria": "ELÉTRICO", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Zapdos", "categoria": "ELÉTRICO", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Charizard", "categoria": "FOGO", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Arcanine", "categoria": "FOGO", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Flareon", "categoria": "FOGO", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Typhlosion", "categoria": "FOGO", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Moltres", "categoria": "FOGO", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Blastoise", "categoria": "ÁGUA", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Gyarados", "categoria": "ÁGUA", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Vaporeon", "categoria": "ÁGUA", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Feraligatr", "categoria": "ÁGUA", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Articuno", "categoria": "ÁGUA", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Venusaur", "categoria": "PLANTA", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Meganium", "categoria": "PLANTA", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Sceptile", "categoria": "PLANTA", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Celebi", "categoria": "PLANTA", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Leafeon", "categoria": "PLANTA", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Mewtwo", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Mew", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Lugia", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Ho-Oh", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Suicune", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Rayquaza", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Kyogre", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Groudon", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Arceus", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Você", "categoria": "LENDÁRIO", "imagem_url": "/figurinhas/30/imagem"}
]

# Endpoint GET "/figurinhas" que retorna a lista de figurinhas (mantendo "/figuras" para compatibilidade)
@app.get("/figurinhas")
@app.get("/figuras")
def listar_figuras():
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem" que retorna o arquivo da imagem correspondente
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Procura pelo arquivo com o prefixo do ID formatado em 2 dígitos (ex: 01, 12, 30)
    # garantindo que o próximo caractere não seja um número para evitar falsos positivos
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    # Retorna o arquivo encontrado usando FileResponse
    return FileResponse(arquivos[0])
