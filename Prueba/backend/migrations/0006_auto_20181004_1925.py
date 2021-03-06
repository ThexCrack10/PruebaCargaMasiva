# Generated by Django 2.1.1 on 2018-10-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20180929_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidadDeConsultas',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tipo',
        ),
    ]
