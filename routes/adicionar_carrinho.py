from flask import Blueprint, request, jsonify, url_for


adicionar_carrinho_bp = Blueprint("adicionar_carrinho", __name__)

@adicionar_carrinho_bp.route("/adicionar_carrinho", methods=["POST"])
def adicionar_carrinho():

    dados = request.get_json()


    item = dados["item"]
    quantidade = dados["quantidade"]
    opcoes = dados["opcoes"]

    print(item)
    print(quantidade)
    print(opcoes)

    url_destino = url_for("estabelecimento.estabelecimento", id=item["id_estabelecimento"])

    return jsonify({
        "url": url_destino
    })