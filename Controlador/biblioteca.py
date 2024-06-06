from Modelo import livros, membros


class Biblioteca:
    def __init__(self):
        self.catalogo_de_livros = []
        self.registro_de_membros = []

    def adicionar_livro_ao_catalogo(self):
        while True:
            try:
                titulo_do_livro = input("Insira o título do livro: ").capitalize()
                autor_do_livro = input("Insira o nome do autor do livro: ").capitalize()
                id_do_livro = input("Insira o código do livro: ")

                if not (titulo_do_livro and autor_do_livro and id_do_livro):
                    raise ValueError("Por favor, preencha todos os campos.")
                novo_livro = livros.Livro(titulo_do_livro, autor_do_livro, id_do_livro)
                self.catalogo_de_livros.append(novo_livro)
                return "Livro cadastrado com sucesso!"

            except ValueError as error:
                print(error)

    def cadastrar_membro(self):
        while True:
            try:
                nome_do_membro = input("Insira o nome do membro: ").capitalize()
                numero_do_membro = input("Insira o numero de membro: ")

                if not (nome_do_membro and numero_do_membro):
                    raise ValueError("Por favor, preencha todos os campos.")
                novoMembro = membros.Membro(nome_do_membro, numero_do_membro)
                self.registro_de_membros.append(novoMembro)
                return "Membro cadastrado com sucesso!"

            except ValueError as error:
                print(error)

    def registrar_emprestimo_de_livro(self):
        locatario = input("Insira o nome do membro que vai alugar o livro: ").capitalize()
        membro_encontrado = None
        for membro in self.registro_de_membros:
            if membro.nome == locatario:
                membro_encontrado = membro
                break
        if not membro_encontrado:
            return "Membro não encontrado no cadastro"

        livro_a_ser_alugado = input("Insira o título do livro que será alugado: ").capitalize()
        livro_encontrado = None
        for livro in self.catalogo_de_livros:
            if livro.titulo == livro_a_ser_alugado:
                livro_encontrado = livro
                break
        if not livro_encontrado:
            return "Livro não encontrado no cadastro"

        livro_encontrado.status_de_emprestimo = "emprestado"
        membro_encontrado.historico_de_livros_emprestados.append(livro_encontrado)
        return "O aluguel do livro foi realizado com sucesso!"

    def registrar_devolucao_de_livro(self):
        locatario = input("Insira o nome do membro que vai alugar o livro: ").capitalize()
        membro_encontrado = None
        for membro in self.registro_de_membros:
            if membro.nome == locatario:
                membro_encontrado = membro
                break
        if not membro_encontrado:
            return "Membro não encontrado no cadastro"

        livro_a_ser_devolvido = input("Insira o título do livro que será devolvido: ").capitalize()
        livro_encontrado = None
        for livro in membro_encontrado.historico_de_livros_emprestados:
            if livro.titulo == livro_a_ser_devolvido:
                livro_encontrado = livro
                break
        if not livro_encontrado:
            return "Livro não encontrado no histórico do usuário"

        livro_encontrado.status_de_emprestimo = "disponível"
        return "A devolução do livro foi realizada com sucesso!"

    def mostrar_livros_disponiveis(self):
        if len(self.catalogo_de_livros) > 0:
            for livro in self.catalogo_de_livros:
                if livro.status_de_emprestimo != "emprestado":
                    print(livro.__dict__)

        else:
            print("Nenhum livro consta no cadastro")

    def consultar_livro(self):
        chave_de_consulta = input("Insira o título do livro ou código que deseja consultar: ").capitalize()

        for livro in self.catalogo_de_livros:
            if livro.titulo == chave_de_consulta or livro.id == chave_de_consulta:
                return livro.__dict__

            else:
                return "Livro não encontrado"
