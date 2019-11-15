from app.models.Pessoa import Pessoa
from app import db


def cadastra_pessoa_repository(body):
    i = Pessoa(nome_pessoa='teste')
    db.session.add(i)
    db.session.commit()

    return i
