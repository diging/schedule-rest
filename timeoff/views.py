from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .models import Timeoff
from .serializers import TimeoffSerializer, TimeoffPostSerializer


class TimeoffViewSet(viewsets.ModelViewSet):
	queryset = Timeoff.objects.all()
	serializer_class = TimeoffSerializer


@api_view(['GET'])
def list_user_timeoff_requests(request):
	timeoff_requests = Timeoff.objects.filter(user=request.user)
	Serializer = TimeoffSerializer(timeoff_requests, many=True)
	return Response(Serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_all_timeoff_requests(request):
	timeoff_requests = Timeoff.objects.all()
	Serializer = TimeoffSerializer(timeoff_requests, many=True)
	return Response(Serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def submit_timeoff_view(request):
	serializer = TimeoffPostSerializer(data=request.data)
	if serializer.is_valid():
		Timeoff.objects.create(
			user = request.user,
			to_date = serializer.validated_data['to_date'],
			from_date = serializer.validated_data['from_date'],
			description = serializer.validated_data['description'],
			status = 'pending',
			timeoff_type = serializer.validated_data['timeoff_type']
		)
		return Response(status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)