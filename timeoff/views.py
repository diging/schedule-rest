from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Timeoff
from .serializers import TimeoffSerializer


class TimeoffViewSet(viewsets.ModelViewSet):
	queryset = Timeoff.objects.all()
	serializer_class = TimeoffSerializer


@api_view(['GET'])
def list_user_timeoff_requests(request):
	timeoff_requests = Timeoff.objects.filter(user=request.user)
	Serializer = TimeoffSerializer(timeoff_requests, many=True)
	return Response(Serializer.data, status=status.HTTP_200_OK)
