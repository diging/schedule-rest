from .models import Schedule, Availability, TeamMeeting
from .serializers import AvailabilityDayTimeStringsSerializer, AvailabilityListSerializer, AvailabilityPostSerializer, AvailabilityUpdateDayTimesSerializer, ScheduleSerializer, MaxHoursSerializer, AvailabilityUpdateSerializer, TeamMeetingSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from datetime import datetime
from .utils import create_schedule, check_hours

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
	meetings = TeamMeeting.objects.all()
	Serializer = TeamMeetingSerializer(meetings, many=True)
	return Response(Serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_team_meeting(request):
	meeting_serializer = TeamMeetingSerializer(data=request.data)
	if meeting_serializer.is_valid():
		TeamMeeting.objects.create(
			start = meeting_serializer.validated_data['start'],
			end = meeting_serializer.validated_data['end'],
			days = meeting_serializer.validated_data['days'],
			date = meeting_serializer.validated_data['date'],
			meeting_type = meeting_serializer.validated_data['meeting_type'],
			attendees = meeting_serializer.validated_data['attendees']
		)
		return Response(status=status.HTTP_201_CREATED)
	else:
		print(meeting_serializer.errors)
		return Response(meeting_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)