#webapp_essentials/src/database/database_setup.py
from logging import INFO, basicConfig, getLogger
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.config import get_settings

log = getLogger(__name__)
basicConfig(level=INFO)

DB_SETTINGS = get_settings()
DATABASE_URL = str(DB_SETTINGS.get("DATABASE_URL"))  # Accès correct au dictionnaire

engine = create_engine(DATABASE_URL)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, Session, None]:
    log.info("Initialising database session...")
    with Session(engine) as session:
        yield session
