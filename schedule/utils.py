from .models import Schedule
from datetime import datetime, date, timedelta

def check_hours(availability):
	availability_iterable = iter(vars(availability).items())
	total_increments = 0
	for attr, value in availability_iterable:
		if 'start' in attr or 'end' in attr:
			start = value
			attr, value = next(availability_iterable)
			duration = datetime.combine(date.today(), value) - datetime.combine(date.today(), start)
			total_increments += duration / timedelta(minutes=15)
	total_hours = total_increments/4
	if total_hours > availability.max_hours:
		return [False, total_hours]
	else:
		return [True, total_hours]
	
def create_schedule(availability, scheduled_hours):
	if Schedule.objects.filter(user=availability.user):
		Schedule.objects.filter(user=availability.user).delete()
	schedule = Schedule()
	availability_iterable = iter(vars(availability).items())
	for attr, value in availability_iterable:
		if 'start' in attr or 'end' in attr:
			start = value
			start_day = attr
			attr, value = next(availability_iterable)
			setattr(schedule, start_day, start)
			setattr(schedule, attr, value)
	schedule.total_hours = scheduled_hours
	setattr(schedule, 'user', availability.user)
	schedule.save()
