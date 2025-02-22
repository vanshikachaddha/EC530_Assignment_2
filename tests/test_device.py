from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_device():
    create_device = client.post("/devices/", json = {
        "name": "Google_Home",
        "status": 0
    })

    assert create_device.status_code == 200
    assert create_device.json()["name"] == "Google_Home"

def test_get_device():
    get_device = client.get("/devices/name/Google_Home")
    assert get_device.status_code == 200

def test_update_device():
    updated_device = client.put("/devices/name/Google_Home", json = {
        "name": "Google_Home",
        "status": 1
    })

    assert updated_device.status_code == 200
    assert updated_device.json()["status"] == 1

def test_delete_device():
    deleted_device = client.delete("/devices/Google_Home")

    assert deleted_device.status_code == 200
    assert deleted_device.json()["message"] == "Device deleted successfully"
