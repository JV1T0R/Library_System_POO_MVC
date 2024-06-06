from Controlador import biblioteca

biblioteca = biblioteca.Biblioteca()

while True:
    print('''
    ----BEM VINDO A BIBLIOTECA----    
    [1] Adicionar livro ao catálogo
    [2] Cadastrar membro
    [3] Registrar empréstimo de livro
    [4] Registrar devolução de livro
    [5[ Consultar Livro
    [6] Sair
    ------------------------------ 
    ''')
    opcao = int(input("insira o número da opção para executa-la: "))

    if opcao == 1:
        print("\n----CADASTRO DE LIVRO----\n")
        print(biblioteca.adicionar_livro_ao_catalogo())
        print("\n-------------------------\n")

    elif opcao == 2:
        print("\n----CADASTRO DE MEMBRO----\n")
        print(biblioteca.cadastrar_membro())
        print("\n--------------------------\n")

    elif opcao == 3:
        print("\n----EMPRÉSTIMO DE LIVRO----\n")
        print(biblioteca.registrar_emprestimo_de_livro())
        print("\n---------------------------\n")

    elif opcao == 4:
        print("\n----DEVOLUÇÃO DE LIVRO----\n")
        print(biblioteca.registrar_devolucao_de_livro())
        print("\n--------------------------\n")

    elif opcao == 5:
        while True:
            print('''
            ----CONSULTAR LIVRO----    
            [1] Ver todos os livros disponíveis
            [2] Consultar livro por título ou código
            [3] Sair
            ----------------------- 
            ''')
            sub_opcao = int(input("insira o número da opção para executa-la: "))

            if sub_opcao == 1:
                print("\n----CONSULTAR LIVRO----\n")
                biblioteca.mostrar_livros_disponiveis()
                print("\n--------------------------\n")

            elif sub_opcao == 2:
                print("\n----CONSULTAR LIVRO----\n")
                print(biblioteca.consultar_livro())
                print("\n-----------------------\n")

            elif sub_opcao == 3:
                break

            else:
                print("Opção Invalida")

    elif opcao == 6:
        print("Sistema Encerrado.")
        break

    else:
        print("Opção Invalida")