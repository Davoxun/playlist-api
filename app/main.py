from fastapi import FastAPI
from .database import engine, Base
from .routes import users, playlists
from .routes import tracks


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(playlists.router)
app.include_router(tracks.router)