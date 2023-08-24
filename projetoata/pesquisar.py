import sqlite3


def Pesquisar_ata():
    print("\n=========PESQUISAR ATA========\n")
    palavra_chave = input("Digite a palavra chave da ata: ")
    con = sqlite3.connect('atas.db')
    cursor = con.cursor()
    consulta = """SELECT * FROM tabAta WHERE palavra_chave LIKE?"""
    cursor.execute(consulta, ('%' + palavra_chave + '%',))
    nomes_colunas = [descricao[0] for descricao in cursor.description]

    registros = cursor.fetchone()
    if registros:

        print("Detalhes da Ata:")
        print(f"Título: {registros[1]}")
        print(f"Data: {registros[2]}")
        print(f"Início: {registros[3]}")
        print(f"Término: {registros[4]}")
        print(f"Pauta: {registros[5]}")
        print(f"Descrição: {registros[6]}")
        print(f"Palavra-chave: {registros[7]}")
        
    else:
        print("Nenhum registro correspondente encontrado.")
    cursor.close()
    con.close()
    return

