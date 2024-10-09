from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base


engine = create_engine("sqlite:///db.sqlite")
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base.metadata.bind = engine
