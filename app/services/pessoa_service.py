from app.models.Pessoa import Pessoa
from app.repository import base_repository
from app.repository.base_repository import retorna_objeto_por_id, retorna_todos_objetos


def cadastra_pessoa_service(pessoa_dto):
    pessoa = Pessoa()

    pessoa.nome_pessoa = pessoa_dto['nome_pessoa']
    pessoa.email = pessoa_dto['email']
    pessoa.nr_documento = pessoa_dto['nr_documento']
    pessoa.id_endereco = pessoa_dto['id_endereco']

    base_repository.gravar_objeto(pessoa)

    return pessoa


def lista_pessoa_service():
    pessoas = base_repository.retorna_todos_objetos(Pessoa)
    return pessoas


def recebe_pessoa_por_id_service(id_pessoa):
    pessoa = retorna_objeto_por_id(Pessoa, id_pessoa)

    return pessoa
