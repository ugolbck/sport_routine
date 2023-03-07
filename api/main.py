from fastapi import FastAPI
from api.routers import data, users


app = FastAPI(title="Sport memories")
app.include_router(data.router)
app.include_router(users.router)


@app.get("/")
def index() -> str:
    return "This is the index"
