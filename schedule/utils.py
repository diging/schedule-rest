from .models import Schedule
from datetime import datetime, date, time, timedelta

def create_schedule(availability):
	schedule = Schedule()
	time_increments_left = float(availability.max_hours) / .25

	availability_iterable = iter(vars(availability).items())
	for attr, value in availability_iterable:
		if 'start' in attr: 
			start = value
			start_day = attr
			attr, value = next(availability_iterable)
			duration = datetime.combine(date.today(), value) - datetime.combine(date.today(), start)
			current_increments = duration / timedelta(minutes=15)
			if current_increments < time_increments_left:
				setattr(schedule, start_day, start)
				setattr(schedule, attr, value)
				time_increments_left -= current_increments
			elif time_increments_left > 0:
				setattr(schedule, start_day, start)
				minutes_left = time_increments_left * 15
				duration = datetime.combine(date.today(), start) + timedelta(minutes=minutes_left)
				setattr(schedule, attr, duration.time())
				# this needs to be fixed
				schedule.total_hours = availability.max_hours
				schedule.user = availability.user
				time_increments_left = 0
			else:
				setattr(schedule, start_day, time(0,0))
				setattr(schedule, attr, time(0,0))
	schedule.save()