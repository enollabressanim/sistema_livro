class Sistema():
    def __init__(self, titulo= str, autor=str, emprestimo= str, estado= str, assunto= str, arq= str):
        self.titulo = titulo
        self.autor = autor
        self.emprestimo= emprestimo
        self.estado = estado
        self.assunto = assunto
        self.arq = arq
        self.livros_cadastrados = []

    def verificar_sistema(self, titulo=str):
        for livro in self.livros_cadastrados:
            if livro["titulo"] == titulo:
                return livro
        return None

    def cadastrar_livro(self, titulo= str, autor= str, emprestimo= str, estado= str, assunto= str):
        if self.verificar_sistema(titulo) is None:
            livros = {"titulo":titulo,
                      "autor": autor,
                      "emprestimo": emprestimo,
                      "estado": estado,
                      "assunto": assunto} 
            self.livros_cadastrados.append(livros)
            print('Livro cadastrado com sucesso!')
            print(self.livros_cadastrados)
            return True
        else:
            print('Livro já cadastrado!')
            return False
        pass

    def salvar_arquivo(self, arq= str):
        arquivo = open(arq, "a")
        letra = str(self.livros_cadastrados) + '\n'
        arquivo.write(letra)
        arquivo.close()
        print('Arquivo salvo com sucesso')
        return arquivo

    def remover_livro(self, titulo= str):
        livro = self.verificar_sistema(titulo)
        if livro is None:
            print("Livro inexistente")
            return False
        else:
            self.livros_cadastrados.remove(livro)
            print("Livro removido")
            return True

    def buscar_autor(self, autor= str):
        pass

    def atualizar_livro(self, titulo= str):
        if self.remover_livro(titulo):
            self.cadastrar_livro()
            return True
        return False

class Menu():
    def __init__(self):
        self.sistema = Sistema()

    def imprimir_commandos(self):
        print(" ")
        print("1 - Cadastrar Livro")
        print("2 - Remover Livro")
        print("3 - Atualizar informação de livro")
        print("4 - Buscar livros por autor")
        print("5 - Salvar e Sair")

    def main(self):
        self.imprimir_commandos()
        opcao = int(input("Digite uma opção acima: "))
        while opcao != 6:
            if opcao == 1:
                titulo = input("titulo: ")
                autor = input("autor: ")
                emprestimo = input("emprestimo: ")
                estado = input("estado: ")
                assunto = input("assunto: ")
                self.sistema.cadastrar_livro(titulo, autor, emprestimo, estado, assunto)

            elif opcao == 2:
                titulo = input('titulo que deseja remover: ')
                self.sistema.remover_livro(titulo)

            elif opcao == 3:
                titulo = input('Titulo que desejas atualizar: ')
                self.sistema.atualizar_livro(titulo)
            
            elif opcao == 4:
                pass
            
            elif opcao == 5:
                arq = input('digite o nome do arquivo: ')
                self.sistema.salvar_arquivo(arq)

            self.imprimir_commandos()
            opcao = int(input("Digite uma opção acima: "))


if __name__ == "__main__":
    g = Menu()
    g.main()