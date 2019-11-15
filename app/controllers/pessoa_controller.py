import json

from app import app
from app.services import pessoa_service
from flask import request
import jsonpickle


@app.route("/pessoa", methods=["POST"])
def criar_pessoa():
    user = request.args.get('user')
    pessoa = pessoa_service.cadastra_pessoa_service(user)
    return
