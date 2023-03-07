"""Route to manage the user"""

from fastapi import APIRouter

router = APIRouter(prefix="/user")


@router.get("/add")
def add_user():
    return
