from flask import request

from app import app
from app.models.Usuario import UsuarioSchema
from app.services import autenticacao_service
from app.utils.util import serialize_entidade


@app.route("/autenticacao", methods=["GET"])
def autentica_usuario():
    usuario = autenticacao_service.autentica_service(request.get_json())
    return serialize_entidade(usuario, UsuarioSchema), 200
