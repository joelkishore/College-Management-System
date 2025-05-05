from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

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
                pass
            elif role=='teacher':
                pass
            elif role=='student':
                pass
            else:
                return redirect('home')

    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})