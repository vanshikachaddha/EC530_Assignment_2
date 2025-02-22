from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_test_user():
    test_user = client.post("/users/", json = {
        "first_name": "Vanshika",
        "middle_name": None,
        "last_name": "Chaddha",
        "email": "vchaddha@bu.edu"})
    
    assert test_user.status_code == 200
    assert test_user.json()["message"] == "User created successfully"

def test_duplicate_user():
        test_user1 = client.post("/users/", json = {
        "first_name": "Vanshika",
        "middle_name": None,
        "last_name": "Chaddha",
        "email": "vchaddha@bu.edu"})

        test_user2 = client.post("/users/", json = {
        "first_name": "Angela",
        "middle_name": None,
        "last_name": "Gu",
        "email": "vchaddha@bu.edu"})

        assert test_user2.status_code == 400
        assert test_user2.json()['detail'] == "Email already exists"

def test_get_user():
    test_user = client.post("/users/", json = {
        "first_name": "Vanshika",
        "middle_name": None,
        "last_name": "Chaddha",
        "email": "vchaddha@bu.edu"})
    
    get_user = client.get("/users/email/vchaddha@bu.edu")
    assert get_user.status_code == 200
    assert get_user.json() == {
        "first_name": "Vanshika",
        "middle_name": None,
        "last_name": "Chaddha",
        "email": "vchaddha@bu.edu"
        }
    
def test_delete_user():
    test_user = client.post("/users/", json = {
        "first_name": "Vanshika",
        "middle_name": None,
        "last_name": "Chaddha",
        "email": "vchaddha@bu.edu"})
    
    delete_user = client.delete("/users/email/vchaddha@bu.edu")
    assert delete_user.status_code == 200
    assert delete_user.json()["message"] == "User deleted successfully"

def cannot_delete_user():
    test_user = client.post("/users/", json = {
        "first_name": "Vanshika",
        "middle_name": None,
        "last_name": "Chaddha",
        "email": "vchaddha@bu.edu"})
    delete_user = client.delete("/users/email/gchaddha@bu.edu")
    assert delete_user.status_code == 400
