from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import *
class CreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  
        fields = ('username', 'role', 'password1', 'password2')  

class userupdateForm(UserCreationForm):
    class Meta:
        model = get_user_model()  
        fields = ('username', 'role', 'password1', 'password2') 
        
# class Subjectform(forms.ModelForm):
#     class Meta:
#         model=Subject
#         fields=['subject_name','teacher']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'teacher', 'students','subject']
        widgets = {
            'students': forms.CheckboxSelectMultiple(),  # Use checkboxes for students
        } 
