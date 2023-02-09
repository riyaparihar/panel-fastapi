import fastapi as _fastapi
import sqlalchemy.orm as _orm
from ..dependencies import get_db
from ..services import parameter_service as _parameter_service
from ..schemas import parameter_schema as _schemas

router = _fastapi.APIRouter()


@router.post("/parameter/{parameter_id}")
def update_parameter(parameter_id: int, parameter: _schemas.Parameter_Update, db: _orm.Session =
                     _fastapi.Depends(get_db)):
    return _parameter_service.update(db, parameter)


@router.get("/parameter/{parameter_id}")
def get_parameter(parameter_id: int, db: _orm.Session =
                  _fastapi.Depends(get_db)):
    return _parameter_service.get(db, parameter_id)


@router.delete("/parameter/{parameter_id}")
def delete_parameter(parameter_id: int, db: _orm.Session =
                     _fastapi.Depends(get_db)):
    return _parameter_service.delete(db, parameter_id)


@router.get("/parameters")
def get_parameters_list(db: _orm.Session =
                        _fastapi.Depends(get_db)):
    return _parameter_service.list(db)


@router.patch("/parameters")
def create_parameters(db: _orm.Session =
                      _fastapi.Depends(get_db)):
    return _parameter_service.create(db)
