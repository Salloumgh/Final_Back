from sqlalchemy import Column,ForeignKey,String,Integer
from sqlalchemy.orm import relationship,Session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
metadata = Base.metadata

SQLALHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/final"

engine = create_engine (
    SQLALHEMY_DATABASE_URL
)

SessionLocal=sessionmaker(autocommit = False,autoflush=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Volunteers (Base):
    __tablename__ ="volunteers"
    volunteer_id = Column(Integer,primary_key=True,nullable=False) 
    name = Column(String(255))
    address = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255))
    experience = Column(String(1200))
    skills = Column (String(1200))
    availability = Column (String(1200))
    #shelter_id =Column(Integer)
    #FOREIGN KEY (shelter_id) REFERENCES Shelters(shelter_id)


class Organizations (Base):
    __tablename__ ="organizations"
    organization_id= Column (Integer ,autoincrement=True ,primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    phone = Column(String(255))
    email = Column(String(255))
    unique_identifier = Column(String(255)) 
   


class Shelters (Base):
    __tablename__ ="shelters"
    shelter_id = Column(Integer,primary_key=True,nullable=False) 
    name = Column(String(255))
    address = Column(String(255))
    


class Locations (Base):
    __tablename__ ="Locations"
    location_id = Column(Integer,primary_key=True,nullable=False) 
    street = Column(String(255)) 
    city = Column(String(255)) 
    postal_code = Column(String) 
 
    



