from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    OPTIONS=(
        ('admin','admin'),
        ('teacher','teacher'),
        ('student','student'),
    )
    role=models.CharField(max_length=20,choices=OPTIONS)
    profile=models.URLField(default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")

    def __str__(self):
        return self.username

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    def __str__(self):
        return self.subject_name
    

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'teacher'})
    students = models.ManyToManyField(
        User,
        related_name='classes',
        limit_choices_to={'role': 'student'}
    )
    subject= models.ForeignKey(Subject,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name