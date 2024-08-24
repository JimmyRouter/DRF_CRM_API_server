from django.db import models
from django.urls import reverse


class BaseInfo(models.Model):
    title = models.CharField(max_length=256)
    tag = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creation_t = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        abstract = True
        ordering = ['id']


class Bank(BaseInfo):
    corr_n = models.CharField(max_length=1024, blank=True)
    bik = models.CharField(max_length=1024, blank=True)
    addr = models.CharField(max_length=2048, blank=True)


class BankAcc(BaseInfo):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    org = models.ForeignKey('Organization', on_delete=models.CASCADE)
    acc_n = models.CharField(max_length=1024, blank=True)


class Organization(BaseInfo):
    full_title = models.CharField(max_length=1024, blank=True)
    inn = models.CharField(max_length=32, blank=True, null=True)
    ogrn = models.CharField(max_length=32, blank=True, null=True)


class Unit(BaseInfo):
    okei = models.CharField(max_length=10, default='000', null=True, blank=True)


class Category(BaseInfo):     # сделать по ферам разбивку категорий или свою? или обе
    smth = models.CharField(max_length=128, blank=True, null=True)


class Entity(BaseInfo):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    img = models.ImageField(upload_to='services', blank=True, null=True)

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse('this_entity', kwargs={'pk': self.pk})


class Work(Entity):
    FER = 'FER'
    TER = 'TER'
    MY = 'MY'
    work_type = {
        FER: 'ФЕР',
        TER: 'ТЕР',
        MY: 'СВОЙ'
    }
    estimate_type = models.CharField(max_length=128, choices=work_type, default=MY)
    estimate_code = models.CharField(max_length=128, blank=True, null=True)


class Material(Entity):
    FER = 'FER'
    TER = 'TER'
    MY = 'MY'
    mat_type = {
        FER: 'ФЕР',
        TER: 'ТЕР',
        MY: 'СВОЙ'
    }
    estimate_type = models.CharField(max_length=128, choices=mat_type, default=MY)
    estimate_code = models.CharField(max_length=128, blank=True, null=True)
