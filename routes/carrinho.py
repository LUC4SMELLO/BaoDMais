from flask import Blueprint, render_template, session


carrinho_bp = Blueprint("carrinho", __name__)

@carrinho_bp.route("/carrinho", methods=["GET", "POST"])
def carrinho():

    carrinho = session.get("carrinho", [])

    if len(carrinho) > 0:
        nome_estabelecimento = carrinho[0]["nome_estabelecimento"]
    else:
        nome_estabelecimento = ""

    total_geral = sum(float(item['preco_total']) for item in carrinho)
    
    return render_template("carrinho.html", carrinho=carrinho, nome_estabelecimento=nome_estabelecimento, total_geral=total_geral)
