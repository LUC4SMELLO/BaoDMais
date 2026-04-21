from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_CATEGORIAS, TABELA_ESTABELECIMENTOS


def criar_tabela_categorias():
    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_CATEGORIAS} (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(100),
        id_estabelecimento INTEGER,
        FOREIGN KEY (id_estabelecimento) REFERENCES {TABELA_ESTABELECIMENTOS} (id)
        )
        """
    )

    conexao.commit()
    conexao.close()
