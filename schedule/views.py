from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Schedule, Availability
from .serializers import ScheduleSerializer, AvailabilitySerializer, MaxHoursSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from accounts.models import User

# Create your views here.

class ScheduleViewset(viewsets.ViewSet):

	def list(self, request, format=None):
		schedules = Schedule.objects.all()
		serializer = ScheduleSerializer(schedules, many=True)
		return Response(serializer.data)

	def create(self, request, format=None):
		serializer = ScheduleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_schedule(request):
	serializer = ScheduleSerializer(data=request.data)
	if serializer.is_valid():
		Schedule.objects.create(
			user =request.user,
			mon_start_1 = serializer.validated_data['mon_start_1'],
			mon_end_1 = serializer.validated_data['mon_end_1'],
			mon_start_2 = serializer.validated_data['mon_start_2'],
			mon_end_2 = serializer.validated_data['mon_end_2'],
			tue_start_1 = serializer.validated_data['tue_start_1'],
			tue_end_1 = serializer.validated_data['tue_end_1'],
			tue_start_2 = serializer.validated_data['tue_start_2'],
			tue_end_2 = serializer.validated_data['tue_end_2'],
			wed_start_1 = serializer.validated_data['wed_start_1'],
			wed_end_1 = serializer.validated_data['wed_end_1'],
			wed_start_2 = serializer.validated_data['wed_start_2'],
			wed_end_2 = serializer.validated_data['wed_end_2'],
			thur_start_1 = serializer.validated_data['thur_start_1'],
			thur_end_1 = serializer.validated_data['thur_end_1'],
			thur_start_2 = serializer.validated_data['thur_start_2'],
			thur_end_2 = serializer.validated_data['thur_end_2'],
			fri_start_1 = serializer.validated_data['fri_start_1'],
			fri_end_1 = serializer.validated_data['fri_end_1'],
			fri_start_2 = serializer.validated_data['fri_start_2'],
			fri_end_2 = serializer.validated_data['fri_end_2'],
			total_hours = serializer.validated_data['total_hours']
		)
		return Response(status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_schedules(request):
		schedules = Schedule.objects.all()
		Serializer = ScheduleSerializer(schedules, many=True)
		return Response(Serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_user_schedules(request):
		schedules = Schedule.objects.filter(user=request.user)
		Serializer = ScheduleSerializer(schedules, many=True)
		return Response(Serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_availability(request):
	serializer = AvailabilitySerializer(data=request.data['schedule'])
	max_hours_serializer = MaxHoursSerializer(data={'maxHours': request.data['maxHours']})
	print('hit')
	print(max_hours_serializer)
	print(request.data['maxHours'])
	print(serializer.is_valid())
	print(max_hours_serializer.is_valid())
	if serializer.is_valid() and max_hours_serializer.is_valid():
		Availability.objects.create(
			user =request.user,
			mon_start_1 = serializer.validated_data['Monday']['startTime1'],
			mon_end_1 = serializer.validated_data['Monday']['endTime1'],
			mon_start_2 = serializer.validated_data['Monday']['startTime2'],
			mon_end_2 = serializer.validated_data['Monday']['endTime2'],
			tue_start_1 = serializer.validated_data['Tuesday']['startTime1'],
			tue_end_1 = serializer.validated_data['Tuesday']['endTime1'],
			tue_start_2 = serializer.validated_data['Tuesday']['startTime2'],
			tue_end_2 = serializer.validated_data['Tuesday']['endTime2'],
			wed_start_1 = serializer.validated_data['Wednesday']['startTime1'],
			wed_end_1 = serializer.validated_data['Wednesday']['endTime1'],
			wed_start_2 = serializer.validated_data['Wednesday']['startTime2'],
			wed_end_2 = serializer.validated_data['Wednesday']['endTime2'],
			thur_start_1 = serializer.validated_data['Thursday']['startTime1'],
			thur_end_1 = serializer.validated_data['Thursday']['endTime1'],
			thur_start_2 = serializer.validated_data['Thursday']['startTime2'],
			thur_end_2 = serializer.validated_data['Thursday']['endTime2'],
			fri_start_1 = serializer.validated_data['Friday']['startTime1'],
			fri_end_1 = serializer.validated_data['Friday']['endTime1'],
			fri_start_2 = serializer.validated_data['Friday']['startTime2'],
			fri_end_2 = serializer.validated_data['Friday']['endTime2'],
			max_hours = max_hours_serializer.validated_data['maxHours']
		)
		return Response(status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_availabilities(request):
		availabilities = Availability.objects.all()
		Serializer = AvailabilitySerializer(availabilities, many=True)
		return Response(Serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_user_availabilities(request):
		availabilities = Availability.objects.filter(user=request.user)
		Serializer = AvailabilitySerializer(availabilities, many=True)
		return Response(Serializer.data, status=status.HTTP_200_OK)