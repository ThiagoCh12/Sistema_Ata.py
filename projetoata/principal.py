

resposta = 's'
while(resposta == 's'):

    menu = ('''=========== SISTEMA ATAS ===========
          \r[1] CADASTRAR MEMBRO               |
          \r[2] EMITIR ATA                     |
          \r[3] EMITIR RELÓRIO                 |
          \r[4] CONCLUIR ATA                   |
          \r[5] CONSULTAR ATA                  |
          \r====================================''')
    
    print(menu)

    opcao = input('\nDigite uma opção: ')
    verificacao = str.isnumeric(opcao)

    if verificacao is True:
        if opcao == 1:
            print("1")
        elif opcao == 2:
            print("2")
        elif opcao == 3:
            print("3")
        elif opcao == 4:
            print("4")
        elif opcao == 5:
            print("5")
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


        
