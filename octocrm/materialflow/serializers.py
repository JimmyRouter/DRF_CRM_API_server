from rest_framework import serializers

from materialflow.models import Warehouse, WarehouseMaterial
from simple_s.serializers import MaterialSerializer


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    class Meta:
        model = WarehouseMaterial
        fields = "__all__"