from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

class _DBConnect():
    _SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://' + settings.db_username + ':' + settings.db_password + '@' + settings.db_host_address + '/' + settings.db_database_name
    _engine = create_engine(_SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(bind=_engine, autocommit=False, autoflush=False)
    Base = declarative_base()
    Base.metadata.create_all(bind=_engine)

BASE = _DBConnect.Base

def get_db():
    db = _DBConnect.SessionLocal()
    try:
        yield db
    finally:
        db.close()
