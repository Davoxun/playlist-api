from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy import Table


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)

    playlists = relationship("Playlist", back_populates="owner")

class Playlist(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="playlists")


playlist_tracks = Table(
    "playlist_tracks",
    Base.metadata,
    Column("playlist_id", ForeignKey("playlists.id"), primary_key=True),
    Column("track_id", ForeignKey("tracks.id"), primary_key=True)
)
tracks = relationship(
    "Track",
    secondary=playlist_tracks,
    back_populates="playlists"
)

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)

    playlists = relationship(
        "Playlist",
        secondary=playlist_tracks,
        back_populates="tracks"
    )