import requests
from models.campground import Campground
url = "https://thedyrt.com/api/v6/locations/search-results"

params = {
    'page[number]': '1',
    'page[size]': '100',
}

response = requests.get(url, params=params)
data = response.json()

print(f"Found {len(data['data'])} campgrounds.")
for campground in data["data"]:
    attr = campground["attributes"]
    flat = {
        
        **attr,
        "id": campground["id"],
        "type": campground["type"],
        "links": campground["links"]
    }

    try:
        validated = Campground(**flat)
        print(f" {validated.name} ({validated.latitude}, {validated.longitude})")
    except Exception as e:
        print(f" Validation fail {e}")