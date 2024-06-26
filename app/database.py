from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app.config import settings
import os
from sqlalchemy import create_engine

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ipaddress>/<hostname>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

while True:  
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='4610707748', cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print(("Database connection was successfully"))
        break
    except Exception as error:
        print("Connection to db was failed")
        print("Error:", error)
        time.sleep(2)   # maybe an essue (interupt connection net,....) dant access to conectig in first time