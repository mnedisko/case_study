from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.models.campground_orm import CampgroundORM
from src.models.campground import Campground
def upsert_campground(db: Session, campground: Campground):
    data = campground.model_dump()
    data["photo_url"] = str(data["photo_url"]) if data["photo_url"] else None
    data["self_link"] = str(data["links"]["self"])
    data["photo_urls"] = [str(url) for url in data.get("photo_urls", [])]
    data.pop("links", None)

    obj = db.query(CampgroundORM).filter(CampgroundORM.id == data["id"]).first()

    if obj:
        for field, value in data.items():
            setattr(obj, field, value)
    else:
        obj = CampgroundORM(**data)
        db.add(obj)

    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        print(f" DB Error: {e}")
    except Exception as e:
        db.rollback()
        print(f"Unexpected DB Error: {e}")
