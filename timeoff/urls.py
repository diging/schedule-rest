from django.urls import path
from rest_framework import routers

from .views import list_user_timeoff_requests

app_name = 'timeoff'

router = routers.SimpleRouter()

urlpatterns = [
	path('user', list_user_timeoff_requests, name='list_user_timeoff_requests'),
]
