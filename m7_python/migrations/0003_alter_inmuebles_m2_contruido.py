# Generated by Django 4.0.4 on 2022-05-07 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0002_rename_numero_estacionamientos_inmuebles_numero_est_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmuebles',
            name='m2_contruido',
            field=models.IntegerField(),
        ),
    ]