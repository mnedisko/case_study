from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# db.py
DATABASE_URL = "postgresql://user:password@localhost:5432/case_study"


engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
