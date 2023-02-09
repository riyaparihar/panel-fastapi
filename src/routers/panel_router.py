from typing import Optional
import fastapi as _fastapi

import sqlalchemy.orm as _orm
from ..dependencies import get_db
from ..services import panel_service as _panel_service
from ..schemas import panel_schema as _panel, pagination_info_schema as _pagination_info

router = _fastapi.APIRouter()


@router.patch("/panel/create")
def create_panel(
    panel: _panel.Panel_Create, db: _orm.Session =
    _fastapi.Depends(get_db)
):
    return _panel_service.create(db, panel)


@router.get("/panel/list")
def get_panel_list(limit: int = 10, db: _orm.Session =
                   _fastapi.Depends(get_db)):
    return _panel_service.list(db, limit)


@router.get("/panel/{panel_name}")
def get_panel_by_name(panel_name: str, db: _orm.Session =
                      _fastapi.Depends(get_db)):
    return _panel_service.get(db, panel_name)


@router.delete("/panel/{panel_id}")
def delete_panel(panel_id: int, db: _orm.Session =
                 _fastapi.Depends(get_db)):
    return _panel_service.delete(db, panel_id)
