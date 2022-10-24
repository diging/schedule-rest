from django.shortcuts import get_object_or_404
from accounts.models import User
from .serializers import UserInfoSerializer, UserSerializer, UserSerializerAdminAccess
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint

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
	user_email = request.GET.get('email', '')
	user = get_object_or_404(User, email=user_email)
	if user:
		serializer = UserInfoSerializer(user)
		return Response(serializer.data, status=status.HTTP_200_OK)


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


@api_view(['GET'])
def get_current_user(request):
	user = get_object_or_404(User, id=request.user.id)
	serializer = UserSerializerAdminAccess(user)
	return Response(serializer.data, status=status.HTTP_200_OK)
 
@api_view(['GET'])
def user_info(request):
	serializer = UserInfoSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def users_list(request):
	users = User.objects.all()
	serializer = UserInfoSerializer(users, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([AllowAny])
def update_user_role(request, pk):
	user = get_object_or_404(User, id=pk)
	serializer = UserInfoSerializer(data=request.data)
	if serializer.is_valid() and user:
		user.is_superuser = serializer._validated_data['is_superuser']
		user.save()
		return Response(status=status.HTTP_200_OK)
	else:
		print(serializer.errors)
		return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)