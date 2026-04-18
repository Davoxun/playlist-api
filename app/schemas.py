from pydantic import BaseModel

class UserCreate(BaseModel):
    email:str
    password:str

class PlaylistCreate(BaseModel):
    name:str

class TrackCreate(BaseModel):
    title: str
    artist: str    
