# Generated by Django 4.0.4 on 2022-05-07 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m7_python', '0003_alter_inmuebles_m2_contruido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inmuebles',
            name='m2_contruido',
        ),
        migrations.AddField(
            model_name='inmuebles',
            name='m2_construido',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
