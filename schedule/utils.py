from .models import Schedule
from datetime import datetime, date, time, timedelta
import math


def create_schedule(availability):
	schedule = Schedule()
	time_increments_left = float(availability.max_hours) / .25
	time_binary_list = []
	scheduled_increments = 0
	availability_iterable = iter(vars(availability).items())
	for attr, value in availability_iterable:
		if 'start' in attr:
			print(type(value))
			start_time_units = int((value.hour * 4) + (value.minute / 15))
			start = value
			start_day = attr
			attr, value = next(availability_iterable)
			duration = datetime.combine(date.today(), value) - datetime.combine(date.today(), start)
			current_increments = duration / timedelta(minutes=15)
			if current_increments < time_increments_left:
				end_time_units = int((value.hour * 4) + (value.minute / 15))
				time_binary_list.append(create_time_increment_binaries(start_time_units, end_time_units))
				setattr(schedule, start_day, start)
				setattr(schedule, attr, value)
				if current_increments > 20:
					time_increments_left -= (current_increments - 2)
					scheduled_increments += (current_increments - 2)
				else:
					time_increments_left -= current_increments
					scheduled_increments += current_increments
			elif time_increments_left > 0:
				end_time_units = int((value.hour * 4) + (value.minute / 15))
				time_binary_list.append(create_time_increment_binaries(start_time_units, end_time_units))
				setattr(schedule, start_day, start)
				minutes_left = time_increments_left * 15
				duration = datetime.combine(date.today(), start) + timedelta(minutes=minutes_left)
				scheduled_increments += time_increments_left
				setattr(schedule, attr, duration.time())
				time_increments_left = 0
			else:
				end_time_units = int((value.hour * 4) + (value.minute / 15))
				time_binary_list.append(create_time_increment_binaries(start_time_units, end_time_units))
				setattr(schedule, start_day, time(0,0))
				setattr(schedule, attr, time(0,0))
	hours = divmod(scheduled_increments, 4)
	left_over = hours[1] * .25
	schedule.total_hours = hours[0] + left_over
	setattr(schedule, 'user', availability.user)
	schedule.save()
	return time_binary_list


time_binaries = [
	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
]

def create_time_increment_binaries(start_time_units, end_time_units):
	for unit in range(start_time_units, end_time_units):
		time_binaries[unit] = 1
	return time_binaries
