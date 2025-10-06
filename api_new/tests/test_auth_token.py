import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_obtain_auth_token():
    # Criar usuário de teste
    username = "testuser"
    password = "testpassword123"
    user = User.objects.create_user(username=username, password=password)

    client = APIClient()

    # Requisição POST para gerar token
    response = client.post("/api_new/api-token-auth/", {"username": username, "password": password}, format="json")
    
    # Verificar status code
    assert response.status_code == 200

    # Verificar se o token foi retornado
    assert "token" in response.data
    assert len(response.data["token"]) > 0

    # Testar login com dados incorretos
    response_invalid = client.post("/api_new/api-token-auth/", {"username": username, "password": "wrongpass"}, format="json")
    assert response_invalid.status_code == 400
    assert "non_field_errors" in response_invalid.data
