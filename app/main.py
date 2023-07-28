from fastapi import FastAPI
from app.database import engine, SessionLocal
from app.controllers import cocktail
from alembic.config import Config
from alembic import command

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


# # Function to apply all Alembic migrations
# def apply_migrations():
#     # Load the Alembic configuration
#     alembic_cfg = Config("alembic.ini")

#     # Apply all migrations
#     command.upgrade(alembic_cfg, "head")


# # Call the function to apply migrations when the app starts
# apply_migrations()

# FastAPI App
app = FastAPI()

app.include_router(cocktail.router)
