from marshmallow import fields
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app import db, ma
from app.models.Permissoes import PermissoesSchema


class PermissaoPerfil(db.Model):
    __tablename__ = 'tb_permissao_perfil'

    id = db.Column(db.Integer, primary_key=True)

    id_perfil = db.Column('id_perfil', db.Integer, db.ForeignKey("tb_perfil.id"))
    perfil = db.relationship("Perfil", foreign_keys=[id_perfil])

    id_permissao = db.Column('id_permissao', db.Integer, db.ForeignKey("tb_permissoes.id"))
    permissoes = db.relationship('Permissoes', foreign_keys=[id_permissao])

    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())


class PermissaoPerfilSchema(ma.Schema):
    permissoes = fields.Nested(PermissoesSchema)

    class Meta:
        fields = (
            "id",
            "id_perfil",
            "permissoes"
        )


def __init__(self, id_perfil, id_permissao):
    self.id_perfil = id_perfil
    self.id_permissao = id_permissao
