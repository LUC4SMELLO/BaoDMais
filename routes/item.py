from flask import Blueprint, render_template, request, session

from models.item_model import ItemModel

from scripts.montar_opcoes import montar_opcoes


item_bp = Blueprint("item", __name__)

@item_bp.route("/item/<int:id>/<int:id_estabelecimento>/<string:nome_estabelecimento>", methods=["GET"])
def item(id, id_estabelecimento, nome_estabelecimento):
    
    item = ItemModel.buscar_item(id, id_estabelecimento)
    opcoes = montar_opcoes(id)
    

    index = request.args.get("index")
    modo_edicao = index is not None

    item_carrinho = None
    if modo_edicao:

        carrinho = session.get("carrinho", [])

        item_carrinho = carrinho[int(index)]


    return render_template(
        "item.html",
        id=id,
        id_estabelecimento=id_estabelecimento,
        nome_estabelecimento=nome_estabelecimento,
        nome=item[0],
        descricao=item[1],
        opcoes=opcoes.values(),
        item_carrinho=item_carrinho,
        index=index
        )
