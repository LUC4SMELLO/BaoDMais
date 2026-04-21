from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_OPCOES_VALORES, TABELA_OPCOES, TABELA_ESTABELECIMENTOS


def criar_tabela_opcoes_valores():
    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_OPCOES_VALORES} (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(100),
        preco REAL,
        id_opcao INTEGER,
        id_estabelecimento INTEGER,
        FOREIGN KEY (id_opcao) REFERENCES {TABELA_OPCOES} (id),
        FOREIGN KEY (id_estabelecimento) REFERENCES {TABELA_OPCOES} (id)
        )
        """
    )

    conexao.commit()
    conexao.close()
