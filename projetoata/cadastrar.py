import datetime
import sqlite3
import os

def Cadastrar_membro():
    opcao = int(input('''+------------------------+
|[1]-Participante externo|
|[2]-Funcionario         |
+------------------------+
Seleciona uma funçao: '''))
    
    if opcao == 1:
        funcao = 'participante_externo'
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        empresa = input("Digite o nome da sua empresa: ")
        con = sqlite3.connect("atas.db")
        cursor = con.cursor()
        cursor.execute('''INSERT INTO tabPessoa(funcao, nome, email, empresa) VALUES (?,?,?,?)''', (funcao, nome, email, empresa))
        con.commit()
        cursor.close()
        con.close()

    elif opcao == 2:
        os.system('cls') or None
        opc = int(input('''+------------------------+
|[1]- Administrador      |
|[2]- Funcionário        |
|[3]- Emissor            |
+------------------------+
Digite sua funcao: '''))
        if opc <=3:
            if opc == 1:
                funcao = "administrador"
            if opc == 2:
                funcao = "funcionario"
            else:
                funcao = "emissor"
            nome = input("Digite seu nome: ")
            matricula = int(input("Digite sua matricula: "))
    
            sexo = input("Digite seu sexo (m/f): ")
            while True:
                data_nasc = input("Digite sua data de nascimento (YYYY-MM-DD): ")
                try:
                    data_nasc = datetime.datetime.strptime(data_nasc, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Formato de data inválido!")
                    continue
                break
            email = input("Digite seu email: ")
            con = sqlite3.connect("atas.db")
            cursor = con.cursor()
            cursor.execute('''INSERT INTO tabPessoa(funcao, nome, email, matricula, sexo, data_nascimento) VALUES (?,?,?,?,?,?)''', (funcao, nome, email, matricula, sexo, data_nasc))
            con.commit()
            cursor.close()
            con.close()
    else:
        print("Opção inválida!\n")
        return Cadastrar_membro()
    return 0
    
