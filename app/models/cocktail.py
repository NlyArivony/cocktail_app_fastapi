from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cocktail(Base):
    __tablename__ = "cocktails"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    ingredients = Column(Text)
    instructions = Column(Text)

    __table_args__ = (UniqueConstraint("name", name="_name_uc"),)
