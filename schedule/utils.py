from .models import Schedule
from datetime import datetime, date, time, timedelta

def create_schedule(availability):
	schedule = Schedule()
	time_increments_left = float(availability.max_hours) / .25
	scheduled_increments = 0
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
				if current_increments > 20:
					time_increments_left -= (current_increments - 2)
					scheduled_increments += (current_increments - 2)
				else:
					time_increments_left -= current_increments
					scheduled_increments += current_increments
				print("Scheduled First {}".format(scheduled_increments))
			elif time_increments_left > 0:
				setattr(schedule, start_day, start)
				minutes_left = time_increments_left * 15
				duration = datetime.combine(date.today(), start) + timedelta(minutes=minutes_left)
				scheduled_increments += time_increments_left
				print("Scheduled Second {}".format(scheduled_increments))
				setattr(schedule, attr, duration.time())
				# this needs to be fixed
				schedule.user = availability.user
				time_increments_left = 0
			else:
				setattr(schedule, start_day, time(0,0))
				setattr(schedule, attr, time(0,0))
	print("Scheduled Fin {}".format(scheduled_increments))
	hours = divmod(scheduled_increments, 4)
	left_over = hours[1] * .25
	schedule.total_hours = hours[0] + left_over
	schedule.user_id = availability.user_id
	schedule.save()