import fastapi as _fastapi
from fastapi.middleware.cors import CORSMiddleware
from .routers import panel_router, parameter_router
from .database import engine
from .models import panel, parameter

panel.Base.metadata.create_all(bind=engine)
parameter.Base.metadata.create_all(bind=engine)

app = _fastapi.FastAPI()
app.include_router(panel_router.router)
app.include_router(parameter_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Control Panel"}


# *command to start server*:
#  uvicorn src.map:app --port 3000 --reload
