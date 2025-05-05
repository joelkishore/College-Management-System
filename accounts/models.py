from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    options=(
        ('admin','admin'),
        ('teacher','teacher'),
        ('student','student'),
    )
    role=models.CharField(max_length=20,choices=options)
    profile=models.URLField(default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")