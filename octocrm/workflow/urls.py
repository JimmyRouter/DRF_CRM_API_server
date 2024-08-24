from django.conf.urls.static import static
from django.urls import path, include, re_path
from .views import ObjectViewSet, AreaViewSet, AreaLayerViewSet, LayerWorkViewSet, LayerMaterialViewSet, WorkListViewSet, FileUploadView
from octocrm import settings
from rest_framework import routers


crm_router = routers.SimpleRouter()

crm_router.register(r'object', ObjectViewSet, basename='Object')
crm_router.register(r'area', AreaViewSet, basename='Area')
crm_router.register(r'arealayer', AreaLayerViewSet, basename='AreaLayer')
crm_router.register(r'layerwork', LayerWorkViewSet, basename='LayerWork')
crm_router.register(r'layermaterial', LayerMaterialViewSet, basename='LayerMaterial')
crm_router.register(r'worklist', WorkListViewSet, basename='WorkList')


urlpatterns = [
    path('', include(crm_router.urls)),
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)