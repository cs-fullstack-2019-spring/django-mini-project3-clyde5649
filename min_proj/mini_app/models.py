from django.db import models
from django.utils import timezone
# Create your models here.


#data model for user

class TimeCard(models.Model):
    teachername = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=4,decimal_places=2)
    dateofwork = models.DateField(max_length=20)
    dateofentry = models.DateTimeField(default=timezone.now())
