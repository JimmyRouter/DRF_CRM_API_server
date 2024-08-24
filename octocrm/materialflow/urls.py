from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from octocrm import settings
from .views import WarehouseViewSet, WarehouseMaterialViewSet


material_router = routers.SimpleRouter()

material_router.register(r'warehouse', WarehouseViewSet, basename='Warehouse')
material_router.register(r'warehousematerial', WarehouseMaterialViewSet, basename='WarehouseMaterial')

urlpatterns = [
    path('', include(material_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)