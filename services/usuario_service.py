from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_USUARIOS


def buscar_por_nome(nome: str):

    conexao = None
    try:
        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            SELECT nome
            FROM {TABELA_USUARIOS}
            WHERE nome = ?
            """,
                (
                    nome,
                )
            )
        
        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        print("Erro ao buscar por nome: ", erro)
        return
    
    finally:
        if conexao:
            conexao.close()

def buscar_por_email(email: str):

    conexao = None
    try:
        conexao = conectar_banco_dados_principal()
        cursor = conexao.cursor()

        cursor.execute(
            f"""
            SELECT email
            FROM {TABELA_USUARIOS}
            WHERE email = ?
            """,
                (
                    email,
                )
            )
        
        resultado = cursor.fetchone()

        return resultado

    except Exception as erro:
        print("Erro ao buscar por e-mail: ", erro)
        return
    
    finally:
        if conexao:
            conexao.close()
