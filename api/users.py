from typing import Optional,List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter(
     prefix='/users',
    tags=['Users']
)

users = []

class User (BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@router.get("/",response_model=List[User])
async def get_users():
    return users

@router.post("/")
async def create_users(user:User):
    users.append(user)
    return "Success"

@router.get("/{id}")
async def get_user(id:int):
    return {"user" : users[id]}
