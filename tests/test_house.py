from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_house():
    test_house = client.post("/houses", json = {
            "id": 12,
            "name": "Vanshika",
            "address": "5442 Tasha Dr.",
            "owner_email": ["vchaddha@bu.edu"]
    })

    assert test_house.status_code == 200
    assert test_house.json()["message"] == "House created successfully"

def test_duplicate_house():
    test_house1 = client.post("/houses", json = {
            "id": 12,
            "name": "Vanshika",
            "address": "5442 Tasha Dr.",
            "owner_email": ["vchaddha@bu.edu"]
    })

    test_house2 = client.post("/houses", json = {
            "id": 12,
            "name": "Vanshika",
            "address": "5442 Tasha Dr.",
            "owner_email": ["vchaddha@bu.edu"]
    })

    assert test_house2.status_code == 400
    assert test_house2.json()["detail"] == "House already exists"

def test_get_house():

    get_house = client.get("/houses/id/12")
    assert get_house.status_code == 200
    assert get_house.json()["name"] == "Vanshika"

def test_get_owners():
    test_house1 = client.post("/houses", json = {
            "id": 15,
            "name": "Vanshika",
            "address": "1056 Comm. Ave",
            "owner_email": ["vchaddha@bu.edu", "sharanya@bu.edu", "dhanvi@bu.edu"]
    })


    get_owners = client.get("/houses/id/15/owners")
    print("Expected:", ["vchaddha@bu.edu", "sharanya@bu.edu", "dhanvi@bu.edu"])
    print("Received:", get_owners.json())  # ✅ Debugging step

    assert get_owners.status_code == 200
    assert get_owners.json() == ["vchaddha@bu.edu", "sharanya@bu.edu", "dhanvi@bu.edu"]

def test_update_house():
    test_house1 = client.post("/houses", json = {
            "id": 12,
            "name": "Vanshika",
            "address": "1056 Comm. Ave",
            "owner_email": ["vchaddha@bu.edu", "sharanya@bu.edu", "dhanvi@bu.edu"]
    })


    update_house = client.put("/houses/id/12", json = {
            "id": 13,
            "name": "Vanshika",
            "address": "1056 Comm. Ave",
            "owner_email": ["vchaddha@bu.edu", "sharanya@bu.edu", "dhanvi@bu.edu", "shravya@bu.edu"]
    })
    assert update_house.status_code == 200
    assert update_house.json()["owner_email"] == ["vchaddha@bu.edu", "sharanya@bu.edu", "dhanvi@bu.edu", "shravya@bu.edu"]

def test_delete_house():
    test_house1 = client.post("/houses", json = {
            "id": 12,
            "name": "Vanshika",
            "address": "1056 Comm. Ave",
            "owner_email": ["vchaddha@bu.edu", "sharanya@bu.edu", "dhanvi@bu.edu"]
    })

    del_house = client.delete("/houses/id/12")
    assert del_house.status_code == 200
    assert del_house.json()["message"] == "House removed successfully"

def test_delete_nonexisthouse():
    test_house1 = client.post("/houses", json = {
            "id": 12,
            "name": "Vanshika",
            "address": "1056 Comm. Ave",
            "owner_email": ["vchaddha@bu.edu", "sharanya@bu.edu", "dhanvi@bu.edu"]
    })

    del_house = client.delete("/houses/id/14")
    assert del_house.status_code == 404
    assert del_house.json()["detail"] == "House not found"






