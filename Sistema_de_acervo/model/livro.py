from model.db.db import BaseModel
from model.usuario import Usuario
from peewee import CharField, IntegerField, ForeignKeyField
from model.acervo import Acervo

class Livro(BaseModel):
    """Modelo de Livro"""
    id_livro = IntegerField(primary_key=True)
    titulo = CharField()
    autor = CharField()
    dataLancamento = CharField()
    genero = CharField()
    dono = ForeignKeyField(Usuario, backref='usuario')
    acervo = ForeignKeyField(Acervo, backref='livros')

  

