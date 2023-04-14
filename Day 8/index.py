from flask import Flask, render_template, redirect, request
from conexão import *
app = Flask(__name__)


# Criação da primeira rota da pagina inicial
@app.route("/")
def index():
    return render_template("index.html")


'''
Rota de contato junto com o parametro de contatos 
puxando do banco de dados
'''


@app.route("/contatos")
def contatos():
    return render_template(
        "contatos.html",
        contato=session.query(Contatos).all()
    )


# Rota do sobre será editado pelos alunos
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


'''
Rota da aba de criação de contatos nela terá 
o rediricionamento
'''


@app.route("/new_contatos")
def new_contatos():
    return render_template("new_contatos.html")


'''
Rota especifica para adicição de dado no banco 
de dados atraves do metodo post
'''


@app.route("/salvar_contato", methods=["POST"])
def salva_contato():
    '''
    Condição para pegar o nome do icone de acordo 
    com o que a pessoa escreveu
    '''
    if request.form.to_dict()['tag'] == "família":
        img = "group"
    elif request.form.to_dict()['tag'] == "trabalho":
        img = "business_center"
    else:
        img = "person"

    # Adicição do contato no banco de dados
    contato = Contatos(
        nome=request.form.to_dict()['nome'],
        email=request.form.to_dict()['email'],
        celular=request.form.to_dict()['celular'],
        tag=request.form.to_dict()['tag'],
        link=img
    )

    session.add(contato)
    session.commit()

    return redirect("contatos")


# Rota especifica para exclusão de alunos a parti do id
@app.route("/deletar_contato/<id>")
def deletar_contato(id):
    pessoa = session.query(Contatos).filter(Contatos.id == id).one()

    session.delete(pessoa)
    session.commit()

    return redirect("/contatos")


'''
Rota de edição de dados pegando informação com id 
e mandando-as para uma página
'''


@app.route("/editar/<id>")
def editar_contato(id):
    pessoa = session.query(Contatos).filter(Contatos.id == id).one()

    return render_template(
        "edicao.html",
        pessoa=pessoa
    )


'''
Rota parecida com a criar contato, só que aqui é passado 
o metodo post para a atualização de dados do contato
'''


@app.route("/editar_contato/<id>", methods=["POST"])
def seditar_contato(id):
    pessoa = session.query(Contatos).filter(Contatos.id == id).one()

    if request.form.to_dict()['tag'] == "família":
        img = "group"
    elif request.form.to_dict()['tag'] == "trabalho":
        img = "business_center"
    else:
        img = "person"

    pessoa.nome = request.form.to_dict()['nome']
    pessoa.email = request.form.to_dict()['email']
    pessoa.celular = request.form.to_dict()['celular']
    pessoa.tag = request.form.to_dict()['tag']
    pessoa.link = img

    session.add(pessoa)
    session.commit()

    return redirect("/contatos")


if __name__ == "__main__":
    app.run(debug=True)
