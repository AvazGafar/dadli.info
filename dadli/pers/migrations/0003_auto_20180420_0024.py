# Generated by Django 2.0.2 on 2018-04-19 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pers', '0002_auto_20170918_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ustags',
            name='object',
        ),
        migrations.RemoveField(
            model_name='ustags',
            name='user',
        ),
        migrations.DeleteModel(
            name='Ustags',
        ),
    ]
