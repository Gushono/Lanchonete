
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app import db, ma


class Produto(db.Model):
    __tablename__ = 'tb_produto'

    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String)
    qtd_produto = db.Column(db.Integer)
    preco_venda_unidade = db.Column(db.Float)

    enum_produto_ingrediente = db.Column('id_tipo', db.Integer, db.ForeignKey("tb_enum_produto_ingreditente.id"))
    produto_ingrediente = db.relationship('EnumProdutoIngrediente', foreign_keys=[enum_produto_ingrediente])

    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())
    updated_by = db.Column(db.String)


class ProdutoSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nome_produto",
            "qtd_produto",
            "preco_venda_unidade",
            "produto_ingrediente",
            "created_at",
            "updated_at"
        )


def __init__(self, nome_produto, qtd_produto, preco_venda_unidade):
    self.nome_produto = nome_produto
    self.qtd_produto = qtd_produto
    self.preco_venda_unidade = preco_venda_unidade
