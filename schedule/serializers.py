from rest_framework import serializers
from .models import Schedule, Availability

class ScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schedule

		fields = ['id', 
		'mon_start_1',
		'mon_end_1',
		'mon_start_2',
		'mon_end_2',
		'tue_start_1',
		'tue_end_1',
		'tue_start_2',
		'tue_end_2',
		'wed_start_1',
		'wed_end_1',
		'wed_start_2',
		'wed_end_2',
		'thur_start_1',
		'thur_end_1',
		'thur_start_2',
		'thur_end_2',
		'fri_start_1',
		'fri_end_1',
		'fri_start_2',
		'fri_end_2',
		'created',
		'total_hours'
		]

class AvailabilitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Availability
		
		fields = ['id', 
		'mon_start_1',
		'mon_end_1',
		'mon_start_2',
		'mon_end_2',
		'tue_start_1',
		'tue_end_1',
		'tue_start_2',
		'tue_end_2',
		'wed_start_1',
		'wed_end_1',
		'wed_start_2',
		'wed_end_2',
		'thur_start_1',
		'thur_end_1',
		'thur_start_2',
		'thur_end_2',
		'fri_start_1',
		'fri_end_1',
		'fri_start_2',
		'fri_end_2',
		'created',
		'max_hours'
		]