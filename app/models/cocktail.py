from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from app.database import Base


# Database Model
class Cocktail(Base):
    __tablename__ = "cocktails"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    ingredients = Column(Text)
    instructions = Column(Text)

    # Add a unique constraint to the combination of (name, )
    __table_args__ = (UniqueConstraint("name", name="_name_uc"),)
