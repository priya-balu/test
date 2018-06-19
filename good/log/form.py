from django import forms
from .models import employee

class employeeForms(forms.ModelForm):
    class Meta:
        model= employee
        fields= ["emp_id", "name", "mail_id", "team"]
