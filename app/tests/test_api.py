from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "username": "user2",
        "email": "user2@example.com",
        "password": "user2123"
    })
    assert response.status_code == 200

    assert response.json()["username"] == "user2"

def test_create_recipe():
    response = client.post("/recipes/?user_id=1", json={
        "title": "Maggi",
        "description": "Soupy hot Maggi noodles",
        "ingredients": "Noodles, Maggi masala",
        "instructions": "Follow Instructions on packet"
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Maggi"

def test_get_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
