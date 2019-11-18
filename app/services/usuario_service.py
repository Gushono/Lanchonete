from app.models.Pessoa import Pessoa
from app.models.Usuario import Usuario
from app.models.exceptions import PadraoException
from app.repository import base_repository
from app.repository.usuario_repository import verifica_existencia_usuario_repository


def cadastra_usuario_service(usuario_dto):
    verificacao = verifica_existencia_usuario_repository(usuario_dto['email'])

    if verificacao:
        raise PadraoException('Impossível cadastrar um usuário com um email já cadastrado', 422)
    pessoa = Pessoa()
    usuario = Usuario()

    pessoa.nome_pessoa = usuario_dto['nome_pessoa']
    pessoa.email = usuario_dto['email']
    pessoa.nr_documento = usuario_dto.get('nr_documento')
    pessoa.id_endereco = usuario_dto.get('id_endereco')

    base_repository.gravar_objeto(pessoa)

    usuario.id_pessoa = pessoa.id
    usuario.id_perfil = usuario_dto['id_perfil']
    usuario.senha = usuario_dto['senha']

    base_repository.gravar_objeto(usuario)

    return usuario


def lista_usuario_service():
    usuarios = base_repository.retorna_todos_objetos(Usuario)
    return usuarios


def recebe_usuario_por_id_service(id_usuario):
    usuario = base_repository.retorna_objeto_por_id(Usuario, id_usuario)

    return usuario


