from rest_framework import serializers

from .models import Object, Area, AreaLayer, LayerMaterial, LayerWork
from simple_s.serializers import WorkSerializer


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = "__all__"


class AreaLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaLayer
        fields = "__all__"


class LayerWorkSerializer(serializers.ModelSerializer):
    work = WorkSerializer()

    class Meta:
        model = LayerWork
        fields = "__all__"


class LayerMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayerMaterial
        fields = "__all__"


class WorkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayerWork
        fields = "__all__"