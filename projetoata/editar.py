import sqlite3

def Editar_ata():
    
    conexao = sqlite3.connect("atas.db")
    cursor = conexao.cursor()


    palavra_chave = input("Digite a palavra-chave da ata que deseja editar: ")


    consulta_pesquisa = """
SELECT * FROM tabAta
WHERE palavra_chave LIKE ?
"""

    cursor.execute(consulta_pesquisa, ('%' + palavra_chave + '%',))
    ata_encontrada = cursor.fetchone()

    if ata_encontrada:

        print("Detalhes da Ata:")
        print(f"Título: {ata_encontrada[1]}")
        print(f"Data: {ata_encontrada[2]}")
        print(f"Início: {ata_encontrada[3]}")
        print(f"Término: {ata_encontrada[4]}")
        print(f"Pauta: {ata_encontrada[5]}")
        print(f"Descrição: {ata_encontrada[6]}")
        print(f"Palavra-chave: {ata_encontrada[7]}")

        novo_titulo = input("Novo Título: ")
        nova_data = input("Nova Data (AAAA-MM-DD): ")
        novo_inicio = input("Novo Início (HH:MM): ")
        novo_termino = input("Novo Término (HH:MM): ")
        nova_pauta = input("Nova Pauta: ")
        nova_descricao = input("Nova Descrição: ")
    
        consulta_atualizacao = """
UPDATE tabAta
SET titulo=?, data_emissao=?, inicio=?, termino=?, pauta=?, descricao=?
WHERE palavra_chave=?"""
    
        cursor.execute(consulta_atualizacao, (novo_titulo, nova_data, novo_inicio, novo_termino, nova_pauta, nova_descricao, palavra_chave))
    

        conexao.commit()
    
        print("Ata atualizada com sucesso.")
    else:
        print("Nenhuma ata correspondente encontrada.")

    cursor.close()
    conexao.close()

