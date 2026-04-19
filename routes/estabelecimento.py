from flask import Blueprint, render_template

from models.estabelecimento_model import EstabelecimentoModel


estabelecimento_bp = Blueprint("estabelecimento", __name__)

@estabelecimento_bp.route("/estabelecimento/<int:id>")
def estabelecimento(id):

    resultado = EstabelecimentoModel.buscar_estabelecimento(id)

    return render_template(
        "estabelecimento.html",
        nome=resultado[0],
        tipo=resultado[1],
        avaliacao=resultado[2],
        pedido_minimo=resultado[3],
        tempo_delivery=resultado[4],
        caminho_foto=resultado[5]
        )
