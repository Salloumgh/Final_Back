from fastapi import APIRouter,FastAPI, Depends, Request, Body
from sqlalchemy.orm import Session
from db.db_models import get_db,Volunteers
from models import VolunteerModel

auth_router = APIRouter()

@auth_router.get('/')
def test():
    return"hello world" 


@auth_router.post("/")
async def root2(volunteer:VolunteerModel,db: Session = Depends(get_db)):
    print ("connecting to mysql")
    volunteer = Volunteers(volunteer_id=volunteer.id,name=volunteer.name,address=volunteer.address,phone=volunteer.phone ,email=volunteer.email,experience = volunteer.experience,skills=volunteer.skills,availability=volunteer.availability)
    db.add(volunteer)
    db.commit()
    return volunteer.email