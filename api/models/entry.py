"""Entry model"""

from datetime import datetime
from pydantic import BaseModel
from api.utils.enums import SportTypeEnum


class Entry(BaseModel):
    discipline: SportTypeEnum
    date: datetime
    precisions: str | None
    duration: int | None
    country: str | None = "France"
    location: str | None
