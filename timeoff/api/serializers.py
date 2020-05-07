from rest_framework import serializers
from timeoff.models import Timeoff, Status
from datetime import datetime


class TimeoffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeoff
        fields = ['id', 'username', 'requested_timeoff', 'text_box', 'created']

    def update(self, instance, validated_data):
        # Update and return an existing 'Timeoff' instance, given the validated data.
        instance.requested_timeoff = validated_data.get('requested_timeoff', instance.requested_timeoff)
        instance.created = validated_data.get('created', instance.created)
        return instance


class StatusSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID',read_only=True)
    username = serializers.CharField(required=True, allow_blank=False)
    class Meta:
        model = Status
        fields = ['id', 'status', 'approved_by']

    def update(self, instance, validated_data):
        # Update and return an existing 'Status' instance, given the validated data.
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
