from flask import Flask, jsonify
import os 
import platform
import psutil

APP = Flask(__name__)

@APP.get("/")
def index():
    return "<h1>Página Inicial, utilize /info ou /metricas para acessar as outras páginas</h1>"

@APP.get("/info")
def info():
    integrante = "Nicolas Felix Hrescak"

    dados = {
        "Integrantes": integrante
    }

    return jsonify(dados)

@APP.get("/metricas")
def metricas():
    integrante = "Nicolas Felix Hrescak"
    #Utiliza o modulo OS pra pegar o PID do processo
    pid = os.getpid()
    
    #psutil serve pra criar um objeto desse prrocesso
    processo = psutil.Process(pid)

    #memory_info().rss serve para retornar o valor da memoria utilizada pelo processo em MB
    #fazendo-se necessário dividir 
    memoria = processo.memory_info().rss / (1024 * 1024)

    #a função cpu_percent retorna o percentual e o "interval = None"
    #Serve para delimitar desde a ultima chamada
    CPUper = processo.cpu_percent(interval = None)

    #Usamos o modulo platform pra pegar detalhes do OS
    sistemaOperacional = f"{platform.system()}({platform.platform()})"

    #Montando o JSON pro requisito 4.2
    dados = {
        "Integrantes": integrante,
        "pid": pid,
        "Memoria": round(memoria, 2),
        "Porcentagem da CPU": CPUper,
        "Sistema Operacional": sistemaOperacional
    }

    return jsonify(dados)

if __name__ == '__main__':
    psutil.cpu_percent(interval=None)
    APP.run(host="0.0.0.0", port = 5001)
    
