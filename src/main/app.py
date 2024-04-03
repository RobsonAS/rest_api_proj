from fastapi import FastAPI
# from src.infra.db.settings.connection import init_db
from src.main.routes.songs import router as router_songs

app = FastAPI()


@app.get('/')
async def read_root():
    return {'ping': 'pong'}


# @app.on_event('startup')
# async def on_startup():
#     await init_db()


app.include_router(router_songs)
