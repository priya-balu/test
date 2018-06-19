from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.

class Dashboard_details(models.Model):
    employee_id = models.CharField(max_length=10)
    employee_name = models.CharField(max_length=20)
    team = models.CharField(max_length=20)
    employee_email = models.CharField(max_length=20)
    class Meta:
      db_table = "employeedetails"
   