# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0011_auto_20180614_1551'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dashboard_details',
            table='employeedetails',
        ),
    ]
