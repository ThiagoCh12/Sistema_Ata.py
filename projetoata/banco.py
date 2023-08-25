import sqlite3 as sql

con = sql.connect("atas.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE tabAta(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                titulo TEXT, 
                data_emissao DATE, 
                inicio DATE, 
                termino DATE,
                pauta TEXT, 
                descricao TEXT, 
                palavra_chave TEXT
                
                )''')



cursor.execute('''CREATE TABLE tabPessoa(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                matricula INTEGER UNIQUE,
                sexo TEXT,
                empresa TEXT,
                data_nascimento DATE,
                email TEXT,
                funcao TEXT           
                ) ''')



cursor.execute('''
    CREATE TABLE IF NOT EXISTS tabSugestao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_ata INTEGER,
        matricula_pessoa TEXT,
        texto_sugestao TEXT,
        FOREIGN KEY (id_ata) REFERENCES tabAta(titulo),
        FOREIGN KEY (matricula_pessoa) REFERENCES tabPessoa(matricula)
    )''')
                
con.commit()
cursor.close()
con.close()