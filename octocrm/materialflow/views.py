from rest_framework import viewsets

from materialflow.models import Warehouse, WarehouseMaterial
from materialflow.serializers import WarehouseSerializer, WarehouseMaterialSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    serializer_class = WarehouseSerializer

    def get_queryset(self):
        org_id = self.request.GET.get('parent_id')
        if org_id:
            return Warehouse.objects.filter(organization_id=org_id)
        else:
            return Warehouse.objects.all()


class WarehouseMaterialViewSet(viewsets.ModelViewSet):
    serializer_class = WarehouseMaterialSerializer

    def get_queryset(self):
        wh_id = self.request.GET.get('parent_id')
        if wh_id:
            return WarehouseMaterial.objects.filter(warehouse_id=wh_id)
        else:
            return WarehouseMaterial.objects.all()