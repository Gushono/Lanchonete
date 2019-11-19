from app.dto.permissao_perfil_dto import PermissaoDTO
from app.models.exceptions import PadraoException
from app.repository.autenticacao_repository import autentica_repository, lista_permissoes_repository


def autentica_service(autenticacao_dto):
    usuario = autentica_repository(autenticacao_dto['email'], autenticacao_dto['senha'])
    if not usuario:
        raise PadraoException('Usuário ou senha incorretos', 403)
    return usuario


def lista_permissoes_service(autenticacao_dto):
    list_objects = []
    permissoes = lista_permissoes_repository(autenticacao_dto['id_perfil'])

    for item in permissoes:
        permissao_dto = PermissaoDTO()
        permissao_dto.nome_permissao = item.permissoes.nome_permissao
        permissao_dto.id_perfil = item.perfil.id
        list_objects.append(permissao_dto)

    return list_objects

