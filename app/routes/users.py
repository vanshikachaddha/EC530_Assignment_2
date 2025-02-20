from fastapi import APIRouter, HTTPException
from app.data_model import User
from types import List
from pydantic import EmailStr


router = APIRouter()
users: List[User] = []

#Create a new user
@router.post("/")
def create_user(user: User ):
    for u in users:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
        
    
    users.append(user)
    return {"User created successfully", user}

# Get a single user by email
@router.get("/{user_email}", response_model = User)
def get_user(email: EmailStr):
    for u in users:
        if u.email == email:
            return u
    raise HTTPException(status_code=400, detail="Email already exists")


