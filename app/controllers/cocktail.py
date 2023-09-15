from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.cocktail import CocktailCreate, CocktailSchema
from app.models.cocktail import Cocktail
from typing import List
from app.database import SessionLocal


router = APIRouter()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API endpoints
@router.post("/cocktails/", response_model=CocktailCreate)
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


@router.get("/cocktails/", response_model=List[CocktailSchema])
def read_cocktails(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):  # noqa
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


@router.get("/cocktails/{cocktail_id}", response_model=CocktailCreate)
def read_cocktail(cocktail_id: int, db: Session = Depends(get_db)):
    cocktail = db.query(Cocktail).filter(Cocktail.id == cocktail_id).first()
    if not cocktail:
        raise HTTPException(status_code=404, detail="Cocktail not found")
    return CocktailCreate(
        name=cocktail.name,
        ingredients=cocktail.ingredients.split(", "),
        instructions=cocktail.instructions,
    )


@router.delete("/cocktails/{cocktail_id}", response_model=CocktailCreate)
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
