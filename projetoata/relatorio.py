import sqlite3, os

def Relatorio_atas():
    conexao = sqlite3.connect('atas.db')
    cursor = conexao.cursor()

   
    consulta_atas = "SELECT * FROM tabAta"
    cursor.execute(consulta_atas)

    atas = cursor.fetchall()

    # Consulta SQL para selecionar todas as sugestões
    consulta_sugestao = "SELECT * FROM tabSugestao"
    cursor.execute(consulta_sugestao)

    sugestoes = cursor.fetchall()

    # Exibir relatório de atas
    if atas:
        os.system('cls')
        print("Relatório das atas registradas:")
        for ata in atas:
            print(f"Título: {ata[1]}")
            print(f"Data: {ata[2]}")
            print(f"Início: {ata[3]}")
            print(f"Término: {ata[4]}")
            print(f"Pauta: {ata[5]}")
            print(f"Descrição: {ata[6]}")
            print(f"Palavra-chave: {ata[7]}")
            print("-" * 30)
    else:
        print("Nenhuma ata encontrada.")

    if sugestoes:
        print("Relatório de Sugestões:")
        for sugestao in sugestoes:
            id_sugestao = sugestao[0]
            id_ata = sugestao[1]
            titulo_ata = Titulo_ata(id_ata)
            matricula_pessoa = sugestao[2]
            texto_sugestao = sugestao[3]

            print(f"ID da Sugestão: {id_sugestao}")
            print(f"Título da ATA: {titulo_ata}")
            print(f"Matrícula da Pessoa: {matricula_pessoa}")
            print(f"Sugestão: {texto_sugestao}")
            print("-" * 30)
    else:
        print("Nenhuma sugestão encontrada.")

    conexao.close()

def Titulo_ata(id_ata):
    conexao = sqlite3.connect('atas.db')
    cursor = conexao.cursor()

    consulta = "SELECT titulo FROM tabAta WHERE id = ?"
    cursor.execute(consulta, (id_ata,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return resultado[0]
    else:
        return "Título não encontrado"



