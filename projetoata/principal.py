import cadastrar, emitir, editar, pesquisar, excluir

resposta = 's'
while(resposta == 's'):

    menu = ('''=========== SISTEMA ATAS ===========
          \r[1] CADASTRAR MEMBRO               |
          \r[2] EMITIR ATA                     |
          \r[3] EXCLUIR ATA                    |
          \r[4] EDITAR ATA                     |
          \r[5] PESQUISAR ATA                  |
          \r====================================''')
    
    print(menu)

    opcao = int(input('\nDigite uma opção: '))
   
    if opcao == 1:
            cadastrar.Cadastrar_membro()
    elif opcao == 2:
            emitir.Emitir_ata()
    elif opcao == 3:
            excluir.Excluir_ata()
    elif opcao == 4:
            editar.Editar_ata()
    elif opcao == 5:
            pesquisar.Pesquisar_ata()
    elif opcao == 6:
            print("6")
    elif opcao == 7:
            print("7")
    elif opcao == 8:
            print("8")
    elif opcao == 9:
            print("9")
    else:
        print("\nOpção inválida\n")
    resposta = input("Deseja continuar? (s/n): ").lower()


        
