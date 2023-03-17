from django.db import models
from accounts.models import User


class EmptyStringToNoneField(models.DateField):
    def get_prep_value(self, value):
        if value == '':
            return None
        return value

class Timeoff(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	start_date = models.DateField(auto_now=False, default='2000-01-01')
	end_date = EmptyStringToNoneField(auto_now=False, null=True, blank=True, default='2000-01-01')
	start_time = models.TimeField(null=True, blank=True)
	end_time = models.TimeField(null=True, blank=True)
	all_day = models.BooleanField(default=False)
	request_type = models.CharField(max_length=25)
	reason = models.TextField(blank=True)
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
	approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_by', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)


