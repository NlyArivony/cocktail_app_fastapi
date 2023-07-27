from pydantic import BaseModel
from typing import List


class CocktailCreate(BaseModel):
    name: str
    ingredients: List[str]
    instructions: str


class CocktailSchema(BaseModel):
    id: int
    name: str
    ingredients: List[str]
    instructions: str
