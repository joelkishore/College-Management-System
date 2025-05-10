from django.db import models
from accounts.models import Class,Subject
# Create your models here.

class createschedule(models.Model):
    DAY=[

        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    day=models.CharField(max_length=20, choices=DAY)
    class_name=models.ForeignKey(Class,on_delete=models.CASCADE)
    hour1 = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=None, null=True, related_name='hour1_schedules')
    hour2 = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=None, null=True, related_name='hour2_schedules')
    hour3 = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=None, null=True, related_name='hour3_schedules')
    hour4 = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=None, null=True, related_name='hour4_schedules')
    hour5 = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=None, null=True, related_name='hour5_schedules')
    def __str__(self):
        return f"{self.day} -  H1 : {self.hour1},  H2 : {self.hour2},  H3 : {self.hour3}, H4 : {self.hour4},  H5 : {self.hour5}"

