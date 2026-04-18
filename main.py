from flask import Flask

from routes.index import index_bp
from routes.pagina_inicial import pagina_inicial_bp

from routes.carrinho import carrinho_bp


app = Flask(__name__)
app.secret_key = "secret_key"


app.register_blueprint(index_bp)
app.register_blueprint(pagina_inicial_bp)

app.register_blueprint(carrinho_bp)


if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=True)
