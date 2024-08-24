from django.contrib import admin

from workflow.models import Object, Area, AreaLayer, LayerWork, LayerMaterial

admin.site.register(Object)
admin.site.register(Area)
admin.site.register(AreaLayer)
admin.site.register(LayerWork)
admin.site.register(LayerMaterial)
