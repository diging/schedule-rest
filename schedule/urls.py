from rest_framework import routers
from .views import ScheduleViewset, list_schedules, list_user_schedules, create_availability, list_availabilities, list_user_availabilities, delete_availability, approve_schedule, update_availability, list_team_meetings, create_team_meeting
from django.urls import path

app_name = 'schedules'

router = routers.SimpleRouter()
router.register(r'schedules', ScheduleViewset, basename="schedules")

urlpatterns = [
	path('list/', list_schedules, name='list_schedules'),
	path('user/', list_user_schedules, name='list_user_schedules'),
	path('availability/create', create_availability, name='create_availability'),
	path('availability/list', list_availabilities, name='list_availabilities'),
	path('user/availability', list_user_availabilities, name='list_user_availabilities'),
	path('availability/delete/<int:pk>', delete_availability, name='delete_availability'),
	path('availability/approve/<int:pk>', approve_schedule, name='approve_availability'),
	path('availability/update/<int:pk>', update_availability, name='update_availability'),
    path('meeting/create/', create_team_meeting, name='create_team_meeting'),
    path('meetings/list/', list_team_meetings, name='list_team_meetings')
]
