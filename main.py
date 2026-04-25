from flask import Flask

from routes.index import index_bp
from routes.login import login_bp
from routes.cadastro import cadastro_bp

from routes.pagina_inicial import pagina_inicial_bp

from routes.carrinho import carrinho_bp
from routes.usuario import usuario_bp
from routes.estabelecimento import estabelecimento_bp
from routes.item import item_bp


app = Flask(__name__)
app.secret_key = "secret_key"


app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(cadastro_bp)

app.register_blueprint(pagina_inicial_bp)

app.register_blueprint(carrinho_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(estabelecimento_bp)
app.register_blueprint(item_bp)


if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=True)
