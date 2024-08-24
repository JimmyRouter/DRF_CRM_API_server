from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from octocrm import settings
from .views import MaterialArrivalViewSet, MaterialRelocationViewSet, MaterialConsumptionViewSet



logistic_router = routers.SimpleRouter()

logistic_router.register(r'materialarrival', MaterialArrivalViewSet, basename='MaterialArrival')
logistic_router.register(r'materialrelocation', MaterialRelocationViewSet, basename='MaterialRelocation')
logistic_router.register(r'materialconsumption', MaterialConsumptionViewSet, basename='MaterialConsumption')

urlpatterns = [
    path('', include(logistic_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)