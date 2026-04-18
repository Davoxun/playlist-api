import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, declarative_base

engine = db.create_engine("sqlite:///./app.db")
con = engine.connect()

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
