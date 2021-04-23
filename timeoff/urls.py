from django.urls import include, path
from rest_framework import routers

from .views import TimeoffViewSet
from .views import list_user_timeoff_requests

app_name = 'timeoff'

router = routers.SimpleRouter()
router.register(r'timeoff', TimeoffViewSet, basename="timeoff")

urlpatterns = [
	path('', include(router.urls)),
	path('user/', list_user_timeoff_requests, name='list_user_timeoff_requests'),
]
