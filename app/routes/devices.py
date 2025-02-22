from fastapi import APIRouter, HTTPException
from app.data_model import Devices
from typing import List
from pydantic import EmailStr

router = APIRouter()
devices: List[Devices] = []

# Create a new device
@router.post("/", response_model=Devices)
def create_device(device: Devices):
    for d in devices:
        if d.name == device.name:
            raise HTTPException(status_code=400, detail="Device already exists")
    
    devices.append(device)
    return device 

# Get details about a device
@router.get("/name/{device_name}", response_model=Devices)
def get_device(device_name: str):
    for d in devices:
        if d.name == device_name:
            return d
    raise HTTPException(status_code=404, detail="Device not found")

# Update details about a device
@router.put("/name/{device_name}", response_model=Devices)
def update_device(device_name: str, updated_device: Devices):
    for index, d in enumerate(devices):
        if d.name == device_name:
            devices[index] = updated_device
            return updated_device

    raise HTTPException(status_code=404, detail="Device not found")

# Delete device by name
@router.delete("/{device_name}")
def delete_device(device_name: str):
    global devices
    devices = [d for d in devices if d.name != device_name]
    return {"message": "Device deleted successfully"}