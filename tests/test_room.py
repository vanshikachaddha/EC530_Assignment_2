from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_room():
    test_room = client.post("/rooms/", json = {
        "name": "Kitchen",
        "devices": ["Google home", "Alexa"]
    })

    assert test_room.status_code == 200
    assert test_room.json()["message"] == "Room created successfully"

def test_create_roomdupe():
    test_room2 = client.post("/rooms", json = {
        "name": "Kitchen",
        "devices": None
    })

    assert test_room2.status_code == 400
    assert test_room2.json()["detail"] == "Room already exists"

def test_get_room():
    get_room = client.get("/rooms/name/Kitchen") 
    assert get_room.status_code == 200
    assert get_room.json()["name"] == "Kitchen"


def test_update_room():
    update_room = client.put("/rooms/name/Kitchen", json = {
        "name": "Kitchen",
        "devices": ["Google home", "Alexa", "Apple lights"]
    })

    assert update_room.status_code == 200
    assert update_room.json()["devices"] == ["Google home", "Alexa", "Apple lights"]

def test_delete_room():
    delete_room = client.delete("/rooms/name/Kitchen") 

    assert delete_room.json()["message"] == "Room removed successfully"
