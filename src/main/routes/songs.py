from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from src.infra.db.entities.songs import Song
from src.infra.db.settings.connection import get_session

router = APIRouter()


@router.get('/songs', response_model=List[Song])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]
