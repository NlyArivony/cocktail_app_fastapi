# main.py

from sqlalchemy import create_engine, Column, Integer, String, Text, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy Setup
DATABASE_URL = "sqlite:///./cocktail.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Database Model
class Cocktail(Base):
    __tablename__ = "cocktails"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String, index=True, unique=True
    )  # Add unique constraint to the name column
    ingredients = Column(Text)
    instructions = Column(Text)

    # Add a unique constraint to the combination of (name, )
    __table_args__ = (UniqueConstraint("name", name="_name_uc"),)


# Create tables in the database
Base.metadata.create_all(bind=engine)
