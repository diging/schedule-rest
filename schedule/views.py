from django.shortcuts import render, get_object_or_404
from rest_framework import response
from rest_framework.serializers import Serializer
from .models import Schedule, Availability, BaseSchedule, TeamMeetings
from .serializers import AvailabilityDayTimeStringsSerializer, AvailabilityListSerializer, AvailabilityPostSerializer, AvailabilityUpdateDayTimesSerializer, ScheduleSerializer, MaxHoursSerializer, AvailabilityUpdateSerializer, TeamMeetingSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from accounts.models import User
from datetime import datetime, date, timedelta, time
from .utils import create_schedule, check_hours
import json

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
def create_schedule2(request):
	serializer = ScheduleSerializer(data=json.loads(request.data['schedule']))
	if serializer.is_valid():
		Schedule.objects.create(
			user = request.user,
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
			thu_start_1 = serializer.validated_data['thu_start_1'],
			thu_end_1 = serializer.validated_data['thu_end_1'],
			thu_start_2 = serializer.validated_data['thu_start_2'],
			thu_end_2 = serializer.validated_data['thu_end_2'],
			fri_start_1 = serializer.validated_data['fri_start_1'],
			fri_end_1 = serializer.validated_data['fri_end_1'],
			fri_start_2 = serializer.validated_data['fri_start_2'],
			fri_end_2 = serializer.validated_data['fri_end_2'],
			total_hours = serializer.validated_data['total_hours']
		)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
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
	serializer = AvailabilityPostSerializer(data=request.data['schedule'])
	max_hours_serializer = MaxHoursSerializer(data={'maxHours': request.data['maxHours']})
	if serializer.is_valid() and max_hours_serializer.is_valid():
		availability = Availability.objects.create(
			user = request.user,
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
			thu_start_1 = serializer.validated_data['Thursday']['startTime1'],
			thu_end_1 = serializer.validated_data['Thursday']['endTime1'],
			thu_start_2 = serializer.validated_data['Thursday']['startTime2'],
			thu_end_2 = serializer.validated_data['Thursday']['endTime2'],
			fri_start_1 = serializer.validated_data['Friday']['startTime1'],
			fri_end_1 = serializer.validated_data['Friday']['endTime1'],
			fri_start_2 = serializer.validated_data['Friday']['startTime2'],
			fri_end_2 = serializer.validated_data['Friday']['endTime2'],
			max_hours = max_hours_serializer.validated_data['maxHours']
		)
		serializer = AvailabilityListSerializer(availability)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_availabilities(request):
	availabilities = Availability.objects.all()
	Serializer = AvailabilityListSerializer(availabilities, many=True)
	return Response(Serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_user_availabilities(request):
	availabilities = Availability.objects.filter(user=request.user)
	Serializer = AvailabilityListSerializer(availabilities, many=True)
	return Response(Serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def create_schedules_auto(request, pk):
	availability = Availability.objects.get(id=pk)
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
				time_increments_left -= current_increments
				scheduled_increments += current_increments
			elif time_increments_left > 0:
				setattr(schedule, start_day, start)
				minutes_left = time_increments_left * 15
				duration = datetime.combine(date.today(), start) + timedelta(minutes=minutes_left)
				scheduled_increments += time_increments_left
				setattr(schedule, attr, duration.time())
				# this needs to be fixed
				#schedule.user = availability.user
				time_increments_left = 0
			else:
				setattr(schedule, start_day, time(0,0))
				setattr(schedule, attr, time(0,0))
	setattr(schedule, 'user', availability.user)
	hours = divmod(scheduled_increments, 4)
	left_over = hours[1] * .25
	schedule.total_hours = hours[0] + left_over
	return Response(status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_availability(request, pk):
	avail = Availability.objects.get(id=pk)
	if avail.status == '0' and (request.user == avail.user or request.user.is_superuser == True):
		avail.delete()
		return Response(status=status.HTTP_200_OK)
	return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['PATCH'])
def approve_schedule(request, pk):
	avail = Availability.objects.get(id=pk)
	serializer = AvailabilityUpdateSerializer(data=request.data)
	if serializer.is_valid() and avail:
		avail.status = serializer._validated_data['status']
		avail.approval_date = datetime.now()
		avail.reason = serializer._validated_data['reason']
		avail.save()
		check_hours_results = check_hours(avail)
		if check_hours_results[0]:
			create_schedule(avail, check_hours_results[1])
			return Response(status=status.HTTP_200_OK)
		print("The schedule that you are trying to approve exceeds the maximum hours alotted, please adjust accordingly")
		return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
	else:
		print(serializer.errors)
		return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['PATCH'])
def update_availability(request, pk):
	sched_times_serializer = AvailabilityUpdateDayTimesSerializer(data={'day': request.data['sched_times']})
	day_time_strings_serializer = AvailabilityDayTimeStringsSerializer(data={'day_times': request.data['time_strings']})
	if sched_times_serializer.is_valid() and day_time_strings_serializer.is_valid():
		avail = Availability.objects.get(id=pk)
		setattr(avail, day_time_strings_serializer.validated_data['day_times'][0], sched_times_serializer.validated_data['day']['startTime1'])
		setattr(avail, day_time_strings_serializer.validated_data['day_times'][2], sched_times_serializer.validated_data['day']['endTime1'])
		setattr(avail, day_time_strings_serializer.validated_data['day_times'][1], sched_times_serializer.validated_data['day']['startTime2'])
		setattr(avail, day_time_strings_serializer.validated_data['day_times'][3], sched_times_serializer.validated_data['day']['endTime2'])
		avail.save()
		return Response(sched_times_serializer.data, status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
		
@api_view(['GET'])
def list_team_meetings(request):
	meetings = TeamMeetings.objects.all()
	Serializer = TeamMeetingSerializer(meetings, many=True)
	return Response(Serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_team_meetings(request):
	meetings = TeamMeetings.objects.all()
	Serializer = TeamMeetingSerializer(meetings, many=True)
	if Serializer.is_valid():
		meetings = TeamMeetings.objects.create(
			start = Serializer.validated_data['start'],
			end = Serializer.validated_data['end'],
			meeting_type = Serializer.validated_data['meeting_type'],
			attendees = TeamMeetings.set_attendees(Serializer.validated_data['attendees'])
		)
		return Response(meetings.data, status=status.HTTP_201_CREATED)
	else:
		return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)