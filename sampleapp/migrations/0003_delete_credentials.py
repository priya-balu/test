# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 12:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0002_auto_20180609_1513'),
    ]

    operations = [
        migrations.DeleteModel(
            name='credentials',
        ),
    ]
