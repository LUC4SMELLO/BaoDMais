from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_USUARIOS


class UsuarioModel:
    def __init__(self):
        pass

    @staticmethod
    def inserir_usuario(nome, email, senha):
        
        conexao = None
        try:
            conexao = conectar_banco_dados_principal()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_USUARIOS} (
                    nome,
                    email,
                    senha
                )
                VALUES (?, ?, ?)
                """,
                    (
                        nome,
                        email,
                        senha
                    )
                )
            
            conexao.commit()

        except Exception as erro:
            print("Erro ao inserir usuário: ", erro)
            return

        finally:
            if conexao:
                conexao.close()


    @staticmethod
    def buscar_usuario(dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_principal()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                SELECT nome, email
                FROM {TABELA_USUARIOS}
                WHERE nome = ? AND email = ?
                """,
                    (
                        dados["nome"],
                        dados["email"]
                    )
                )
            
            resultado = cursor.fetchone()

            return resultado

        except Exception as erro:
            print("Erro ao inserir usuário: ", erro)
            return

        finally:
            if conexao:
                conexao.close()
