from django import forms
from .models import *

class scheduleform(forms.ModelForm):
    class Meta:
        model=createschedule
        fields=['day','class_name','hour1','hour2','hour3','hour4','hour5']