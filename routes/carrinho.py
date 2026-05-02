from flask import Blueprint, render_template, session


carrinho_bp = Blueprint("carrinho", __name__)

@carrinho_bp.route("/carrinho", methods=["GET", "POST"])
def carrinho():

    carrinho = session.get("carrinho", [])

    try:
        nome_estabelecimento = carrinho[0]["nome_estabelecimento"]
    except Exception:
        nome_estabelecimento = ""
    
    return render_template("carrinho.html", carrinho=carrinho, nome_estabelecimento=nome_estabelecimento)
