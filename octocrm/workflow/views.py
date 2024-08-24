from rest_framework import viewsets, views, status
from rest_framework.parsers import FileUploadParser, JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Object, AreaLayer, Area, LayerWork, LayerMaterial
from .serializers import ObjectSerializer, AreaSerializer, AreaLayerSerializer, LayerWorkSerializer, LayerMaterialSerializer, WorkListSerializer


class ObjectViewSet(viewsets.ModelViewSet):
    serializer_class = ObjectSerializer

    def get_queryset(self):
        org_id = self.request.GET.get('parent_id')
        if org_id:
            return Object.objects.filter(org=int(org_id))
        else:
            return Object.objects.all()

    def create(self, request: Request, *args, **kwargs):
        # try:
        created = Object.objects.create(org_id=request.query_params['parent_id'], title=request.data['title'])
        serializer = self.get_serializer(data=request.data)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    parser_classes = [JSONParser]
    def get_queryset(self):
        obj_id = self.request.GET.get('parent_id')
        if obj_id:
            return Area.objects.filter(object=obj_id)
        else:
            return Area.objects.all()

    def create(self, request:Request, *args, **kwargs):
        created = Area.objects.create(object_id=request.query_params['parent_id'],title=request.data['title'])  #default post bad request
        # or wrong type, tried different encoding #TOASK
        # in frontend: no result
        print('request>>>parwsers>', request.parsers)
        print('request>>>data>', request.data)
        print('request>>>POST>', request.POST)
        serializer = self.get_serializer(data=request.data)
        print('areaserializer_valid', serializer.is_valid()) # invalid #TOASK
        print('areaserializer_errors', serializer.errors)
        # self.perform_create(serializer)  # better way  to save in viewset, serializer(problems with nested saving, validation) #TOASK
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AreaLayerViewSet(viewsets.ModelViewSet):
    serializer_class = AreaLayerSerializer

    def get_queryset(self):
        area_id = self.request.GET.get('parent_id')
        if area_id:
            return AreaLayer.objects.filter(area=area_id)
        else:
            return AreaLayer.objects.all()


    def create(self, request:Request, *args, **kwargs):
        created = AreaLayer.objects.create(area_id=request.query_params['parent_id'], title=request.data['title'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LayerWorkViewSet(viewsets.ModelViewSet):
    serializer_class = LayerWorkSerializer

    def get_queryset(self):
        arealayer_id = self.request.GET.get('parent_id')
        if arealayer_id:
            layer = AreaLayer.objects.get(pk=arealayer_id)
            workset = layer.layerwork_set.all()
            print('workset>>\n', workset)
            return workset #LayerWork.objects.filter(arealayer=arealayer_id)
        else:
            return LayerWork.objects.all()


    def create(self, request:Request, *args, **kwargs):
        created = LayerWork.objects.create(
            arealayer_id=request.query_params['parent_id'],
            work_id=int(request.data['work']),
            amount=float(request.data['amount'])

        )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LayerMaterialViewSet(viewsets.ModelViewSet):
    serializer_class = LayerMaterialSerializer

    def get_queryset(self):
        materiallist_id = self.request.GET.get('parent_id')
        if materiallist_id:
            return LayerMaterial.objects.filter(arealayer=materiallist_id)
        else:
            return LayerMaterial.objects.all()

    def create(self, request:Request, *args, **kwargs):
        created = LayerWork.objects.create(
            arealayer_id=request.query_params['parent_id'],
            material_id=int(request.data['material']),
            amount=float(request.data['amount'])

        )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class WorkListViewSet(viewsets.ModelViewSet):
    serializer_class = WorkListSerializer

    def get_queryset(self):
        arealayer_id = self.request.GET.get('parent_id')
        if arealayer_id:
            layer = AreaLayer.objects.get(pk=arealayer_id)
            workset = layer.layerwork_set.all()
            print('workset>>\n', workset)
            return workset #LayerWork.objects.filter(arealayer=arealayer_id)    ##TOASK get objects via (filter by parent_id); get parent-> .children_set
        else:
            return LayerWork.objects.all()


class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]
    queryset = LayerWork.objects.all()
    def put(self, request:Request, filename, format=None):
        print('\nUPLOAD req data>>>>\n', request.data['file'])
        print('\nUPLOAD req dict>>>>\n', request.FILES['file'].__dict__['file'].read())

        # parsr = Smeta()
        file_obj = request.data['file']
        print('\nFile Put>>obj>>\n', file_obj)
        # ...
        # do some stuff with uploaded file
        # ...
        # fl = parsr.exel_parser(io=file_obj)
        # print('File Put>>parsed>>', fl)

        return Response(status=204)

