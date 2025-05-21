
from controller.usuarioController import UsuarioController
from controller.livroController import LivroController
from controller.acervoController import AcervoController
from model.usuario import Usuario
from model.livro import Livro
from model.acervo import Acervo
from model.db.db import db


db.connect()
db.create_tables([Usuario, Acervo, Livro])


def menuLogin():
    while True:
        print("Sistema de Biblioteca")
        print("1. Criar Usuário")
        print("2. Autenticar Usuário") 
        print("3. Sair") 
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            username = input("Username: ")
            senha = input("Senha: ")
            usuario = UsuarioController.criarUsuario(nome, username, senha)
            acervo = AcervoController.criarArcevo(usuario)
            print(f"Usuário {usuario.nome} criado com sucesso!")

        elif opcao == "2":
            username = input("Username: ")
            senha = input("Senha: ")
            autenticado, usuario = UsuarioController.autenticar(username, senha)
            if autenticado:
                print(f"Usuário {usuario.nome} autenticado com sucesso!")
                return usuario
            else:
                print("Falha na autenticação!")

        elif opcao == "3":
            break

        else:
            print("Opção inválida! Tente novamente.")

def menuPrincipal(usuario):
    while True:
        print("Sistema de Biblioteca")
        print("1. Criar Livro")
        print("2. Editar Livro")
        print("3. Excluir Livro")
        print("4. Listar Livros")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            dataLancamento = input("Data de Lançamento: ")
            genero = input("Gênero: ")
            acervo = AcervoController.buscarArcevoPorUsuario(usuario)
            livro = LivroController.criarLivro(titulo, autor, dataLancamento, genero, usuario.id_usuario, acervo)

            livro = LivroController.visualizarLivro(livro.id_livro)
            if livro:
                print(f"Livro criado com sucesso!")

        elif opcao == "2":
            id_livro = int(input("ID do Livro: "))
            dados = {}
            titulo = input("Título (deixe em branco para não alterar): ")
            if titulo:
                dados["titulo"] = titulo
            autor = input("Autor (deixe em branco para não alterar): ")
            if autor:
                dados["autor"] = autor
            dataLancamento = input("Data de Lançamento (deixe em branco para não alterar): ")
            if dataLancamento:
                dados["dataLancamento"] = dataLancamento
            genero = input("Gênero (deixe em branco para não alterar): ")
            if genero:
                dados["genero"] = genero

            livro = LivroController.editarLivro(id_livro, **dados)
            if livro:
                print(f"Livro editado com sucesso!")

        elif opcao == "3":
            nomeLivro = input("Nome do Livro: ")
            livros = LivroController.buscarLivroPorNome(nomeLivro, usuario)
            if len(livros)==0: # ! Defeito injetado: livros == 0 faz com que o livro não seja encontrado
                print("Livro não encontrado.")
            else:
                if len(livros) > 1:
                    print("Vários livros encontrados:")
                    for i, l in enumerate(livros):
                        print(f"{i + 1}. ID: {l.id} | Título: {l.titulo} | Autor: {l.autor}")
                    try:
                        escolha = int(input("Escolha qual excluir (número): ")) - 1
                        if 0 <= escolha < len(livros):
                            livro_escolhido = livros[escolha]
                        else:
                            print("Escolha inválida.")
                            return
                    except ValueError:
                        print("Entrada inválida.")
                        return
                else:
                    livro_escolhido = livros[0]

                livro_excluido = LivroController.excluirLivro(livro_escolhido.id, usuario)
                if livro_excluido:
                    print("Livro excluído com sucesso!")


        elif opcao == "4":
            livros = AcervoController.listarAcervo(usuario)
            print("Livros no Acervo:")
            print("-" * 20)
            for livro in livros[1:]: # ! Defeito injetado: livros[1:] faz com que o primeiro livro não seja exibido
                for chave, valor in livro.items():
                    print(f"{chave} {valor}")
                    print("-" * 20)
                print()
            if not livros:
                print("Nenhum livro encontrado.")


        elif opcao == "5":
            break

        else:
            print("Opção inválida! Tente novamente.")

def main():
    usuario = menuLogin()
    if usuario:
        menuPrincipal(usuario)
    else:
        print("Nenhum usuário autenticado.")



if __name__ == "__main__":
    main()
    db.close()