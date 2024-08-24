from django.db import models

from simple_s.models import Organization, Material


class Warehouse(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.title)


class WarehouseMaterial(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        ordering = ['id']