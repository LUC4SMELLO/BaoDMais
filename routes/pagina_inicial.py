from flask import Blueprint, render_template

from models.estabelecimento_model import EstabelecimentoModel


pagina_inicial_bp = Blueprint("pagina_inicial", __name__)

@pagina_inicial_bp.route("/pagina_inicial", methods=["GET", "POST"])
def pagina_inicial():

    estabelecimentos = EstabelecimentoModel.listar_estabelecimentos()

    return render_template("pagina_inicial.html", estabelecimentos=estabelecimentos)