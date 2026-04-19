from flask import Blueprint, render_template


estabelecimento_bp = Blueprint("estabelecimento", __name__)

@estabelecimento_bp.route("/estabelecimento")
def estabelecimento():
    return render_template("estabelecimento.html")
