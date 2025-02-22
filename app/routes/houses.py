from fastapi import APIRouter, HTTPException
from app.data_model import House
from typing import List
from pydantic import EmailStr

router = APIRouter()
houses: List[House] = []

# Create a new house
@router.post("/")
def create_house(house: House):
    for h in houses:
        if h.id == house.id:
            raise HTTPException(status_code=400, detail="House already exists")
        
    houses.append(house)
    return {"message":"House created successfully", "house": house}

# Get house details through id
@router.get("/id/{house_id}", response_model = House)
def get_house(house_id: int):
    for h in houses:
        if h.id == house_id:
            return h
        
    raise HTTPException(status_code=404, detail="House does not exist")

# Get owners of house through id
@router.get("/id/{house_id}/owners", response_model = List[EmailStr])
def get_house_owners(house_id: int):
    for h in houses:
        if h.id == house_id:
            return h.owner_email
        
    raise HTTPException(status_code=404, detail="House does not exist")

# Update house by id
@router.put("/id/{house_id}", response_model = House)
def update_house(house_id: int, updated_house: House):
    for index, h in enumerate(houses):
        if h.id == house_id:
            houses[index] = updated_house
            return updated_house

    raise HTTPException(status_code=404, detail="House not found")

# Delete house by id
@router.delete("/id/{house_id}")
def delete_house(house_id: int):
    for index, h in enumerate(houses):
        if h.id == house_id:
            houses.pop(index)
            return {"message": "House removed successfully"}
    raise HTTPException(status_code=404, detail="House not found")



