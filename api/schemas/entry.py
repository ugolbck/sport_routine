"""Entry Pydantic models to perform data validation"""

from datetime import datetime
from pydantic import BaseModel
from api.utils.enums import SportTypeEnum


class EntryBase(BaseModel):
    id: int
    discipline: SportTypeEnum
    date: datetime
    precisions: str | None
    weather: str | None
    duration: int | None
    country: str | None = "France"
    location: str | None


class Training(EntryBase):
    """Represents a training session."""
    pass

    class Config:
        orm_mode = True


class Event(EntryBase):
    """Represents an event."""
    objective: str | None
    scratch_position = int | None
    category_position = int | None

    class Config:
        orm_mode = True
