from flask import Blueprint, render_template

from models.item_model import ItemModel

from scripts.montar_opcoes import montar_opcoes


item_bp = Blueprint("item", __name__)

@item_bp.route("/item/<int:id>/<int:id_estabelecimento>", methods=["GET"])
def item(id, id_estabelecimento):
    
    item = ItemModel.buscar_item(id, id_estabelecimento)
    opcoes = montar_opcoes(id)

    return render_template(
        "item.html",
        id=id,
        id_estabelecimento=id_estabelecimento,
        nome=item[0],
        descricao=item[1],
        opcoes=opcoes.values()
        )
