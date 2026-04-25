from flask import Blueprint, request, render_template

from models.estabelecimento_model import EstabelecimentoModel


cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":
        nome = request.form.get("nome_completo")
        email = request.form.get("email")
        senha = request.form.get("senha")

        print(nome, email, senha)

        estabelecimentos = EstabelecimentoModel.listar_estabelecimentos()

        return render_template("pagina_inicial.html", estabelecimentos=estabelecimentos)


    return render_template("cadastro.html")
