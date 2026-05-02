from flask import Blueprint, request, session, jsonify, url_for


adicionar_carrinho_bp = Blueprint("adicionar_carrinho", __name__)

@adicionar_carrinho_bp.route("/adicionar_carrinho", methods=["POST"])
def adicionar_carrinho():

    dados = request.get_json()


    item = dados["item"]
    quantidade = dados["quantidade"]
    opcoes = dados["opcoes"]

    index = dados.get("index")


    item_carrinho = {
        "id_estabelecimento": item["id_estabelecimento"],
        "nome_estabelecimento": item["nome_estabelecimento"],
        "id_item": item["id"],
        "nome": item["nome"],
        "quantidade": quantidade,
        "opcoes": [
            {
                "id_opcao_valor": i["id_opcao_valor"],
                "nome": i["nome"],
                "id_opcao": i["id_opcao"],
                "preco": float(i["preco"].replace(",", "."))
            }
            for i in opcoes
        ]
    }
    item_carrinho["preco_total"] = (
        sum(opcao["preco"] for opcao in item_carrinho["opcoes"]) * quantidade
    )

    
    if "carrinho" not in session:
        session["carrinho"] = []
    carrinho = session["carrinho"]


    if index != "":
        carrinho[int(index)] = item_carrinho
    else:
        carrinho.append(item_carrinho)


    session["carrinho"] = carrinho

    url_destino = url_for("estabelecimento.estabelecimento", id=item["id_estabelecimento"])

    return jsonify({
        "url": url_destino
    })