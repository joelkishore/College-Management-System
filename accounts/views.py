from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import *
from django.contrib.auth import get_user_model
from django.http import Http404
from schedule.models import createschedule
from schedule.form import scheduleform

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

def ad(request):
    User = get_user_model()

    users = User.objects.all()
    return render(request,'admin/admin.html',{'datas':users})

def create(request):
    if request.method=='POST':
        form=CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form=CreationForm()
    User = get_user_model()

    users = User.objects.all()

    return render(request,'admin/create_user.html',{'form':form,'users':users})

# def delete(request):

#     User = get_user_model()
#     users = User.objects.all()

#     return render(request,'admin/delete_user.html',{'users':users})

def delete_user(request, user_id=None):
    # Get the user to delete
    if request.method=='POST':
        User = get_user_model()
        user = User.objects.get(id=user_id)
        
        # Ensure that the logged-in user is allowed to delete (admin only)
        if request.user.is_superuser:
            user.delete()
            return redirect('dash')  # Redirect to the user list after deletion
        else:
            raise Http404("You do not have permission to delete this user.")
    User = get_user_model()
    users = User.objects.all()
    return render(request,'admin/delete_user.html',{'users':users})

# def update(request):
#     User = get_user_model()
#     users = User.objects.all()
#     return render(request,'admin/update_user.html',{'users':users})

def update_user(request, user_id=None):
    User = get_user_model()
    users = User.objects.all()
    if user_id:
        user = get_object_or_404(User, id=user_id)

        if request.method == 'POST':
            form = userupdateForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('update_users')  # Go back to list
        else:
            form = userupdateForm(instance=user)

        return render(request, 'admin/update_user.html', {'form': form,'user_to_update': user})

    else:
        users = User.objects.exclude(role='admin')
        return render(request, 'admin/update_user.html', {'users': users})
    
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash')  # Redirect to the class list view
    else:
        form = ClassForm()
    data=Class.objects.all()
    return render(request, 'admin/add_class.html', {'form': form,'class':data})

def delete_class(request,pk):
    data=Class.objects.get(id=pk)
    data.delete()
    return redirect('add_class')

def viewschedule(request):
    if request.method=='POST':
        form=scheduleform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewschedule')
    else:
        form=scheduleform()
    schedule=createschedule.objects.all()
    return render(request,'schedule/schedule.html',{'schedule':schedule,'form':form})