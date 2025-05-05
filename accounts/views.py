from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def log_in(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            role=user.role
            login(request,user)
            if role=='admin':
                return redirect('dash')
            elif role=='teacher':
                return redirect('staff')
            elif role=='student':
                return redirect('student')
            else:
                return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def out(request):
    logout(request)
    return redirect('home')

def create(request):
    if request.method=='POST':
        form=CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CreationForm()
    return render(request,'admin/admin_dash.html',{'form':form})