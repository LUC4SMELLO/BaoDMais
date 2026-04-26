from flask import Blueprint, request, redirect, url_for, flash, session, render_template

from validators.validar_login import validar_login
from services.usuario_service import buscar_por_email


login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email").lstrip().rstrip().lower()
        senha = request.form.get("senha").lstrip().rstrip()

        resultado = validar_login(email, senha)
        if not resultado["sucesso"]:
            flash(resultado["mensagem"], "erro")
            return redirect(url_for("login.login"))
        
        usuario = buscar_por_email(email)
        
        session["nome"] = usuario[1].title()
        session["id"] = usuario[0]
        return redirect(url_for("pagina_inicial.pagina_inicial"))


    return render_template("login.html")
