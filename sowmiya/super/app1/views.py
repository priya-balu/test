from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from app1.models import *
from django.contrib.auth import login as auth_login



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
        if user is not None:
            login(request,user)
            return HttpResponse('success')
        else:
            return HttpResponse('Not Matched')
    elif request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard')
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
        return render(request, 'dashboard.html')   
@login_required
def emp_details(request):
   if request.method == "POST":  
       d = Dashboard_details.objects.values()
       return render(request, "empdetails.html", {"emp":d})

def some_view(request):
    import csv
    result = []
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Dashboard_details.csv"'
    writer = csv.writer(response)
    d = Dashboard_details.objects.all()
    print d
    writer.writerow(['employee_name', 'employee_id', 'team', 'employee_email'])
    for i in d:
       result.append([ i.employee_name, i.employee_id, i.team, i.employee_email])
    print result
    for j in result:
        writer.writerow(j)

    return response
    



