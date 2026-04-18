from flask import Flask

from routes.index import index_bp
from routes.pagina_inicial import pagina_inicial_bp


app = Flask(__name__)
app.secret_key = "secret_key"


app.register_blueprint(index_bp)
app.register_blueprint(pagina_inicial_bp)


if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=True)
