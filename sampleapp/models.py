from django.db import models

# Create your models here.
class Login_cred(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
      db_table = "logincred"

class Dashboard_details(models.Model):
    employee_id = models.CharField(max_length=10)
    employee_name = models.CharField(max_length=20)
    team = models.CharField(max_length=20)
    employee_email = models.CharField(max_length=20)
    production_count = models.CharField(max_length=5)
      

