from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

""""""
# import psycopg2  # Import psycopg2 to handle PostgreSQL connections

""""""

# Load environment variables from .env
load_dotenv()

# SQLAlchemy Setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./cocktail.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
