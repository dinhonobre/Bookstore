from rest_framework.routers import DefaultRouter
from .views import OrderViewSet  # agora importa de views.py

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = router.urls
