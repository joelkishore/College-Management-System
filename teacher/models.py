from django.db import models
from accounts.models import Class,User

# Create your models here.

class announcements(models.Model):
    announcement=models.CharField(max_length=100)
    class_name=models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.announcement
    
class documents(models.Model):
    doc_name=models.CharField(max_length=100,default='study material')
    doc=models.FileField(upload_to='documents/')
    teacher=models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'role':'teacher'})
    class_name=models.ForeignKey(Class, on_delete=models.CASCADE)
    def __str__(self):
        return self.doc_name