from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from logistic.models import MaterialArrival, MaterialRelocation, MaterialConsumption
from logistic.serializers import MaterialArrivalSerializer, MaterialRelocationSerializer, MaterialConsumptionSerializer
from materialflow.models import WarehouseMaterial


class MaterialArrivalViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialArrivalSerializer

    def get_queryset(self):
        org_id = self.request.GET.get('parent_id')
        if org_id:
            return MaterialArrival.objects.filter(organization_id=org_id) or []
        else:
            try:
                return MaterialArrival.objects.all()
            except Exception as ex:
                print('logistics Arrival Exception:>>>', ex)
                return []

    def create(self, request: Request, *args, **kwargs):

        created = MaterialArrival.objects.create(
            organization_id=request.query_params['parent_id'],
            material_id=int(request.data['material']),
            amount=float(request.data['amount']),
            sender_id=int(request.data['sender']),
            reciever_id=int(request.data['reciever']),

        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MaterialRelocationViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialRelocationSerializer

    def get_queryset(self):
        org_id = self.request.GET.get('parent_id')
        if org_id:
            return MaterialRelocation.objects.filter(organization_id=org_id) or []
        else:
            return MaterialRelocation.objects.all() or []

    def create(self, request: Request, *args, **kwargs):
        whmaterial = WarehouseMaterial.objects.get(id=int(request.data['warehousematerial']))
        material = whmaterial.material
        print('relocation post data>>>\n', request.data)
        created = MaterialRelocation.objects.create(
            organization_id=request.query_params['parent_id'],
            material=material,
            amount=float(request.data['amount']),
            sender_id=int(request.data['sender']),
            reciever_id=int(request.data['reciever']),

        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MaterialConsumptionViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialConsumptionSerializer

    def get_queryset(self):
        org_id = self.request.GET.get('parent_id')
        if org_id:
            return MaterialConsumption.objects.filter(organization_id=org_id) or []
        else:
            return MaterialConsumption.objects.all() or []

    def create(self, request: Request, *args, **kwargs):
        whmaterial = WarehouseMaterial.objects.get(id=int(request.data['warehousematerial']))
        material = whmaterial.material
        print('relocation post data>>>\n', request.data)
        created = MaterialConsumption.objects.create(
            organization_id=request.query_params['parent_id'],
            material=material,
            amount=float(request.data['amount']),
            sender_id=int(request.data['sender']),
            reciever_id=int(request.data['reciever']),

        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

