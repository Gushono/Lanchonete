from app import db
from app.models.Pessoa import Pessoa
from app.models.Usuario import Usuario


def autentica_repository(email, senha):
    return db.session.query(Usuario). \
        join(Pessoa, Pessoa.id == Usuario.id_pessoa). \
        filter(Pessoa.email == email). \
        filter(Usuario.senha == senha).first()
