from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite:///devconnect.db")

SessionLocal = sessionmaker(bind = engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()