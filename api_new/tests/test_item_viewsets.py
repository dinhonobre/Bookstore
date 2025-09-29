import pytest
from rest_framework.test import APIClient
from api_new.models.item import Item
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@pytest.mark.django_db
def test_pagination_items():
    # Criar usuário e token
    user = User.objects.create_user(username="testuser", password="testpass123")
    token = Token.objects.create(user=user)

    # Criar 10 itens para testar a paginação (PAGE_SIZE=5)
    for i in range(10):
        Item.objects.create(name=f"Item {i+1}", description=f"Descrição {i+1}")

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)  # <- envia o token

    # Testar primeira página
    response1 = client.get("/api_new/items/?page=1")
    assert response1.status_code == 200
    assert len(response1.data["results"]) == 5
    assert response1.data["next"] is not None
    assert response1.data["previous"] is None

    # Testar segunda página
    response2 = client.get("/api_new/items/?page=2")
    assert response2.status_code == 200
    assert len(response2.data["results"]) == 5
    assert response2.data["next"] is None
    assert response2.data["previous"] is not None
