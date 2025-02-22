from fastapi import APIRouter, HTTPException
from app.data_model import User
from typing import List
from pydantic import EmailStr


router = APIRouter()
users: List[User] = []

# Create a new user
@router.post("/")
def create_user(user: User):
    for u in users:
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    users.append(user)
    return {"message": "User created successfully", "user": user}

# Get a single user by email
@router.get("/email/{email}", response_model = User)
def get_user(email: EmailStr):
    for u in users:
        if u.email == email:
            return u
    raise HTTPException(status_code=400, detail="Email does not exist")

# Update user by email
@router.put("/email/{email}", response_model = User) 
def update_user(email: EmailStr, updated_user: User):
    for index,u in enumerate(users):
        if u.email == email:
            users[index] = updated_user
            return {"message": "User updated successfully", "user": updated_user}
    
    raise HTTPException(status_code=400, detail="Email does not exist")

# Delete user by email
@router.delete("/email/{email}")
def delete_user(email: EmailStr):
    for index, u in enumerate(users):
        if u.email == email:
            users.pop(index)
            return {"message": "User deleted successfully"}
    
    raise HTTPException(status_code=400, detail="Email does not exist")











