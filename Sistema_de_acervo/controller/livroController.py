from model.livro import Livro
from peewee import DoesNotExist
from model.usuario import Usuario
from model.acervo import Acervo

class LivroController:
    @staticmethod
    def criarLivro(titulo, autor, dataLancamento, genero, id_dono, id_acervo):
        try:
            dono = Usuario.get_by_id(id_dono)
            acervo = Acervo.get_by_id(id_acervo)
            livro = Livro.create(
                    titulo=titulo,
                    autor=autor, 
                    dataLancamento=dataLancamento,
                    genero=genero,
                    dono=dono,
                    acervo=acervo
                )

            return Livro
        except Exception as e:
            print(f"Erro ao criar livro: {e}")
            return None

    @staticmethod
    def excluirLivro(livro_id: int, usuario: Usuario): # ! Defeito: não exclui o livro
        try:
            livro = Livro.get_by_id(livro_id)
            if livro.dono == usuario:
                livro.delete_instance()
                return True
            else:
                print("Você não tem permissão para excluir este livro.")
                return False
        except Livro.DoesNotExist:
            print("Livro não encontrado.")
            return False
        except Exception as e:
            print(f"Erro ao excluir livro: {e}")
            return False@staticmethod

    @staticmethod
    def editarLivro(livro: Livro, **dados):
        try:
            livro = Livro.get_by_id(livro.id_livro)
            for chave, valor in dados.items():
                setattr(livro, chave, valor)
                print(chave, valor)
            livro.save()
        except Livro.DoesNotExist:
            print("Livro Não Encontrado!")
    
    @staticmethod
    def visualizarLivro(id_livro):
        try:
            livro = Livro.get_by_id(id_livro)
            dicionario = {
                "Titulo: ": livro.titulo,
                "Autor: ": livro.autor,
                "Data de lançamento: ": livro.dataLancamento,
                "Genero: ": livro.genero,
            }
            return dicionario
        except Livro.DoesNotExist:
            print("Livro não encontrado")

    @staticmethod
    def buscarLivroPorNome(livro: str, usuario: Usuario):
        try:
            acervo = Acervo.get(Acervo.usuario == usuario)
            livros = list(
                Livro.select().where(
                    Livro.titulo.contains(livro),  # ou: Livro.titulo.ilike(f"%{livro}%")
                    Livro.acervo == acervo
                )
            )
            return livros
        except DoesNotExist:
            print("Nenhum livro encontrado.")
            return []
        except Exception as e:
            print(f"Erro ao buscar livro: {e}")
            return []




