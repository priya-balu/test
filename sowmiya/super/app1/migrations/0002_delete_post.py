# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-06-09 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
