# This module defines Data Models (User, House, Rooms, Devices)

from pydantic import BaseModel, EmailStr
from typing import Union, Optional, List, Any

class User(BaseModel):
    first_name: str 
    middle_name: Union[str, None]
    last_name: str
    email: EmailStr

class House(BaseModel):
    id: int
    name: str
    address: str
    owner_email: List[EmailStr]

class Rooms(BaseModel):
    name: str
    devices: Optional[List[str]] = []

class Devices(BaseModel):
    name: str
    status: bool

    