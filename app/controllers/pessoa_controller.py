import json

from flask import request

from app import app
from app.models.Pessoa import PessoaSchema
from app.services import pessoa_service
from app.utils.util import serialize_entidade


@app.route("/pessoa", methods=["POST"])
def criar_pessoa():

    pessoa = pessoa_service.cadastra_pessoa_service(request.get_json())
    return serialize_entidade(pessoa, PessoaSchema), 201


@app.route("/pessoa/<id_pessoa>", methods=["GET"])
def pessoa_por_id(id_pessoa):
    pessoa = pessoa_service.recebe_pessoa_service(id_pessoa)
    return serialize_entidade(pessoa, PessoaSchema), 200
