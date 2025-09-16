from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets.item_viewsets import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
]
