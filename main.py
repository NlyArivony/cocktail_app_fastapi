from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Text, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List

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
    glasstype = Column(String)  # Add the new column glasstype

    # Add a unique constraint to the combination of (name, )
    __table_args__ = (UniqueConstraint("name", name="_name_uc"),)


# Dependency to get the database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create tables in the database
Base.metadata.create_all(bind=engine)


# Pydantic model for creating a new Cocktail
class CocktailCreate(BaseModel):
    name: str
    ingredients: List[str]
    instructions: str


# Pydantic model for Cocktail with ID
class CocktailSchema(BaseModel):
    id: int
    name: str
    ingredients: List[str]
    instructions: str


# FastAPI App
app = FastAPI()


# API endpoints
@app.post("/cocktails/", response_model=CocktailCreate)
def create_cocktail(cocktail: CocktailCreate, db: Session = Depends(get_db)):
    ingredients_str = ", ".join(cocktail.ingredients)
    db_cocktail = Cocktail(
        name=cocktail.name,
        ingredients=ingredients_str,
        instructions=cocktail.instructions,
    )
    db.add(db_cocktail)
    try:
        db.commit()
        db.refresh(db_cocktail)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="Cocktail with this name already exists"
        )

    return CocktailCreate(
        name=db_cocktail.name,
        ingredients=db_cocktail.ingredients.split(", "),
        instructions=db_cocktail.instructions,
    )


@app.get("/cocktails/", response_model=List[CocktailSchema])
def read_cocktails(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cocktails = db.query(Cocktail).offset(skip).limit(limit).all()
    return [
        CocktailSchema(
            id=cocktail.id,
            name=cocktail.name,
            ingredients=cocktail.ingredients.split(", "),
            instructions=cocktail.instructions,
        )
        for cocktail in cocktails
    ]


@app.get("/cocktails/{cocktail_id}", response_model=CocktailCreate)
def read_cocktail(cocktail_id: int, db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).filter(Cocktail.id == cocktail_id).first()
    if not cocktail:
        raise HTTPException(status_code=404, detail="Cocktail not found")
    return CocktailCreate(
        name=cocktail.name,
        ingredients=cocktail.ingredients.split(", "),
        instructions=cocktail.instructions,
    )


@app.delete("/cocktails/{cocktail_id}", response_model=CocktailCreate)
def delete_cocktail(cocktail_id: int, db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).filter(Cocktail.id == cocktail_id).first()
    if not cocktail:
        raise HTTPException(status_code=404, detail="Cocktail not found")

    db.delete(cocktail)
    db.commit()
    return CocktailCreate(
        name=cocktail.name,
        ingredients=cocktail.ingredients.split(", "),
        instructions=cocktail.instructions,
    )
