from fastapi import FastAPI
from app.database import engine, SessionLocal
from app.controllers import cocktail

# Create the tables in the database
from app.models.cocktail import Base


# Dependency to get the database session
from sqlalchemy.orm import sessionmaker, Session


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create tables in the database
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

app.include_router(cocktail.router)
