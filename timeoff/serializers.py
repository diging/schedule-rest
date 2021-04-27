from rest_framework import serializers
from .models import Timeoff


class TimeoffSerializer(serializers.ModelSerializer):
	class Meta:
		model = Timeoff
		fields = '__all__'

class TimeoffPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Timeoff
		fields = [
			'to_date',
			'from_date',
			'description',
			'timeoff_type',
			'start_time',
			'end_time',
		]