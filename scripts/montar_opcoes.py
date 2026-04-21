from database.banco_dados_principal import conectar_banco_dados_principal
from constants.banco_dados import TABELA_OPCOES, TABELA_OPCOES_VALORES


def montar_opcoes(id_item):

    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute(
        f"""
        SELECT 
            o.id,
            o.nome,
            v.id,
            v.nome,
            v.preco

        FROM {TABELA_OPCOES} o
        LEFT JOIN {TABELA_OPCOES_VALORES} v ON v.id_opcao = o.id
        WHERE o.id_item = ?
        ORDER BY o.id;
        """,
            (
                id_item,
            )
        )

    resultados = cursor.fetchall()
    conexao.close()

    opcoes = {}

    for row in resultados:
        opcao_id = row[0]
        opcao_nome = row[1]

        if opcao_id not in opcoes:
            opcoes[opcao_id] = {
                "nome": opcao_nome,
                "itens": []
            }

        if row[2]:
            opcoes[opcao_id]["itens"].append({
                "nome": row[3],
                "preco": row[4]
            })

    return opcoes
