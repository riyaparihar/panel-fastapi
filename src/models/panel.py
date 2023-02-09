import sqlalchemy as _sql
import datetime as _dt
from ..database import Base


class Control_Panel(Base):
    __tablename__ = "control_panel"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, unique=True, server_default=str(
        _dt.datetime.strftime(_dt.datetime.now(), '%s')))
    components = _sql.Column(_sql.JSON)
