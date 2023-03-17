from lista import usuarios
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
         'index.html',
         usuarios = usuarios
    )

app.run(debug=True)
