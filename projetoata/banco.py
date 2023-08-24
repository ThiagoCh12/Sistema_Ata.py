import sqlite3 as sql

con = sql.connect("atas.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE tabAta(
                id INTEGER PRIMARY KEY, 
                titulo TEXT, 
                data_emissao DATE, 
                inicio DATE, 
                termino DATE,
                pauta TEXT, 
                descricao TEXT, 
                palavra_chave TEXT
                
                )''')



cursor.execute('''CREATE TABLE tabPessoa(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                matricula INTEGER UNIQUE,
                sexo TEXT,
                empresa TEXT,
                data_nascimento DATE,
                email TEXT,
                funcao TEXT           
                ) ''')

con.commit()
cursor.close()
con.close()