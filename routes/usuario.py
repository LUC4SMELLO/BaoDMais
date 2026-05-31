from flask import Blueprint, render_template, session, request, flash, redirect, url_for

from validators.validar_alteracao import validar_alteracao
from models.usuario_model import UsuarioModel


usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/usuario", methods=["GET"])
def usuario():
    nome = session.get("nome", [])
    email = session.get("email", [])
    return render_template("usuario.html", nome=nome, email=email)

@usuario_bp.route("/alterar_informacoes", methods=["POST"])
def alterar_informacoes():

    id = session.get("id", [])
    novo_nome = request.form.get("nome_completo")
    novo_email = request.form.get("email")

    resultado = validar_alteracao(novo_nome, novo_email)
    if not resultado["sucesso"]:
            flash(resultado["mensagem"], "erro")
            return redirect(url_for("usuario.usuario"))
    
    UsuarioModel.editar_usuario(id, novo_nome, novo_email)

    print(novo_nome, novo_email)

    session["nome"] = novo_nome
    session["email"] = novo_email

    flash("Informações alteradas!", "sucesso")
    return redirect(url_for("usuario.usuario"))
