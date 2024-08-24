from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("workflow.urls")),
    path("api/v1/", include("materialflow.urls")),
    path("api/v1/", include("logistic.urls")),

    path("api/v1/", include("simple_s.urls")),
    path('api-auth/', include('rest_framework.urls'))

]
