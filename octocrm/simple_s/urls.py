from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from .views import *
from octocrm import settings


s_router = routers.SimpleRouter()
s_router.register(r'organization', OrganizationViewSet)
s_router.register(r'unit', UnitViewSet)
s_router.register(r'category',CategoryViewSet)
s_router.register(r'material', MaterialViewSet)
s_router.register(r'work', WorkViewSet)


urlpatterns = [
    path('', include(s_router.urls)),
    # path("org/", OrganizationViewSet.as_view(), name="organization"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

