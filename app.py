from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "POC DO GEISSIVAN PRA AULA DE DEVOPS DA FIAP | DESAFIOS-DONE"

if __name__ == '__main__':
    app.run('0.0.0.0', port=port)