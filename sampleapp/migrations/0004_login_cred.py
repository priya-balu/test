# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sampleapp', '0003_delete_credentials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_cred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
