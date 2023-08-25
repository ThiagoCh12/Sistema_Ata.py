import sqlite3


def Pesquisar_ata():
    print("\n=========PESQUISAR ATA========\n")
    palavra_chave = input("Digite a palavra chave da ata: ")
    con = sqlite3.connect('atas.db')
    cursor = con.cursor()
    consulta = """SELECT * FROM tabAta WHERE palavra_chave LIKE?"""
    cursor.execute(consulta, ('%' + palavra_chave + '%',))

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


def Pesquisar_pessoa():

    print("\n=========PESQUISAR PESSOA========\n")
    matricula = input("Digite a matricula da pessoa: ")
    con = sqlite3.connect('atas.db')
    cursor = con.cursor()
    consulta = """SELECT * FROM tabPessoa WHERE matricula LIKE?"""
    cursor.execute(consulta, ('%' + matricula + '%',))

    registros = cursor.fetchone()
    if registros:

        print("Detalhes do usuario:")
        print(f"Nome: {registros[1]}")
        print(f"Matricula: {registros[2]}")
        print(f"Sexo: {registros[3]}")
        print(f"Empresa: {registros[4]}")
        print(f"Data nascimento: {registros[5]}")
        print(f"Email: {registros[6]}")
        print(f"Funcao: {registros[7]}")
        
    else:
        print("Nenhum registro correspondente encontrado.")
    cursor.close()
    con.close()
    return

