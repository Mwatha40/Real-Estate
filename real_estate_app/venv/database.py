from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///real_estate.db"  # SQLite database

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Create a function to initialize the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
