from django import forms
from .models import Dashboard_details

class Formsubmit(forms.Form):
    class Meta:
        model= Dashboard_details
        fields= ["employee_id", "employee_name", "team", "employee_email"]

