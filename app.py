from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "POC DO GEISSIVAN PRA AULA DE DEVOPS DA FIAP | 08-DONE"

if __name__ == '__main__':
    app.run()