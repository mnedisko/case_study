from src.db import Base, engine
from src.models.campground_orm import CampgroundORM
def create_tables():
    
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
