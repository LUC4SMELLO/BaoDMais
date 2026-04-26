from services.usuario_service import buscar_por_email, buscar_senha


def validar_login(email, senha):

    email = email.lstrip().rstrip().lower()
    senha = senha.lstrip().rstrip()

    if not email:
        return {
            "sucesso": False,
            "mensagem": "O e-mail é obrigatório."
        }
    if not senha:
        return {
            "sucesso": False,
            "mensagem": "A senha é obrigatória."
        }
    
    usuario = buscar_por_email(email)
    if not usuario:
        return {
            "sucesso": False,
            "mensagem": "E-mail ou senha inválidos."
        }
    
    senha_buscada = buscar_senha(email)
    print(senha_buscada[0])
    if senha != senha_buscada[0]:
        return {
            "sucesso": False,
            "mensagem": "E-mail ou senha inválidos."
        }

    
    return {
        "sucesso": True,
        "mensagem": "Login realizado com sucesso!"
        }
    