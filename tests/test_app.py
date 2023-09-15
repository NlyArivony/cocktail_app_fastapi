import pytest, pdb
from fastapi.testclient import TestClient
from app.main import app

# Create a test client using the TestClient class
client = TestClient(app)

# Define test cases


def test_create_cocktail():
    # Test creating a new cocktail
    payload = {
        "name": "Test Cocktail",
        "ingredients": ["Ingredient 1", "Ingredient 2"],
        "instructions": "Mix the ingredients.",
    }
    response = client.post("/cocktails/", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Cocktail"


def test_read_cocktails():
    # Test reading a list of cocktails
    response = client.get("/cocktails/")
    assert response.status_code == 200
    # Add assertions to check the response data


def helper():
    response = client.get("/cocktails/")
    # Store the dynamically generated ID for later use
    for cocktail in response.json():
        if cocktail["name"] == "Test Cocktail":
            created_cocktail_id = cocktail["id"]
    # Retrieve and return the dynamically generated ID
    return created_cocktail_id


def test_read_cocktail():
    id = helper()
    # Test reading a specific cocktail by ID
    response = client.get(f"/cocktails/{id}")  # Use f-string for string formatting
    assert response.status_code == 200
    # Add assertions to check the response data


def test_delete_cocktail():
    id = helper()
    # Test deleting a specific cocktail by ID
    response = client.delete(f"/cocktails/{id}")  # Assuming ID 1 exists in the database
    assert response.status_code == 200
    # Add assertions to check the response data
