from rest_framework import serializers
from .models import Timeoff
from accounts.serializers import UserInfoSerializer


class TimeoffSerializer(serializers.ModelSerializer):
	user = UserInfoSerializer()

	class Meta:
		model = Timeoff
		fields = '__all__'
    
class TimeoffPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Timeoff
		fields = [
			'start_date',
			'end_date',
			'start_time',
			'end_time',
			'all_day',
			'request_type',
			'reason',
		]
	
	#Handle case where timeoff request is only for one day, i.e. end date field
	def to_internal_value(self, data):
		if data.get('end_date') == '':
			data['end_date'] = None
		return super().to_internal_value(data)