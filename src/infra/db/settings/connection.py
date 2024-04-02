from sqlmodel import create_engine, SQLModel, Session

from src.config.settings import Settings

settings = Settings()

engine = create_engine(settings.DATABASE_URL, echo=settings.DEBUG)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
