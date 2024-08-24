from django.contrib import admin
from logistic.models import MaterialArrival, MaterialRelocation, MaterialConsumption

admin.site.register(MaterialArrival)
admin.site.register(MaterialRelocation)
admin.site.register(MaterialConsumption)

