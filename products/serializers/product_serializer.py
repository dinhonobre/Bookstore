from rest_framework import serializers
from products.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Só os campos existentes no modelo

class ProductSerializer(serializers.ModelSerializer):
    # Para leitura completa da categoria
    category = CategorySerializer(read_only=True)
    # Para escrita, aceitando apenas o id da categoria
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'category_id']
