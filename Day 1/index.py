# Aqui importamos a miniframework flask
from flask import Flask

'''
A parti daqui criamos uma conexação com toda a class 
Flask e com isso conseguimos fazer uso de todas as 
ferramentas do mesmo
'''
app = Flask(__name__)

'''
Com esse decorador '@' temos como passar uma função a outra função
no caso dessa debaixo irá criar uma nova rota para a nossa pag
'''


@app.route("/")  # Para cada rota temos que passar uma função que irá retorna a pag
def index():
    return "<p>Esta é minha primeira página web</p>"


'''
Toda vez que criarmos uma nova rota temos que passar um novo 
endereço para a mesma, isto é, passar um endereço após a barra da rota
com isso teremos outra pag.
'''


@app.route("/segunda_pagina/")
def segunda_pagina():
    """
    Aqui embaixo vemos uma nova
    função para as 3 aspas que é criar
    uma ‘string’ com mais de uma linha
    """
    return '''
    <form>
        <label>Primeiro nome:</label>
        <input  type="text"><br><br>
        <label>Segundo  Nome</label>
        <input  type="text" ><br><br>
        <input  type="submit" value="enviar">
    </form>
            '''


# E no final de tudo colocamos o projeto para rodar
app.run()
