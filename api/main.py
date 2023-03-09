from fastapi import FastAPI
from api.routers import entries, users
from api.db_app.database import ENGINE
from api.db_app.models import Base


Base.metadata.create_all(bind=ENGINE)

app = FastAPI(title="Sport data")
app.include_router(entries.router)
app.include_router(users.router)


@app.get("/")
def index() -> str:
    return "This is the index"
