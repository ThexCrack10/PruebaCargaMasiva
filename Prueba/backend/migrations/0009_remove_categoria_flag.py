# Generated by Django 2.1.1 on 2018-10-05 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='flag',
        ),
    ]