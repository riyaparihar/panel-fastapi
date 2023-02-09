from fastapi import HTTPException
import sqlalchemy.orm as _orm
from src.models.panel import Control_Panel
from ..schemas import panel_schema as _panel_schema, pagination_info_schema as _pagination_info
import datetime as _dt


def create(db: _orm.Session, panel: _panel_schema.Panel_Create):
    components = panel.json()
    name = str(_dt.datetime.strftime(_dt.datetime.now(), '%s'))
    db_contol_panel = Control_Panel(components=components, name=name)
    db.add(db_contol_panel)
    db.commit()
    db.refresh(db_contol_panel)
    return db_contol_panel


def list(db: _orm.Session, limit: int = 100):
    return db.query(Control_Panel).order_by(Control_Panel.name.desc()).limit(limit).all()


def get(db: _orm.Session, panel_name: str):
    panel = db.query(Control_Panel).filter(
        Control_Panel.name == panel_name).first()
    if not panel:
        raise HTTPException(status_code=404, detail="Panel not found")
    return panel


def delete(db: _orm.Session, panel_id: int):
    panel = db.get(Control_Panel, {"id": panel_id})
    if not panel:
        raise HTTPException(status_code=404, detail="Panel not found")
    db.query(Control_Panel).filter(Control_Panel.id == panel_id).delete()
    db.commit()
    return db.query(Control_Panel).all()
