from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_ITENS, TABELA_ESTABELECIMENTOS, TABELA_CATEGORIAS


def criar_tabela_itens():
    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_ITENS} (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(100),
        descricao TEXT,
        preco REAL,
        id_estabelecimento INTEGER,
        id_categoria INTEGER,
        FOREIGN KEY (id_estabelecimento) REFERENCES {TABELA_ESTABELECIMENTOS} (id),
        FOREIGN KEY (id_categoria) REFERENCES {TABELA_CATEGORIAS} (id)
        )
        """
    )

    conexao.commit()
    conexao.close()
