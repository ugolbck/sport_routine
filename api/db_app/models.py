"""SQLAlchemy schemas"""

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, DateTime
#
# Base = declarative_base()
#
#
# class Training(Base):
#     __tablename__ = "training"
#
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     discipline = Column(String(30), index=True)
#     date = Column(DateTime)
#     precisions = Column(String)
#     weather = Column(String)
#     duration = Column(Integer)
#     country = Column(String)
#     location = Column(String)
#
#
# class Event(Base):
#     __tablename__ = "event"
#
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     discipline = Column(String(30), index=True)
#     date = Column(DateTime)
#     precisions = Column(String)
#     weather = Column(String)
#     duration = Column(Integer)
#     country = Column(String)
#     location = Column(String)
#     objective = Column(String)
#     scratch_position = Column(Integer)
#     category_position = Column(Integer)
