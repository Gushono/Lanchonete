from app.models.Pessoa import Pessoa, PessoaSchema
from app.repository import base_repository
from app.repository.pessoa_repository import pessoa_por_id


def cadastra_pessoa_service(pessoa_dto):
    pessoa = Pessoa()

    pessoa.nome_pessoa = pessoa_dto['nome_pessoa']
    pessoa.email = pessoa_dto['email']
    pessoa.nr_documento = pessoa_dto['nr_documento']
    pessoa.id_endereco = pessoa_dto['id_endereco']

    base_repository.gravar_objeto(pessoa)

    return pessoa


def recebe_pessoa_service(id_pessoa):
    pessoa = pessoa_por_id(id_pessoa)

    return pessoa
