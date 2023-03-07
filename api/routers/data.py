"""Routes for manipulating data in the DB"""

from fastapi import APIRouter

router = APIRouter(prefix="/data")


@router.get("/list_all")
def list_all_rows() -> list:
    return []
