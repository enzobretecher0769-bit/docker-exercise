import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Hello World" in response.text

def test_get_items():
    response = requests.get(f"{BASE_URL}/items")
    assert response.status_code == 200
    items = response.json()
    assert len(items) >= 2

def test_add_item():
    new_item = {
        "name": "Item Test Ajout",
        "description": "Ajouté via pytest"
    }
    response = requests.post(f"{BASE_URL}/items", json=new_item)
    assert response.status_code == 201
    added_item = response.json()["item"]
    
    # Vérifie qu'il est bien ajouté
    get_response = requests.get(f"{BASE_URL}/items")
    items = get_response.json()
    assert any(item["id"] == added_item["id"] for item in items)

def test_delete_item():
    # Ajouter un item temporaire pour le supprimer
    temp_item = {
        "name": "Item à Supprimer",
        "description": "Test suppression"
    }
    add_resp = requests.post(f"{BASE_URL}/items", json=temp_item)
    item_id = add_resp.json()["item"]["id"]
    
    # Supprimer
    del_resp = requests.delete(f"{BASE_URL}/items/{item_id}")
    assert del_resp.status_code == 200
    
    # Vérifier suppression
    get_resp = requests.get(f"{BASE_URL}/items")
    items = get_resp.json()
    assert not any(item["id"] == item_id for item in items)

def test_delete_non_existent():
    response = requests.delete(f"{BASE_URL}/items/999999")
    assert response.status_code == 404
