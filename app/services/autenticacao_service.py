from app.repository.autenticacao_repository import autentica_repository


def autentica_service(autenticacao_dto):
    usuario = autentica_repository(autenticacao_dto['email'], autenticacao_dto['senha'])
    return usuario
