from flask import Flask, render_template, redirect, request
from conexão import *
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contatos")
def contatos():
    return render_template(
        "contatos.html",
        contato=session.query(Contatos).all()
    )


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/new_contatos")
def new_contatos():
    return render_template("new_contatos.html")


@app.route("/salvar_contato", methods=["POST"])
def salva_contato():
    if request.form.to_dict()['tag'] == "família":
        img = "group"
    elif request.form.to_dict()['tag'] == "trabalho":
        img = "business_center"
    else:
        img = "person"

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


@app.route("/deletar_contato/<id>")
def deletar_contato(id):
    pessoa = session.query(Contatos).filter(Contatos.id == id).one()

    session.delete(pessoa)
    session.commit()

    return redirect("/contatos")


@app.route("/editar/<id>")
def editar_contato(id):
    pessoa = session.query(Contatos).filter(Contatos.id == id).one()

    return render_template(
        "edicao.html",
        pessoa=pessoa
    )


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
