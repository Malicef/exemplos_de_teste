from model.usuario import Usuario
from peewee import DoesNotExist

class UsuarioController:
    @staticmethod
    def criarUsuario(nome : str, username : str, senha : str) -> Usuario:
        return Usuario.create(nome= nome, username=username, senha= senha)

    @staticmethod
    def autenticar(username : str, senha : str) -> bool:
        try:
            usuario = Usuario.get(Usuario.username == username, Usuario.senha == senha) 
            return True, usuario
        except DoesNotExist:
            return False

# ! Defeito Injetado: Na View espera-se que retorne duas variaveis, mas na exceçãao retorna apenas uma