from rest_framework import routers
from .views import TimeoffViewSet
from .views import list_user_timeoff_requests
from django.urls import path

from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'heroes', views.HeroViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


app_name = 'timeoff'

router = routers.SimpleRouter()
router.register(r'timeoff', TimeoffViewSet, basename="timeoff")

urlpatterns = [
	path('', include(router.urls)),
	path('user/', list_user_timeoff_requests, name='list_user_timeoff_requests'),
]
