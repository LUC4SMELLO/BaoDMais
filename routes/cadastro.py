from flask import Blueprint, render_template


cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    return render_template("cadastro.html")
