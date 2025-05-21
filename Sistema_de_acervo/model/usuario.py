from model.db.db import BaseModel
from peewee import CharField, IntegerField


class Usuario(BaseModel):
    id_usuario = IntegerField(primary_key=True)
    nome = CharField()
    username = CharField()
    senha = CharField()