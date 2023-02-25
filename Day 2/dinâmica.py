from flask import Flask

app = Flask(__name__)

@app.route("/user/idade/<nome>")
def retonar_idade(nome):
    if nome == "getulio":
        return {"idade": 22}
    else:
        return "Nome não está na lista"
    

app.run()