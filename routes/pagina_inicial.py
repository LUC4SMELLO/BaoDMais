from flask import Blueprint, render_template


pagina_inicial_bp = Blueprint("pagina_inicial", __name__)

@pagina_inicial_bp.route("/pagina_inicial", methods=["GET", "POST"])
def pagina_inicial():
    return render_template("pagina_inicial.html")