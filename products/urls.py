from rest_framework.routers import DefaultRouter
from .views import ProductViewSet  # agora importa de views.py

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls
