from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.main.routes.songs import router as router_songs

# from src.infra.db.settings.connection import init_db

app = FastAPI()

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/')
async def read_root():
    return {'ping': 'pong'}


# @app.on_event('startup')
# async def on_startup():
#     await init_db()


app.include_router(router_songs)
