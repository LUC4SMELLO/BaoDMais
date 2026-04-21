from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_ITENS

class ItemModel:
    def __init__(self):
        pass

    @staticmethod
    def buscar_item(id, id_estabelecimento):
        
        conexao = None
        try:
            conexao = conectar_banco_dados_principal()
            cursor = conexao.cursor()

            cursor.execute(
                f"""
                SELECT
                nome,
                descricao,
                preco
                FROM {TABELA_ITENS}
                WHERE id = ? AND id_estabelecimento = ?
                """,
                    (
                        id,
                        id_estabelecimento
                    )
                )
            
            resultado = cursor.fetchone()
            
            return resultado

        except Exception as erro:
            print("Erro ao buscar item: ", erro)
            return
        
        finally:
            if conexao:
                conexao.close()
