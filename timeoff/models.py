from django.db import models
from datetime import datetime, date

# Create your models here.

class Users(models.Model):
    p_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    requested_date = models.DateField(auto_now=False)
    submit_date = models.DateField(auto_now_add=False, auto_now=False)
    choice_text = models.CharField(max_length=400)

class Status(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.TextChoices('status', 'Approved Denied Pending')
    modified_by = models.TextChoices('modified_by', 'admin1 admin2')










