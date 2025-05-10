from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from accounts.models import Class
from .form import *
# Create your views here.

def staff(request):
    news=announcements.objects.all()
    # subject=Subject.objects.filter(teacher=request.user)
    class_name=Class.objects.filter(teacher=request.user)
    context={
            'class':class_name,
            'news':news
             }
    return render(request,'teacher/teacher_dash.html',context)

def announcements_view(request):
    if request.method=='POST':
        form=announcementsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form=announcementsform()
    return render(request,'teacher/announcements.html',{'form':form})

def delete_announcements(request,pk):
    data=announcements.objects.get(id=pk)
    data.delete()
    return redirect('staff')

def add_document(request):
    if request.method=='POST':
        form = documentform(request.POST, request.FILES)
        form.fields['class_name'].queryset = Class.objects.filter(teacher=request.user)
        if form.is_valid():
            data=form.save(commit=False)
            data.teacher=request.user
            data.save()
            return redirect('staff')
    else :
        form=documentform()
    return render(request,'teacher/add_document.html',{'form':form})