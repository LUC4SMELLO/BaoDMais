import sqlite3

from constants.banco_dados import BANCO_DADOS_ESTABELECIMENTOS, TABELA_ESTABELECIMENTOS


def conectar_banco_dados_estabelecimento():
    return sqlite3.connect(BANCO_DADOS_ESTABELECIMENTOS)

def criar_tabela_estabelecimentos():
    conexao = conectar_banco_dados_estabelecimento()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_ESTABELECIMENTOS} (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(100),
        tipo TEXT,
        avaliacao TEXT,
        pedido_minimo TEXT,
        tempo_delivery TEXT
        )
        """
    )

    conexao.commit()
    conexao.close()
