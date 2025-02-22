from fastapi import FastAPI
from app.routes.users import router as users_router
from app.routes.houses import router as houses_router
from app.routes.rooms import router as rooms_router
from app.routes.devices import router as devices_router



app = FastAPI(title="Smart Home API", version="1.0", description="API for managing users, houses, rooms, and devices.")
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(houses_router, prefix="/houses", tags=["Houses"])
app.include_router(rooms_router, prefix="/rooms", tags=["Rooms"])
app.include_router(devices_router, prefix="/devices", tags=["Devices"])

@app.get("/")
def root():
    return {"message": "Welcome to the Smart Home API!"}