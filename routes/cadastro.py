from flask import Blueprint, request, redirect, url_for, flash, session, render_template

from validators.validar_cadastro import validar_cadastro
from models.usuario_model import UsuarioModel


cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":
        nome = request.form.get("nome_completo").lstrip().rstrip()
        email = request.form.get("email").lstrip().rstrip()
        senha = request.form.get("senha").lstrip().rstrip()


        resultado = validar_cadastro(nome, email, senha)
        if not resultado["sucesso"]:
            flash(resultado["mensagem"], "erro")
            return redirect(url_for("cadastro.cadastro"))
        
        UsuarioModel.inserir_usuario(nome, email, senha)

        session["nome"] = nome.title()
        session["email"] = email
        return redirect(url_for("pagina_inicial.pagina_inicial"))


    return render_template("cadastro.html")
