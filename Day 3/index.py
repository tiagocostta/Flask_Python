from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index.html")
@app.route("/")
def index():
    return render_template(
         'index.html'
    )

@app.route("/new_contatos.html")
def contatos():
    return render_template(
        'new_contatos.html'
    )

app.run(debug=True)
