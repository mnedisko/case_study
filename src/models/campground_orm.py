# src/models/campground_orm.py
from sqlalchemy import Column, String, Float, Boolean, Integer, JSON
from src.db import Base

class CampgroundORM(Base):
    __tablename__ = "campgrounds"

    id = Column(String, primary_key=True, index=True) 
    type = Column(String)
    name = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    region_name = Column(String)
    administrative_area = Column(String)
    nearest_city_name = Column(String)
    accommodation_type_names = Column(JSON)
    bookable = Column(Boolean)
    camper_types = Column(JSON)
    operator = Column(String)
    photo_url = Column(String)
    photo_urls = Column(JSON)
    photos_count = Column(Integer)
    rating = Column(Float)
    reviews_count = Column(Integer)
    slug = Column(String)
    price_low = Column(Float)
    price_high = Column(Float)
    availability_updated_at = Column(String)
    self_link = Column(String)
