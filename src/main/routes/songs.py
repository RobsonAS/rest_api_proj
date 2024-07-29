from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.infra.db.entities.songs import Song, SongCreate
from src.infra.db.settings.connection import get_session

router = APIRouter()


@router.get('/songs', response_model=List[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    if songs:        
        return [Song(name=song.name, artist=song.artist, id=song.id, year=song.year) for song in songs]
    return []
        


@router.post('/songs', status_code=201, response_model=Song)
async def create_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
