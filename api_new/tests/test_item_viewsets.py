import pytest
from rest_framework.test import APIClient
from api_new.models.item import Item

@pytest.mark.django_db
def test_list_items():
    Item.objects.create(name="Item Teste", description="Um item de teste")
    client = APIClient()
    response = client.get("/api_new/items/")
    assert response.status_code == 200
    assert response.data[0]["name"] == "Item Teste"

@pytest.mark.django_db
def test_create_item():
    client = APIClient()
    payload = {"name": "Novo Item", "description": "Descrição teste"}
    response = client.post("/api_new/items/", payload, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Novo Item"
