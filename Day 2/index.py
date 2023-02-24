from flask import Flask

app = Flask(__name__)

# Rota estatica
@app.route("/index")
def index():
    return "Pagina inicial"


#Abaixo uma comparação de um retorno de um string e um dicionario(JSON)
@app.route("/index/st")
def st():
    return "Nome: Getulio\nIdade: 22"

@app.route("/index/js")
def js():
    return {"Nome": "Getulio", "Idade": 22}

app.run()