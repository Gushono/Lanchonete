
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app import db, ma


class Usuario(db.Model):
    __tablename__ = 'tb_usuario'

    id = db.Column(db.Integer, primary_key=True)

    id_perfil = db.Column('id_perfil', db.Integer, db.ForeignKey("tb_perfil.id"))
    perfil = db.relationship('Perfil', foreign_keys=[id_perfil])

    id_pessoa = db.Column('id_pessoa', db.Integer, db.ForeignKey("tb_pessoa.id"))
    pessoa = db.relationship('Pessoa', foreign_keys=[id_pessoa])

    senha = db.Column(db.String)

    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "id_perfil",
            "id_pessoa",
            "senha",
            "created_at",
            "updated_at"
        )


def __init__(self, id_perfil, id_pessoa, senha):
    self.id_perfil = id_perfil
    self.id_pessoa = id_pessoa
    self.senha = senha
