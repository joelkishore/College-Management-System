from django.shortcuts import render
from accounts.models import Class
from teacher.models import documents,announcements
from schedule.models import createschedule

# Create your views here.

def std(request):
    name=Class.objects.filter(students=request.user)
    document=documents.objects.all()
    schedule=createschedule.objects.filter(class_name__in=name)
    announcement=announcements.objects.filter(class_name__in=name)
    context={
            'class_name':name,
            'document':document,
            'schedule':schedule,
            'news':announcement
    }
    return render(request,'student/std_dash.html',context)