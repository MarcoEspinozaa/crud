# Generated by Django 4.0.4 on 2022-05-07 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmuebles',
            old_name='numero_estacionamientos',
            new_name='numero_est',
        ),
        migrations.RemoveField(
            model_name='inmuebles',
            name='numero_hab',
        ),
        migrations.RemoveField(
            model_name='inmuebles',
            name='precio_mensual',
        ),
    ]
