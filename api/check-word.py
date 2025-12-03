from http.server import BaseHTTPRequestHandler
import json
from difflib import SequenceMatcher

def normalize_text(text):
    """Normaliza o texto removendo acentos e convertendo para minúsculas"""
    text = text.lower().strip()
    
    # Mapeamento de caracteres acentuados
    replacements = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e',
        'í': 'i',
        'ó': 'o', 'ô': 'o', 'õ': 'o',
        'ú': 'u', 'ü': 'u',
        'ç': 'c'
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def calculate_similarity(s1, s2):
    """Calcula a similaridade entre duas strings"""
    return round(SequenceMatcher(None, s1, s2).ratio() * 100, 2)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        
        expected = normalize_text(data.get('expected', ''))
        spoken = normalize_text(data.get('spoken', ''))
        
        # Calcular similaridade
        similarity = calculate_similarity(expected, spoken)
        
        # Considerar correto se a similaridade for maior que 80%
        is_correct = similarity >= 80
        
        response = {
            'correct': is_correct,
            'similarity': similarity,
            'expected': data.get('expected', ''),
            'spoken': data.get('spoken', '')
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())
        return
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        return
