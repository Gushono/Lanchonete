from app import db


def gravar_objeto(objeto):
    try:
        db.session.add(objeto)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        raise Exception(error)
