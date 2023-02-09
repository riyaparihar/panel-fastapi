import sqlalchemy.orm as _orm
from ..schemas import parameter_schema as _parameter_schema

from src.models.parameter import Parameter
from ..constants import parameter_constant


def create(db: _orm.Session):
    db.query(Parameter).delete()
    db.bulk_insert_mappings(Parameter, parameter_constant.INITIAL_PARAMETERS)
    db.commit()
    return db.query(Parameter).all()


def update(db: _orm.Session, parameter: _parameter_schema.Parameter_Update):
    query = db.query(Parameter).filter(Parameter.id == parameter.id)
    query.update({
        Parameter.value: parameter.value
    })
    db.commit()
    return query.first()


def get(db: _orm.Session, parameter_id: int):
    return db.query(Parameter).filter(Parameter.id == parameter_id).first()


def list(db: _orm.Session):
    return db.query(Parameter).all()


def delete(db: _orm.Session, parameter_id: int):
    db.query(Parameter).filter(Parameter.id == parameter_id).delete()
    db.commit()
    return {
        "msg": "deleted successfully"
    }
