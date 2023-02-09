from pydantic import BaseModel, validator


class Parameter_Update(BaseModel):
    id: int
    value: int


class Parameter(BaseModel):
    name: str
    value: int
    id: int
