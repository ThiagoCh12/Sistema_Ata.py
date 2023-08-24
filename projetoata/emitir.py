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
        

