from flask import Flask

app = Flask(__name__)

lista_usuarios = \
    [
        {"Nome": "Getulio", "Idade": 22, "E-mail": "a@gmail.com"},
        {"Nome": "Carlos", "Idade": 35, "E-mail": "b@gmail.com"},
        {"Nome": "José", "Idade": 40, "E-mail": "c@gmail.com"}

    ]


@app.route('/')
def index():
    return "<p>Digite o caminho para retonar alguma informação</p>"


@app.route('/v1/user/idade/<nome>')
def idade(nome):
    contador = 0
    for i in lista_usuarios:

        if nome == lista_usuarios[contador]["Nome"]:
            return f"{lista_usuarios[contador]['Idade']}"
        contador += 1
    return "Usuario não encontrado"


@app.route('/v1/user/email/<nome>')
def email(nome):
    contador = 0
    for i in lista_usuarios:

        if nome == lista_usuarios[contador]["Nome"]:
            return f"{lista_usuarios[contador]['E-mail']}"
        contador += 1
    return "Usuario não encontrado"


@app.route('/v1/user/info/nome/<nome>')
@app.route('/v1/user/info/email/<email>')
def info(nome=None, email=None):
    contador = 0
    for i in lista_usuarios:

        if nome == lista_usuarios[contador]["Nome"]:
            return f"{lista_usuarios[contador]}"

        if email == lista_usuarios[contador]["E-mail"]:
            return f"{lista_usuarios[contador]}"

        contador += 1
    return "Usuario não encontrado"


app.run()
