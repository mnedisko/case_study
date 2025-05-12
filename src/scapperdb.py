from src.models.campground import Campground as CampgroundSchema
from src.db import SessionLocal
import requests
from src.crud import upsert_campground
url = "https://thedyrt.com/api/v6/locations/search-results"

params = {
    'page[number]': '1',
    'page[size]': '100',
}

response = requests.get(url, params=params)
data = response.json()
db = SessionLocal()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def fetch_campgrounds():
    for campground in data["data"]:
        attr = campground["attributes"]
        flat = {
            **attr,
            "id": campground["id"],
            "type": campground["type"],
            "links": campground["links"]
        }

        try:
            validated = CampgroundSchema(**flat)
            upsert_campground(db, validated)
            print(f" {validated.name} ({validated.latitude}, {validated.longitude})")
        except Exception as e:
            print(f" Validation fail {e}")


