import sqlite3 as sql

con = sql.connect("atas.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE tabAta(
                tbId INTEGER PRIMARY KEY, 
                tbTitulo TEXT, 
                tbData_emissao DATE, 
                tbInicio DATE, 
                tbTermino DATE,
                tbPauta TEXT, 
                tbDescricao TEXT, 
                tbPalavra_chave TEXT
                )''')

cursor.execute('''CREATE TABLE tabPessoa(
                tbId INTEGER PRIMARY KEY,
                tbNome TEXT,
                tbMatricula INTEGER,
                tbSexo TEXT,
                tbData_nascimento DATE,
                tbEmail TEXT) ''')

cursor.execute('''CREATE TABLE tabFuncao(tbFunc TEXT)

                ''')


con.commit()
cursor.close()
con.close()