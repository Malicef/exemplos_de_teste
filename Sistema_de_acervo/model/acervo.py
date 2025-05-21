from model.db.db import BaseModel
from model.usuario import Usuario
from peewee import *

class Acervo(BaseModel):
    id_acervo = IntegerField(primary_key=True)
    usuario = ForeignKeyField(Usuario, backref='acervos')