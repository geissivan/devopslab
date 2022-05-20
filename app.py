from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "POC DO GEISSIVAN PRA AULA DE DEVOPS DA FIAP"

if __name__ == '__main__':
    app.run()