from django.shortcuts import render, get_object_or_404

from app.forms import *
from app.models import Task 
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from datetime import datetime
# Create your views here.


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        AUO=authenticate(request,username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect('/list')
        else:
            return HttpResponse("Invalid Login")
        
    return render(request,"user_login.html")

def user_regestration(request):
    EUFO=UserForm()
    d={'EUFO':EUFO}
    if request.method=='POST':
        NUFO=UserForm(request.POST)
        if NUFO.is_valid():
            MUFO = NUFO.save(commit=False)
            pw=NUFO.cleaned_data['password']
            MUFO.set_password(pw)
            MUFO.save()
            return HttpResponseRedirect('/user_login')
    return render(request, 'user_regestration.html',d)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/list')



# used to display all the task in the database

def list(request):
    if request.user.is_authenticated:
        TFO=Task.objects.filter(username=request.user).order_by('completed', 'due_date')
        d={'TFO':TFO}
        return render(request, 'list.html',d)
    else:
        return render(request, 'list.html')


#Adding new Task to the database
# used to add new task to the database
def add(request):
    ETFO=TaskForm()
    d={'ETFO':ETFO}
    
    if request.method=='POST':
        TFO=TaskForm(request.POST)
        if TFO.is_valid():
            task=TFO.save(commit=False)
            task.username=request.user
            task.save()
            return HttpResponseRedirect('/list')     
        
    return render(request, 'add.html',d)


def edit(request,id):
    task=get_object_or_404(Task, id=id)
    if request.method=='POST':
        ETFO=TaskForm(request.POST, instance=task)
        if ETFO.is_valid():
            ETFO.save(commit=False)
            ETFO.username=request.user
            ETFO.save()
            return HttpResponseRedirect('/list')
    else:
        ETFO=TaskForm(instance=task)
    d={'ETFO':ETFO}
    return render(request, 'add.html',d)


def delete(request,id):
    TFO=Task.objects.all()
    d={'TFO':TFO}
    task=get_object_or_404(Task, id=id)
    task.delete()
    return HttpResponseRedirect('/list')



def complete(request,id):
    task = get_object_or_404(Task, id=id)
    task.completed = True 
    task.save()
    return HttpResponseRedirect('/list')  
    # 1. Get the task by id or return 404 if not found
    # 2. Mark it as completed
    # 3. Save changes to the database
    # 4. Redirect back to the task list




