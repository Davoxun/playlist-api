from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/tracks", tags=["Tracks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_track(track: schemas.TrackCreate, db: Session = Depends(get_db)):
    new_track = models.Track(title=track.title, artist=track.artist)

    db.add(new_track)
    db.commit()
    db.refresh(new_track)

    return new_track


@router.get("/")
def get_tracks(db: Session = Depends(get_db)):
    return db.query(models.Track).all()