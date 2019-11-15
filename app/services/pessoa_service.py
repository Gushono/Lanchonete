from app.repository.pessoa_repository import cadastra_pessoa_repository


def cadastra_pessoa_service(body):
    return cadastra_pessoa_repository(body)
