import jsonpickle
import json
from flask import request, jsonify

from app import app
from app.models.Permissao_perfil import PermissaoPerfilSchema
from app.models.Usuario import UsuarioSchema
from app.services import autenticacao_service
from app.utils.util import serialize_entidade


@app.route("/autenticacao", methods=["GET"])
def autentica_usuario():
    usuario = autenticacao_service.autentica_service(request.get_json())
    return serialize_entidade(usuario, UsuarioSchema), 200


@app.route("/autenticacao-permissoes", methods=["GET"])
def autentica_permissoes():
    permissoes = autenticacao_service.lista_permissoes_service(request.get_json())
    # test = PermissaoPerfilDto(permissoes)
    return json.dumps([ob.__dict__ for ob in permissoes]), 200
