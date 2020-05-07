from timeoff.models import Timeoff,Status
from .serializers import TimeoffSerializer,StatusSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from accounts.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


class TimeoffViewSet(viewsets.ViewSet):
    # Create, Retreive, Delete, Return list
    def create(self, request):
        queryset = Timeoff.objects.all()
        serializer = TimeoffSerializer
        if User:
            serializer.save(username=self.request.username)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request):
        queryset = Timeoff.objects.all()
        user = get_object_or_404(queryset.filter(username=self.request.username), pk=self.request.id)
        serializer = TimeoffSerializer(user)
        return Response(serializer.data)

    def return_list(self,request):
        queryset = Timeoff.objects.all()
        serializer = TimeSerializer(queryset, many=True)
        if User.is_superuser:
            return queryset.order_by('-created')
        else:
            queryset = Timeoff.objects.all().filter(username=self.request.username)
            return queryset.order_by('-created')

    def delete(self, request):
        instance = Timeoff.objects.get(pk=self.request.id)
        instance.delete()
        return HttpResponse("Deleted!!")
