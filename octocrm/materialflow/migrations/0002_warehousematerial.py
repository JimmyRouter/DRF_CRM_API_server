# Generated by Django 5.0.1 on 2024-06-05 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materialflow', '0001_initial'),
        ('simple_s', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=15)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='simple_s.material')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materialflow.warehouse')),
            ],
        ),
    ]