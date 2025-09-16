import pytest
from api_new.serializers.item_serializer import ItemSerializer
from api_new.models.item import Item
from django.utils import timezone

@pytest.mark.django_db
def test_item_serializer_serialization():
    # Criando um objeto Item de teste
    item = Item.objects.create(
        name="Teste Item",
        description="Descrição do item",
        created_at=timezone.now()
    )

    # Serializando o objeto
    serializer = ItemSerializer(item)

    # Verificando se os campos estão corretos
    data = serializer.data
    assert data['id'] == item.id
    assert data['name'] == "Teste Item"
    assert data['description'] == "Descrição do item"
    assert 'created_at' in data

@pytest.mark.django_db
def test_item_serializer_validation():
    # Dados válidos
    data = {
        "name": "Novo Item",
        "description": "Descrição do novo item",
        "created_at": timezone.now()
    }
    serializer = ItemSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
