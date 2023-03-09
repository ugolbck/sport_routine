"""Routes for manipulating data in the DB"""

from api.schemas import TrainingSchema, TrainingSchemaCreate, EventSchema, EventSchemaCreate
from api.db_app import crud
from api.db_app.database import get_db

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

router = APIRouter(prefix="/data")


@router.post("/training", response_model=TrainingSchema)
def create_training(training: TrainingSchemaCreate, db: Session = Depends(get_db)):
    return crud.create_training(db=db, training=training)


@router.post("/event", response_model=EventSchema)
def create_event(event: EventSchemaCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)


@router.get("/training/{training_id}", response_model=TrainingSchema)
def get_training(training_id: int, db: Session = Depends(get_db)):
    training = crud.get_training_by_id(db=db, training_id=training_id)
    if not training:
        raise HTTPException(status_code=404, detail="Event not found")
    return training


@router.get("/event/{event_id}", response_model=EventSchema)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = crud.get_event_by_id(db=db, event_id=event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.get("/training/list", response_model=list[TrainingSchema])
def get_trainings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_trainings(db=db, skip=skip, limit=limit)


@router.get("/event/list", response_model=list[EventSchema])
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_events(db=db, skip=skip, limit=limit)
