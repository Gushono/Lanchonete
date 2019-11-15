import datetime

from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app import db, ma


class Pessoa(db.Model):
    __tablename__ = 'tb_pessoa'

    id = db.Column(db.Integer, primary_key=True)
    nome_pessoa = db.Column(db.String)
    email = db.Column(db.String)
    nr_documento = db.Column(db.String)
    id_endereco = db.Column(db.String)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())


class PessoaSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id",
            "nome_pessoa",
            "email",
            "nr_documento",
            "id_endereco",
            "created_at",
            "updated_at"
        )


def __init__(self, nome_pessoa, email, nr_documento, id_endereco):
    self.nome_pessoa = nome_pessoa
    self.email = email
    self.nr_documento = nr_documento
    self.id_endereco = id_endereco


def __repr__(self):
    return "<nome %r " % self.nome_pessoa
