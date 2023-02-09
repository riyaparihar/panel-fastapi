
from sqlite3 import Timestamp
from pydantic import BaseModel, Json
from datetime import datetime
from ..enums import action_enum

from typing import Type


class Cell(BaseModel):
    action: action_enum.Action_Type
    position:int
    parameter_id: int


class Panel_Base(BaseModel):
    components:list[Cell]

class Panel_Create(Panel_Base):
    pass

class Panel(Panel_Base):
    id:int
    name:str
     
    class Config:
        orm_mode=True
     
