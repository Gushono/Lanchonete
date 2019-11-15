from flask import jsonify
from sqlalchemy.orm.collections import InstrumentedList


def serialize_entidade(entidade, entidade_schema, apply_jsonify=True):
    """
    Função responsável por serializar uma ou várias entidades
    :param apply_jsonify: Responsável por applicar a função jsonify ao retorno/output
    :param entidade: List ou Entidade - Uma lista ou uma entidade, por exemplo, Cidade
    :param entidade_schema: Schema o esquema da entidade que será serialized
    :return: retorna a entidade serialized
    """

    schema = (
        entidade_schema(many=True)
        if type(entidade) == list or type(entidade) == InstrumentedList
        else entidade_schema()
    )
    output = (
        jsonify(schema.dump(entidade).data)
        if apply_jsonify
        else schema.dump(entidade).data
    )
    return output