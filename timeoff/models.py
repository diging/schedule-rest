from django.db import models
from datetime import datetime, date
from django.utils import timezone
from accounts.models import User


# Create your models here.
class Timeoff(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_timeoff = models.DateField(auto_now=False)
    text_box = models.TextField(max_length=500)
    submission_date = models.DateTimeField('date submitted',default=timezone.now)



class Status(models.Model):
    STATUS_CHOICES = [ ('A','Approved'),('D','Denied'),('P','Pending')]
    id = models.OneToOneField('Timeoff', on_delete=models.CASCADE, primary_key=True)
    status = models.CharField('status', choices=STATUS_CHOICES, max_length=1)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
