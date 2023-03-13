"""Entry Pydantic models to perform data validation"""
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel, Field
from api.utils.enums import SportTypeEnum, WeatherEnum


class Session(BaseModel):
    id: str = Field(default_factory=uuid4, alias="_id")
    discipline: SportTypeEnum = Field(..., description="Which sport?")
    date: datetime = Field(..., description="When?")
    precisions: str | None = Field(description="Free text to write about the session")
    weather: list[WeatherEnum] = Field(default_factory=[], description="What weather?")
    duration: int | None = Field(description="How long?")
    country: str | None = Field(description="In which country?")
    location: str | None = Field(description="In which area?")


class EventSchema(EntryBase):
    """Represents an event. Will be returned with an id from DB."""
    id: int
    objective: str | None
    scratch_position: int | None
    category_position: int | None

    class Config:
        orm_mode = True


class EventSchemaCreate(EntryBase):
    """Represents an event to insert in DB."""
    pass
