from fastapi import FastAPI
from app.models import engine
from app.controllers import cocktail_controller

# Create the tables in the database
from app.models.cocktail import Base
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(cocktail_controller.router)
# Adding the endpoints to the FastAPI app
# app.include_router(create_cocktail)
# app.include_router(read_cocktails)
# app.include_router(read_cocktail)
# app.include_router(delete_cocktail)
