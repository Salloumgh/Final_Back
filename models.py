from pydantic import BaseModel


class VolunteerModel(BaseModel):
    id: int
    name : str
    address: str
    phone:int
    email:str
    experience:str
    skills: str
    availability:str
    #shelter_id:int
