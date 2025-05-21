from model.acervo import Acervo
from peewee import DoesNotExist
from controller.livroController import LivroController
from model.usuario import Usuario
from model.livro import Livro


class AcervoController:
    @staticmethod
    def criarArcevo(usuario:Usuario) -> Acervo:
        try:
            return Acervo.create(usuario=usuario)
        except Exception as e:
            print("Erro inesperado!")

    @staticmethod
    def listarAcervo(usuario: Usuario) -> list:
        try:
            acervo = Acervo.get(Acervo.usuario == usuario)
            livros = Livro.select().where(Livro.acervo == acervo)

            lista = []
            for livro in livros:
                livro_info = LivroController.visualizarLivro(livro.id_livro)
                lista.append(livro_info)

            if not lista:
                print("Nenhum livro encontrado.")
                return []

            return lista
        except DoesNotExist:
            print("Acervo não encontrado.")
            return []
        except Exception as e:
            print(f"Erro ao listar acervo: {e}")
            return []

    @staticmethod
    def buscarArcevoPorUsuario(usuario: Usuario) -> Acervo:
        try:
            acervo = Acervo.get(Acervo.usuario == usuario)
            return acervo
        except DoesNotExist:
            print("Acervo não encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao buscar acervo: {e}")
            return None