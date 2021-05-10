from django.urls import include, path
from rest_framework import routers

from .views import TimeoffViewSet, list_all_timeoff_requests, list_user_timeoff_requests, submit_timeoff_view, review_user_timeoff_request

app_name = 'timeoff'

router = routers.SimpleRouter()
router.register(r'timeoff', TimeoffViewSet, basename="timeoff")

urlpatterns = [
	path('', include(router.urls)),
	path('user/', list_user_timeoff_requests, name='list_user_timeoff_requests'),
	path('all/', list_all_timeoff_requests, name='list_all_timeoff_requests'),
	path('create/', submit_timeoff_view, name='submit_timeoff_view'),
	path('<int:pk>' + '/review_user_timeoff_request/', review_user_timeoff_request, name='review_user_timeoff_request')
]
