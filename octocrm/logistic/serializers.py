from rest_framework import serializers

from logistic.models import MaterialArrival, MaterialRelocation, MaterialConsumption
from simple_s.serializers import MaterialSerializer, OrganizationSerializer
from materialflow.serializers import WarehouseSerializer
from workflow.serializers import AreaLayerSerializer


class MaterialArrivalSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    sender = OrganizationSerializer()
    reciever = WarehouseSerializer()

    class Meta:
        model = MaterialArrival
        fields = "__all__"


class MaterialRelocationSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    sender = WarehouseSerializer()
    reciever = WarehouseSerializer()

    class Meta:
        model = MaterialRelocation
        fields = "__all__"


class MaterialConsumptionSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    sender = WarehouseSerializer()
    reciever = AreaLayerSerializer()

    class Meta:
        model = MaterialConsumption
        fields = "__all__"