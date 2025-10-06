from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api_new.viewsets.item_viewsets import ItemViewSet
from api_new.viewsets.order_viewsets import OrderViewSet
from api_new.viewsets.product_viewsets import ProductViewSet
from api_new.viewsets.category_viewsets import CategoryViewSet

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'items', ItemViewSet, basename='item')
=======
router.register(r'items', ItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
>>>>>>> 45dda2e (Adicionados ViewSets e Serializers para Order, Product e Category sem alterar Item existente)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <- endpoint de login via token
]
