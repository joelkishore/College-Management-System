from django.shortcuts import render
from accounts.models import Class
from teacher.models import documents
# Create your views here.

def std(request):
    class_name=Class.objects.filter(students=request.user)
    document=documents.objects.all()
    return render(request,'student/std_dash.html',{'class_name':class_name,'document':document})