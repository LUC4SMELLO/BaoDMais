from flask import Blueprint, render_template


carrinho_bp = Blueprint("carrinho", __name__)

@carrinho_bp.route("/carrinho", methods=["GET", "POST"])
def carrinho():
    return render_template("carrinho.html")
