
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app import db, ma


class EnumProdutoIngrediente(db.Model):
    __tablename__ = 'tb_enum_produto_ingrediente'

    id = db.Column(db.Integer, primary_key=True)
    nome_enum = db.Column(db.String)

    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())


class EnumProdutoIngredienteSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nome_enum",
            "created_at",
            "updated_at"
        )


def __init__(self, nome_enum):
    self.nome_enum = nome_enum
