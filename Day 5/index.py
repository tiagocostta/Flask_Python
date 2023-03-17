from flask import Flask, render_template, redirect, request
from lista import lista_contatos

app = Flask(__name__)


@app.route("/index.html")
@app.route("/")
def index():
    return render_template(
         'index.html'
    )

@app.route("/contatos.html")
def contatos():
    return render_template(
        'contatos.html',
        lista_contatos = lista_contatos
    )

@app.route("/new_contatos.html")
def new_contatos():
    return render_template(
        'new_contatos.html'
    )

@app.route("/sobre.html")
def sobre():
    return render_template(
        'sobre.html '
    )

@app.route("/salvar_contato", methods=['POST'])
def salvar_contato():
    if request.form.to_dict()['tag'] == "família":
        img = "group"
    elif request.form.to_dict()['tag'] == "trabalho":
        img = "business_center"
    else:
        img = "people"

    lista_contatos.append({
        "nome": request.form.to_dict()['nome'],
        "email": request.form.to_dict()['email'],
        "celular": request.form.to_dict()['celular'],
        "tag":request.form.to_dict()['tag'],
        'link': f'{img}'
    })
    return redirect('/contatos.html')

app.run(debug=True)
