# Generated by Django 2.1.1 on 2018-09-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180926_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidadDeConsultas',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='comentario',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.TextField(default=''),
        ),
    ]
