# Generated by Django 5.0.1 on 2024-06-05 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_initial'),
        ('materialflow', '0001_initial'),
        ('simple_s', '0001_initial'),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialarrival',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='materialconsumption',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='materialrelocation',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='materialarrival',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='simple_s.organization'),
        ),
        migrations.AddField(
            model_name='materialconsumption',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='simple_s.organization'),
        ),
        migrations.AddField(
            model_name='materialrelocation',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='simple_s.organization'),
        ),
        migrations.AlterField(
            model_name='materialarrival',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='arrival_to', to='materialflow.warehouse'),
        ),
        migrations.AlterField(
            model_name='materialarrival',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='arrival_from', to='simple_s.organization'),
        ),
        migrations.AlterField(
            model_name='materialconsumption',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='consumption_to', to='workflow.object'),
        ),
        migrations.AlterField(
            model_name='materialconsumption',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='consumption_from', to='materialflow.warehouse'),
        ),
    ]