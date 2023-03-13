"""DB side code"""
from functools import lru_cache

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
#
# SQLALCHEMY_DATABASE_URL = "sqlite:///./db_app.db_app"
# ENGINE = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
#
#
# # Dependency
# def get_db():
#     db = SESSIONLOCAL()
#     try:
#         yield db
#     finally:
#         db.close()
