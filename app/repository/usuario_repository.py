from app import db
from app.models.Pessoa import Pessoa
from app.models.Usuario import Usuario


def verifica_existencia_usuario_repository(email):
    return db.session.query(Usuario). \
        join(Pessoa, Pessoa.id == Usuario.id_pessoa). \
        filter(Pessoa.email == email).first()
