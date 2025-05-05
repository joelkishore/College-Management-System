from django.shortcuts import render

# Create your views here.

def std(request):
    return render(request,'student/std_dash.html')