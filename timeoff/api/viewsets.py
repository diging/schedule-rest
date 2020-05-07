from timeoff.models import Timeoff,Status
from .serializers import TimeoffSerializer,StatusSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from accounts.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


class TimeoffViewSet(viewsets.ViewSet):
    # Create, Retreive, Delete, list
    def create(self, request):
        my_username = Timeoff.POST['username']
        queryset = Timeoff.objects.all()
        serializer = TimeoffSerializer
        if user:
            serializer.save(username=self.request.username)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request):
        my_username = Timeoff.POST['username']
        my_id = Timeoff.POST['id']
        queryset = Timeoff.objects.all()
        user = get_object_or_404(queryset.filter(username=my_username), pk=my_id)
        serializer = TimeoffSerializer(user)
        return Response(serializer.data)

    def return_list(self,request):
        my_username = Timeoff.POST['username']
        queryset = Timeoff.objects.all()
        serializer = TimeSerializer(queryset, many=True)
        if my_username.is_superuser:
            return queryset.order_by('-created')
        else:
            queryset = Timeoff.objects.all().filter(username=my_username)
            return queryset.order_by('-created')

    def delete(self, request):
        my_id = Timeoff.POST['id']
        instance = Timeoff.objects.get(pk=my_id)
        instance.delete()
        return HttpResponse("Deleted!")
