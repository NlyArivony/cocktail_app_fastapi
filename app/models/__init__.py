from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Database connection details
DATABASE_URL = "sqlite:///./cocktail.db"

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker to manage the database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
