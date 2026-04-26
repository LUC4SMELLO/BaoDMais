import re
from services.usuario_service import buscar_por_nome, buscar_por_email


EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def validar_cadastro(nome, email, senha):

    nome = nome.lstrip().rstrip().lower()
    email = email.lstrip().rstrip().lower()
    senha = senha.lstrip().rstrip().lower()

    if not nome:
        return {
            "sucesso": False,
            "mensagem": "O campo nome é obrigatório."
        }
    if not email:
        return {
            "sucesso": False,
            "mensagem": "O campo e-mail é obrigatório."
        }
    if not senha:
        return {
            "sucesso": False,
            "mensagem": "O campo senha é obrigatório."
        }
    if not re.match(EMAIL_REGEX, email):
        return {
            "sucesso": False,
            "mensagem": "O e-mail é inválido."
        }
    
    if len(senha) < 8 or not re.search(r"[A-Za-z]", senha) or not re.search(r"\d", senha):
        return {
            "sucesso": False,
            "mensagem": "A senha deve ter pelo menos 8 caracteres, com letras e números."
        }
    
    if buscar_por_nome(nome):
        return {
            "sucesso": False,
            "mensagem": "Nome já encontrado."
        }
    if buscar_por_email(email):
        return {
            "sucesso": False,
            "mensagem": "E-mail já cadastrado."
        }


    return {
        "sucesso": True,
        "mensagem": "Usuário cadastrado com sucesso!"
    }
