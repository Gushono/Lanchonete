
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app import db, ma


class Permissoes(db.Model):
    __tablename__ = 'tb_permissoes'

    id = db.Column(db.Integer, primary_key=True)
    nome_permissao = db.Column(db.String)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())


class PermissoesSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nome_permissao",
            "created_at",
            "updated_at"
        )


def __init__(self, nome_permissao):
    self.nome_permissao = nome_permissao
