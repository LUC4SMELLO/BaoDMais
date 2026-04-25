from flask import Blueprint, request, render_template

from models.estabelecimento_model import EstabelecimentoModel


login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        print(email, senha)

        estabelecimentos = EstabelecimentoModel.listar_estabelecimentos()

        return render_template("pagina_inicial.html", estabelecimentos=estabelecimentos)


    return render_template("login.html")
