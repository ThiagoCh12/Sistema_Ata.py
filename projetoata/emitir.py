import datetime, sqlite3



def verificacao(fim):
    try:
        datetime.datetime.strptime(fim, '%H:%M')
        return True
    except ValueError:
        return False
    


def Emitir_ata():
    matricula = int(input("Digite sua matricula:"))

    con = sqlite3.connect('atas.db')
    cursor = con.cursor()

    cursor.execute("SELECT funcao FROM tabPessoa WHERE matricula=?", (matricula,))
    resultado = cursor.fetchone()
    if resultado == None:
        print("Você não tem permissão para emitir ata.")
    cargo_usuario = resultado[0]
    cargos = ['emissor']
    if cargo_usuario in cargos:
        titulo = input("Digite o titulo da ata: ")
        data = datetime.datetime.today()
    while True:
        inicio = input("Digite a hora de inicio da ata (HH:MM): ")
        fim = input("Digite a hora de fim da ata (HH:MM): ")
        if verificacao(fim):
            inicio = datetime.datetime.strptime(inicio, '%H:%M').strftime("%H:%M")
            fim = datetime.datetime.strptime(fim, '%H:%M').strftime("%H:%M")
            if inicio < fim:               
                pauta = input("Digite a pauta da ata: ")
                descricao = input("Digite a descricao da ata: ")
                palavra_chave = input("Digite a palavra chave da ata: ")

                cursor.execute('''INSERT INTO tabAta (titulo, data_emissao, inicio, termino, pauta, descricao, palavra_chave)
VALUES (?, ?, ?, ?, ?, ?, ?)''',(titulo, data, inicio, fim, pauta, descricao, palavra_chave))
                con.commit()
                cursor.close()
                con.close()
                print("Ata emitida com sucesso.")
                break
            else:
                print("A hora de fim deve ser posterior à hora de início.")
        else:
            print("Formato de hora inválido. Por favor, use o formato HH:MM.")
        


        
def Emitir_sugestao():
    conexao = sqlite3.connect('atas.db')
    cursor = conexao.cursor()
    matricula_usuario = input("Digite sua matrícula: ")

    consulta_verificacao = "SELECT * FROM tabPessoa WHERE matricula = ?"
    cursor.execute(consulta_verificacao, (matricula_usuario,))
    pessoa_existente = cursor.fetchone()

    if not pessoa_existente:
        print("Matrícula não encontrada. Verifique sua matrícula e tente novamente.")
        conexao.close()
        return

    titulo_ata = input("Digite o título da ATA: ")

    consulta_verificacao = "SELECT * FROM tabAta WHERE titulo = ?"
    cursor.execute(consulta_verificacao, (titulo_ata,))
    ata_existente = cursor.fetchone()

    if not ata_existente:
        print("Título da ATA não encontrado. Verifique o título e tente novamente.")
        conexao.close()
        return

    texto_sugestao = input("Digite sua sugestão: ")

    cursor.execute("""
    INSERT INTO tabSugestao (id_ata, matricula_pessoa, texto_sugestao)
    VALUES (?, ?, ?)
    """, (ata_existente[0], matricula_usuario, texto_sugestao))
    conexao.commit()
    conexao.close()
    print("Sugestão inserida com sucesso.")


    