import os

from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

POSTGRES_USER = os.getenv("POSTGRES_USER", "swapi")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")
POSTGRES_DB = os.getenv("POSTGRES_DB", "swapi")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(PG_DSN)
Session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


class People(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True)
    birth_year: Mapped[str] = mapped_column(String(128))
    eye_color: Mapped[str] = mapped_column(String(128))
    films: Mapped[str] = mapped_column(String(256))
    gender: Mapped[str] = mapped_column(String(128))
    hair_color: Mapped[str] = mapped_column(String(128))
    height: Mapped[str] = mapped_column(String(128))
    homeworld: Mapped[str] = mapped_column(String(128))
    mass: Mapped[str] = mapped_column(String(128))
    name: Mapped[str] = mapped_column(String(128))
    skin_color: Mapped[str] = mapped_column(String(128))
    species: Mapped[str] = mapped_column(String(256))
    starships: Mapped[str] = mapped_column(String(256))
    vehicles: Mapped[str] = mapped_column(String(256))
