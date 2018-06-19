# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from log.models import *

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')

def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['userpass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/dashboard')
        else:
            return HttpResponse('Not Matched')
    elif request.method == "GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request,'login.html')


def auth_logout(request):
    logout(request);
    return HttpResponseRedirect('/');

@login_required
def dashboard(request):
    if request.method == "POST":
        emp_id = request.POST.get('emp_id',"")
        name = request.POST.get('name',"")
        mail_id = request.POST.get('mail_id',"")
        team = request.POST.get('team',"")
        data =employee(emp_id=emp_id, name=name, mail_id=mail_id, team=team)
        data.save()
        return HttpResponse("succes")
    else:
        return render(request,'dashboard.html')
    
def view(request):
    if request.method == "POST":
        g = employee.objects.values()
        return render(request,"view.html",{"output":g})


def csv(request):
    if request.method == "POST":
        g = employee.objects.values()
        return render(request,"csv.html",{"output":g})
