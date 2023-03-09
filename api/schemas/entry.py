"""Entry Pydantic models to perform data validation"""

from datetime import datetime
from pydantic import BaseModel
from api.utils.enums import SportTypeEnum


class EntryBase(BaseModel):
    discipline: SportTypeEnum
    date: datetime
    precisions: str | None
    weather: str | None
    duration: int | None
    country: str | None = "France"
    location: str | None


class TrainingSchema(EntryBase):
    """Represents a training session. Will be returned with an id from DB."""
    id: int

    class Config:
        orm_mode = True


class TrainingSchemaCreate(EntryBase):
    """Represents a training session to insert in DB."""
    pass


class EventSchema(EntryBase):
    """Represents an event. Will be returned with an id from DB."""
    id: int
    objective: str | None
    scratch_position = int | None
    category_position = int | None

    class Config:
        orm_mode = True


class EventSchemaCreate(EntryBase):
    """Represents an event to insert in DB."""
    pass
