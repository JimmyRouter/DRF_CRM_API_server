from django.db import models

from simple_s.models import BaseInfo, Organization, Work, Material

class Object(BaseInfo):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)


class CRMSection(models.Model):
    WORKS = 'works'
    MATERIALS = 'materials'
    DOCUMENTS = 'documents'
    LOGISTICS = 'logistics'
    FINANCES = 'finances'

    type_choices = {
        WORKS: "РАБОТЫ",
        MATERIALS: "МАТЕРИАЛЫ",
        DOCUMENTS: "ДОКУМЕНТЫ",
        LOGISTICS: "ЛОГИСТИКА",
        FINANCES: "ФИНАНСЫ",
    }
    type = models.CharField(max_length=64, choices=type_choices, default=WORKS)


class Area(BaseInfo):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    coords = models.JSONField(default=list, blank=True, null=True)


class AreaLayer(BaseInfo):                 #РАБОТЫ +Модель
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class LayerWork(models.Model):
    arealayer = models.ForeignKey(AreaLayer, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=3)


class LayerMaterial(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    arealayer = models.ForeignKey(AreaLayer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=3)


class TimeChart(BaseInfo):
    layer = models.ForeignKey(AreaLayer, on_delete=models.CASCADE)
    start_t = models.DateTimeField()
    finish_t = models.DateTimeField()


class Tickets(models.Model):
    client_email = models.EmailField()
    client_phone = models.IntegerField(blank=True, null=True)
    client_name = models.CharField(max_length=64, blank=True, null=True)
    ticket_subject = models.TextField(blank=True, null=True)


