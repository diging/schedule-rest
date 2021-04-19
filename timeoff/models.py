from django.db import models
from datetime import datetime, date
from django.utils import timezone
from accounts.models import User


# Create your models here.
class Timeoff(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	to_date = models.DateField(auto_now=False)
	from_date = models.DateField(auto_now=False)
	description = models.TextField(max_length=500)
	submission_date = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=9)
	approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_by')
