from django import forms
from .models import *

class announcementsform(forms.ModelForm):
    class Meta:
        model=announcements
        fields=['announcement','class_name']
        # widgets = {
        #     'students': forms.CheckboxSelectMultiple(),  # Use checkboxes for students
        # }
class documentform(forms.ModelForm):
    class Meta:
        model=documents
        fields=['doc_name','doc','class_name']