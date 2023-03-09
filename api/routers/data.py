"""Routes for manipulating data in the DB"""

from api.schemas import Entry
from fastapi import APIRouter

router = APIRouter(prefix="/data")


@router.get("/list_all", response_model=list[Entry])
def list_all_entries():
    return []


@router.post("/insert", response_model=Entry, status_code=201)
def insert_entry(data) -> Entry:
    result = _insert_one(data)
    return result


def _insert_one(data) -> bool:
    pass
