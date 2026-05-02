from flask import Blueprint, session, redirect, url_for


remover_carrinho_bp = Blueprint("remover_carrinho", __name__)

@remover_carrinho_bp.route("/remover_carrinho/<int:index>")
def remover_carrinho(index):

    carrinho = session.get("carrinho", [])

    if index < len(carrinho):
        carrinho.pop(index)

    session["carrinho"] = carrinho

    return redirect(url_for("carrinho.carrinho"))
