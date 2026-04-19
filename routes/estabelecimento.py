from flask import Blueprint, render_template


estabelecimento_bp = Blueprint("estabelecimento", __name__)

@estabelecimento_bp.route("/estabelecimento/<int:id>")
def estabelecimento(id):
    return render_template("estabelecimento.html", id=id)
