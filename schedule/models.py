from django.db.models.fields import DateTimeField, TextField
from accounts.models import User
from django.db import models
from accounts.models import User
# Create your models here.

class BaseSchedule(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	mon_start_1 = models.TimeField()
	mon_end_1 = models.TimeField()
	mon_start_2 = models.TimeField()
	mon_end_2 = models.TimeField()
	tue_start_1 = models.TimeField()
	tue_end_1 = models.TimeField()
	tue_start_2 = models.TimeField()
	tue_end_2 = models.TimeField()
	wed_start_1 = models.TimeField()
	wed_end_1 = models.TimeField()
	wed_start_2 = models.TimeField()
	wed_end_2 = models.TimeField()
	thu_start_1 = models.TimeField()
	thu_end_1 = models.TimeField()
	thu_start_2 = models.TimeField()
	thu_end_2 = models.TimeField()
	fri_start_1 = models.TimeField()
	fri_end_1 = models.TimeField()
	fri_start_2 = models.TimeField()
	fri_end_2 = models.TimeField()
	created = DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

class Availability(BaseSchedule):
	max_hours = models.DecimalField(max_digits=4, decimal_places=2)
	STATUS_CHOICES = [
		(0, 'Pending'),
		(1, 'Approved'),
		(2, 'Denied')
	]
	status = models.CharField(
		max_length=8,
		choices=STATUS_CHOICES,
		default=0
	)
	approval_date = DateTimeField(blank=True, null=True)
	reason = TextField(blank=True)

class Schedule(BaseSchedule):
	total_hours = models.DecimalField(max_digits=4, decimal_places=2)

