import sqlalchemy as _sql
from sqlalchemy.orm import validates
from ..database import Base, engine


class Parameter(Base):
    __tablename__ = "parameter"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String)
    value = _sql.Column(_sql.Integer, _sql.CheckConstraint(
        'value>=-100 AND value<=100'))

    def __init__(self, name):
        self.name = name
        self.value = 0

    @validates('value')
    def validate_parameter_value(value):
        if not -100 <= value <= 100:
            raise ValueError(f'value must be between -100 to 100(inclusive)')
        return value
