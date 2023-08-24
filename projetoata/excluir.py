import sqlite3


def Excluir_ata():
    conexao = sqlite3.connect("atas.db")
    cursor = conexao.cursor()


    palavra_chave = input("Digite a palavra-chave do registro que deseja excluir: ")


    consulta_selecao = """
SELECT * FROM tabAta
WHERE palavra_chave = ?
"""


    cursor.execute(consulta_selecao, (palavra_chave,))
    registro = cursor.fetchone()

    if registro:
    
        print("Detalhes do Registro:")
        print(f"Título: {registro[1]}")
        print(f"Data: {registro[2]}")
        print(f"Início: {registro[3]}")
        print(f"Término: {registro[4]}")
        print(f"Pauta: {registro[5]}")
        print(f"Descrição: {registro[6]}")
    
    
        confirmacao = input("Tem certeza que deseja excluir este registro? (s/n): ").lower()
    
        if confirmacao == "s":
        
            consulta_exclusao = """
        DELETE FROM tabAta
        WHERE palavra_chave = ?
        """
        
        
            cursor.execute(consulta_exclusao, (palavra_chave,))
        
        # Commit para salvar as alterações no banco de dados
            conexao.commit()
        
            print("Registro excluído com sucesso.")
        else:
            print("Exclusão cancelada.")
    else:
        print("Nenhum registro correspondente encontrado para exclusão.")

# Fechar a conexão com o banco de dados
    conexao.close()

    return