from rest_framework import serializers
from .models import Timeoff


class TimeoffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeoff
        fields = '__all__'
