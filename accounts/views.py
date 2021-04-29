from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from accounts.models import User
from .forms import SignupForm
from .serializers import UserInfoSerializer, UserSerializer, UserSerializerAdminAccess

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from datetime import date
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
	if request.method == 'POST':
		print(request.body)
		user_serializer = UserSerializer(data=request.data)
		if user_serializer.is_valid():
			user = user_serializer.save()
			print("User: %s", user)
			token = RefreshToken.for_user(user)
			print("TOKEN: %s", token)
			context = {
				'refresh': str(token),
				'access': str(token.access_token),
			}
			return Response(context, status=status.HTTP_201_CREATED)
		else:
			print(user_serializer.errors)
			return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_search(request):
	email = request.GET.get('email', '')
	user = User.objects.get(email=email)
	if user:
		serializer = UserInfoSerializer(user)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_user(request):
	serializer = UserSerializerAdminAccess(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(data=serializer.data, status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def update_user(request, pk):
	user = get_object_or_404(User, id=pk)
	serializer = UserSerializerAdminAccess(user, data=request.data, partial=True)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, pk):
	user = get_object_or_404(User, id=pk)
	User.objects.filter(id=user.id).delete()
	return Response(status=status.HTTP_200_OK)
