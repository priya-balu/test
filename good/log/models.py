# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class employee(models.Model):
    emp_id= models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    mail_id= models.EmailField()
    team=models.CharField(max_length=200)
    # production= models.CharField(max_length=200)
    def __str__(self):
        return self.name


# Create your models here.
