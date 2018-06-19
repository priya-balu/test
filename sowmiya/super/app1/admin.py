from django.forms import TextInput, Textarea
from django.contrib import admin
from app1.models import *
# Register your models here.

class Dashboard_detailsAdmin(admin.ModelAdmin):
     list_display = ('employee_name','employee_id',)
     search_fields = ('employee_name','employee_id',)
admin.site.register(Dashboard_details,Dashboard_detailsAdmin)
