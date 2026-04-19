import sqlite3

from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_ESTABELECIMENTOS


def criar_tabela_estabelecimentos():
    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABELA_ESTABELECIMENTOS} (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(100),
        tipo TEXT,
        avaliacao TEXT,
        pedido_minimo TEXT,
        tempo_delivery TEXT,
        caminho_foto TEXT
        )
        """
    )

    conexao.commit()
    conexao.close()
