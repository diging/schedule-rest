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

class DaySerializer(serializers.Serializer):
	startTime1 = serializers.TimeField()
	endTime1 = serializers.TimeField()
	startTime2 = serializers.TimeField()
	endTime2 = serializers.TimeField()

class AvailabilitySerializer(serializers.Serializer):
	Monday = DaySerializer()
	Tuesday = DaySerializer()
	Wednesday = DaySerializer()
	Thursday = DaySerializer()
	Friday = DaySerializer()
	

class MaxHoursSerializer(serializers.Serializer):
	maxHours = serializers.DecimalField(max_digits=4, decimal_places=2)

class AvailabilityListSerializer(serializers.ModelSerializer):
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
		'max_hours',
		'status'
		]