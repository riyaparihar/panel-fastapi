from pydantic import BaseModel

# TO_DO: implement server side pagination


class Pagination_Info(BaseModel):
    limit: int
    offset: int

    def __init__(self):
        self.limit = 10
        self.offset = 1
