from flask import request

from app import app
from app.models.Usuario import UsuarioSchema
from app.services import usuario_service
from app.utils.util import serialize_entidade


@app.route("/usuario", methods=["POST"])
def criar_usuario():
    usuario = usuario_service.cadastra_usuario_service(request.get_json())
    return serialize_entidade(usuario, UsuarioSchema), 201


@app.route("/usuario", methods=["GET"])
def listar_usuarios():
    usuario = usuario_service.lista_usuario_service()
    return serialize_entidade(usuario, UsuarioSchema), 200


@app.route("/usuario/<id_usuario>", methods=["GET"])
def usuario_por_id(id_usuario):
    usuario = usuario_service.recebe_usuario_por_id_service(id_usuario)
    return serialize_entidade(usuario, UsuarioSchema), 200
