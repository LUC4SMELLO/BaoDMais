from database.banco_dados_principal import conectar_banco_dados_principal


def montar_cardapio(id_estabelecimento):
    conexao = conectar_banco_dados_principal()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT 
            c.id,
            c.nome,
            i.id,
            i.nome,
            i.descricao,
            i.preco
        FROM categorias c
        LEFT JOIN itens i 
            ON i.id_categoria = c.id
            AND i.id_estabelecimento = c.id_estabelecimento
        WHERE c.id_estabelecimento = ?
        ORDER BY c.nome, i.nome
        """, (id_estabelecimento,)
    )

    resultados = cursor.fetchall()

    cardapio = {}

    for row in resultados:
        categoria_id = row[0]
        categoria_nome = row[1]

        if categoria_id not in cardapio:
            cardapio[categoria_id] = {
                "nome": categoria_nome,
                "itens": []
            }

        if row[2]:
            cardapio[categoria_id]["itens"].append({
                "id": row[2],
                "nome": row[3],
                "descricao": row[4],
                "preco": row[5]
            })

    return cardapio
