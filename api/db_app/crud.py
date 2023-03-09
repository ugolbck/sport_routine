"""CRUD operations"""

from sqlalchemy.orm import Session
from api.db_app import Training, Event
from api.schemas import TrainingSchemaCreate, EventSchemaCreate

# Get functions


def get_training_by_id(db: Session, training_id: int, ):
    return db.query(Training).filter(Training.id == training_id).first()


def get_trainings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Training).offset(skip).limit(limit)


def get_event_by_id(db: Session, event_id: int, ):
    return db.query(Event).filter(Event.id == event_id).first()


def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit)


# Create functions

def create_training(db: Session, training: TrainingSchemaCreate):
    db_item = Training(**training.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_event(db: Session, event: EventSchemaCreate):
    db_item = Event(**event.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
