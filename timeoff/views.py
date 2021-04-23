from .models import Timeoff
from .serializers import TimeoffSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class TimeoffViewSet(viewsets.ModelViewSet):
	queryset = Timeoff.objects.all()
	serializer_class = TimeoffSerializer

	def patch(self, request, *args, **kwargs):
		print("entered")
		return


@api_view(['GET'])
def list_user_timeoff_requests(request):
	timeoff_requests = Timeoff.objects.filter(user=request.user)
	Serializer = TimeoffSerializer(timeoff_requests, many=True)
	return Response(Serializer.data, status=status.HTTP_200_OK)
