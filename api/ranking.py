from http.server import BaseHTTPRequestHandler
import json
import os
import base64
import urllib.request
import urllib.error

# Configurações do GitHub
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
GITHUB_REPO = os.environ.get('GITHUB_REPO', '')  # formato: usuario/repositorio
RANKING_FILE = 'ranking.json'

def get_ranking_from_github():
    """Busca o ranking do arquivo no GitHub"""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        return {"ranking": []}
    
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{RANKING_FILE}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            content = base64.b64decode(data['content']).decode('utf-8')
            return json.loads(content)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"ranking": []}
        raise
    except Exception:
        return {"ranking": []}

def get_file_sha():
    """Obtém o SHA do arquivo para atualização"""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        return None
    
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{RANKING_FILE}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('sha')
    except:
        return None

def save_ranking_to_github(ranking_data):
    """Salva o ranking no arquivo do GitHub"""
    if not GITHUB_TOKEN or not GITHUB_REPO:
        return False
    
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{RANKING_FILE}"
    
    content = json.dumps(ranking_data, indent=2, ensure_ascii=False)
    content_base64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    
    sha = get_file_sha()
    
    payload = {
        "message": "Atualização do ranking",
        "content": content_base64
    }
    
    if sha:
        payload["sha"] = sha
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
        with urllib.request.urlopen(req) as response:
            return response.status == 200 or response.status == 201
    except Exception as e:
        print(f"Erro ao salvar: {e}")
        return False

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Retorna o ranking atual"""
        try:
            ranking_data = get_ranking_from_github()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps(ranking_data).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def do_POST(self):
        """Adiciona um novo resultado ao ranking"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(body)
            
            name = data.get('name', '')
            score = data.get('score', 0)
            
            if not name:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Nome é obrigatório"}).encode())
                return
            
            ranking_data = get_ranking_from_github()
            
            # Adiciona novo resultado
            ranking_data['ranking'].append({
                "name": name,
                "score": score
            })
            
            # Ordena por pontuação (maior primeiro) e mantém top 10
            ranking_data['ranking'] = sorted(
                ranking_data['ranking'], 
                key=lambda x: x['score'], 
                reverse=True
            )[:10]
            
            # Salva no GitHub
            success = save_ranking_to_github(ranking_data)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({
                "success": success,
                "ranking": ranking_data['ranking']
            }).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def do_DELETE(self):
        """Reseta o ranking (requer senha)"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(body)
            
            password = data.get('password', '')
            
            if password != 'Camila':
                self.send_response(403)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Senha incorreta"}).encode())
                return
            
            # Reseta o ranking
            ranking_data = {"ranking": []}
            success = save_ranking_to_github(ranking_data)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({
                "success": success,
                "message": "Ranking resetado com sucesso"
            }).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
