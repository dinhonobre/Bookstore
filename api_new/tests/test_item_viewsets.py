import pytest
from rest_framework.test import APIClient
from api_new.models.item import Item

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')  # garante ordem consistente
    serializer_class = ItemSerializer


@pytest.mark.django_db
def test_pagination_items():
    # Criar 10 itens para testar a paginação (PAGE_SIZE=5)
    for i in range(10):
        Item.objects.create(name=f"Item {i+1}", description=f"Descrição {i+1}")
    
    client = APIClient()

    # Testar primeira página
    response1 = client.get("/api_new/items/?page=1")
    assert response1.status_code == 200
    assert len(response1.data["results"]) == 5  # primeira página com 5 itens
    assert response1.data["next"] is not None
    assert response1.data["previous"] is None

    # Testar segunda página
    response2 = client.get("/api_new/items/?page=2")
    assert response2.status_code == 200
    assert len(response2.data["results"]) == 5  # segunda página com os 5 itens restantes
    assert response2.data["next"] is None
    assert response2.data["previous"] is not None
