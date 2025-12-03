from http.server import BaseHTTPRequestHandler
import json
import random

# Palavras reais
real_words = [
    "caderno", "chuva", "garrafa", "ventilador", "escola",
    "parque", "computador", "caminhar", "estudante", "livro",
    "mesa", "janela", "buscando", "esperança", "bicicleta",
    "lousa", "sorriso", "alegria", "travesseiro", "folha"
]

# Pseudopalavras
pseudo_words = [
    "vaspino", "bruleca", "tombir", "fegrila", "salbino",
    "crefuso", "lomilha", "febluda", "sambote", "grotina",
    "belfasi", "nabrico", "trupira", "ligote", "mabruta",
    "flosibe", "remputa", "pecadole", "vimbula", "derfati"
]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Escolher aleatoriamente entre palavra real e pseudopalavra
        word_type = random.choice(['real', 'pseudo'])
        
        if word_type == 'real':
            word = random.choice(real_words)
        else:
            word = random.choice(pseudo_words)
        
        response = {
            'word': word,
            'type': word_type
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
        return
