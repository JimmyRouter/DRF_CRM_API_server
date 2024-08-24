from decimal import Decimal

from django.db import models

from materialflow.models import Warehouse, WarehouseMaterial
from simple_s.models import Organization, Material
from workflow.models import AreaLayer, LayerMaterial


class LogisticAction(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)  # TODO add made_by field when Staff model is added
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    changed = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_performed = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['id']


class MaterialArrival(LogisticAction):
    sender = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, related_name='arrival_from')
    reciever = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING,related_name='arrival_to')

    def save(self, *args, **kwargs):
        try:
            whmaterial = WarehouseMaterial.objects.get(material=self.material, warehouse=self.reciever)
            whmaterial.amount += Decimal(str(self.amount))
            whmaterial.save()
            print('models>arrival>whmaterial>>>>\n', whmaterial)
        except WarehouseMaterial.DoesNotExist:
            new_whmaterial = WarehouseMaterial.objects.create(
                warehouse=self.reciever,
                material=self.material,
                amount=Decimal(str(self.amount))
            )

        return super().save(*args, **kwargs)


class MaterialRelocation(LogisticAction):
    sender = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING, related_name='sender_warehouse')
    reciever = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING, related_name='reciever_warehouse')

    def save(self, *args, **kwargs):
        try:
            whmaterial_reciever = WarehouseMaterial.objects.get(material=self.material, warehouse=self.reciever)
            whmaterial_reciever.amount += Decimal(str(self.amount))
            whmaterial_reciever.save()

        except WarehouseMaterial.DoesNotExist:
            new_whmaterial = WarehouseMaterial.objects.create(
                warehouse=self.reciever,
                material=self.material,
                amount=self.amount
            )
        whmaterial_sender = WarehouseMaterial.objects.get(material=self.material, warehouse=self.sender)
        if whmaterial_sender.amount == Decimal(str(self.amount)):
            whmaterial_sender.delete()
        else:
            whmaterial_sender.amount -= Decimal(str(self.amount))
            whmaterial_sender.save()

        return super().save(*args, **kwargs)


class MaterialConsumption(LogisticAction):
    sender = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING, related_name='consumption_from')
    reciever = models.ForeignKey(AreaLayer, on_delete=models.DO_NOTHING, related_name='consumption_to')

    def save(self, *args, **kwargs):
        try:
            layermaterial_reciever = LayerMaterial.objects.get(material=self.material, arealayer=self.reciever)
            layermaterial_reciever.amount += Decimal(str(self.amount))
            layermaterial_reciever.save()

        except LayerMaterial.DoesNotExist:
            new_layermaterial = LayerMaterial.objects.create(
                arealayer=self.reciever,
                material=self.material,
                amount=self.amount
            )

        whmaterial_sender = WarehouseMaterial.objects.get(material=self.material, warehouse=self.sender)
        if whmaterial_sender.amount == Decimal(str(self.amount)):
            whmaterial_sender.delete()
        else:
            whmaterial_sender.amount -= Decimal(str(self.amount))
            whmaterial_sender.save()

        return super().save(*args, **kwargs)
