from django.urls import path
from rest_framework import routers

from .views import list_all_timeoff_requests, list_user_timeoff_requests, submit_timeoff_view

app_name = 'timeoff'

router = routers.SimpleRouter()

urlpatterns = [
	path('user/', list_user_timeoff_requests, name='list_user_timeoff_requests'),
	path('all/', list_all_timeoff_requests, name='list_all_timeoff_requests'),
	path('create/', submit_timeoff_view, name='submit_timeoff_view'),
]
