# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dart', '0003_bus_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='timestamp',
            field=models.BigIntegerField(),
        ),
    ]