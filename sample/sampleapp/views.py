import csv
import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from sampleapp.models import *

from .forms import Formsubmit


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponse('Success')
    else:
        return HttpResponse('Authentication failed')

def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['userpass']
        user = authenticate(request, username=username, password=password)
        print user
        h =  login(request,user)
        print h
        if user is not None:
            return HttpResponseRedirect('/dashboard')
        else:
            return HttpResponse('Not Matched')
    else:
        return render(request,'login.html') 

def auth_logout(request): 
    logout(request)
    return HttpResponseRedirect('/login')

@login_required    
def dashboard(request):
    if request.method == "POST":  
        employee_id = request.POST.get('employee_id','')
        employee_name = request.POST.get('employee_name','')
        team = request.POST.get('team','')
        employee_email = request.POST.get('employee_email','')
        print employee_id,employee_name,team,employee_email
        value = Dashboard_details(employee_id=employee_id, employee_name=employee_name, team=team, employee_email=employee_email)
        value.save()
        if value is not None:
            return HttpResponse('Thanks')
        else:
            return HttpResponse('Enter all fields')
    else:
        return render(request, 'dashboard.html')   
     
def empdetails(request):
    if request.method == "POST":  
        a = Dashboard_details.objects.values()
          # print data
            # for Dashboard_details in value:
            #     print value
    return render(request, "empdetails.html", {"test": a})

def export_csv(request):
    if request.method == "POST":
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment;filename="Employeedetails.csv"'
        writer = csv.writer(response)
        values = Dashboard_details.objects.values()
        for j in values:
            writer.writerow(values)
        return response

      
    # return model._meta.fields
    #     getattr(instance, field.name)
    # with open('employeedetails.csv', 'wb') as csvfile:
    #     writer = csv.writer(csvfile)
    #     # write your header first
    # for obj in Dashboard_details.objects.all():
    #     row = ""
    #     for j in test:
    #         row += getattr(obj, j.name) + ","
    #         writer.writerow(row)
