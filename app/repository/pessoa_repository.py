from app import db
from app.models.Pessoa import Pessoa


def pessoa_por_id(id_pessoa):
    return db.session.query(Pessoa). \
        filter(Pessoa.id == id_pessoa).first()
