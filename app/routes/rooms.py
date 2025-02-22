from fastapi import APIRouter, HTTPException
from app.data_model import Rooms
from typing import List
from pydantic import EmailStr

router = APIRouter()
rooms: List[Rooms] = []

# Get a room through name
@router.post('/', response_model=Rooms)
def create_room(room: Rooms):
    for r in rooms:
        if r.name == room.name:
            raise HTTPException(status_code=400, detail="Room already exists")
    
    rooms.append(room)
    return {"message": "Room created successfully", "room": room}

# Get room details through name
@router.get("/name/{room_name}", response_model = Rooms)
def get_room(room_name: str):
    for r in rooms:
        if r.name == room_name:
            return r
    
    raise HTTPException(status_code=404, detail="Room does not exist")

# Get room devices through name
@router.get("/name/{room_name}/devices", response_model = List[str]) 
def get_room_devices(room_name:str):
    for r in rooms:
        if r.name == room_name:
            return r.devices
    
    raise HTTPException(status_code=404, detail="Room does not exist")

# Update room by name
@router.put("/name/{room_name}", response_model=Rooms)
def update_room(room_name:str, updated_room: Rooms):
    for index, r in enumerate(rooms):
        if r.name == room_name:
            rooms[index] = updated_room
            return {"message": "Room updated successfully", "room": updated_room}

    raise HTTPException(status_code=404, detail="Room does not exist")

# Delete room by name
@router.delete("/name/{room_name}")
def delete_room(room_name:str):
    for index, r in enumerate(rooms):
        if r.name == room_name:
            rooms.pop(index)
            return {"message": "Room removed successfully"}
    raise HTTPException(status_code=404, detail="House not found")
        
