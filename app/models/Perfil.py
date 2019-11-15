
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app import db, ma


class Perfil(db.Model):
    __tablename__ = 'tb_perfil'

    id = db.Column(db.Integer, primary_key=True)
    nome_perfil = db.Column(db.String)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())


class PerfilSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nome_perfil",
            "created_at",
            "updated_at"
        )


def __init__(self, nome_perfil):
    self.nome_perfil = nome_perfil
