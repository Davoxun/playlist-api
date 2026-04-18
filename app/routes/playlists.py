from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from ..auth import get_current_user

router = APIRouter(prefix="/playlists", tags = ["Playlists"])

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
    

@router.post("/")
def create_playlist(
    playlist: schemas.PlaylistCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    new_playlist = models.Playlist(name=playlist.name, owner_id=user.id)

    db.add(new_playlist)
    db.commit()
    db.refresh(new_playlist)

    return new_playlist


@router.get("/")
def get_playlists(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    return db.query(models.Playlist).filter(models.Playlist.owner_id == user.id).all()

@router.post("/{playlist_id}/add-track/{track_id}")
def add_track_to_playlist(
    playlist_id: int,
    track_id: int,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    playlist = db.query(models.Playlist).filter(
        models.Playlist.id == playlist_id,
        models.Playlist.owner_id == user.id
    ).first()

    track = db.query(models.Track).filter(models.Track.id == track_id).first()

    if not playlist or not track:
        return {"error": "Playlist or Track not found"}

    playlist.tracks.append(track)

    db.commit()

    return {"message": "Track added"}