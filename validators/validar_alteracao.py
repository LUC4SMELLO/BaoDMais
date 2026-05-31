import re


EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def validar_alteracao(nome, email):

    nome = nome.lstrip().rstrip()
    email = email.lstrip().rstrip()

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
    if not re.match(EMAIL_REGEX, email):
        return {
            "sucesso": False,
            "mensagem": "O e-mail é inválido."
        }
    
    return {
        "sucesso": True,
        "mensagem": "Alterações válidas!"
    }