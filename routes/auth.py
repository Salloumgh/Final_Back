from fastapi import APIRouter


auth_router = APIRouter()

@auth_router.get('/')
def test():
    return"hello world" 
