# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0007_auto_20180613_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard_details',
            old_name='empployee_email',
            new_name='employee_email',
        ),
    ]
