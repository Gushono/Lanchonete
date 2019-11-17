from app import db


def gravar_objeto(objeto):
    try:
        db.session.add(objeto)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        raise Exception(error)


def retorna_objeto_por_id(classe, id_objeto):
    return db.session.query(classe). \
        filter(classe.id == id_objeto).first()


def retorna_todos_objetos(classe):
    return db.session.query(classe).all()
