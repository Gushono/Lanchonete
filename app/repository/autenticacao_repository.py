from app import db
from app.models.Permissao_perfil import PermissaoPerfil
from app.models.Permissoes import Permissoes
from app.models.Pessoa import Pessoa
from app.models.Usuario import Usuario


def autentica_repository(email, senha):
    return db.session.query(Usuario). \
        join(Pessoa, Pessoa.id == Usuario.id_pessoa). \
        filter(Pessoa.email == email). \
        filter(Usuario.senha == senha).first()


def lista_permissoes_repository(id_perfil):
    return db.session.query(PermissaoPerfil). \
        filter(PermissaoPerfil.id_perfil == id_perfil).all()

