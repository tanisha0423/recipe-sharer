from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_recipe():
    response = client.post(
        "/recipes/",
        json={
            "title": "Masala Dosa",
            "ingredients": "Rice, Urad dal, Potato, Onion, Mustard seeds, Curry leaves, Oil, Salt",
            "instructions": "Soak rice and dal overnight, grind to a batter, ferment, make dosas on tawa, and fill with potato masala."
        },
    )
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["title"] == "Masala Dosa"

def test_read_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "title" in data[0]
        assert "ingredients" in data[0]
