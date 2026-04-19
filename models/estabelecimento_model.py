from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_ESTABELECIMENTOS

class EstabelecimentoModel:
    def __init__(self):
        pass

    def inserir_estabelecimento(self, dados: dict):

        conexao = None
        try:
            conexao = conectar_banco_dados_principal()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                INSERT INTO {TABELA_ESTABELECIMENTOS} (
                    nome,
                    tipo,
                    avaliacao,
                    pedido_minimo,
                    tempo_delivery
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                    (
                        dados["nome"],
                        dados["tipo"],
                        dados["avaliacao"],
                        dados["pedido_minimo"],
                        dados["tempo_delivery"]
                    )
            )

            conexao.commit()
        
        except Exception as erro:
            print("Erro ao inserir estabelecimento: ", erro)
            return
        
        finally:
            if conexao:
                conexao.close()


    @staticmethod
    def buscar_estabelecimento(id):

        conexao = None
        try:
            conexao = conectar_banco_dados_principal()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                SELECT
                nome,
                tipo,
                avaliacao,
                pedido_minimo,
                tempo_delivery,
                caminho_foto
                FROM {TABELA_ESTABELECIMENTOS}
                WHERE id = ?
                """,
                (
                    id,
                )
            )

            resultado = cursor.fetchone()

            return resultado
            
        except Exception as erro:
            print("Erro ao buscar estabelecimento: ", erro)
            return
        
        finally:
            if conexao:
                conexao.close()


    @staticmethod
    def listar_estabelecimentos():

        conexao = None
        try:
            conexao = conectar_banco_dados_principal()
            cursor = conexao.cursor()

            cursor.execute(f"SELECT * FROM {TABELA_ESTABELECIMENTOS}")

            registros = cursor.fetchall()

            return registros
        
        except Exception as erro:
            print("Erro ao listar estabelecimentos: ", erro)
            return
        
        finally:
            if conexao:
                conexao.close()
